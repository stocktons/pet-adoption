"""Flask app for adopt app."""

from flask import Flask, render_template, request, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet

from forms import AddPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

@app.route("/")
def show_pets_list(): 
    """Shows list of all pets."""

    pets = Pet.query.all()

    return render_template("pet_listing.html", pets=pets)

@app.route("/add", methods=["GET", "POST"])
def add_pet_form():
    """Pet add form; handle adding."""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data or None
        age = form.age.data
        notes = form.notes.data
        available = None

        pet = Pet(name=name,
                  species=species,
                  photo_url=photo_url,
                  age=age,
                  notes=notes,
                  available=available)
        
        db.session.add(pet)
        db.session.commit()

        return redirect("/")
    else:
        return render_template("add_pet_form.html", form=form)