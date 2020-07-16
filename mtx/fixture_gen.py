import os
import json
import uuid

WORK_DIR = "C:\\Users\\yoyon\\Desktop\\blinkist_project"
categories, books = [], []
book_count, error_count = 0, 0

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
        book_count += 1

        try:
            with open(os.path.join(WORK_DIR, dir_name, book_html), "r", encoding="cp1252") as f:
                book_text = f.read()
        except UnicodeDecodeError as e:
            try:
                with open(os.path.join(WORK_DIR, dir_name, book_html), "r", encoding="utf-8") as f:
                    book_text = f.read()
            except UnicodeDecodeError as e:
                print("Cannot decode book " + book_name)
                print(str(e))
                error_count += 1

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

    with open(os.path.join(os.path.abspath("../fixtures"), category_name + ".json"), "a+") as f:
        f.write(json.dumps(books))

with open(os.path.abspath("../fixtures/categories.json"), "w+") as f:
    f.write(json.dumps(categories))
