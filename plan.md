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

I'm making a python ``CacheHandler`` class which stores and retreieves files from the cache.
I'll deal with downloading media files later and for now I'll just pass in the url to the browser.
Media is not rate-limited but does not work offline.

## Colors

[wallhaven.cc](https://wallhaven.cc) provides 5 dominant colors in a given wallpaper.
I wanted to have themed elements on the startpage according to the user's preferred wallpaper.
The problem is that the colors are organised pretty much randomly.
I could not find documentation regarding color ordering.

I initially thought I'll take the brightest and darkest and use those are foreground and background colors.
ChatGPT suggested the rest can be considered as accent colors.
ChatGPT also suggested categorizing the colors based on their brightness like me, but the technical term seems to be luminescence.

Luminescence = 0.2126 x Red + 0.7152 x Green + 0.0722 x Blue

Based on this, the lightest and darkest will be foreground/background colors and the rest will be accent colors.

Also I'm thinking of adding the following to the main stylesheet:
```css
@import 'colors.css'
```
colors.css will serve a style sheet like this:

```css
:root {
    --foreground: #ffffff;
    --background: #000000;
    /* colors below are random for the sake of demonstration */
    --accent1: #12fa45;
    --accent2: #aed331;
    --accent3: #623aff;
}
```
I'm going to run the luminescence calculation and cache it server-side.