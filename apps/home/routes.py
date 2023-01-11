# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
#elan 

from apps.home import blueprint
from flask import render_template, request
from flask_login import login_required, current_user
from jinja2 import TemplateNotFound
from datetime import date


@blueprint.route('/index')
@login_required
def index():
    today = date.today()
    formattedDate = today.strftime("%B %d, %Y")

    return render_template('home/index.html', segment='index', userName = current_user.username, date=formattedDate)


@blueprint.route('/dashboard.html')
@login_required
def dashboard():
    
    today = date.today()
    formattedDate = today.strftime("%B %d, %Y")

    return render_template('home/dashboard.html', segment='dashboard', userName=current_user.username, date=formattedDate)


@blueprint.route('/insights.html')
@login_required
def insights():
    
    today = date.today()
    formattedDate = today.strftime("%B %d, %Y")

    return render_template('home/insights.html', segment='insights', userName=current_user.username, date=formattedDate)




@blueprint.route('/<template>')
@login_required
def route_template(template):

    today = date.today()
    formattedDate = today.strftime("%B %d, %Y")

    try:

        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment, date=formattedDate)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None
