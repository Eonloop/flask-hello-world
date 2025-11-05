from flask import Flask
import psycopg2
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World from Ian Jones in 3308'

@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("postgresql://flask_hello_world_crpk_user:kUVYi3G5SWBKIcqbhBBUjnIptSblXwIf@dpg-d45pj4ili9vc7385q5p0-a.oregon-postgres.render.com/flask_hello_world_crpk")
    conn.close()
    return 'Database connection test successful'

@app.route('/db_create')
def db_create():
    conn = psycopg2.connect("postgresql://flask_hello_world_crpk_user:kUVYi3G5SWBKIcqbhBBUjnIptSblXwIf@dpg-d45pj4ili9vc7385q5p0-a.oregon-postgres.render.com/flask_hello_world_crpk")
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball(
            First varchar(255),
            Last varchar(255),
            City varchar(255),
            Name varchar(255),
            Number int
            );
    ''')
    conn.commit()
    conn.close()
    return 'Basketball Table Successfully Created'