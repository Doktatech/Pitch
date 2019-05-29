# Pitch

 By [Rewel Kinyanjui](https://github.com/Doktatech/Pitch)

## Overview
A web application that allow users to pitch their ideas within a minute.

## Description
The Pitch web application allow users to pith their ideas in the following categories:
    1. Interview Pitch
    2. Business
    3. Maths Pitch
    4. Pick-up lines
    5. Science and Tech

Consequently, a user is able to make a perfect pitch within a limited time frame and catch the audiences attention. Furthermore, users can be able to comment and upvote or downvote other users pitch(es)

## Specifications

Get the specs [here](https://github.com/Doktatech/Pitch/)

## Set-up and Installation

### Prerequiites

    - Python 3.6
    - Ubuntu software
    

### Create a Virtual Environment

Run the following commands in the same terminal:

```sudo apt-get install python3.6-venv```

```python3.6 -m venv virtual```

```source virtual/bin/activate```

### Install dependancies

Install dependancies that will create an environment for the app to run

```pip3 install -r requirements```

Install [Postgres](https://www.postgresql.org/download/) {An SQL database for storing app details}

### Prepare environment variables

```export DATABASE_URL='postgresql+psycopg2://username:password@localhost/pitchperfect'```

```export SECRET_KEY='Your secret key'```

### Run Database Migrations

```python manage.py db init```

```python manage.py db migrate -m "migration comment"```

```python manage.py db upgrade```


### Running the app in development

In the same terminal type:
`python3.6 manage.py server`

Open the browser on `http://localhost:5000/`

## Known bugs

The upvote and downvote buttons are not operation as per the latest commit

## Technologies used

    - Python 3.6
    - HTML v5
    - Bootstrap 4
    - Postgresql

## Support and contact details

Contact me using provided details on my profile

### License

    **MIT LICENSE** 
&copy; Copyright **Rewel Kinyanjui**