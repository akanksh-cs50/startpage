# Plan

Multi-User authentication can be done in a different branch.
For this branch (flask-server) I will focus on a single-user case.

I'm thinking of having a separate route like '/settings' which will allow the user to change settings and there will be gear icon in the bottom right corner which takes the user to this route.

## Index aka homepage '/'

I want these features in the startpage:

- [ ] Search box with a magnifying glass as the search icon beside it.

The search provider should be displayed as placeholder text in the search box and should be modifiable from '/settings'.

Another setting would be to open the search in a new tab or redirect the current tab to the search.

- [ ] Bookmarks 

## '/settings'

There are a few features which I think are necessary.

- [ ] preview of the wallpaper and it's color palette.
the preview will be small and will probably use the css property ``background-size: contain``.

- [ ] ability to save and restore settings from a file eg. settings.json which can be imported to the application.

## Cache

To limit number of api requests to [wallhaven.cc](https://wallhaven.cc) I will have a directory 'cache/' in the root of the flask application which will store the json responses from [wallhaven.cc](https://wallhaven.cc). I'll store the image as well because I want the startpage to be working regardless of internet connectivity.

So a directory cache like this:
```
cache/[id]/response.json
cache/[id]/large_thumb.jpg
cache/[id]/full.png
cache/[id]/uploader_avatar.png
```

Something like this.
This will be ignored by git using the ``.gitignore`` file.