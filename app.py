from flask import Flask, render_template, request, redirect, jsonify
import sqlite3

app = Flask(__name__)

# -DATABASE -
def connect_db():
    return sqlite3.connect("mis.db")

def create_table():
    con = connect_db()
    con.execute("""
    CREATE TABLE IF NOT EXISTS company(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        rd REAL,
        admin REAL,
        marketing REAL,
        profit REAL
    )
    """)
    con.commit()
    con.close()

create_table()

# -AI LOGIC --
def summary(p):
    if p > 25:
        return "Strong performance"
    elif p > 10:
        return "Stable growth"
    else:
        return "Needs improvement"

def mis_score(revenue, expense, profit_percent):
    score = (profit_percent * 1.5) + ((100-(expense/revenue)*100)*0.8)
    return int(score)

# - ROUTES -
@app.route("/")
def add_page():
    return render_template("add.html")

@app.route("/save", methods=["POST"])
def save():
    con = connect_db()
    con.execute("""
    INSERT INTO company(name,rd,admin,marketing,profit)
    VALUES(?,?,?,?,?)
    """,(
        request.form["name"],
        request.form["rd"],
        request.form["admin"],
        request.form["marketing"],
        request.form["profit"]
    ))
    con.commit()
    con.close()
    return redirect("/report")

@app.route("/report")
def report_page():
    return render_template("report.html")

@app.route("/api/data")
def api_data():
    con = connect_db()
    rows = con.execute("SELECT * FROM company").fetchall()
    con.close()

    data=[]
    for r in rows:
        total_expense = r[2]+r[3]+r[4]
        revenue = total_expense + r[5]
        profit_percent = (r[5]/revenue)*100

        score = mis_score(revenue,total_expense,profit_percent)

        if score>=80:
            status="High Performer"
        elif score>=50 :
            status="Stable Growth"
        else:
            status="Under Observation"

        data.append({
            "id": r[0], 
            "name": r[1],
            "revenue": round(revenue,2),
            "expense": round(total_expense,2),
            "profit": round(profit_percent,2),
            "summary": summary(profit_percent),
            "score": score,
            "status": status
        })

    return jsonify(data)

# -DELETE ROUTE -
@app.route("/delete/<int:company_id>", methods=["POST"])
def delete_company(company_id):
    """Delete a single company record by its id."""
    con = connect_db()
    con.execute("DELETE FROM company WHERE id = ?", (company_id,))
    con.commit()
    con.close()
    return jsonify({"success": True})

if __name__=="__main__":
    app.run(debug=True, host='localhost', port=5095)