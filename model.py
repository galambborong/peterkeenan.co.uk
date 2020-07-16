import json


def load_db_a():
    with open("public_db.json") as f:
        return json.load(f)


dba = load_db_a()


def load_db_b():
    with open("other_db.json") as f:
        return json.load(f)


dbb = load_db_b()


def load_db_c():
    with open("engraving_db.json") as f:
        return json.load(f)


dbc = load_db_c()


def load_db_d():
    with open("blog_db.json") as f:
        return json.load(f)


dbd = load_db_d()
