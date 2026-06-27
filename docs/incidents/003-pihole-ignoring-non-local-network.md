# Pi-hole ignoring queries from non-local network — 2026-06-26

**Service:** pihole
**Duration:** ~10 min

## What happened
Pi-hole started successfully but rejected DNS queries from my local
machine (192.168.1.215) with the message:
`dnsmasq: ignoring query from non-local network 192.168.1.215`

## Root cause
Pi-hole runs inside a Docker network (172.x.x.x range). From its
perspective, my LAN (192.168.1.x) is a non-local network, so it
rejected queries coming from it by default.

## Fix
Added `FTLCONF_dns_listeningMode: "all"` to the environment variables
in docker-compose.yml. This tells Pi-hole to accept DNS queries from
all networks, not just its own Docker network.

## Lesson learned
Containers have their own network perspective. A service running inside
Docker does not see the host's LAN as local, it only sees its own
Docker network. Any service that needs to accept connections from the
LAN needs to be explicitly configured to listen beyond its container
network.