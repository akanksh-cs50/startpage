import requests
from os import makedirs
import json

class CacheHandler:
    def __init__(self, cache_dir='./cache'):
            self.cache_dir = cache_dir
            
    def store(self, id:str):

        # handle cases of url or just the wallpaper id

        if  id.startswith('http'):
            id = id.split('/')[-1]
            
        response = requests.get(f'https://wallhaven.cc/api/v1/w/{id}')

        try:
            makedirs(f'{self.cache_dir}/{id}') # windows might have a problem with this
        except FileExistsError: # if the directory already exists, we'll deal with staleness later.
            pass

        with open(f'{self.cache_dir}/{id}/response.json', 'w+') as file:
            try:
                file.write(response.text)
                file.close()
            except:
                return IOError