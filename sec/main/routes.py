from datetime import datetime
from flask import render_template, request, Blueprint
from sec.models import Post

main= Blueprint('main', __name__)

@main.route('/')
def home():
	return render_template('index.html')

@main.route('/post')
def all_post():
	page = request.args.get('page', 1, type=int)
	posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
	return render_template('all_post.html', title='All Posts', posts=posts)

@main.route('/flask')
def flask(): 
	return render_template('flask.html', title='Flask')

@main.route('/django')
def django():
	return render_template('django.html', title='Django')

@main.route('/about')
def about():
	return render_template('about.html', title='About')

@main.route('/contact')
def contact():
	return render_template('contact.html', title='Contact')