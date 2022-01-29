from cmath import e
import os, shutil
from zipfile import ZipFile

__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

cwd = os.getcwd()
file = f'{cwd}/files/data.zip'
cache_folder = f'{cwd}/files/cache'

# 1 (error handling - done right? - needs practice)
def clean_cache():
    if os.path.exists(cache_folder):
        for filename in os.listdir(cache_folder):
            file_path = os.path.join(cache_folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except OSError:
                print("Failed to delete %s. Reason: %s" % (file_path, e))
    try:  
        os.mkdir(cache_folder)
    except OSError:
        print("Creation of the directory %s failed" % cache_folder)
    else:
        print("Succesfully created the directory %s" % cache_folder)
clean_cache()


# 2
def cache_zip(file, cache_folder):
    clean_cache()
    with ZipFile(file, 'r') as zipObj:
        zipObj.extractall(cache_folder)
cache_zip(file, cache_folder)

# 3
def cached_files():
    path = os.path.abspath(cache_folder)
    return [entry.path for entry in os.scandir(cache_folder) if entry.is_file()]
cached_files()

# 4
def find_password(cached_files):
    for file in cached_files:
        with open(file) as f:
            for line in f:
                if "password:" in line:
                    start_index_password = len("password:")+1
                    password = line[start_index_password:]
                    return password
print(find_password(cached_files()))

