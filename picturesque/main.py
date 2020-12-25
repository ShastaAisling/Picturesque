import pyrebase
from picturesque.authenticate import auth_loop
from picturesque.storage import storage_loop

# Setup API config
config = {
    "apiKey": "AIzaSyBUO6lDdlrejfdqSlrHYLzaqft27VGdFXI",
    "authDomain": "image-repo-for-shopify.firebaseapp.com",
    "databaseURL": "https://image-repo-for-shopify-default-rtdb.firebaseio.com/",
    "storageBucket": "image-repo-for-shopify.appspot.com"
}


# Main program loop
def main():
    # Configure firebase
    fb = pyrebase.initialize_app(config)

    # Get a reference to the auth service
    auth = fb.auth()
    # Get a reference to the database service
    db = fb.database()
    # Get a reference to the storage service
    storage = fb.storage()

    # Run authentication loop
    try:
        user = auth_loop(auth)
    except SystemExit:
        return 0

    storage_loop(user, storage, db)


if __name__ == '__main__':
    main()
