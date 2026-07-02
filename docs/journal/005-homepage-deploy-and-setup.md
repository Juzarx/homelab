# Day 5 - Homepage deploy and configuration

**Date:** 2026-06-27

**Objective:** Deploy and setup homepage

**Status:** Completed

**Related documents:**
- [Roadmap](../roadmap.md)
- [Architecture](../architecture.md)
- [Day 4](./004-pihole-and-networks-configuration.md)
- [Homepage on docker](https://gethomepage.dev/installation/docker/)
- [Homepage Settings](https://gethomepage.dev/configs/settings/)
- [Homepage Docker Compose File](/docker/infrastructure/homepage/docker-compose.yml)
- [Traefik Docker Labels](https://doc.traefik.io/traefik/reference/routing-configuration/other-providers/docker/)

## Deploying homepage
- Created a folder in the VM with the route `~/docker/infrastructure/homepage/config`.
- Navigated to the homepage folder using `cd ~/docker/infrastructure/homepage`.
- Created the [Homepage Docker Compose File](/docker/infrastructure/homepage/docker-compose.yml).
- Added the traefik labels to the compose file.
- Created the [homepage settings file](/docker/infrastructure/homepage/config/settings.yaml) in the config folder.
- Created the [homepage services file](/docker/infrastructure/homepage/config/services.yaml) in the config folder.
- Created the [homepage widgets file](/docker/infrastructure/homepage/config/widgets.yaml) in the config folder.
- Created the [homepage docker file](/docker/infrastructure/homepage/config/docker.yaml) in the config folder.
- Ran the container with `docker compose up -d`.
- Verified the container with `docker compose logs`.
- Realized Homepage files configuration files only works if they are in `.yaml` extension instead of `.yml`.
- Changed the extension of the configuration files.
- Restarted the container with `docker compose down` and then `docker compose up -d`.
- Checked the services were running correctly.

## Configuring widgets

- Added widget config for Traefik and Pi-hole in [services.yaml](/docker/infrastructure/homepage/config/services.yaml), pointing to their internal container ports instead of the `.home` URLs used for `href`.
- Needed to keep the Pi-hole API key out of GitHub, so created a `.env` file and referenced it in `services.yaml` using `{{HOMEPAGE_VAR_PIHOLE_API_KEY}}`.
- Added `env_file: .env` to [docker-compose.yml](/docker/infrastructure/homepage/docker-compose.yml) so Homepage could read the variable.
- Got error `Host validation failed for: homepage.home`. Fixed by adding `HOMEPAGE_ALLOWED_HOSTS=homepage.home` to `.env`.
- Pi-hole widget showed an API error. First copied the wrong credential, the current session token instead of the actual app password. Generated a proper app password from Pi-hole's API settings and it still failed.
- Realized the widget URL was pointing to the host-mapped port (`8888`) instead of the container's internal port. Homepage and Pi-hole share the same Docker network, so the widget needs to use `http://pihole` (port 80 internally) rather than the browser-facing `:8888`.
- Fixed the URL, restarted the container, and both widgets loaded correctly on the dashboard.
- Power outage happened due to an electric storm and decided to end the day.

## Notes
- `.yml` and `.yaml` are the same type of file, but some software expect to use one specific.