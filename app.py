"""Flask App for Flask Cafe."""


from flask import Flask, render_template, request, flash
from flask import redirect, session, g
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Cafe, City
from forms import AddEditCafeForm
from sqlalchemy.exc import IntegrityError

from secrets import FLASK_SECRET_KEY


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///flaskcafe_emi'
app.config['SECRET_KEY'] = FLASK_SECRET_KEY
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = True

toolbar = DebugToolbarExtension(app)

connect_db(app)


#######################################
# auth & auth routes

CURR_USER_KEY = "curr_user"
NOT_LOGGED_IN_MSG = "You are not logged in."


# @app.before_request
# def add_user_to_g():
#     """If we're logged in, add curr user to Flask global."""

#     if CURR_USER_KEY in session:
#         g.user = User.query.get(session[CURR_USER_KEY])

#     else:
#         g.user = None


# def do_login(user):
#     """Log in user."""

#     session[CURR_USER_KEY] = user.id


# def do_logout():
#     """Logout user."""

#     if CURR_USER_KEY in session:
#         del session[CURR_USER_KEY]


#######################################
# homepage

@app.route("/")
def homepage():
    """Show homepage."""

    return render_template("homepage.html")


#######################################
# cafes


@app.route('/cafes')
def cafe_list():
    """Return list of all cafes."""

    cafes = Cafe.query.order_by('name').all()

    return render_template(
        'cafe/list.html',
        cafes=cafes,
    )

@app.route('/cafes/<int:cafe_id>')
def cafe_detail(cafe_id):
    """Show detail for cafe."""

    cafe = Cafe.query.get_or_404(cafe_id)

    return render_template(
        'cafe/detail.html',
        cafe=cafe,
    )

@app.route("/cafes/add", methods=["GET", "POST"])
def cafe_add():
    """ show form for adding cafe and handle form"""
    form = AddEditCafeForm()

    #get city_code choice from current cities in db
    form.city_code.choices = City.get_all_cities()
    
    if form.validate_on_submit():
        new_cafe = Cafe(
            name=form.name.data,
            description=form.description.data,
            url=form.url.data,
            address=form.address.data,
            city_code=form.city_code.data,
            image_url=form.image_url.data or None
        )

        db.session.add(new_cafe)
        db.session.commit()
        
        flash(f'{new_cafe.name} added')
        return redirect(f"/cafes/{new_cafe.id}")
    
    return render_template("cafe/add-form.html", form=form)

@app.route('/cafes/<cafe_id>/edit', methods=["GET", "POST"])
def cafe_edit(cafe_id):
    """ show form for editting cafe and handle form"""
    cafe = Cafe.query.get(cafe_id)
    form = AddEditCafeForm(obj=cafe)

    #get city_code choice from current cities in db
    form.city_code.choices = City.get_all_cities()
    
    if form.validate_on_submit():
        cafe.name = form.name.data
        cafe.description = form.description.data
        cafe.url = form.url.data
        cafe.address = form.address.data
        cafe.city_code = form.city_code.data
        cafe.image_url = form.image_url.data 
        
        db.session.commit()
        
        flash(f'{cafe.name} edited')
        return redirect(f"/cafes/{cafe.id}")
    
    return render_template("cafe/edit-form.html", form=form, cafe=cafe)

    #######################################
    # users

    