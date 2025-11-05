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