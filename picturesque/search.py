
def search_by_tag(user_id, db):
    query = input("Search for: ")
    all_images = db.child("users").child(user_id).child("image-tag").order_by_value().equal_to(query).get().val()
    print(all_images)
