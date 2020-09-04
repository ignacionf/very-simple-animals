# very-simple-animals

A simple python web app to get a animal and one image url from them.

## Install

This code support python 3.6, 3.7 or 3.8

```
 $ python3 -m venv venv
 $ source venv/bin/activate
 $ pip install -r requeriments.txt
```

## Configure

In `animals.py` you can modify the list `ANIMALS` with a tuple of ("animal name", "url").

## Run

```
 $ export FLASK_APP=animals.py
 $ flask run
```

## View

Just go "localhost:5000" in a browser
