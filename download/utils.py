import zipfile
import filetype
from archiveAPI.settings import FILES_BASE_DIR,LOGGER
import fitz
import re
def split_path(path):
    if path[-1] == '/':
        path = path[:-1]

    return path.split('/')


def get_file_name(path):
    return split_path(path)[-1]


def is_in_compressed(path):
    try:
        splitted_path = split_path(path)
        for index, item in enumerate(splitted_path):
            if item.lower().endswith('.zip') and index + 1 != len(splitted_path):
                zip_path = '/'.join(splitted_path[:index + 1])
                file_path = '/'.join(splitted_path[index + 1:])
                return True, zip_path, file_path
    except IndexError:
        pass
    return False, None, None


def get_absolute_file_path(relative_path):
    return FILES_BASE_DIR +'/'+ relative_path


def get_file_or_none(relative_path):
    try:
        return open(get_absolute_file_path(relative_path), 'rb')
    except FileNotFoundError:
        return None


def get_file_from_zip(zip_file, inner_file):
    try:
        archive = zipfile.ZipFile(get_absolute_file_path(zip_file))
        return archive.open(inner_file)
    except KeyError:
        return None
    except FileNotFoundError:
        return None


def get_file_type(path: str):
    return filetype.guess(path)

def create_single_image(image_path):
    pdf_name = FILES_BASE_DIR + "/" + "/".join(image_path.split("/")[:-1]).removesuffix("_files")
    page_number = int(re.search(r"(\d+).webp",image_path).group(1))
    try:
        doc = fitz.open(pdf_name)
    except Exception as Ex:
        LOGGER.error(msg=f"[{pdf_name}][{Ex}]")
    for page in doc:
        if page.number == page_number:
            pix = page.get_pixmap()
            pix.save(f"{FILES_BASE_DIR}/{image_path}")