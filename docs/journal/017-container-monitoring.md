# Day 17 - Container monitoring

**Date:** 2026-08-14

**Objective:** Deploy cAdvisor and exporting to grafana

**Status:** Completed

**Related documents:**
- [Roadmap](../roadmap.md)
- [Architecture](../architecture.md)
- [Day 16](./016-starting-with-monitoring.md)
- [Grafana Community dashboards](https://grafana.com/grafana/dashboards/)

## Installing cAdvisor in all VMs
- Connected to the infrastructure VM.
- Created the cAdvisor folder.
- Created the [Infra cAdvisor Compose File](/docker/infrastructure/cadvisor/docker-compose.yaml).
- Repeated the process in media VM and created the [Media cAdvisor Compose File](/docker/media/cadvisor/docker-compose.yaml).
- Repeated the process in games VM and created the [Games cAdvisor Compose File](/docker/games/cadvisor/docker-compose.yaml).
- Deployed the service in all VMs

## Adding cAdvisor data to Prometheus
- Added the cadvisor nodes to the [Prometheus File](/docker/infrastructure/prometheus/prometheus.yaml).
- Stopped the prometheus container with `docker compose down`.
- Started the container with `docker compose up -d`.

## Adding a grafana dashboard
- Created a new dashboard.
- Imported the cAdvisor `14282` dashboard.
- Used Prometheus as data provider.