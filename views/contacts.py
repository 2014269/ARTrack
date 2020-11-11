from flask import Blueprint, render_template, request, redirect, url_for, session
from models.original import Original
from models.contact import Contact
from flask import session, flash
from models.user import requires_login

contact_blueprint = Blueprint("contacts", __name__)


@contact_blueprint.route("/")
@requires_login
def index():
    contacts = Contact.find_many_by('user_email', session['email'])
    return render_template("contacts/index.html", contacts=contacts)


@contact_blueprint.route("/new", methods=['GET', 'POST'])
@requires_login
def new_contact():
    if request.method == "POST":
        # Populate the Data
        name_first = request.form["name_first"]
        name_last = request.form["name_last"]
        phone = request.form["phone"]
        email = request.form["email"]
        address = request.form["address"]
        user_email = session['email']

        # Initialize Object and save to database
        Contact(name_first,
                name_last,
                phone,
                email,
                address,
                user_email).save_to_mongo()

        #Success notification
        flash(f"{name_first} {name_last} successfully added to your contact list.", 'success')

    return render_template("contacts/new_contact.html")


@contact_blueprint.route("/edit/<string:contact_id>", methods=['GET', 'POST'])
@requires_login
def edit_contact(contact_id):
    if request.method == "POST":
        # Populate the Data
        name_first = request.form["name_first"]
        name_last = request.form["name_last"]
        phone = request.form["phone"]
        email = request.form["email"]
        address = request.form["address"]

        contact = Contact.get_by_id(contact_id)

        # Update data and save
        contact.name_first = name_first
        contact.name_last = name_last
        contact.phone = phone
        contact.email = email
        contact.address = address
        contact.save_to_mongo()

        # Future: some sort of confirmation that this worked
        return redirect(url_for('contacts.details_contact', contact_id=contact_id))

    return render_template("contacts/edit_contact.html", contact=Contact.get_by_id(contact_id))


@contact_blueprint.route("/delete/<string:contact_id>")
@requires_login
def delete_contact(contact_id):
    contact = Contact.get_by_id(contact_id)
    if contact.user_email == session['email']:
        contact.remove_from_mongo()
    return redirect(url_for(".index"))


@contact_blueprint.route("/details/<string:contact_id>")
@requires_login
def details_contact(contact_id):
    return render_template("contacts/details.html", contact=Contact.get_by_id(contact_id))
