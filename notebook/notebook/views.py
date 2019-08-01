from flask import flash, redirect, url_for, render_template

from notebook import app, db
from notebook.models import Message
from notebook.forms import HelloForm


@app.route('/', methods=['GET', 'POST'])
def index():
    form = HelloForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(body=body, name=name)
        db.session.add(message)
        db.session.commit()
        flash('Your message have been sent to the world!')
        return redirect(url_for('index'))
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    return render_template('index.html', form=form, messages=messages)
