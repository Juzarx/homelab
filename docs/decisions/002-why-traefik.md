# Why I chose Traefik — 2026-06-17

## Context
I need to connect to my services without memorizing ip addresses,
this is the routing layer that sits behind Tailscale.
## Decision
Traefik sits in front of all my Docker containers and routes requests to
the right one based on the hostname. When I add a new container, I just
add a label to it and Traefik picks it up automatically — no config file
to edit.
## Why not Nginx
Nginx requires manually editing a central config file and reloading the
service every time I add or remove a container. Traefik auto-discovers
containers through Docker labels, so there's nothing to reload.