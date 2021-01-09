from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from picturesque.tagging import tag_image
from picturesque.search import search_loop
import os


def add_picture_to_storage(user, storage, db):
    try:
        # Open dialog to select image
        root = Tk()
        root.withdraw()
        filepath = askopenfilename()
        root.update()
        if not filepath: raise FileExistsError

        # Get name of image
        filename, fileext = os.path.splitext(filepath)
        filename = filename.split('/')[len(filename.split('/')) - 1]

        # Verify the file is an image (jpg or png)
        if fileext != ".jpg" and fileext != ".png":
            raise TypeError

        # Run through tagging AI
        tag = tag_image(filepath)

        # Upload image to repository
        user_id = user['localId']
        storage.child("user/{}/{}".format(user_id, filename)).put(filepath, user['idToken'])
        print("File {} uploaded successfully!".format(filename))

        # Add metadata to database
        data = {filename: tag}
        db.child("users/{}/image-tag/".format(user_id)).update(data)

    except TypeError:
        print("File is not a .jpg or .png. Please try again.")
    except FileExistsError:
        print("No file selected.")
    except:
        print("Something went wrong. File not uploaded.")


def download_image(user, storage):
    # Get image name
    user_id = user['localId']
    image_name = input("Name of file (without .jpg or .png): ")
    try:
        # Try to download image
        root = Tk()
        root.withdraw()
        filepath = asksaveasfilename(defaultextension=".jpg")
        file_ref = "user/{}/{}".format(user_id, image_name)
        storage.child(file_ref).download(filepath)
        root.update()
        if os.path.isfile(filepath):
            print("Download succeeded!")
        else:
            raise FileExistsError
    except:
        print("Download failed. Did you enter an existing file?")
        return




def storage_loop(user, storage, db):
    while True:
        print("Options: 1 - Upload image, 2 - Search images, 3 - Download image, 4 - Quit")
        answer = input("Enter one of the options above: ")
        try:
            if int(answer) == 1:
                add_picture_to_storage(user, storage, db)
            elif int(answer) == 2:
                search_loop(user, db)
            elif int(answer) == 3:
                download_image(user, storage)
            elif int(answer) == 4:
                print("Exiting program.")
                return
            else:
                print("Please enter one of the options (1, 2, 3, or 4).")
        except ValueError:
            print("Please enter one of the options (1, 2, 3, or 4).")
