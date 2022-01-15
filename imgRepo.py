import tkinter as tk
import tkinter.filedialog as fd
import os
import shutil
acceptedFiles= [('image files', ('.png', '.jpg'))] #control of allowed image file types
'''
To Do:
make a UI for the add items
upload to github
'''

def addImg():
    root = tk.Tk()
    files = fd.askopenfilenames(parent=root, title="Select files", filetypes=acceptedFiles)
    existFolder = input("Do you have folder where you would like to store this? Enter 1 if yes else enter 0:")#0 is a suggestion as anything other than 1 will cause a fail
    copied = 0

    if(existFolder == "1"):
        folder = fd.askdirectory(title="What Folder would like to use?")
        print(f"Using folder {folder}")

        for file in files:
            lastBackslash = file.rindex("/")
            target = f"{folder}{file[lastBackslash:]}"

            shutil.copyfile(file, target)
            copied+=1


    else:
        while(True):
            newFolderName = input(
                "Name the new folder:\t")  # make a new folder then have the user pick the one that was just created
            if(os.path.exists(os.getcwd()+f"\\{newFolderName}")==False):
                os.makedirs(newFolderName)
                folder = f"{os.getcwd()}\{newFolderName}"
                print(f"Using folder {folder}")

                for file in files:
                    lastBackslash = file.rindex("/")
                    target = f"{folder}{file[lastBackslash:]}"

                    shutil.copyfile(file, target)
                    copied += 1
                break
            else: #handles a duplicate folder
                print(f"Using {os.getcwd()}\\{newFolderName}")
                folder = f"{os.getcwd()}\{newFolderName}"
                for file in files:
                    lastBackslash = file.rindex("/")
                    target = f"{folder}{file[lastBackslash:]}"
                    shutil.copyfile(file, target) #simulates uploading to a new location
                    copied+=1
                break
            break


    print(f"Done uploading {len(files)} files")
    return copied #return value to be used in testing

#addImg()