# Microblog

## Features
* Users can signup.
* Users can login.
* Users can view their profile and they can update.
* Users can follow and unfollow each other
* support to receive email/error logs for bugs while in production and development
* Users can reset their passwords via email
* Support for language translation

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
python manage.py db upgrade 

#Start the application
flask run

#View the application
navigate to localhost:5000 to view the application

#to test email bug reporting locally
run  `python -m smtpd -n -c DebuggingServer localhost:8025` on another terminal
hit a bug

# run tests 
python tests.py

# generate a new language 
* flask translate init <language-code>
update all texts you need to translate to client by calling the language markers _() _l() and pass in the text as arguments:
* flask translate update
* flask translate compile
```

## Technologies 

### Backend

* [Python-Flask](http://flask.pocoo.org/) Flask is a microframework for Python based on Werkzeug, Jinja 2 and good intentions

* [SQLAlchemy](https://www.sqlalchemy.org/) SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.

* [SQLite](https://www.sqlite.org/index.html) SQLite is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine

### Frontend
* [Jinja](https://palletsprojects.com/p/jinja/) is a full-featured template engine for Python. It has full unicode support, an optional integrated sandboxed execution environment, widely used and BSD licensed.

### Style Guide
* coming soon


## Authors

* **Akaniru victory** - *Initial work* - [Vic3king](https://github.com/vic3king) 

This is spin off of the [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world).