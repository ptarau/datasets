import os
import shutil
import zipfile
import urllib.request

def extract_zip(path: str, folder: str):
    with zipfile.ZipFile(path, 'r') as f:
        f.extractall(folder)

def fetch_tox21():
   shutil.rmtree("tox21_full_data/")
   url="https://raw.githubusercontent.com/ptarau/datasets/master/tox21_full_data.zip"
   filename, headers = urllib.request.urlretrieve(url, filename="datafile.zip")
   extract_zip(filename,'datafolder')
   os.rename("datafolder/tox21_full_data/", "./tox21_full_data/")
   os.remove('datafile.zip')
   shutil.rmtree("datafolder/")

if __name__=="__main__":
    fetch_tox21()
