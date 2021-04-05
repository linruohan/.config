import tkinter as tk
from tkinter import filedialog
import os

root = tk.Tk()
root.withdraw()

# file_path = filedialog.askopenfilenames()
file_paths=filedialog.askdirectory()
for root,dir,files in os.walk(file_paths):
    print(root,dir)
    for i in files:
        print(i)
# for f in file_path:
#     with open(f, 'r', encoding='utf-8') as fn:
#         fn.readline()
#         for line in fn.readlines():
#             li = line.strip()
#             print(li)
