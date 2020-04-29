from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
from flask_login import current_user, login_required
from sec import db 
from sec.models import Post
from sec.posts.forms import PostForm
from sec.users.utils import save_photo


posts = Blueprint('posts', __name__)


@posts.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
	form = PostForm()
	photo = None
	if form.validate_on_submit():
		if form.photo.data:
			photo = save_photo(form.photo.data)
		post = Post(title=form.title.data, content=form.content.data, image=photo ,author=current_user)	
		db.session.add(post)
		db.session.commit()
		flash('Now you can see your post', 'success')
		return redirect(url_for('main.all_post'))
	return render_template('create_post.html', title='New Post', legend='Create New Post', form=form)

	

@posts.route('/post/<int:post_id>', methods=['GET', 'POST'])
def show_post(post_id):
	post = Post.query.get_or_404(post_id)
	return render_template('show_post.html', title=post.title, post=post)



@posts.route('/post/<int:post_id>/update', methods=["GET", "POST"])
@login_required
def update_post(post_id):

	post = Post.query.get_or_404(post_id)
	if post.author != current_user:
		abort(403)

	form = PostForm()
	if form.validate_on_submit():
		post.title = form.title.data
		post.content = form.content.data
		post.image = form.photo.data
		if form.photo.data:
			photo = save_photo(form.photo.data)
			post.image = photo
		db.session.commit()
		flash('Your Post has been updated!', 'success')
		return redirect(url_for('main.all_post', post_id=post.id))
	
	elif request.method == 'GET':
		form.title.data = post.title
		form.content.data = post.content
		
	return render_template('create_post.html', title='Update Post', legend='Update Post', form=form)


@posts.route('/post/<int:post_id>/delete', methods=["POST"])
@login_required
def delete_post(post_id):
	post = Post.query.get_or_404(post_id)
	if post.author != current_user:
		abort(403)
	db.session.delete(post)
	db.session.commit()
	flash('Post has been deleted!', 'success')
	return redirect(url_for('main.all_post'))