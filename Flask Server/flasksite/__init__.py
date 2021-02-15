from flask import Flask, render_template, url_for
import sqlite3


app = Flask(__name__)
app.config["DEBUG"] = True


with sqlite3.connect("mainDB.db", timeout = 15) as conn:
    datab = conn.cursor()

    datab.execute('''CREATE TABLE IF NOT EXISTS Users(username TEXT, password TEXT, email TEXT, balance REAL)''')
    datab.execute('''CREATE TABLE IF NOT EXISTS Server(blocks REAL, lastBlockHash TEXT)''')

    # datab.execute('''CREATE TABLE IF NOT EXISTS Jobs(blocks REAL, lastBlockHash TEXT)''')

    conn.commit()


    # datab.execute("INSERT INTO Server(blocks, lastBlockHash) VALUES(?, ?)", (1, "ba29a15896fd2d792d5c4b60668bf2b9feebc51d"))
    # conn.commit()

conn = sqlite3.connect("mainDB.db", timeout = 15)
c = conn.cursor()









from os import walk
import importlib


blueprint_dirnames = []
for (dirpath, dirnames, filenames) in walk("flasksite/Blueprints"):
    blueprint_dirnames.extend(dirnames)
    break

for lib in blueprint_dirnames:
    lib_mod = f'flasksite.Blueprints.{lib}.routes'
    # print(f"{bcolors.OKGREEN}Success: Successfully imported blueprint: {bcolors.ENDC}{bcolors.OKBLUE}{lib}{bcolors.ENDC}")
    cls = getattr(importlib.import_module(lib_mod), lib)
    app.register_blueprint(cls)
    logging.info(f"Successfully imported blueprint: {lib}")






