import requests
import random
import os

from flask import Flask, render_template

app = Flask(__name__)

ANIMALS = (
    ("lion", None),
    ("otter", None),
    ("platypus", None),
    ("dog", None),
    ("cat", None),
    ("cow", None),
    ("sheep", None),
    ("rabbit", None),
    ("duck", None),
    ("horse", None),
    ("pig", None),
    ("turkey", None),
    ("chicken", None),
    ("donkey", None),
    ("goat", None),
    ("guinea pig", None),
    ("llama", None),
)


def get_animal_url(animal):
    """ Get url from animal list.  """

    if animal[1]:
        return animal[1]

    raise Exception(f"The animal '{animal[0]}' does not have a defined url")

@app.route('/')
def index():

    animal = random.choice(ANIMALS)
    context = {'animal': animal[0]}

    try:
        context['url'] = get_animal_url(animal)
    except Exception as e:
        context['error'] = e

    return render_template("index.html", context=context)
