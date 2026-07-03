# Day 7 - Traefik labels in all containers

**Date:** 2026-07-02

**Objective:** Add traefik labels in all compose file to get rid of ports in the URLs

**Status:** Completed

**Related documents:**
- [Roadmap](../roadmap.md)
- [Architecture](../architecture.md)
- [Day 6](./006-power-outage-and-dns-troubleshooting.md)
- [Incident-005](../incidents/005-tailscale-dns-resolving-lan-ip.md)

## Setting up labels
- Set up the labels on the [pi-hole docker compose file](/docker/infrastructure/pihole/docker-compose.yml).
- Set up the labels on teh [traefik docker compose file](/docker/infrastructure/traefik/docker-compose.yml).
- Restarted both containers with `docker compose down` and `docker compose up -d`.
- Removed the port mappings in the [homepage services file](/docker/infrastructure/homepage/config/services.yaml).
- Check if everything worked fine. Everything OK.

## Setting up tailscale
- Installed Tailscale with `curl -fsSL https://tailscale.com/install.sh | sh`.
- Start the client with `sudo tailscale up`.
- Used the link to log in and add the VM to my tailnet.
- Used `tailscale ip -4` to see my tailscale ip.
- Installed Tailscale on my phone and logged in with the same account.
- Tested `http://100.x.x.x` on mobile data, got a 404. Confirmed the tunnel itself was working.
- Added Pi-hole as a custom nameserver on the Tailscale admin console with Override DNS servers enabled.
- Homepage still wouldn't load on my phone, `.home` domains not resolving.
- Ruled out Private DNS on Android, MagicDNS conflicts and mismatched nameserver IP, none were the issue.
- Tested `nslookup homepage.home 100.x.x.x` from both PC and phone, both resolved correctly to `192.168.1.x`.
- Realized Pi-hole was answering with the VM's LAN IP, not reachable from mobile data outside the house.
- Fixed by advertising the LAN subnet through the VM instead of changing DNS records. Check [Incident-005](../incidents/005-tailscale-dns-resolving-lan-ip.md).
- Enabled IP forwarding on the VM with `net.ipv4.ip_forward = 1` in `/etc/sysctl.conf`.
- Ran `sudo tailscale up --advertise-routes=192.168.1.0/24`.
- Approved the route in the Tailscale admin console.
- Tested `homepage.home` on my phone with mobile data, worked correctly.

## Notes
- Planning to share media and game servers with close friends later, will need to set up Tailscale ACLs to limit what they can access.