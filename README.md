# Microblog

## Features
* Users can sign up.
* Users can write multiple posts

## Requirements and Installation
**Via Cloning The Repository**
```
# Clone the app
git clone https://github.com/vic3king/flask-microblog.git

# Setup Env
Follow the format specified in the .env example

# Switch to directory
cd flask-microblog

# Create virtual env
virtualenv --python=python3 venv

# Activate virtual env
source venv/bin/activate

# Install Package dependencies
 pip install -r requirements.txt

# create and setup .env file according to .env.exampl

# Run migrations
python manage.py db init
python manage.py db migrate
python manage.py db upgrade 

#Start the application
flask run

#View the application
navigate to localhost:3000 to view the application
```

 ```
## Technologies 

### Backend

* [Python-Flask](http://flask.pocoo.org/) Flask is a microframework for Python based on Werkzeug, Jinja 2 and good intentions
* [Jinja](https://palletsprojects.com/p/jinja/)inja2 is a full-featured template engine for Python. It has full unicode support, an optional integrated sandboxed execution environment, widely used and BSD licensed.
* [SQLAlchemy](https://www.sqlalchemy.org/) SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.
* [SQLite](https://www.sqlite.org/index.html) SQLite is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine


### Style Guide
* coming soon


## Authors

* **Akaniru victory** - *Initial work* - [Vic3king](https://github.com/vic3king) 

This is spin off of the [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world).