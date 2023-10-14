import firebase_admin
import google.cloud
from firebase_admin import credentials, firestore

from os import listdir
from os.path import isfile, join
import tkinter as tk
from tkinter.filedialog import askdirectory
import base64

cred = credentials.Certificate("./ServiceAccountKey.json")
app = firebase_admin.initialize_app(cred)

store = firestore.client()


root = tk.Tk()
root.withdraw()

path = askdirectory(title='Select Folder')
print(path)

filenames = [f for f in listdir(path) if isfile(join(path, f))]
print(filenames)

names = []
imgStr = []

for f in filenames:
    parts = f.split("-")
    name = " ".join(parts)
    parts = name.split("_")
    name = parts[0]

    filepath = join(path, f)
    binary_fc       = open(filepath, 'rb').read()  # fc aka file_content
    base64_utf8_str = base64.b64encode(binary_fc).decode('utf-8')
    ext     = filepath.split('.')[-1]
    dataurl = f'data:image/{ext};base64,{base64_utf8_str}'

    names.append(name)
    imgStr.append(dataurl)

    doc_ref = store.collection('exercises').document(name)
    doc_ref.set({'name': name, 'imgHref': dataurl})


# #write to firestore db
# doc_ref = store.collection('test').document("ciao")
# doc_ref.set({'name': 'test', 'added': 'just now'})