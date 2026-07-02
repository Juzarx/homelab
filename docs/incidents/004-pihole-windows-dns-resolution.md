# Windows preferring router IPv6 DNS over Pi-hole — 2026-07-01

**Service:** pihole / DNS resolution
**Duration:** ~1 hour

## What happened
After a power outage, `.home` domains stopped resolving on my PC even
though Pi-hole was running correctly and DNS records were intact. Only
IP addresses worked, not hostnames.

## Root cause
My Ethernet adapter gets its IPv4 address via DHCP, but DNS servers were
also being assigned automatically by the router, separate from the IPv4
address itself. The router was pushing multiple DNS servers, IPv6 ones
first:

    2806:1030:ffff:4::e   (IPv6, tried first)
    2806:1020:ffff:4::e   (IPv6)
    192.168.1.65          (Pi-hole, third in line)
    8.8.8.8               (fallback)

Windows prefers IPv6 DNS when available, so it kept resolving through
the router's IPv6 DNS and skipping Pi-hole entirely — even though Pi-hole
was manually set as preferred DNS in the general network settings.

Disabling IPv6 in the OS-wide toggle (Settings > general network options)
was not enough, since it didn't apply to the Ethernet adapter specifically.

## Fix
Set DNS manually on the Ethernet adapter itself (not the router, not the
general Windows network toggle):

- IPv4 DNS: `192.168.1.65` (Pi-hole)
- IPv6 DNS: `::1` (disables IPv6 resolution instead of leaving it on
  automatic, which would keep pulling from the router)

Done via Control Panel > Network Connections > Ethernet > Properties >
IPv4 and IPv6 settings, rather than the newer Settings app.

## Lesson learned
DHCP can hand out an IP address and DNS servers independently — disabling
IPv6 in a general settings page does not guarantee it's disabled per
adapter. When multiple DNS servers are configured, Windows tries them in
order and prefers IPv6 over IPv4 by default. Any manual DNS override
needs to be applied at the specific network adapter level, not through
router settings or OS-wide toggles, to reliably take effect.