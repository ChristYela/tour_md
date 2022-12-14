
from tokenize import Comment
from flask import render_template, redirect, session, request, flash
import flask
from flask_app import app
from flask_app.models.comments import Comments
from werkzeug.utils import secure_filename
import os


from flask_app.models.users import User

from flask_app.models.tour import Tour


@app.route('/new/place')
def new_tour():

    if 'usuario_id' not in session:
        return redirect('/')

    formulario = {
        "id": session['usuario_id']
    }

    user = User.get_by_id(formulario)
    tours = Tour.get_image_by_admin(formulario)

    return render_template('new_tour.html', user=user, tours=tours)


@app.route('/create/tour', methods=['POST'])
def create_tour():
    if 'usuario_id' not in session:
        return redirect('/')

    if not Tour.valida_tour(request.form):
        return redirect('/new/place')

    Tour.save(request.form)

    return redirect('/dashboard')


@app.route('/like', methods=['POST'])
def like_place():
    Tour.likes(request.form)
    return redirect('/dashboard')


@app.route('/places', methods=['POST'])
def contar():
    Tour.insert_like(request.form)
    return redirect('/show/place/' + request.form['place_id'])


# !NO PUEDO UTLIZAR RUTAS CON EL MISMO NOMBRE!
@app.route('/show/place/<int:id>')
def show_tour(id):
    if 'usuario_id' not in session:
        return redirect('/')

    formulario = {
        "id": session['usuario_id']
    }
    user = User.get_by_id(formulario)
    formulario_m = {"id": id}
    # Como ya tenemos el formulario que teniamos en la ruta anterior de comments no hay nesesidad de repetirlos solo llamar comments y con el mismas variables que seria(formulario_m) ya que esa era la variable que creamos
    comments = Comments.get_all(formulario_m)

    tour = Tour.get_by_id(formulario_m)
    mag = Tour.get_all()
    likes = []
    data = {}
    for revista in mag:
        num_likes = Tour.contar_likes(revista.id)
        n = num_likes[0]['num_likes']
        data[revista] = n

    return render_template('show_tour.html', user=user, tour=tour, data=data, comments=comments)


@app.route('/nightclubs')
def night_clubs():
    if 'usuario_id' not in session:
        return redirect('/')

    formulario = {
        "id": session['usuario_id']
    }

    user = User.get_by_id(formulario)

    tour = Tour.get_all()

    return render_template('clubs.html', theclubs=tour, user=user)


@app.route('/restaurants')
def rests():
    if 'usuario_id' not in session:
        return redirect('/')

    formulario = {
        "id": session['usuario_id']
    }

    user = User.get_by_id(formulario)

    tour = Tour.get_all()

    return render_template('restaurants.html', therests=tour, user=user)


@app.route('/coffee')
def coffee():
    if 'usuario_id' not in session:
        return redirect('/')

    formulario = {
        "id": session['usuario_id']
    }

    user = User.get_by_id(formulario)

    tour = Tour.get_all()

    return render_template('coffees.html', thecoffee=tour, user=user)


@app.route('/museum')
def museum():
    if 'usuario_id' not in session:
        return redirect('/')

    formulario = {
        "id": session['usuario_id']
    }

    user = User.get_by_id(formulario)

    tour = Tour.get_all()

    return render_template('musetheat.html', themuseum=tour, user=user)


@app.route('/nature')
def nature():
    if 'usuario_id' not in session:
        return redirect('/')

    formulario = {
        "id": session['usuario_id']
    }

    user = User.get_by_id(formulario)

    tour = Tour.get_all()

    return render_template('nature.html', thenature=tour, user=user)


@app.route('/others')
def others():
    if 'usuario_id' not in session:
        return redirect('/')

    formulario = {
        "id": session['usuario_id']
    }

    user = User.get_by_id(formulario)

    tour = Tour.get_all()

    return render_template('otherpl.html', theothersplaces=tour, user=user)


@app.route('/delete/tour/<int:id>')
def delete_tour(id):
    if 'usuario_id' not in session:
        return redirect('/')

    formulario = {"id": id}
    Tour.delete(formulario)

    return redirect('/edit/user/<id>')


# GUARDAR COMETARIOS
@app.route("/comments", methods=['POST'])
def comments():
    Comments.save_comments(request.form)
    return redirect('/show/place/' + request.form["place_id"])
