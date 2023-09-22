import os
from PIL import Image
from archiveAPI.settings import MONGO_DATA_COLLECTION_NAME,MONGO_CON_STR,MONGO_DB_NAME
from pymongo import MongoClient
import fitz

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
    mongo_objects = connection_string.find({"attachments.files_inside": []})[0]
    pdf_names = []
    attachments_list = mongo_objects["attachments"]
    for attachment in attachments_list:
        pdf_names.append(attachment["local_address"])
    return pdf_names

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
        doc = fitz.open(pdf)
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
    pathes = name_page.keys()
    page_counts = name_page.values()
    for index ,path in enumerate(pathes):
        name = path.split("/")[-1]
        images = []
        for page_number in range(page_counts):
            image_object = {}
            meta = get_image_meta(f"{path}_files/{name.strip('.pdf')}-page-{page_number}")
            image_object["width"] = meta["width"]
            image_object["height"] = meta["height"]
            image_object["local_address"] = f"{path}_files/{name.strip('.pdf')}-page-{page_number}"
            images.append(image_object)
        search = {"attachments.name": name}
        update = {
            "$set": {
                "attachments.$[element].files_inside": images
            }
        }
        filter = [
            {"element": index}
        ]
        connection_string.update_one(search, update, array_filters=filter)

def create_update():
    name_page  = create_pdf_img()
    update_db(name_page)

