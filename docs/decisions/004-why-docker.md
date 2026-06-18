# Why I chose Docker — 2026-06-17

## Context
I needed a way to run multiple services (Nextcloud, Grafana, Minecraft,
etc.) on the same Ubuntu VM without them interfering with each other.

## Decision
Each service runs in its own container. Docker handles the isolation and
docker-compose makes the whole stack declarative — one file describes
every service, its ports, volumes, and dependencies.

## Why not installing services directly
Installing everything with apt means services share the same filesystem,
the same dependencies, and the same process space. One broken update can
affect unrelated services. Containers also match how applications are
deployed in real companies, which matters for my portfolio.