from flask import Blueprint, render_template

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

@bp.route('/contact')
def contact():
    """
    Route for the contact page.

    Returns:
        str: Rendered HTML for the contact page.
    """
    return render_template('contact.html')
