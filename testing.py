
file_ext = {'.doc': 'Documents', '.docx': 'Documents', '.odt': 'Documents', '.txt': 'Documents', '.rtf': 'Documents', '.xls': 'Documents', '.xlsx': 'Documents', '.csv': 'Documents', '.ppt': 'Documents', '.pptx': 'Documents',
            '.mp3': 'Audios', '.wav': 'Audios', '.aac': 'Audios', '.flac': 'Audios', '.ogg': 'Audios',
            '.mp4': 'Videos', '.avi': 'Videos', '.mov': 'Videos', '.wmv': 'Videos', '.mkv': 'Videos',
            '.pdf': 'PDFs',
            '.exe': 'Executables', '.dmg': 'Executables', '.apk': 'Executables',
            '.jpg': 'Images', '.jpeg': 'Images', '.png': 'Images', '.gif': 'Images', '.bmp': 'Images', '.tiff': 'Images', '.tif': 'Images', '.psd': 'Images', '.ai': 'Images', '.jfif': 'Images',
            '.zip': 'Archives', '.rar': 'Archives', '.7z': 'Archives', '.tar': 'Archives', '.gzip': 'Archives'}

print(file_ext)


import os
import shutil

# def sort(file):
#     root, ext = os.path.splitext(file)
#     if ext in image:
#         move_path = os.path.join(current_dir,'Images', file)
#         try:
#             shutil.move(file,move_path)
#             logging.info(f"Moved '{file}' to Images folder")
#             sorted_files.append(file)
#         except Exception as e:
#             logging.error(f"Error while moving file '{file}': {e}")

current_dir = os.getcwd()

def sort(file):
    root, ext = os.path.splittext(file)
    path = file_ext.get(ext, 'Unknown')

    if path == 'Unknown':
        # log unsorted
        pass
    else:
        move_path = os.path.join(current_dir, path, file)
        try:
            shutil.move(file,move_path)
            # log moved
            # append into sorted
        except Exception as e:
            # log error
            pass

# yea this should work



# starts
# checks for certain folders in the current working directory, if trueL do nothing else create them
# feteches all the files in the directory and makes a list of it
# if none ends
# compares the ext of the files and sorts them acco to it
# ends