import pyrebase
from picturesque.authenticate import auth_loop

config = {
    "apiKey": "AIzaSyBUO6lDdlrejfdqSlrHYLzaqft27VGdFXI",
    "authDomain": "image-repo-for-shopify.firebaseapp.com",
    "databaseURL": "https://image-repo-for-shopify-default-rtdb.firebaseio.com/",
    "storageBucket": "image-repo-for-shopify.appspot.com"
}


def main():
    # Configure firebase
    fb = pyrebase.initialize_app(config)

    # Get a reference to the auth service
    auth = fb.auth()

    # Run authentication loop
    user = None
    try:
        user = auth_loop(auth)
    except:
        return 0

    # Get a reference to the database service
    db = fb.database()



if __name__ == '__main__':
    main()
