# Day 3 - Docker installation and first containers

**Date:** 2026-06-25

**Objective:** Install Docker on Ubuntu server VM and start creating the first containers

**Status:** Completed

**Related documents:**
- [Roadmap](../roadmap.md)
- [Architecture](../architecture.md)
- [Day 2](./002-ssh-and-first-vm.md)
- [Docker Installation Guide](https://docs.docker.com/engine/install/ubuntu/)
- [Traefik Documentation](https://doc.traefik.io/traefik/)
- [Incident-001](../incidents/001-traefik-docker-provider-mismatch.md)
  
## qemu guest agent
- Noticed Proxmox was showing "guest agent not running" in the VM summary.
- The agent was installed but the option wasn't enabled in Proxmox VM options.
- Had to shut down completely (reboot command doesn't work for this) and power on.

## Docker Installation
- Searched on docker official documentation.
- Used the next commands to add Docker's official GPG key:
 ```bash
sudo apt update
sudo apt install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
```
- Then used the next commands to add the repository to APT sources
```bash
sudo tee /etc/apt/sources.list.d/docker.sources <<EOF
Types: deb
URIs: https://download.docker.com/linux/ubuntu
Suites: $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}")
Components: stable
Architectures: $(dpkg --print-architecture)
Signed-By: /etc/apt/keyrings/docker.asc
EOF
sudo apt update
```
- Then installed Docker latest version using `sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin`.
- After installation we can verify Docker is running with  `sudo systemctl status docker` if Docker is not running we can start it with `sudo systemctl start docker`.
- Finally to verify the installation we run `sudo docker run hello-world`.
- After we verify docker is successfully installed we add the user to docker group with `sudo usermod -aG docker $USER` to avoid using sudo while configuring docker. Log out and reconnect for this to take effect.

## Traefik installation
- Created a folder to install Traefik using `mkdir -p ~/docker/infrastructure/traefik/config`.
- Navigated to the created Traefik folder using `cd ~/docker/infrastructure/traefik` /config folder will be used later for services connections.
- Created the docker network infra using `sudo docker network create infra`.
- Created the Traefik configuration file [traefik.yml](/docker/infrastructure/traefik/traefik.yml).
- Created the [docker-compose.yml file](/docker/infrastructure/traefik/docker-compose.yml).
- Started Traefik with `docker compose up -d`.
- Checked if it started correctly with `docker compose logs`.
- Got the error "Error response from daemon: client version 1.24 is too old. Minimum supported API version is 1.40, please upgrade your client to a newer version"
- Error fixed changing the Traefik version. Check on [Incident-001](../incidents/001-traefik-docker-provider-mismatch.md).
- Accessed the service in my browser using `MyVMIP:8080`.