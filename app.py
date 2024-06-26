from flask import Flask, redirect, render_template, request
from cache import CacheHandler

app = Flask(__name__)
cache = CacheHandler() # custom directory will be implemented later in '/settings' or settings.json
current = '1pyp9v'

@app.route('/')
def index():
    wallpaper_url = cache.retrieve(current)['data']['path']
    return render_template('index.html', wallpaper_url=wallpaper_url)