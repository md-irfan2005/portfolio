from flask import Flask, render_template, request, redirect, url_for
from models import db, Message

app = Flask(__name__)

# Configure SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/projects")
def projects():
    project_list = [
        {"title": "AI Text Summarizer", "desc": "Summarizes long text using NLP.", "link": "#"},
        {"title": "Micro Journal App", "desc": "Logs your daily thoughts.", "link": "#"}
    ]
    return render_template("projects.html", projects=project_list)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        msg = request.form["message"]
        new_msg = Message(name=name, email=email, message=msg)
        db.session.add(new_msg)
        db.session.commit()
        return redirect(url_for('contact'))
    
    all_messages = Message.query.order_by(Message.timestamp.desc()).all()
    return render_template("contact.html", messages=all_messages)

if __name__ == "__main__":
    app.run(debug=True)
