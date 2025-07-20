import os    #importing module
from datetime import datetime

#print(dir(os))   #attributes & methods that we have access

# print(os.getcwd())          #prints current working directory

# os.chdir('/Users/Lenovo/OneDrive/Desktop/vscode/python-learning-series')    #change directory to this 

# print(os.getcwd())   #now print changed directory

# print(os.listdir())    #it list the folders from the current working directory


# os.mkdir('test-folder')    #it is used to create folder not subfolder
# os.makedirs('test-folder-1/test-1.txt')    # it can create both folder and subfolder at once

# os.rmdir('test-folder')   #it is used to delete folder only not subfolder
# os.removedirs('test-folder-1/test-1.txt')      # it can delete both folder and subfolder at once


# os.mkdir('test-folder')
# os.rename('test-folder' , 'demo-folder')   #rename test-folder to demo-folder

# os.mkdir('demo.txt')
# print(os.stat('demo.txt').st_size)     # print size
# print(os.stat('demo.txt').st_mtime)

# mod_time = os.stat('demo.txt').st_mtime   #time when file created
# print(datetime.fromtimestamp(mod_time))   #human readable format

# for dirpath , dirnames, filenames in  os.walk('/Users/Lenovo/OneDrive/Desktop/vscode/python-learning-series'):   # it's like a tree it prints all current path , dir name and files name all of
#     print('Current path:' , dirpath)
#     print('Directories:', dirnames)
#     print('files:', filenames)
#     print()

# print(os.environ.get('Home'))   #home directory

# file_path = os.path.join(os.environ.get('USERPROFILE') , 'test.txt')  
# print(file_path)     # output:  C:\Users\Lenovo\test.txt


print(os.path.basename('/tmp/test.txt'))  #o: test.txt
print(os.path.dirname('/tmp/test.txt'))   #o: /tmp
print(os.path.split('/tmp/test.txt'))     #o: ('/tmp', 'test.txt')

print(os.path.exists('/tmp/test.txt'))    #o: False   :-because path not exists

print(os.path.splitext('/tmp/test.txt'))    #o: ('/tmp/test', '.txt')

print(dir(os.path))

























