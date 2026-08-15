# Day 16 - Monitoring stack deploy

**Date:** 2026-08-10

**Objective:** Start with the monitoring services

**Status:** Completed

**Related documents:**
- [Roadmap](../roadmap.md)
- [Architecture](../architecture.md)
- [Day 15](./015-deploying-minecraft-server.md)
- [Node-Exporter Github](https://github.com/prometheus/node_exporter)
- [Prometheus Github](https://github.com/prometheus/prometheus)
- [Traefik labels](https://doc.traefik.io/traefik/reference/routing-configuration/other-providers/docker/)
- [Grafana on docker](https://grafana.com/docs/grafana/latest/setup-grafana/installation/docker/)
- [Grafana Community dashboards](https://grafana.com/grafana/dashboards/)
- [Day 17](./017-container-monitoring.md).

## Installing node-exporter in all VMs
- Connected to the infrastructure VM.
- Created the node exporter folder.
- Created the [Infra Node-exporter compose file](/docker/infrastructure/node-exporter/docker-compose.yaml).
- Did the same on the media VM to create the [Media Node-exporter compose file](/docker/media/node-exporter/docker-compose.yaml).
- Did the same on the games VM to create the [Games Node-exporter compose file](/docker/games/node-exporter/docker-compose.yaml).
- Tried all the connections with `curl localhost:9100/metrics` on each VM.

## Deploying Prometheus
- Connected to the infrastructure VM.
- Created the prometheus folder with `mkdir -p ~/docker/infrastructure/prometheus`.
- Navigated to the folder with `cd ~/docker/infrastructure/prometheus`.
- Created the [Prometheus config file](/docker/infrastructure/prometheus/prometheus.yaml).
- Created the [Prometheus docker compose file](/docker/infrastructure/prometheus/docker-compose.yaml).
- Started the container with `docker compose up -d`.
- Verified if all targets were up in http://prometheus.home.
- Everything worked fine.

## Deploying Grafana
- Created the grafana folder with `mkdir -p ~/docker/infrastructure/grafana`.
- Navigated to the folder with `cd ~/docker/infrastructure/grafana`.
- Created the [.env grafana file](/docker/infrastructure/grafana/.env.example).
- Created the [Grafana docker compose file](/docker/infrastructure/grafana/docker-compose.yaml).
- Started the container with `docker compose up -d`.
- Entered grafana in http://grafana.home.
- Logged in with my credentials.
- Added prometheus as a source.
- Used a community dashboard with the ID:1860.

## Adding services to Homepage
- Added Prometheus widget to the [Homepage services file](/docker/infrastructure/homepage/config/services.yaml).
- Added Grafana and widget to the [Homepage services file](/docker/infrastructure/homepage/config/services.yaml).
- Added Grafana variables to the [.env file](/docker/infrastructure/homepage/.env.example).
- Removed and started the homepage container to update the environmental variables.