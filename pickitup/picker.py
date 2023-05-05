import os
import shutil
import time
import calendar
import json

def program():
    with open('extensions.json') as file:
        extensions = json.load(file) 

    files = os.listdir(os.curdir)
    filelist = []
    for f in files:
        filelist.append(f)

    def ext_folders():
        for file in filelist:
            filename ,file_extension = os.path.splitext(file)
            for category in types:
                if file_extension in types[category]:
                    path = "./" + category
                    if os.path.exists(path) == False:
                        os.makedirs(path) 

        for file in filelist:
            filename ,file_extension = os.path.splitext(file)
            for category in types:
                if file_extension in types[category]:
                    dst_path = "./" + category + "/" + file
                    src_path = "./" + file
                    try:
                        shutil.move(src_path, dst_path)
                    except:
                        pass

    def size_folders():
        for file in filelist:
            file_source = "./" + file
            file_size = os.stat(file_source)
            if file_size.st_size < 1000000:
                if os.path.exists("./Less Than 1 MB") == False:
                    os.makedirs("./Less Than 1 MB")
                try:
                    shutil.move(file_source, "./Less Than 1 MB/"+file)
                except:
                    pass
            elif 1000000 <= file_size.st_size and file_size.st_size < 10000000:
                if os.path.exists("./1-10 MB") == False:
                    os.makedirs("./1-10 MB")
                try:
                    shutil.move(file_source, "./1-10 MB/"+file)
                except:
                    pass
            elif 10000000 <= file_size.st_size and file_size.st_size < 100000000:
                if os.path.exists("./10-100 MB") == False:
                    os.makedirs("./10-100 MB")
                try:
                    shutil.move(file_source, "./10-100 MB/"+file)
                except:
                    pass
            elif 100000000 <= file_size.st_size and file_size.st_size < 1000000000:
                if os.path.exists("./100 MB - 1 GB") == False:
                    os.makedirs("./100 MB - 1 GB")
                try:
                    shutil.move(file_source, "./100 MB - 1 GB/"+file)
                except:
                    pass
            elif file_size.st_size >= 1000000000:
                if os.path.exists("./More than 1 GB") == False:
                    os.makedirs("./More than 1 GB")
                try:
                    shutil.move(file_source, "./More than 1 GB/"+file)
                except:
                    pass

    def date_folders():
        for file in filelist:
            file_source = "./" + file
            file_mod_date = time.localtime(os.path.getmtime(file_source))
            folder_name = calendar.month_abbr[file_mod_date.tm_mon] + " " + str(file_mod_date.tm_year)
            folder_path = "./" + folder_name
            if os.path.exists(folder_path) == False:
                os.makedirs(folder_path)
            try:
                shutil.move(file_source, folder_path)
            except:
                pass

    print("PickItUp 1.0\nCommands:\n ext: Folder by extension\n date: Folder by modification date\n size: Folder by file size\n quit: Quit PickItUp")
    action = input("> ")

    while True:
        if action == "ext" or action == "size" or action == "date" or action == "quit":
            break
        else:
            print("Command not found")
            action = input("> ")
        
    if action == "ext":
        ext_folders()
    elif action == "date":
        date_folders()
    elif action == "size":
        size_folders()
    elif action == "quit":
        quit()
  
