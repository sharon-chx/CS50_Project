import spotipy
import os
from spotipy.oauth2 import SpotifyClientCredentials
import requests
import urllib.parse

from flask import redirect, render_template, request, session
from functools import wraps


def track_search(name):

    # to use the client ID and client secret that set as environment variables to get access to API. DO NOT DELETE THIS PART
    # see here to create your client ID and client secret: https://developer.spotify.com/documentation/general/guides/app-settings/#register-your-app

    client = os.environ.get("SPOTIFY_CLIENT_ID")
    secret = os.environ.get("SPOTIFY_CLIENT_SECRET")

    spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id = client, client_secret = secret))


    # to search artist's tracks (including the track that was sung more than 1 artist), return a list of tracks

    name = name.lower()
    tracks = []

    total = spotify.search(q='artist:' + name, limit = 50, type='track')["tracks"]["total"]
    for j in range(0, total, 50):
        results = spotify.search(q='artist:' + name, limit = 50, offset = j, type='track')["tracks"]["items"]
        for track in results:
            for i in range(len(track["artists"])):
                if track["artists"][i]["name"].lower() == name:
                    tracks.append(track["name"])
    return tracks


def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function
