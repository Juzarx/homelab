# Day 11 - Grimmory deploy

**Date:** 2026-07-10

**Objective:** Deploy Grimmory and route it with traefik

**Status:** Complete

**Related documents:**
- [Roadmap](../roadmap.md)
- [Architecture](../architecture.md)
- [Day 10](./010-deploying-nextcloud.md)
- [Grimmory documentation](https://grimmory.org/getting-started/)
- [Grimmory github](https://github.com/grimmory-tools/grimmory)
- [Mariadb Incident](../incidents/006-mariadb-hostname-mismatch.md)

## Deploying Grimmory
- Created all the needed folders with:
   ``` bash
    mkdir -p ~/docker/media/grimmory
    mkdir -p /mnt/media/grimmory/db
    mkdir -p /mnt/media/grimmory/data
    mkdir -p /mnt/media/grimmory/books
    mkdir -p /mnt/media/grimmory/bookdrop
    ```
- Navigated to the previously created Grimmory folder using `cd ~/docker/media/grimmory`.
- Created the [.env file](/docker/media/grimmory/.env.example).
- Added the `ALLOWED_ORIGINS` to the [.env file](/docker/media/grimmory/.env.example).
- Created the [grimmory docker compose file](/docker/media/grimmory/docker-compose.yaml).
- Started the container with `docker compose up -d`.
- Checked logs using `docker compose logs -f`.
- Got the error `Host 'grimmory.media' is not allowed to connect to this MariaDB server`.
- Ended up wiping the docker volumes and the folders for a fresh start, look at [Incident 006](../incidents/006-mariadb-hostname-mismatch.md).
- Accessed Grimmory web and created the admin user.

## Routing Grimmory trough traefik and homepage
- Added the [Grimmory configuration file](/docker/infrastructure/traefik/config/grimmory.yml).
- Added the Grimmory service to the [homepage services file](/docker/infrastructure/homepage/config/services.yaml).
- Modified the [homepage settings file](/docker/infrastructure/homepage/config/settings.yaml) to change the media layout.
- Tried to access grimmory from homepage and succeeded.

