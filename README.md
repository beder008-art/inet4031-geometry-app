# INET 4031 Geometry Application

Simple Python Flask web application for INET 4031

The "Geometry Calculator" Application

This repository contains a sample (and simple) web application based on Python Flask

https://flask.palletsprojects.com/

## Dynamic Web Applications

A Dynamic Web Application's web pages contain two types of content:

1. Static content in the form of HTML
2. Dynamic content created by a programming language.

In this application the programming language is Python.  In response to user input on the web page, Python creates HTML "on the fly" that is downloaded to the browser and rendered.

## The Code

At the top level of the code in this repo are the Python files.  The "main" piece of code is GeometryCalcWeb.py

Creating dynamic web applications requires the use of a web development framework such as Flask.  Other examples include NodeJS, ASP.NET, Java JSP, Ruby on Rails, and many more.

The development framework is what provides the core web functionality - it implements the web server and the execution environment in which to run the code.

Each web page of this application contains both static and dynamic content.  The static content is provided by the .html files in the ./templates directory.

Take a moment to look at the code and see if you can make sense of it.  Flask is a very popular "lightweight" framework and thus the amount of information available online is volumous.

The code will be dicussed and demonstrated in class.  Take notes!!!

## The Dependencies

All applications have **dependencies**.   In other words, there is the code itself, like the GeometryCalcWeb.py and cylinder.py files, but also the other code that is needed and necessary to run your application.

All of the dependencies for this application are in the **requirements.txt** file.

Dependencies in Python application are usually installed managed using a Python package manager such as PIP or Conda.  For example, if an application needed the "numpy" module installed to do more advanced math functions:

(remember that on some system "pip3" must be used if you want to install the module for Python 3)

`pip install numpy`

If an Python app has multiple dependencies, they can all be put into file and then installed as such:

`pip install -r requirements.txt**`


## Running the Code

Make sure:

Git is installed: https://git-scm.com/
Python is installed: https://python.org

On your development system, it is recommended that you use a Python "Virtual Environment."

Creating a Python virtual environment allows the development to create an isolated environment in which to develop and run Python code.

Python dependencies can often interfere with one another.  Don't want to accidently nuke your laptop right?  

Open up a command line (terminal) prompt on your computer and navigate to a directory that makes sense in which to store this code.

### Get the code:

git clone https://github.com/axbjos/inet_4031_flask.git

This will download a copy of my repo on your system.  It is a complete separate copy.  You will not be able to modify my code in my repo (to do that I'd have to grant you a 'pull' request - which I will not).

Go into the new directory that was created by the clone.  Use your favorite lightweight code editor (which should be Visual Studio Code) to look at the files.

### Run the code:

(remember that to run the commands below, you may need to use python3 and pip3 on your system)

Once in the new directory do this:

`python -m venv venv`

This creates a new virtual environment.

Now activate the virtual environment:

Unix/Linux:  `source ./venv/bin/activate`
Windows: `venv\Scripts\activate`

Your prompt should look similar to this now:

*(venv) joeaxberg@macbookm1pro inet_4031_flask %*

Now you have an isolated "virtual" Python environment.  Modules you install will only be installed for THIS application.  The system-wide module library will not be impacted.

Install the **Dependencies**

`pip install -r requirements.txt`

Make sure there were no errors.

Now run the application:

`python GeometryCalcWeb.py`

There are lots of ways to run Flask apps, this is but one.

Now open up a browser and go to:

http://localhost:5000

Or put in the IP of your laptop instead of local host.  Either way point the URL to TCP port 5000.  By default Flask listens on 5000 so it doesn't interfere with other web servers you may have running like Apache or Nginx which listen on port 80 by default.

## Unit Tests

A Unit Test is a piece of code that is used to test other code.

For example, the cylinderTest.py code "tests" the cylinder.py code.

