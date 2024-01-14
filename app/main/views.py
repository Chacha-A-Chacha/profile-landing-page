from flask import Blueprint, render_template, request, flash

from .forms import ContactForm
from app import mail, message

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
        client_message = form.client_message.data

        msg = message(subject, sender=email, recipients=['your_email@gmail.com'])
        msg.body = f"From: {name} <{email}>\n\n{client_message}"

        try:
            mail.send(msg)
            flash("Your client_message has been sent. Thank you for contacting us.")
        except Exception as e:
            flash(f"An error occurred: {e}")

    return render_template('main/contact.html', form=form)


@bp.route('/sitemap.xml')
def sitemap():
    """
    Route for the sitemap.

    Returns:
        str: Rendered XML for the sitemap.
    """
    return render_template('sitemap.xml')


@bp.route('/robots.txt')
def robots():
    """
    Route for the robots.txt file.

    Returns:
        str: Rendered text for the robots.txt file.
    """
    return render_template('robots.txt')


@bp.route('/favicon.ico')
def favicon():
    """
    Route for the favicon.

    Returns:
        str: Rendered image for the favicon.
    """
    return render_template('favicon.ico')


@bp.route('/apple-touch-icon.png')
def apple_touch_icon():
    """
    Route for the apple touch icon.

    Returns:
        str: Rendered image for the apple touch icon.
    """

    return render_template('apple-touch-icon.png')  # TODO : FIX THIS
