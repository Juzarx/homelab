# Day 21 - Persistent control panel and traefik routing

**Date:** 2026-08-28

**Objective:** Make the web GUI persistent and rout it with traefik, pihole and homepage

**Status:** Completed

**Related documents:**
- [Roadmap](../roadmap.md)
- [Architecture](../architecture.md)
- [Day 20](./020-web-gui-for-minecraft-server.md)

## Making the web GUI persistent
- Found the exact pad i need to use, with `ls ~/scripts/venv/bin/python3`
- Created the systemd service file with `sudo nano /etc/systemd/system/homelab-control.service`
- Fill it with
  ``` ini
  [Unit]
    Description=Homelab Control Panel
    After=network.target

    [Service]
    User=julio
    WorkingDirectory=/home/julio/scripts
    ExecStart=/home/julio/scripts/venv/bin/python3 /home/julio/scripts/app.py
    Restart=always

    [Install]
    WantedBy=multi-user.target
    ```
- Enabled and started the systemd file using:
  ```bash
    sudo systemctl daemon-reload
    sudo systemctl enable homelab-control
    sudo systemctl start homelab-control
    sudo systemctl status homelab-control
    ```
- Tried the connection entering the web GUI without any SSH session.
- Worked fine

## Routing through traefik, pihole and homepage
- As traefik needs only discovers containers using docker I had to create a routing file on traefik
- Created the [Control Panel routing file](/docker/infrastructure/traefik/config/control.yml).
- Added the DNS name in Pihole's web GUI.
- Tried to enter the control panel with the .home domain.
- Got in without issues.
- Added the control panel service to [homepage services file](/docker/infrastructure/homepage/config/services.yaml)
- Tried to get reach the control panel using homepage.
- It worked correctly.