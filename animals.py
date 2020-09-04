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

CLIENT_ID = os.getenv("UNSPLASH_KEY", None)


def get_unsplash_url(query):
    """
        get url from unsplash. Use the animal name
        to get random image
    """

    params = (
        ('client_id', CLIENT_ID),
        ('query', query),
    )

    response = requests.get(
        'https://api.unsplash.com/photos/random',
        params=params)

    if not response.ok:
        raise Exception("<br />".join(response.json()['errors']))

    image_data = response.json()
    # change small for raw or full to get best image resolution
    return image_data['urls']['small']


def get_animal_url(animal):
    """
        Get url from animal list. If url is None,
        call the get_unsplash_url to get a random one
    """

    if animal[1]:
        return animal[1]

    return get_unsplash_url(animal[0])


@app.route('/')
def index():

    animal = random.choice(ANIMALS)
    context = {'animal': animal[0]}

    try:
        context['url'] = get_animal_url(animal)
    except Exception as e:
        context['error'] = e

    return render_template("index.html", context=context)
