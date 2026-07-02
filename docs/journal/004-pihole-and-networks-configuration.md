# Day 4 - Pi-hole and network configuration

**Date:** 2026-06-26

**Objective:** Install and setup Pi-hole

**Status:** Completed

**Related documents:**
- [Roadmap](../roadmap.md)
- [Architecture](../architecture.md)
- [Day 3](./003-docker-installation-and-first-containers.md)
- [Pi-hole on docker](https://github.com/pi-hole/docker-pi-hole/#running-pi-hole-docker)
- [Day 5](./005-homepage-deploy-and-setup.md)

## Pi-hole installation
- Created a new folder on `~/docker/infrastructure/pihole` and opened it.
- Created the [.env](/docker/infrastructure/pihole/.env.example) with password and time zone.
- Created the [Pi-hole docker-compose.yml](/docker/infrastructure/pihole/docker-compose.yml).
- Used port 53 on the docker compose as it is the DNS port.
- Used the port 8888:80 the docker compose because 8080 is already in use by Traefik.
- Navigated to `cd ~/docker/infrastructure/pihole`
- Started pi-hole with `docker compose up -d`.
- Got error `failed to bind host port 0.0.0.0:53/tcp: address already in use`.
- Checked the logs with `docker compose logs`.
- Fixed by disabling Ubuntu's stub listener. Check [Issue-002](../incidents/002-port-53-conflict-with-systemd-resolved.md)
- Checked the logs again with `docker compose logs` everything all right.
- Checked web dashboard with `MyVMIP:8888` and logged in.
- Pointed my local machine DNS to Pi-hole using `MyVMIP` as DNS.
- Tested if it worked with `nslookup google.com MyVMIP`.
- Got warning in Pi-hole logs `dnsmasq: ignoring query from non-local network 192.168.1.215 (logged only once)`.
- Fixed by adding `FTLCONF_dns_listeningMode: "all"` to the compose environment. Check [Incident-003](../incidents/003-pihole-ignoring-non-local-network.md)
- Made sure to flush the DNS cache using `ipconfig /flushdns` on my cmd console.
- Added the first local DNS record adding `MyVMIP` as `homelab.home`.
- Tested if it worked with `nslookup homelab.home` and `ping homelab.home`.
- Added all infrastructure and media services with `MyVMIP` each as `servicename.home`.
- Tested if all the DNS records worked. All worked just fine.
