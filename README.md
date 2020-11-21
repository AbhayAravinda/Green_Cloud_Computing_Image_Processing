# Green Cloud Computing

An image processing web application that provides opencv functionalities and adheres to green cloud computing techniques

## Features

Allows modification of images to:

1. Gray Scale
2. Sepia
3. Gaussian Blur
4. Brightness Increase &amp; Decrease
5. Color Inversion
6. Negative Image
7. Contrast Limited Adaptive Histogram Equalization

Behind the scenes, optimization of the following things take place:

1. User Interface
2. Thread Scheduling
3. Coding Efficiency
4. Data Storage

## Prerequisites

- [virtualenv](https://virtualenv.pypa.io/en/latest/)
- [python](https://www.python.org/)
- [django](https://www.djangoproject.com/)
- [mongodb](https://www.mongodb.com/)

## Getting Started

Create and activate a virtualenv:

```bash
virtualenv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

NOTE: After installing dependencies, pip-tools is also installed. You can now use it to manage package dependencies of your project.

```bash
'''
Add a new package to requirements.in and run the following command to auto-update requirements.txt file
'''
pip-compile requirements.in
'''
Run the following command to sync your virtualenv
'''
pip-sync
```

For more details, https://github.com/nvie/pip-tools

Run the following commands on your local machine. Migrate, create a superuser, and run the server:

```bash
python manage.py migrate
python manage.py makemigrations image_processing
python manage.py migrate image_processing
python manage.py runserver
```
