# Day 12 - Navidrome deploy

**Date:** 2026-07-22

**Objective:** Deploy Navidrome and route it with traefik

**Status:** Complete

**Related documents:**
- [Roadmap](../roadmap.md)
- [Architecture](../architecture.md)
- [Day 11](./011-deploying-grimmory.md)
- [Navidrome Documentation](https://www.navidrome.org/docs/)

## Extending the logical volume
- Realized the 32gb assigned to the VM disk wasn't fully allocated to the filesystem.
- Resized the disk in Proxmox to 64gb.
- Installed the cloud utils with `sudo apt install cloud-guest-utils -y`
- Extended the partition with `sudo growpart /dev/sda 3`
- Extended the logical volume with `sudo lvextend -l +100%FREE /dev/mapper/ubuntu--vg-ubuntu--lv` and `sudo resize2fs`, worked correctly.

## Creating the folders
- Created the needed folders with the next command
``` bash
mkdir -p ~/docker/media/navidrome
cd ~/docker/media/navidrome
mkdir -p /mnt/media/navidrome/data
mkdir -p /mnt/media/navidrome/music
```

## Deploying navidrome
- Created the [.env file](/docker/media/navidrome/.env.example).
- Created the [navidrome docker compose file](/docker/media/navidrome/docker-compose.yaml).
- Started the container with `docker compose up -d`.
- Verified entering the web UI with `MyVMIP:4533`.
- Created the admin account. Worked correctly.

## Routing with traefik and homepage
- Created the [Traefik config file](/docker/infrastructure/traefik/config/navidrome.yml).
- Modified the [Homepage services file](/docker/infrastructure/homepage/config/services.yaml).
- Stopped the homepage container with `docker compose down`.
- Started the homepage container again with `docker compose up -d`.
- Tried the homepage and the `navidrome.home` accesses. Worked fine.

## Adding the Navidrome widget to homepage
- Generated a token with `echo -n "passwordsalt" | md5sum` for subsonic auth.
- Got `Unexpected error` on the widget after adding it.
- Tested the exact token/salt with curl directly against navidrome, confirmed it worked.
- Turned out the first attempt had mismatched credentials, which tripped navidrome's login rate limit (5 requests per 2 min). Fixing the credentials right after still showed the same vague error until the cooldown passed.
- Restarted homepage after the cooldown, worked correctly.