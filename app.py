from flask import Flask, render_template, request, redirect, url_for
import subprocess
from threading import Timer
from file_manager import save_expenses, create_file, get_file_list, load_expenses
import os

app = Flask(__name__)

expenses = []

current_filepath = None

@app.route("/tracker")
def tracker():
    total = 0

    for expense in expenses:
        total += expense[1]

    current_filename = ""

    if current_filepath is not None:
        filename = os.path.basename(current_filepath)

        current_filename = os.path.splitext(filename)[0]

    return render_template(
        "tracker.html",
        expenses=expenses,
        total=total,
        current_filepath=current_filepath,
        current_filename=current_filename
    )
@app.route("/", methods = ['GET', 'POST'])
def home():
    if request.method == "POST":
        name = request.form['name']
        price = int(request.form['price'])

        expense = [name, price]
        expenses.append(expense)

    total = 0

    for expense in expenses:
        total += expense[1]

    files = get_file_list()

    return render_template(
        'index.html',
        expenses=expenses,
        total=total,
        files=files
        )


def open_chrom():
    chrom_path =  r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    subprocess.Popen([
        chrom_path, 
        "http://127.0.0.1:5000"
        ])

@app.route("/add-expense", methods=["POST"])
def add_expense():
    name = request.form["name"]
    price = int(request.form["price"])
    category = request.form["category"]

    expense = [name, price, category]
    expenses.append(expense)

    return redirect(url_for("tracker"))

@app.route("/save", methods=["POST"])
def save():
    if current_filepath is not None:
        save_expenses(current_filepath, expenses)

    return redirect(url_for("home"))

@app.route("/delete-list", methods=["POST"])
def delete_list():
    global expenses
    global current_filepath

    filename = request.form["filename"]

    filepath = os.path.join("data", filename)

    if os.path.exists(filepath):
        os.remove(filepath)

    if current_filepath == filepath:
        current_filepath = None
        expenses = []

    return redirect(url_for("home"))

@app.route("/create-list", methods=["POST"])
def create_list():
    global expenses
    global current_filepath

    filename = request.form["filename"]

    filepath = create_file(filename)

    if filepath is None:
        return redirect(url_for("home"))

    current_filepath = filepath
    expenses = []

    return redirect(url_for("tracker"))

@app.route("/load-list", methods=["POST"])
def load_list():
    global expenses
    global current_filepath

    filename = request.form["filename"]

    current_filepath = "data/" + filename
    expenses = load_expenses(current_filepath)

    return redirect(url_for("tracker"))


@app.route("/delete-expense", methods=["POST"])
def delete_expense():
    index = int(request.form["index"])

    if 0 <= index < len(expenses):
        expenses.pop(index)

    return redirect(url_for("tracker"))


@app.route("/edit-expense")
def edit_expense():
    index = int(request.args["index"])

    expense = expenses[index]

    return render_template(
        "edit.html",
        expense=expense,
        index=index
    )

@app.route("/update-expense", methods=["POST"])
def update_expense():
    index = int(request.form["index"])

    name = request.form["name"]
    price = int(request.form["price"])
    category = request.form["category"]

    if 0 <= index < len(expenses):
        expenses[index] = [name, price, category]

    return redirect(url_for("tracker"))
#맨 마지막에 유지
if __name__ == "__main__":
    Timer(1, open_chrom).start()
    app.run(debug=True, use_reloader=False)