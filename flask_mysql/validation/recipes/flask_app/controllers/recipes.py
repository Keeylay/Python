from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt

from flask_app.models.recipe import Recipe
from flask_app.models.user import User

bcrypt = Bcrypt(app)

@app.route('/dashboard')
def dashboard():
    if 'email' not in session:
        flash('Log in to view dashboard')
        return redirect('/')
    return render_template("dashboard.html", recipes = Recipe.recipe_dashboard())

@app.route('/recipe/new')
def new_recipe():
    return render_template("add_recipe.html")

@app.route('/create/recipe', methods=["POST"])
def create_recipe():

    valid = Recipe.recipe_validation(request.form)

    if valid:
        data = {
            'name' : request.form['name'],
            'description' : request.form['description'],
            'instruction' : request.form['instruction'],
            'preptime' : request.form['preptime'],
            'user_id': session['id']
        }
        Recipe.add_recipe(data)
        return redirect('/dashboard')

    return redirect('/recipe/new')



@app.route('/recipe/<int:id>/edit')
def recipe_update(id):
    return render_template('edit_recipe.html', edit_recipe = Recipe.show_edit({'id': id}))




@app.route('/recipe/<int:id>')
def show_recipe(id):
    return render_template('show_recipe.html', recipe = Recipe.show_edit({'id': id}))


    

@app.route('/recipe/delete/<int:id>')
def delete_recipe(id):
    data = {
        'id':id
    }
    Recipe.delete_recipe(data)
    return redirect('/dashboard')

@app.route('/recipe/update', methods=['POST','GET'])
def edit_recipe():

    valid = Recipe.recipe_validation(request.form)

    if valid:
        data = {
            'name' : request.form['name'],
            'description' : request.form['description'],
            'instruction' : request.form['instruction'],
            'preptime' : request.form['preptime'],
            'id':request.form['id'],
            'user_id': session['id']
        }
        Recipe.edit_recipe(data)
        return redirect('/dashboard')

    return redirect('/recipe/<int:id>/edit')