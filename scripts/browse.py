
import glob
import os
dir_name = 'D:/Personal/Git/'
list_of_files = filter( os.path.isfile, glob.glob(  dir_name + '/**/*', recursive = True) )
print(list(list_of_files))
