from flask import Flask, render_template, url_for, jsonify, Request, Response, request
import sqlite3


server_password = 'Testing123'

allowed_ip = ['127.0.0.1']


app = Flask(__name__)
app.config["DEBUG"] = True


with sqlite3.connect("mainDB.db", timeout = 15) as conn:
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS Users(username TEXT, password TEXT, email TEXT, balance REAL)''')
    c.execute('''CREATE TABLE IF NOT EXISTS Server(blocks REAL, lastBlockHash TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS Transactions(timestamp TEXT, username TEXT, recipient TEXT, amount REAL, hash TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS Blocks(timestamp TEXT, finder TEXT, amount REAL, hash TEXT)''')


    # c.execute('''CREATE TABLE IF NOT EXISTS Jobs(blocks REAL, lastBlockHash TEXT)''')

    conn.commit()


    # datab.execute("INSERT INTO Server(blocks, lastBlockHash) VALUES(?, ?)", (1, "ba29a15896fd2d792d5c4b60668bf2b9feebc51d"))
    # conn.commit()

@app.route("/api/database", methods=['GET','POST'])
def database():
    ip_address = request.remote_addr
    if ip_address not in allowed_ip:
        return jsonify({'error': 'You are not allowed to access this'})


    if 'query' not in request.args:
        return (jsonify({"error": "No query Provided"}))
    else:
        query = request.args.get('query')



    try:
        with sqlite3.connect("mainDB.db", timeout = 15) as conn:
            c = conn.cursor()

            c.execute(f"{query}")
            conn.commit()

            if "SELECT" in query:
                if 'fetch' in request.args:
                    if request.args.get('fetch') == "one":
                        return jsonify({'value': c.fetchone()})

                    elif request.args.get('fetch') == "all":
                        return jsonify({'value': c.fetchall()})

                else:
                    return jsonify({'value': c.fetchall()})

    except Exception as e:
        return jsonify({'error': str(e)})


    return jsonify({'value': 'success'})



@app.route("/", methods=['GET','POST'])
def home():
    ip_address = request.remote_addr
    print('ip_address', ip_address)
    return jsonify(ip_address)


