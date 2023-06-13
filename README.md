# cfe-recommender
A movie recommendation web app based on user's interests

## Getting Started
Navigate to the directory where you want to store this project and then **run the below commands** to get started.

 - git clone https://github.com/sambit-git/cfe-recommender
 - cd cfe-recommender
 - python -m venv venv
 - source .\venv\Scripts\Activate.ps1
 - pip install -r requirements.txt
 - cd src
 - mkdir data
 - python manage.py migrate
 - python manage.py createsuperuser ~~(create the super user)~~
 - python manage.py runserver

## To avoid Cold start problem
- [Download dataset](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset?resource=download) (Needs authentication)
 - unzip the downloaded dataset
 - copy the file "movies_metadata.csv" to src/data
 - Then again run the below commands
 - python manage.py loader --users 5000 --show-total
 - python manage.py loader --movies 10000 --show-total
 - python manage.py fake_ratings 1000 --users 1000 --show-total

## Redis Installation and Running (Tried in Ubuntu 22.04.2 LTS)
 - [Download Redis](https://github.com/redis/redis/archive/7.0.11.tar.gz) 
 - cd &lt;redis downloaded directory&gt;
 - tar -xzf redis-7.0.11.tar.gz
 - cd redis-7.0.11/
 - sudo apt-get install libssl-dev
 - make MALLOC=jemalloc
 - make BUILD_TLS=yes
 - sudo make test install &lt;after tis redis-server will be accessible from any directory&gt;
 - `make distclean` <- Run this if stuck at anyplace in running above instructions and retry

## Start Celery (to run periodic tasks)
- celery -A cinegalaxy worker -l info --beat

## Try running tasks in Django Shell
 - python manage.py shell
    ```
        >>> from movies.tasks import task_claculate_movie_rating

        >>> task_claculate_movie_rating()
        
        >>> task_claculate_movie_rating.delay()
        <AsyncResult: 6ba0e784-b18a-4d3d-a211-72c21e1d570c>
        
        >>> task_claculate_movie_rating.apply_async(countdown=30)
        <AsyncResult: 2b4ffdff-074a-4ddc-bc00-cd49c752da32>
    ```