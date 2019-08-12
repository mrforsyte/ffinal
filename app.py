from flask import Flask, render_template, request, url_for, redirect
app = Flask(__name__)

posts = {
	0:{
		'post_id':0,
		'title':'Matrix',
		'year of production':1999
	}
}

@app.route('/')
def hello():
	return 'little bitch'


@app.route('/home/<int:post_id>')
def home(post_id):
	post = posts.get(post_id)
	if not post:
		return render_template('error.html', message = f'post id number {post_id} was not found')
	
	return render_template('index.html', post = post)

@app.route('/createpost')	
def create_post():
	return render_template('create_form.jinja2')
	

@app.route('/post/create', methods=['POST'])
def create():
	title = request.form.get('title')
	year = request.form.get('year of production')
	post_id = len(posts)
	print( title)
	print(year)
	print(post_id)

	posts[post_id] = {'post_id':post_id, 'title':title, 'year of production': year}

	return redirect(url_for('home', post_id = post_id))



if __name__ == '__main__':
	app.run(debug=True) 