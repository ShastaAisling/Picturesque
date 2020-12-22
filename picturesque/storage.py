from tkinter import Tk
from tkinter.filedialog import askopenfilename
from picturesque.tagging import tag_image
import os

def add_picture_to_storage(user, storage):
    # Open dialog to select image
    Tk().withdraw()
    filepath = askopenfilename()

    # Get name of image
    filename, fileext = os.path.splitext(filepath)
    filename = filename.split('/')[len(filename.split('/')) - 1]

    # Get tag for image
    tag = tag_image(filepath)

    try:
        # Verify the file is an image (jpg or png)
        if fileext != ".jpg" and fileext != ".png":
            raise TypeError
        # Upload image to repository
        id = user['localId']
        storage.child("user/{}/{}".format(id, filename)).put(filepath, user['idToken'])
        print("File {} uploaded successfully!".format(filename))
    except TypeError:
        print("File is not a .jpg or .png. Please try again.")
    except:
        print("Something went wrong. File not uploaded.")


def storage_loop(user, storage, db):
    while True:
        print("Options: 1 - Upload file, 2 - Search tag, 3 - Search filename, 4 - Quit")
        answer = input("Enter one of the options above: ")
        if int(answer) == 1:
            add_picture_to_storage(user, storage)
        elif int(answer) == 4:
            print("Exiting program.")
            return
        else:
            print("Not implemented yet.")
