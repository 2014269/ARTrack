from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from models.original import Original
from flask import session
from models.user import requires_login


original_blueprint = Blueprint("originals", __name__)


@original_blueprint.route("/")
@requires_login
def index():
    originals = Original.find_many_by('user_email', session['email'])
    return render_template("originals/index.html", originals=originals)


@original_blueprint.route("/new", methods=['GET', 'POST'])
@requires_login
def new_original():
    if request.method == "POST":
        # Populate the Data
        title = request.form["title"]
        medium = request.form["medium"]
        dimensions = request.form["dimensions"]
        price = request.form["price"]
        date_created = request.form["date_created"]
        status = request.form["status"]
        possession = request.form["possession"]
        has_prints = request.form["has_prints"]
        is_commission = request.form["is_commission"]
        user_email = session['email']

        # Initialize Object and save to database
        Original(title,
                 medium,
                 dimensions,
                 price,
                 date_created,
                 status,
                 possession,
                 has_prints,
                 is_commission,
                 user_email).save_to_mongo()

        # Future: some sort of confirmation that this worked
        flash(f"{title} successfully added to your collection.", 'success')
    return render_template("originals/new_original.html")


@original_blueprint.route("/edit/<string:original_id>", methods=['GET', 'POST'])
@requires_login
def edit_original(original_id):
    if request.method == "POST":
        # Populate the Data
        title = request.form["title"]
        medium = request.form["medium"]
        dimensions = request.form["dimensions"]
        price = request.form["price"]
        date_created = request.form["date_created"]
        status = request.form["status"]
        possession = request.form["possession"]
        has_prints = request.form["has_prints"]
        is_commission = request.form["is_commission"]

        original = Original.get_by_id(original_id)

        # Update data and save
        original.title = title
        original.medium = medium
        original.dimensions = dimensions
        original.price = price
        original.date_created = date_created
        original.status = status
        original.possession = possession
        original.has_prints = has_prints
        original.is_commission = is_commission
        original.save_to_mongo()

        # Future: some sort of confirmation that this worked
        return redirect(url_for('originals.details_original', original_id=original_id))

    return render_template("originals/edit_original.html", original=Original.get_by_id(original_id))


@original_blueprint.route("/delete/<string:original_id>")
@requires_login
def delete_original(original_id):
    original = Original.get_by_id(original_id)
    if original.user_email == session['email']:
        original.remove_from_mongo()
    return redirect(url_for(".index"))


@original_blueprint.route("/details/<string:original_id>")
@requires_login
def details_original(original_id):
    return render_template("originals/details.html", original=Original.get_by_id(original_id))
