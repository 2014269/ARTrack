import functools
from typing import Callable
from flask import session, flash, redirect, url_for, request, current_app


def requires_login(f: Callable) -> Callable:
    """
    The requires_login decorator ensures that the user is logged in before accessing the page.
    If they are not, the user will be taken to the login page
    :param f:
    :return:
    """

    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('email'):
            flash('You need to be signed in for this page', 'danger')
            return redirect(url_for('users.login_user'))
        return f(*args, **kwargs)

    return decorated_function


def requires_admin(f: Callable) -> Callable:
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('email') != current_app.config.get('ADMIN', ''):
            flash("You need to be an administrator to access this page.", 'danger')
            return redirect(url_for('users.login_user'))
        return f(*args, **kwargs)

    return decorated_function
