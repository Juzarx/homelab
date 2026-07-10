# Day 10 - Nextcloud deploy

**Date:** 2026-07-09

**Objective:** Set up the HDD storage disk and deploy nextcloud

**Status:** Complete

**Related documents:**
- [Roadmap](../roadmap.md)
- [Architecture](../architecture.md)
- [Day 9](./009-seting-up-disk.md)
- [Nextcloud on Docker](https://github.com/nextcloud/docker)
- 

## Deploying nextcloud
- Created the docker directory with `mkdir -p ~/docker/media/nextcloud`.
- Created the storage folders in the HDD with `mkdir -p /mnt/media/nextcloud/db` and `mkdir -p /mnt/media/nextcloud/data`.
- Navigate to the nextcloud directory with `cd ~/docker/media/nextcloud`.
- Created a basic [nextcloud docker compose file](/docker/media/nextcloud/docker-compose.yaml).
- Deployed the container using `docker compose up -d`.
- Entered the web UI with `MyVMIP:8081`
- Got the error `Can't write into config directory! This can usually be fixed by giving the webserver write access to the config directory`.
- Fixed the error giving nextcloud permissions with `sudo chown -R www-data:www-data /mnt/media/nextcloud/data` and refreshed the tab.
- Wrote the credentials and wait for the installation to complete.
- Entered the dashboard and uploaded some files to ensure it is working.

## Routing nextcloud on traefik
- Added the line ` OVERWRITEPROTOCOL: http` and `NEXTCLOUD_TRUSTED_DOMAINS: nextcloud.home` on the [docker compose file](/docker/media/nextcloud/docker-compose.yaml)
- Accessed the infrastructure VM and created the [nextcloud configuration file](/docker/infrastructure/traefik/config/nextcloud.yml) on the traefik config folder.
- The trusted domain only works if it's added in the first time the compose runs.
- Used the command `docker exec -u www-data nextcloud php occ config:system:get trusted_domains` to list the trusted domains.
- Used `docker exec -u www-data nextcloud php occ config:system:set trusted_domains 1 --value=nextcloud.home` to add the nextcloud domain as trusted.
- Tried to get into `Homepage.home` and succeeded.

## Adding nextcloud to homepage
- Modified [homepage services file](/docker/infrastructure/homepage/config/services.yaml).
- Added the homepage widgets info on the [services file](/docker/infrastructure/homepage/config/services.yaml).
- Created a token using `docker exec -u www-data nextcloud php occ config:app:set serverinfo token --value mytoken`.
- Added the token to the [.env file](/docker/infrastructure/homepage/.env.example).
- Restarted the container with `docker compose down` and `docker compose up -d`.

## Notes
- Homepage's `{{...}}` variable substitution only works if the env var name starts with `HOMEPAGE_VAR_`. Used `HOMEPAGE_NEXTCLOUD_TOKEN` instead of `HOMEPAGE_VAR_NEXTCLOUD_TOKEN` and got silent 401s instead of an obvious error.