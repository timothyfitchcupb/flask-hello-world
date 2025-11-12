from flask import Flask                       
import psycopg2                              

app = Flask(__name__)

DB_URL = "postgresql://flask_hello_world_db_45a2_user:xIk0QjbcEemtuuLxLlQhp4SfqsgaeITc@dpg-d4a0mvidbo4c73c2jvn0-a/flask_hello_world_db_45a2"   

@app.route("/")
def index():
    return "Hello World from Timothy Fitch in 3308"            
@app.route("/db_test")
def db_test():
    conn = psycopg2.connect(DB_URL)                        
    conn.close()                                           
    return "Database connection successful"

@app.route("/db_create")
def db_create():
    conn = psycopg2.connect(DB_URL); cur = conn.cursor()   
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Basketball(
            First varchar(255),
            Last varchar(255),
            City varchar(255),
            Name varchar(255),
            Number int
        );
    """)
    conn.commit(); conn.close()
    return "Basketball table created"

@app.route("/db_insert")
def db_insert():
    conn = psycopg2.connect(DB_URL); cur = conn.cursor()
    cur.execute("""
        INSERT INTO Basketball (First, Last, City, Name, Number)
        VALUES
        ('Jayson','Tatum','Boston','Celtics',0),
        ('Stephen','Curry','San Francisco','Warriors',30),
        ('Nikola','Jokic','Denver','Nuggets',15),
        ('Kawhi','Leonard','Los Angeles','Clippers',2);
    """)
    conn.commit(); conn.close()
    return "Basketball table populated"

@app.route("/db_select")
def db_select():
    conn = psycopg2.connect(DB_URL); cur = conn.cursor()
    cur.execute("SELECT * FROM Basketball;")
    rows = cur.fetchall(); conn.close()

    
    html = "<table border='1'>"
    html += "<tr><th>First</th><th>Last</th><th>City</th><th>Name</th><th>Number</th></tr>"
    for r in rows:
        html += "<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>"
    html += "</table>"
    return html

@app.route("/db_drop")
def db_drop():
    conn = psycopg2.connect(DB_URL); cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS Basketball;")
    conn.commit(); conn.close()
    return "Basketball table dropped"

if __name__ == "__main__":
    app.run(host="0.0.0.0")                                
