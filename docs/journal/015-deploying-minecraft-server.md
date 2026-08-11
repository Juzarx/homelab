# Day 15 - Minecraft server deploy

**Date:** 2026-08-01

**Objective:** Deploy the KEO RPG optimized modpack as a dedicated server using docker

**Status:** Completed

**Related documents:**
- [Roadmap](../roadmap.md)
- [Architecture](../architecture.md)
- [Day 14](./014-creating-and-setting-up-games-vm.md)
- [itzg/docker-minecraft-server](https://github.com/itzg/docker-minecraft-server)
- [KEO RPG optimized modpack](https://www.curseforge.com/minecraft/modpacks/keo-rpg-optimized)
- [Day 16](./016-starting-with-monitoring.md)

## Getting the modpack info
- Modpack is KEO RPG optimized, over 200 mods, Minecraft 1.21.1, NeoForge.
- Got a CurseForge API key from https://console.curseforge.com/, now required to auto install modpacks.
- Got the modpack slug `keo-rpg-optimized` and file id from the pack's Files tab.

## Deploying the server
- Created the folders with `mkdir -p ~/docker/games/minecraft/data`.
- Created the [.env file](/docker/games/minecraft/.env.example) with the CF api key, slug and file id.
- Created the [minecraft docker compose file](/docker/games/minecraft/docker-compose.yaml) using itzg/minecraft-server with TYPE AUTO_CURSEFORGE.
- Set MEMORY to 6G instead of the full 8gb available, to leave room for the OS and docker overhead.
- Started the container with `docker compose up -d`.
- Watched the logs with `docker compose logs -f`, first boot takes a while for 200+ mods.
- Got a fatal error, two mods failed to load: Immersive Overlays and Armor HUD, both client-only mods trying to load GUI classes that don't exist on a dedicated server.
- Added `CF_EXCLUDE_MODS` with both mod ids to the compose file.
- Same error still happened even after the compose update.
- Wiped the data folder with `sudo rm -rf data/*` for a clean reinstall, same lesson as the grimmory mariadb incident.
- Changed the mod names in CF_EXCLUDE_MODS to their numeric project ids instead of slugs.
- Got a new error in a resource reload worker thread, looked fatal but the server kept running past it.
- Confirmed with `docker ps` and `docker logs minecraft --tail 15` that the server was actually up and had reached Done.
- Connected from minecraft and it worked, could play normally.

## Setting up the client
- Wanted to avoid the CurseForge app since it requires Overwolf.
- Installed Prism Launcher instead, installs curseforge modpacks directly with no overwolf needed.
- Changed Prism's Instances and Mods folders to the D drive instead of C, to avoid filling the OS disk with 200+ mods.
- Installed the modpack through Prism using the curseforge search.
- Connected to the server through multiplayer using the tailscale ip and port 25565.

## Notes
- AUTO_CURSEFORGE only resolves and downloads the modpack cleanly on a first, uninterrupted run. If a previous attempt failed partway through, wiping the data folder before retrying is more reliable than trusting env var changes alone to fix it.
- Client-only mods failing on a dedicated server is common for packs not specifically built for server hosting, CF_EXCLUDE_MODS with the numeric project id is the fix.