# Day 6 - Power outage and DNS troubleshooting

**Date:** 2026-07-01

**Objective:** Recover homelab after power outage and fix DNS resolution

**Status:** Completed

**Related documents:**
- [Roadmap](../roadmap.md)
- [Architecture](../architecture.md)
- [Day 5](./005-homepage-deploy-and-configuration.md)
- [Incident-004](../incidents/004-windows-ipv6-dns-override.md)

## Power outage recovery
- Electric storm caused a power outage, server was down for some time.
- Restarted the entire server once power was back.
- Confirmed all containers were up with `docker ps`.
- Traefik, Pi-hole and Homepage all showed as running.

## DNS troubleshooting
- Could not reach `homepage.home` or any other service by hostname, only by IP.
- Checked Pi-hole DNS records, all were intact.
- Tested `nslookup homepage.home 192.168.1.65` directly against Pi-hole, worked correctly.
- Checked Windows DNS settings with `ipconfig /all`, found the router was pushing IPv6 DNS servers ahead of Pi-hole.
- Realized DHCP hands out IPv4 address and DNS servers separately.
- Toggling IPv6 off in the general Windows network settings did not apply to the Ethernet adapter specifically.
- Set DNS manually on the Ethernet adapter itself through Control Panel, not the Settings app.
- Set IPv4 DNS to `192.168.1.65` and IPv6 DNS to `::1` to fully stop the router's IPv6 DNS from being used.
- Flushed DNS cache with `ipconfig /flushdns`.
- Tested `nslookup homepage.home`, resolved correctly.
- Documented the full issue on [Incident-004](../incidents/004-pihole-windows-dns-resolution.md).

## Notes
- DHCP reservations keep the server's IP fixed, but do not control what DNS servers get pushed to client devices.
- Set Pi-hole as the DNS server directly in the router's DHCP configuration, so future devices get it automatically without manual per-device setup.