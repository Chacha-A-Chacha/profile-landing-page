from flask import Blueprint, render_template, request, flash
from flask_mail import Mail, Message

from .forms import ContactForm

# Create a Blueprint instance for the main module
bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    """
    Route for the home page.

    Returns:
        str: Rendered HTML for the home page.
    """
    return render_template('index.html')

@bp.route('/about')
def about():
    """
    Route for the about page.

    Returns:
        str: Rendered HTML for the about page.
    """
    return render_template('about.html')

@bp.route('/projects')
def projects():
    """
    Route for the projects page.

    Returns:
        str: Rendered HTML for the projects page.
    """
    return render_template('projects.html')

@bp.route('/contact', methods=['GET', 'POST'])
def contact():
    """
    Route for the contact page.

    Returns:
        str: Rendered HTML for the contact page.
    """

    form = ContactForm()

    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        subject = form.subject.data
        message = form.message.data

        msg = Message(subject, sender=email, recipients=['your_email@gmail.com'])
        msg.body = f"From: {name} <{email}>\n\n{message}"

        try:
            mail.send(msg)
            flash("Your message has been sent. Thank you for contacting us.")
        except Exception as e:
            flash(f"An error occurred: {e}")

    return render_template('main/contact.html', form=form)

    return render_template('contact.html')
