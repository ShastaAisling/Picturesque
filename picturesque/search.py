import json

def list_all(user_id, db):
    try:
        all_images = db.child("users").child(user_id).child("image-tag").get().val()
        pretty_print_results(all_images)
    except:
        all_images = "No images exist."
        print(all_images)

def search_by_tag(user_id, db):
    query = input("Search for: ")
    try:
        all_images = db.child("users").child(user_id).child("image-tag").order_by_value().equal_to(query).get().val()
        pretty_print_results(all_images)
    except:
        all_images = "No images exist with this tag."
        print(all_images)

def search_by_name(user_id, db):
    return 0

def pretty_print_results(all_images):
    print("Name : Tag")
    print(json.dumps(all_images, indent=4))


def search_loop(user, storage, db):
    print("Options: 1 - List all files, 2 - Search tag, 3 - Search filename, 4 - Exit")
    answer = input("Enter one of the options above: ")
    if int(answer) == 1:
        list_all(user['localId'], db)
    elif int(answer) == 2:
        search_by_tag(user['localId'], db)
    elif int(answer) == 3:
        search_by_name(user['localId'], db)
    elif int(answer) == 4:
        print("Exiting program.")
        return
    else:
        print("Please enter one of the options (1, 2, 3, or 4).")

