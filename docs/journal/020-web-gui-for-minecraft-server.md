# Day 19 - Web GUI for Minecraft server

**Date:** 2026-08-27

**Objective:** Create a web GUI to control the minecraft server

**Status:** Completed

**Related documents:**
- [Roadmap](../roadmap.md)
- [Architecture](../architecture.md)
- [Day 19](./019-health-script-and-minecraft-control-api.md)
- [Flask docs](https://flask.palletsprojects.com/)

## Creating the web GUI
- Decided to use pico.css as an easy way of css.
- Created the folders static and templates in the same scripts folder as app.py.
- Modified the [app.py file](/scripts/app.py) to add a player list.
- Created the [index.html file](/scripts/templates/index.html) on the templates folder.
- Created the [app.js file](/scripts/static/app.js) on the static folder.
- With the minecraft list output created a cleaner version of it.

## Cleaning up the player list output
- Raw rcon `list` output included ANSI color codes like `\u001b[0m`, meant for a terminal, showing up as garbage text in the browser.
- Used python's `re` module to strip the ANSI codes with `re.sub`.
- Used `re.search` to grab just the player names after "online:" and split them into a proper list.
- Updated the [app.py file](/scripts/app.py) to return clean player_count and players fields instead of raw text.
- Updated [app.js](/scripts/static/app.js) to loop through the players array and show each as its own list item.