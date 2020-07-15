import os
import json
import uuid

WORK_DIR = "C:\\Users\\yoyon\\Desktop\\blinkist_project"
categories, books = [], []

for dir_name in filter(lambda x: x.endswith("-en"), os.listdir(WORK_DIR)):
    category_name = dir_name[: -3].replace("-", " ").title()
    category_id = str(uuid.uuid4())
    category = {
        "model": "catalog.Category",
        "pk": category_id,
        "fields": {
            "category_name": category_name
        }
    }
    categories.append(category)

    for book_html in os.listdir(os.path.join(WORK_DIR, dir_name)):
        book_name = book_html.rsplit(".")[0].replace("-", " ").title()
        book_id = str(uuid.uuid4())
        if book_name.lower().endswith(" en"):
            book_name = book_name[: -3]
        book_text = ""
        with open(os.path.join(WORK_DIR, dir_name, book_html), "r", encoding="utf-8") as f:
            try:
                book_text = f.read()
            except UnicodeDecodeError:
                print("Cannot decode book " + book_name)

        book = {
            "model": "catalog.Book",
            "pk": book_id,
            "fields": {
                "title": book_name,
                "category_id": category_id,
                "text": book_text
            }
        }
        books.append(book)

with open(os.path.abspath("../fixtures/categories.json"), "w+") as f:
    f.write(json.dumps(categories))

print(books)

