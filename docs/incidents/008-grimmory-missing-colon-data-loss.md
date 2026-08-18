# Grimmory losing all data on every restart, missing colon in volume mount — 2026-08-16

**Service:** grimmory / mariadb
**Duration:** ~2 hours

## What happened
Updated Grimmory's version in the compose file and restarted. Library
showed empty, had to create the admin user again. Turned out not just
users were gone, but also configuration and metadata, a full db wipe.

## Root cause
The mariadb service's volumes line was missing the colon separating host
path from container path:

```yaml
volumes:
  - /mnt/media/grimmory/db/config
```

Should have been:

```yaml
volumes:
  - /mnt/media/grimmory/db:/config
```

Without the colon, Docker never actually mounted the HDD folder into the
container. MariaDB's real data was living only inside the container's own
writable layer, with nothing backing it externally. Confirmed with
`docker volume ls | grep grimmory`, returned nothing, no anonymous volume
either, so nothing was ever recoverable once a container got removed.

Every `docker compose down` removes the container itself, not just stops
it, so every restart wiped everything and MariaDB just silently
reinitialized fresh, no error anywhere pointing to the actual problem.

## Fix
Corrected the volumes line to include the colon. Restarted, hit the same
host-grant mismatch from the original grimmory setup incident, since
MariaDB was genuinely initializing fresh on real persistent storage for
the first time. Fixed the same way as before, wiped `/mnt/media/grimmory/db`
and let it reinit clean:

```bash
docker compose down
sudo rm -rf /mnt/media/grimmory/db/*
docker compose up -d
```

## Lesson learned
A single missing colon in a volumes line doesn't throw any error, the
container just starts normally and appears to work, silently never
persisting anything. Always verify a new bind mount actually landed data
on the host after first deploy, don't just trust the container came up
clean. Checked with `ls -la` on the host path, an empty folder after the
app has clearly been used is the tell.

Also confirmed this wasn't a Grimmory bug, checked their GitHub issues
for similar reports first before digging into the compose file, found
nothing matching but it was worth ruling out before assuming user error.