# Why I chose Traefik — 2026-06-17

## Context
I need a way to route incoming requests to the right Docker container
based on hostname. Pi-hole resolves the name to the server IP, but
something still needs to decide which container handles the request
once it arrives.
## Decision
Traefik is the routing layer between the network and my Docker containers. When I add a new container, I just
add a label to it and Traefik picks it up automatically — no config file
to edit.
## Why not Nginx
Nginx requires manually editing a central config file and reloading the
service every time I add or remove a container. Traefik auto-discovers
containers through Docker labels, so there's nothing to reload.