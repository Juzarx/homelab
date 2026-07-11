# Grimmory MariaDB host not allowed to connect — 2026-07-11

**Service:** grimmory / mariadb
**Duration:** ~45 min

## What happened
Grimmory couldn't connect to its MariaDB container. Logs showed:
`Host 'grimmory.media' is not allowed to connect to this MariaDB server`

## Root cause
Grimmory and Nextcloud both sit on the same external `media` Docker network.
Suspected cause: when containers share an external network across multiple
Compose projects, Docker can resolve a container's internal hostname as
`<container>.<network>` instead of just the short container name, so the
grant MariaDB auto-created at first init didn't match what Grimmory
actually connected as.

## What didn't work
- Tried connecting as root with `-p` to manually widen the grant, kept
  getting rejected. Turned out root in this image authenticates via
  unix_socket, not password: `mariadb -u root` with no `-p` flag worked
  instead.
- Manually running `GRANT ... TO 'grimmory'@'%'` got the host mismatch
  error to go away, but then hit a straight access denied on the
  password instead, even after confirming it matched `.env`.

## Fix
Gave up patching the existing state and wiped it completely:

```bash
docker compose down -v
sudo rm -rf /mnt/media/grimmory/db/*
sudo rm -rf /mnt/media/grimmory/data/*
docker rm -f grimmory grimmory-db
docker compose up -d
```

Let MariaDB auto-initialize fresh from `.env` with no leftover grants or
partial state. Came up clean on the first try, no manual SQL needed.

## Lesson learned
For stateful services like a database, once manual patches start
stacking on top of each other and the state gets confusing, a full wipe
and clean re-init is often faster and more reliable than trying to
surgically fix broken grants. Worth trying earlier next time instead of
as a last resort.