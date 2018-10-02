from flask import Flask, g
import mysql.connector
import json

app = Flask(__name__)

app.config["DATABASE_USER"] = "root"
app.config["DATABASE_PASSWORD"] = "root"
app.config["DATABASE_DB"] = "statistics"
app.config["DATABASE_HOST"] = "db"
app.config["DATABASE_PORT"] = "3306"

def get_db():
    if not hasattr(g, "_database"):
        g._database = mysql.connector.connect(host=app.config["DATABASE_HOST"],
                                              user=app.config["DATABASE_USER"],
                                              password=app.config["DATABASE_PASSWORD"],
                                              database=app.config["DATABASE_DB"],
                                              port=app.config["DATABASE_PORT"])
    return g._database


@app.route('/')
def test_content():
    db = get_db()
    cur = db.cursor()
    try:
        sql = "SELECT f_name, s_name FROM customer"
        cur.execute(sql)
        names=[]
        for (f_name, s_name) in cur:
            names.append({ "f_name":f_name,
                            "s_name": s_name})
        return json.dumps(names)
    except mysql.connector.Error:
        return False
    finally:
        cur.close()




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)