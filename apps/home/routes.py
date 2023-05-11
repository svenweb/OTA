
from apps import db, login_manager

from apps.home import blueprint
from flask import render_template, request, redirect, url_for, session, flash
from flask_login import login_required, current_user
from jinja2 import TemplateNotFound
from datetime import date
from apps.authentication.models import Users, Post, Bicycle, BicyclePart, Image
import os
from werkzeug.utils import secure_filename



UPLOAD_FOLDER = '/Users/woodPecker/Desktop/software/OTA.v.0.3/OTA web app/apps/static/assets/postImages'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS




@blueprint.route('/index')
#@login_required causing error when user logged in
def index():
    today = date.today()
    formattedDate = today.strftime("%B %d, %Y")

    return render_template('home/index.html', segment='index', userName = current_user.username, date=formattedDate)


@blueprint.route('/dashboard.html')
#@login_required
def dashboard():
    
    today = date.today()
    formattedDate = today.strftime("%B %d, %Y")

    return render_template('home/dashboard.html', segment='dashboard', userName=current_user.username, date=formattedDate)


@blueprint.route('/insights.html')
#@login_required
def insights():
    
    today = date.today()
    formattedDate = today.strftime("%B %d, %Y")

    return render_template('home/insights.html', segment='insights', userName=current_user.username, date=formattedDate)




@blueprint.route('/postad.html', methods=['GET', 'POST'])
#@login_required
def postad():
    if request.method == 'POST':
        title = request.form['ad_title']
        price = request.form['price']
        year = request.form['year']
        make = request.form['make']
        model = request.form['model']
        bike_type = request.form['bike_type']
        frame_material = request.form['frame_material']
        frame_size = request.form['frame_size']
        suspension = request.form['suspension']
        front_travel = request.form['front_travel']
        rear_travel = request.form['rear_travel']
        brake_type = request.form['brake_type']
        handlebar_type = request.form['handlebar_type']
        e_assist = request.form['e_assist']
        wheel_size = request.form['wheel_size']
        condition = request.form['condition']
        post_type = request.form['post_type']
        
        
        print(title,price,year,make,model)
        bicycle = Bicycle(title=title, price=price, year=year, make=make, model=model, bike_type=bike_type, frame_material=frame_material, frame_size=frame_size, suspension=suspension, front_travel=front_travel, rear_travel=rear_travel, brake_type=brake_type, handlebar_type=handlebar_type, e_assist=e_assist, wheel_size=wheel_size, condition=condition, user_id=current_user.id,type=post_type)
        db.session.add(bicycle)
        db.session.commit()
        print('000000000000 bicycle added 000000000000')
        
       # check if the post request has the file part
        print(request.files['image[]'])
        if 'image[]' not in request.files:
            flash('No file part')
            return render_template('home/postad.html')
        images = request.files.getlist('image[]')
        print('IMAGES!!')
        print(images)
        for image in images:
            print(image.filename)
            if allowed_file(image.filename):
                print('ALLOOWEDDD')
                image.save(os.path.join(UPLOAD_FOLDER, image.filename))
                img = Image(url=image.filename, post_id=bicycle.id)
                db.session.add(img)
                db.session.commit()
                print("*******IMAGE UPLOADED******")
    return render_template('home/postad.html')




@blueprint.route('/listings.html')
@login_required
def listings():
    user_posts = Post.query.filter_by(user_id=current_user.id).all()
    postToImage = {}
    for post in user_posts:
        try:
            postToImage[post.id] = f"/postImages/{Image.query.filter_by(post_id=post.id).first().url}"
        except AttributeError as e:
            print(e)
    print(postToImage)
    return render_template('home/listings.html', posts=user_posts, images=postToImage)


@blueprint.route('/deletepost/<post_id>', methods=['DELETE'])
def delete_post(post_id):
  error = False
  post = db.session.query(Post).filter_by(id=post_id).first()
  name = post.title
  try:
    Post.query.filter_by(id=post_id).delete()
    db.session.commit()
    print('Sucessfully Deleted ' + name)
  except:
    error = True
    db.session.rollback()
  finally:
    db.session.close()
  if error:
    flash('An Error occured.  The venue ' + name + ' could not be deleted.')
    return redirect(url_for('home_blueprint.listings'))
  else:
    flash('Success.  Post ' + name + ' was deleted.')
    return redirect(url_for('home_blueprint.listings'))




@blueprint.route('/<template>')
#@login_required
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
