from flask import Blueprint, render_template, request, redirect, url_for
from app.db import get_all_plates, add_plate, remove_plate

main = Blueprint('main', __name__)

@main.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        plate = request.form.get("plate")
        if plate:
            add_plate(plate)
        return redirect(url_for("main.index"))

    plates = get_all_plates()
    return render_template("index.html", plates=plates)

@main.route("/delete/<int:plate_id>")
def delete_plate(plate_id):
    remove_plate(plate_id)
    return redirect(url_for("main.index"))