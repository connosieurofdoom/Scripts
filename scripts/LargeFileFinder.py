import glob
import os

from tkinter import filedialog
from tkinter import *

dir_name = ''

def lfs(x):
    s = os.stat(x).st_size/(1024*1024)
    if s > 1000:
        print(x)
        return True
    else:
        return False

def browse_button():
    global dir_name
    filename = filedialog.askdirectory()
    print(filename, type(filename))
    dir_name = filename
    
    # Get list of files in a directory
    list_of_files = filter( os.path.isfile, glob.glob(  dir_name + '/**/*', recursive=True) )
    #print(list(list_of_files))
    # Find the file with max size from the list of files
    max_file = max( list_of_files, key =  lambda x: os.stat(x).st_size)
    large_file = filter(lfs, list(list_of_files))
    print('Max File: ', max_file)
    print('Max File size in MB: ', os.stat(max_file).st_size/(1024*1024))
    print('Large Files:')
    for s in large_file:
        print(s)
    # return filename


root = Tk()
v = StringVar()
button2 = Button(text="Browse", command=browse_button).grid(row=0, column=3)
#print(lfs("D:\\Personal\\phdapplicationdocs\\Canada\\Saskatchewan\\Zadia_task\\Task_3\\ShreyasKeelary_Task3.ipynb - Colaboratory.pdf"))
mainloop()




