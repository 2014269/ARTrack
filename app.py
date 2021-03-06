import os
from models.original import Original
from flask import Flask, render_template
from views.originals import original_blueprint
from views.users import user_blueprint
from views.contacts import contact_blueprint

app = Flask(__name__)
app.secret_key = os.urandom(64)
app.config.update(
    ADMIN=os.environ.get('ADMIN')
)

app.register_blueprint(original_blueprint, url_prefix="/originals")
app.register_blueprint(user_blueprint, url_prefix="/users")
app.register_blueprint(contact_blueprint, url_prefix='/contacts')


@app.route('/')
def landing():
    return render_template('landing.html')


if __name__ == "__main__":
    app.run(debug=True)
