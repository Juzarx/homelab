# Day 19 - Health check script and minecraft control API

**Date:** 2026-08-25

**Objective:** Start phase 6, write a health check script and begin a minecraft control panel

**Status:** Completed

**Related documents:**
- [Roadmap](../roadmap.md)
- [Architecture](../architecture.md)
- [Day 18](./018-lm-sensors-and-infra-disk-fix.md)
- [Requests library docs](https://requests.readthedocs.io/)
- [Flask docs](https://flask.palletsprojects.com/)

## Health check script
- Set up a python venv on the infra VM with `python3 -m venv venv`.
- Wrote a first version checking homepage, traefik, pihole, prometheus and grafana with the requests library.
- Got everything showing DOWN at first, homepage/traefik/pihole returned 404 and prometheus/grafana returned ConnectionError.
- Realized traefik routes by hostname, so hitting localhost with no Host header matches no route, fixed by sending the `.home` hostname manually in the request headers.
- Prometheus and grafana have no exposed ports anymore since they only have traefik labels, fixed the same way, routing through localhost with the right Host header instead of hitting their internal ports directly.
- Extended the script to also check nextcloud, grimmory and navidrome the same way, and minecraft using a raw TCP socket check since it's not http.
- Everything reporting correctly now.
- The [Healthcheck script](/scripts/healthcheck.py) was ready.

## Starting the minecraft control API
- Installed flask on the infra VM.
- Made a minimal flask app with a home route and a status route to confirm it worked.
- Decided against running flask directly on the games VM, didn't want to add any load to an already resource tight machine.
- Set up SSH key access from infra VM to games VM for passwordless remote commands.
- Added a `/api/minecraft/status` route running `docker inspect` on the games VM over ssh.
- Added `/api/minecraft/start` and `/api/minecraft/stop` routes.
- Stop route runs `rcon-cli save-all` first and only then `docker stop`, to make sure the world saves before the container goes down.
- Tested all three routes with curl, working correctly.
- The [Control API base](/scripts/app.py) was ready

## Notes
- subprocess.run only takes one command list per call, tried to pass two lists to save and stop the server in a single call and it doesn't work like that, needed two separate subprocess.run calls done one after another.
