from flask import Blueprint, render_template, redirect, url_for, flash, session
from blog.forms import PostForm
from models import Post


blog_blueprint = Blueprint('blog', __name__, template_folder='templates')


@blog_blueprint.route('/blog', methods=['GET'])
def blog():
    # Retrieve all posts from the database
    posts = Post.query.all()

    # Render the template and pass the posts to it
    return render_template('blog/blog.html', posts=posts)


@blog_blueprint.route('/create', methods=['GET', 'POST'])
def create():
    from application import db

    form = PostForm()

    if form.validate_on_submit():

        new_post = Post(title=form.title.data, content=form.body.data,user_id=1)

        db.session.add(new_post)
        db.session.commit()

        flash('Post created successfully!', 'success')
        return redirect(url_for('blog.blog'))  # Redirect to the blog page

    return render_template('blog/create.html', form=form)
