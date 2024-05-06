import os 
import shutil
import logging
from sys import exit
import time
current_dir = os.getcwd()

folders = ['Documents', 'Audios', 'Videos', 'PDFs', 'Executables', 'Images', 'Archives', 'JARs']

file_ext = {'.doc': 'Documents', '.docx': 'Documents', '.odt': 'Documents', '.txt': 'Documents', '.rtf': 'Documents', '.xls': 'Documents', '.xlsx': 'Documents', '.csv': 'Documents', '.ppt': 'Documents', '.pptx': 'Documents',
            '.mp3': 'Audios', '.wav': 'Audios', '.aac': 'Audios', '.flac': 'Audios', '.ogg': 'Audios',
            '.mp4': 'Videos', '.avi': 'Videos', '.mov': 'Videos', '.wmv': 'Videos', '.mkv': 'Videos',
            '.pdf': 'PDFs',
            '.exe': 'Executables', '.dmg': 'Executables', '.apk': 'Executables',
            '.jpg': 'Images', '.jpeg': 'Images', '.png': 'Images', '.gif': 'Images', '.bmp': 'Images', '.tiff': 'Images', '.tif': 'Images', '.psd': 'Images', '.ai': 'Images', '.jfif': 'Images',
            '.zip': 'Archives', '.rar': 'Archives', '.7z': 'Archives', '.tar': 'Archives', '.gzip': 'Archives',
            '.jar': 'JARs'}

files = []
sorted_files = []
unsorted_files = []

def sort(file):
    root, ext = os.path.splittext(file)
    path = file_ext.get(ext, 'Unknown')

    if path == 'Unknown':
        unsorted_files.append(file)
    else:
        move_path = os.path.join(current_dir, path, file)
        try:
            shutil.move(file,move_path)
            logging.info(f"Moved file '{file}' to {path} folder")
            sorted_files.append(file)
        except Exception as e:
            logging.error(f"Error while moving file '{file}': {e}")

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
        exit()
    
    for file in files:
        sort(file)
        
    logging.info(f'Sorted files: {sorted_files}')
    logging.info(f'Unsorted files: {unsorted_files}')

if __name__ == '__main__':
    main()