from cmath import e
import os, shutil
from zipfile import ZipFile

__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

# HERKANSING: # commentaar mentor bij eerste versie ## mijn reactie
dir_path = os.path.dirname(os.path.realpath(__file__))
cache_folder = os.path.join(dir_path, 'cache')
zip_file = os.path.abspath("files/data.zip")

# cache_folder = f'{os.getcwd}/files/cache' - niet vindbaar op alle systemen - gebruik os.path.join(cwd, 'cache') ## gedaan

# beter geen globale variabele voor cache_folder (als daar een fout in zit, gaan alle functies fout) ## toch globale variabele aangehouden voor cache_folder en zip_file: functie 2 is dan beter leesbaar dan met een uitgeschreven pad als argument

# 1
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
    else:
        os.mkdir(cache_folder) # geen OSError ## try - except verwijderd 
clean_cache()


# 2
def cache_zip(zip_file, cache_folder):
    clean_cache()
    with ZipFile(zip_file, 'r') as zipObj:
        zipObj.extractall(cache_folder)
cache_folder = os.path.join(dir_path, 'cache')
zip_file = os.path.abspath("files/data.zip")
cache_zip(zip_file, cache_folder)

# 3
def cached_files():
    return [entry.path for entry in os.scandir(cache_folder) if entry.is_file()]
cached_files()

# 4
def find_password(cached_files):
    for file in cached_files:
        with open(file) as f:
            for line in f:
                if "password:" in line:
                    start_index_password = len("password:")+1
                    password = line.strip()[start_index_password:]
                    return password # probleem met white spaces of new lines, bij Rishaan geeft wincpy rood; ## waarschijnlijk opgelost met .strip()
print(find_password(cached_files()))

