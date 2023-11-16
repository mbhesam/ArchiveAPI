import os
from PIL import Image
from archiveAPI.settings import MONGO_DATA_COLLECTION_NAME,MONGO_CON_STR,MONGO_DB_NAME
from pymongo import MongoClient
import fitz
from archiveAPI.settings import LOGGER
import subprocess
client = MongoClient(MONGO_CON_STR)
mydb = client[MONGO_DB_NAME]
connection_string = mydb[MONGO_DATA_COLLECTION_NAME]

def get_image_meta(img):
    file=open(img,'rb')
    image = Image.open(img)
    return {
        'type': image.format,
#        'size': len(img.read()),
        'size': len(file.read()),
        'width': image.width,
        'height': image.height
    }

def get_unimaged_pdf():
    mongo_objects = connection_string.find({"attachments.files_inside": [],"attachments.type": {"$eq": "pdf"}})[0]
    pdf_names = []
    attachments_list = mongo_objects["attachments"]
    for attachment in attachments_list:
        pdf_names.append(attachment["local_address"])
    return pdf_names


def get_imaged_pdf():
    output_os = subprocess.check_output(["find", "/archive","-name","'*-page-12.jpeg'"], text=True)
    lines = output_os.split("\n")
    pdf_names_count = {}
    for line in lines[:-1]:
        entity = line.split("/")[3]
        obj = connection_string.find({"identifier": entity})
        attachments_list = obj["attachments"]
        for attachment in attachments_list:
            full_path = attachment["local_address"]
            try:
                doc = fitz.open(full_path)
                page_count = doc.page_count
                pdf_names_count[full_path] = page_count
            except Exception as Ex:
                LOGGER.error(msg=f"[{full_path}][{Ex}]")
                return {}
    return pdf_names_count


def delete_extra_image():
    pdf_names_count = get_imaged_pdf()
    full_path = list(pdf_names_count.keys())
    page_counts = list(pdf_names_count.values())
    for path , count in zip(full_path,page_counts):
        name = path.split("/")[-1]
        for page_number in range(11,count):
            os.remove(f"{path}_files/{name.strip('.pdf')}-page-{page_number}.jpeg")
            LOGGER.info(f"[{full_path}][deleted pages 11 to end]")
def create_image_dir(pdf):
    try:
        os.makedirs(f'{pdf}_files')
    except FileExistsError:
        pass

def create_pdf_img(): # create pdf images and return count of pages
    pdf_full_path = get_unimaged_pdf()
    name_page = {}
    #open your file
    for pdf in pdf_full_path:
        pdf_name = pdf.split("/")[-1]
        create_image_dir(pdf)
        try:
            doc = fitz.open(pdf)
        except Exception as Ex:
            LOGGER.error(msg=f"[{pdf_full_path}][{Ex}]")
        #iterate through the pages of the document and create a RGB image of the page
        page_count = 0
        for page in doc:
            pix = page.get_pixmap()
            pix.save(f"{pdf}_files/{pdf_name.strip('.pdf')}-page-%i.jpeg" % page.number)
            if page.number == '0' :
                os.rename(f"{pdf_name.strip('.pdf')}-page-0.jpeg",f"{pdf_name.strip('.pdf')}_thumb.jpeg",f"{pdf}_files/",f"{pdf}_files/")
            page_count = page_count + 1
        name_page[f'{pdf}'] = page_count
    return name_page

def update_db(name_page):
    pathes = list(name_page.keys())
    page_counts = list(name_page.values())
    for index ,path in enumerate(pathes):
        name = path.split("/")[-1]
        images = []
        all_page_number = page_counts[index]
        for page_number in range(all_page_number):
            image_object = {}
            meta = get_image_meta(f"{path}_files/{name.strip('.pdf')}-page-{page_number}.jpeg")
            image_object["width"] = meta["width"]
            image_object["height"] = meta["height"]
            image_object["local_address"] = f"{path}_files/{name.strip('.pdf')}-page-{page_number}.jpeg"
            images.append(image_object)
        search = {"attachments.name": name}
        update = {
            "$set": {
                f"attachments.{index}.files_inside": images[::-1]
            }
        }
        connection_string.update_one(search, update)
        LOGGER.info(msg=f"[{name} attachments.files_inside updated][{path}]")

def create_update():
    name_page = create_pdf_img()
    update_db(name_page)
