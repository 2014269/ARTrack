from models.original import Original
from flask import Flask, render_template
from views.originals import original_blueprint
from views.users import user_blueprint

app = Flask(__name__)

app.register_blueprint(original_blueprint, url_prefix="/originals")
app.register_blueprint(user_blueprint, url_prefix="/users")

@app.route('/')
def landing():
    return render_template('landing.html')


if __name__ == "__main__":
    app.run(debug=True)
