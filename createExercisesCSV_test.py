from os import listdir
from os.path import isfile, join
import tkinter as tk
from tkinter.filedialog import askdirectory
import base64

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

print(names)
# print(imgStr)