# Google Search

## Table of Contents
1. [Overview](#overview)
2. [Project Structure](#project-structure)
3. [Running the Application](#running-the-application)



## Overview
This project is a front-end implementation for Google Search, Google Image Search, and Google Advanced Search. The objective is to create an HTML and CSS-based front-end that mimics the functionality of Google's search interfaces, utilizing forms to send data to Google's search endpoints. Additionally, this project is extended with a simple Flask application to serve the HTML pages dynamically.

## Project Structure 
app.py: A simple Flask application to serve the HTML templates.
templates/: Directory containing HTML templates.
layout.html: Base template with common structure.
index.html: Template for Google Search.
image_search.html: Template for Google Image Search.
advanced_search.html: Template for Google Advanced Search.
static/: Directory for static files like CSS and images.


## Running the Application
Having the following prerequisites:
- Python 3.x
- pip (Python package installer)


1. clone the repository: ```git clone```

2. then cd into it: ```cd```

3. install flask: ```pip install flask```

4. run the flask server: ```flask run```
