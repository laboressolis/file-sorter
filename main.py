import os 
import shutil
import logging
from sys import exit

current_dir = os.getcwd()

folders = ['Documents', 'Audios', 'Videos', 'PDFs', 'Executables', 'Images', 'Archives']

document = [".doc", ".docx", ".odt", ".txt", ".rtf", ".xls", ".xlsx", ".csv", ".ppt", ".pptx"]
image = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".tif", ".psd", ".ai", ".jfif"]
video = [".mp4", ".avi", ".mov", ".wmv", ".mkv"]
audio = [".mp3", ".wav", ".aac", ".flac", ".ogg"]
archive = [".zip", ".rar", ".7z", ".tar", ".gzip"]
executable = [".exe", ".dmg", ".apk"]
PDF = ['.pdf']

files = []
sorted_files = []
unsorted_files = []

def sort(file):
    root, ext = os.path.splitext(file)
    if ext in image:
        move_path = os.path.join(current_dir,'Images', file)
        shutil.move(file,move_path)
        logging.info(f"Moved '{file}' to Images folder")
        sorted_files.append(file)
    elif ext in document:
        move_path = os.path.join(current_dir,'Documents', file)
        shutil.move(file,move_path)
        logging.info(f"Moved '{file}' to Documents folder")
        sorted_files.append(file)
    elif ext in video:
        move_path = os.path.join(current_dir,'Videos', file)
        shutil.move(file,move_path)
        logging.info(f"Moved '{file}' to Videos folder")
        sorted_files.append(file)
    elif ext in audio:
        move_path = os.path.join(current_dir,'Audios', file)
        shutil.move(file,move_path)
        logging.info(f"Moved '{file}' to Audios folder")
        sorted_files.append(file)
    elif ext in archive:
        move_path = os.path.join(current_dir,'Archives', file)
        shutil.move(file,move_path)
        logging.info(f"Moved '{file}' to Archives folder")
        sorted_files.append(file)
    elif ext in executable:
        move_path = os.path.join(current_dir,'Executables', file)
        shutil.move(file,move_path)
        logging.info(f"Moved '{file}' to Executables folder")
        sorted_files.append(file)
    elif ext in PDF:
        move_path = os.path.join(current_dir,'PDFs', file)
        shutil.move(file,move_path)
        logging.info(f"Moved '{file}' to PDFs folder")
        sorted_files.append(file)
    else:
        unsorted_files.append(file)

def folder_setup(folder_name):
    folder_path = os.path.join(current_dir, folder_name)
    if os.path.exists(folder_path):
        logging.info(f"{folder_name} folder already exists")
    else:
        try:
            os.mkdir(folder_path)
            logging.info(f'{folder_name} folder created')
        except Exception as e:
            logging.error(f'Failed to create folder {folder_name}: {e}')

def get_files():
    current_dir_files = []
    for filename in os.listdir(current_dir):
        if os.path.isfile(os.path.join(current_dir, filename)):
            current_dir_files.append(filename)
    return current_dir_files

def main():
    logging.basicConfig(filename='actions.log', level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)

    logger.info('SCRIPT STARTED')
    logger.info(f'Current working directory: {current_dir}')

    for folder in folders:
        folder_setup(folder)
    
    logger.info('Fetching files')
    files = get_files()
    if files:
        logger.info(f'Fetched files: {files}')
    else:
        logger.info(f'No files found in the directory')
    
    for file in files:
        sort(file)
        
    logging.info(f'Sorted files: {sorted_files}')
    logging.info(f'Unsorted files: {unsorted_files}')

if __name__ == '__main__':
    main()