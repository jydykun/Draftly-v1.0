import os
from datetime import datetime
from flask import Blueprint, render_template, request, \
    redirect, url_for, flash, current_app, jsonify, \
    send_from_directory
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from app import Config
from app.models import db, User, Post, Category, Subscriber
from app.forms import PostForm, SubscribeForm, EditPostForm
from app.utils import remove_image_tag, remove_html_tags


### MAIN BLUEPRINT STARTS HERE ###

title = Config.APP_NAME


main = Blueprint("main", __name__)




# A context processor runs before each request, injecting variables into the template context for all routes.
# You can define a context processor that retrieves categories and makes them available in every template.
@main.context_processor
def inject():
    # Query all the categories
    categories = db.session.scalars(db.select(Category)).all()

    subscribe_form = SubscribeForm()

    return {
        "categories": categories,
        "subscribe_form": subscribe_form,
        }


# Homepage ----------------------------------------------------------

@main.route("/", methods=["GET", "POST"])
def index():

    posts = db.session.scalars(db.select(Post).order_by(Post.timestamp.desc()).limit(4)).all()

    # Remove the image tag of the post in the homepage
    for post in posts:
        #post.body_without_images = remove_image_tag(post.body)
        post.text_only = remove_html_tags(post.body)

    return render_template("index.html", posts=posts, title=f"{title} - Homepage")


@main.route("/<category_key>")
def category_page(category_key):
    category = db.first_or_404(db.select(Category).where(Category.key == category_key))
    posts = db.paginate(db.select(Post).where(Post.category_id == category.id).order_by(Post.timestamp.desc()), per_page=2, error_out=False)

    # Remove the image tag of the post in the homepage
    for post in posts:
        #post.body_without_images = remove_image_tag(post.body)
        post.text_only = remove_html_tags(post.body)

    return render_template("category_page.html", category=category, posts=posts)


@main.route("/profile/<username>", methods=["GET", "POST"])
@login_required
def profile(username):
    # Get the user
    user = db.first_or_404(db.select(User).where(User.username == username))

    # Query all the posts
    posts = db.session.scalars(db.select(Post).where(Post.user_id == user.id)).all()

    # Query all the categories
    categories = db.session.scalars(db.select(Category)).all()

    if user.username != current_user.username:
        return "You must logged in first."
    
    form = PostForm()

    category_choices = [(category.id, category.name) for category in categories]
    form.category.choices = category_choices

    # Validate the form
    if form.validate_on_submit():
        feature_image = form.feature_image.data
        filename = secure_filename(feature_image.filename)

        _, ext = os.path.splitext(filename)
        new_filename = f'f_image_{datetime.now().strftime("%Y%m%d_%H%M%S")}{ext}'
        filename = new_filename

        # Check if the uploads folder exist
        dir = os.path.join(current_app.root_path, Config.UPLOAD_FOLDER)

        if not os.path.exists(dir):
            # Make the uploads folder
            os.makedirs(dir)
            
        # Save the image file to the path
        filepath = os.path.join(dir, new_filename)
        feature_image.save(filepath)

        post = Post(
            title = form.title.data,
            body = form.body.data,
            featured_image = filename,
            user_id = current_user.id,
            category_id = form.category.data
            )
        db.session.add(post)
        db.session.commit()

        flash("Posted Successfully")
        return redirect(url_for("main.profile", username=current_user.username))

    return render_template("profile.html", title=f"{title} - Profile", posts=posts, categories=categories, form=form)


@main.route("/upload", methods=["POST"])
def upload():
    image = request.files.get('file')
    filename = secure_filename(image.filename)

    # Change the file name
    # Reminder: splitext() method from os module
    # is different from split() from built-in method in python.
    # "_" is for the filename, "ext" for extension
    _, ext = os.path.splitext(filename) 
    new_filename = f'Image_{datetime.now().strftime("%Y%m%d_%H%M%S")}{ext}'
    filename = new_filename

    # Check if the uploads folder exist
    dir = os.path.join(current_app.root_path, Config.UPLOAD_FOLDER)

    if not os.path.exists(dir):
        # Make the uploads folder
        os.makedirs(dir)
        
    # Save the image file to the path
    filepath = os.path.join(dir, new_filename)
    image.save(filepath)

    # Get the URL of the uploaded image
    image_url = url_for("main.uploaded_image", filename=filename)

    return jsonify({ "location": image_url }), 200


@main.route("/articles")
def articles():
    # Paginate posts
    posts = db.paginate(db.select(Post).order_by(Post.timestamp.desc()), per_page=9, error_out=False)

    # Remove the image tag of the post in the homepage
    for post in posts:
        #post.body_without_images = remove_image_tag(post.body)
        post.text_only = remove_html_tags(post.body)

    return render_template("articles.html", posts=posts)


@main.route("/post/<int:post_id>")
def single_post(post_id):
    post = db.get_or_404(Post, post_id)
    posts = db.session.scalars(db.select(Post).order_by(Post.timestamp.desc()).limit(4)).all()
    return render_template("post.html", post=post, posts=posts)


@main.route("/subscribe", methods=["POST"])
def subscribe():
    form = SubscribeForm()

    if form.validate_on_submit():
        email = form.email.data
        new_subs = Subscriber(email=email)
        db.session.add(new_subs)
        db.session.commit()
        return jsonify({"success": "Subscription successful!"}), 200
    else:
        # Collect and return validation errors
        errors = {field: errors for field, errors in form.errors.items()}
        return jsonify({'status': 'error', 'errors': errors}), 400


@main.route("/images/<filename>")
def uploaded_image(filename):
    return send_from_directory(Config.UPLOAD_FOLDER, filename)


@main.route("/api/images", methods=["GET"])
def get_images():
    images = []
    for filename in os.listdir(os.path.join(current_app.root_path, Config.UPLOAD_FOLDER)):
        if filename.endswith((".png", ".jpg", ".jpeg", ".webp")):
            images.append({"url": url_for("main.uploaded_image", filename=filename)})

    return jsonify({"images": images}), 200


@main.route("/api/posts", methods=["GET"])
def get_all_posts():
    posts = db.session.scalars(db.select(Post).order_by(Post.timestamp.desc())).all()

    data = [
        {
            "title": post.title,
            "body": post.body,
            "featured_image": url_for("main.uploaded_image", filename=post.featured_image)
        }
        for post in posts
    ]

    return jsonify(data)

@main.route("/delete-post/<int:post_id>", methods=["POST"])
def delete_post(post_id):

    post = db.session.get(Post, post_id)

    db.session.delete(post)
    db.session.commit()
    flash("Post deleted successfully!", "success")

    return redirect(url_for("main.profile", username=current_user.username))


@main.route("/edit-post/<int:post_id>", methods=["GET","POST"])
def edit_post(post_id):

    post = db.session.get(Post, post_id)

    # Query all the categories
    categories = db.session.scalars(db.select(Category)).all()
    category = post.category_id
    
    form = EditPostForm(obj=post) #Populate the form with the existing data

    category_choices = [(category.id, category.name) for category in categories]
    form.category.choices = category_choices
    
    # Validate the form
    if form.validate_on_submit():
        post.title = form.title.data
        post.body = form.body.data
        post.category_id = form.category.data
        new_feature_image = request.form.get("replace_image_picker")

        #Check if there's an updated file for featured image
        if new_feature_image:
            post.featured_image = new_feature_image
        
        db.session.commit()

        flash(f"Updated Successfully", "success")
        return redirect(url_for("main.profile", username=current_user.username))

    return render_template("edit_post.html", title=f"{title} - Edit Post", categories=categories, form=form, category=category, post=post)

