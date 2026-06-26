# Why I chose Pi-hole — 2026-06-26

## Context
I need a local DNS server so my devices can resolve `.home` hostnames
to my server IP. Without it, Traefik's hostname routing is useless —
the browser never finds the server in the first place. Ad-blocking for
all devices on my network was a bonus.

## Decision
Pi-hole runs as a DNS server on the Infra VM. Every device on my network
points to it as their DNS, so when I type `nextcloud.home` my browser
asks Pi-hole first. Pi-hole resolves it to my server IP and the request
reaches Traefik.

It also blocks ads at the DNS level for every device on the network
without installing anything on those devices.

It was recommended by people I trust, has a large homelab community, and
the Docker setup is well documented.

## Why not adGuard Home
Both are valid options with good Docker support. Pi-hole has a larger
homelab community, more tutorials available, and was already recommended
by people I trust.