# Traefik Docker provider API version mismatch — 2026-06-26

**Service:** traefik
**Duration:** ~30 min

## What happened
Traefik started successfully but the Docker provider kept throwing
"client version 1.24 is too old" despite Docker Engine 29.6.0 being
correctly installed.

## Root cause
Traefik v3.3 bundles a Docker client that defaults to API version 1.24.
The host was running API 1.55. Traefik's internal client never negotiated
up to the correct version.

## Fix
Changed the Traefik image from v3.3 to v3.7.5 in [docker-compose.yml](/docker/infrastructure/traefik/docker-compose.yml).
The bug was fixed in a later v3 patch release.

## Lesson learned
A container's internal client version is independent from what's installed
on the host. Always check the container's own dependencies when seeing
version mismatch errors.