from flask import Blueprint, render_template

auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/log')
def loginPage():
    return render_template('loginPage.html')

    

    