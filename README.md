# cfe-recommender
A movie recommendation web app based on user's interests

## Getting Started
Navigate to the directory where you want to store this project and then **run the below commands** to get started.

 - git clone https://github.com/sambit-git/cfe-recommender
 - cd cfe-recommender
 - python -m venv venv
 - pip install -r requirements.txt
 - cd src
 - mkdir data
 - python manage.py migrate
 - python manage.py runserver

## To avoid Cold start problem
- [Download dataset](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset?resource=download) (Needs authentication)
 - unzip the downloaded dataset
 - copy the file "movies_metadata.csv" to src/data
 - Then again run the below commands
 - python manage.py loader --users 1000 --show-total
 - python manage.py loader --movies 100 --show-total
