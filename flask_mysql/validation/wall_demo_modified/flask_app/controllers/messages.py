from flask_app.models.comment import Comment
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User
from flask_app.models.message import Message

@app.route('/messages')
def all_messages():
    if 'user_id' not in session:
        flash('Please log in to view the messages!')
        return redirect('/')

    messages = Message.get_all_messages()
    print(messages)

    return render_template('messages.html', all_messages = messages)

@app.route('/messages/create', methods=['POST'])
def create_message():

    valid = Message.validate_message(request.form)

    if valid == False:
        print('validation failed')
        return redirect('/messages')

    print('validation success!')

    data = {
        'content': request.form['content'],
        'user_id': session['user_id']
    }

    Message.create_message(data)

    return redirect('/messages')

@app.route('/messages/<int:message_id>/delete')
def delete_message(message_id):

    data = {'id': message_id}
    message = Message.get_one_message(data)

    if message == None:
        print('no message with that ID')
    elif message.user_id != session['user_id']:
        print('user cannot delete message')
    else:
        print('user can delete message')
        Message.delete_message(data)


    return redirect('/messages')

@app.route('/messages/<int:message_id>/edit')
def edit_message(message_id):

    data = {'id': message_id}
    message = Message.get_one_message(data)

    if message == None:
        print('no message with that ID')
        return redirect('/messages')
    elif message.user_id != session['user_id']:
        print('user cannot edit message')
        return redirect('/messages')

    return render_template('edit_message.html', message = message)

@app.route('/messages/<int:message_id>/update', methods=['POST'])
def update_message(message_id):

    valid = Message.validate_message(request.form)

    if valid == False:
        print('validation failed!')
        return redirect(f'/messages/{message_id}/edit')

    print('validation success!')

    data = {
        'content': request.form['content'],
        'id': message_id
    }

    Message.update_message(data)

    return redirect('/messages')

@app.route('/messages/<int:message_id>')
def single_message(message_id):

    message = Message.get_one_message({'id': message_id})    

    return render_template('single_message.html', message = message)

@app.route('/messages/<int:message_id>/add_comment', methods=['POST'])
def add_comment_to_message(message_id):

    valid = Comment.validate_comment(request.form)

    if valid == False:
        print('validation failed!')
        return redirect(f'/messages/{message_id}')

    print('validation success!')

    data = {
        'content': request.form['content'],
        'user_id': session['user_id'],
        'message_id': message_id
    }

    Comment.create_comment(data)

    return redirect(f'/messages/{message_id}')