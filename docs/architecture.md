# Architecture

## Physical Host

HP Laptop

* Intel i7 8th Gen
* 16 GB RAM
* 500 GB SSD
* 1 TB HDD

Runs:

* Proxmox VE

---

## Network

Internet

↓

Router

↓

Tailscale Network

↓

Proxmox Host

↓

Virtual Machines

---

## VM 1 - Infrastructure

Purpose:

Core services and management.

Services:

* Docker
* Tailscale
* Homepage
* Reverse Proxy (future)

---

## VM 2 - Media

Purpose:

Personal cloud and media.

Services:

* Nextcloud
* Audiobookshelf
* Navidrome
* Jellyfin

Storage:

* Media files stored on 1 TB HDD.

---

## VM 3 - Games

Purpose:

Dedicated game servers.

Services:

* Minecraft
* Project Zomboid
* Satisfactory

Storage:

* Worlds and backups.

---

## VM 4 - Kubernetes Lab (Future)

Purpose:

Learning environment.

Services:

* Kubernetes
* Helm
* GitOps
* Terraform experiments

---

## Development Workflow

PC

↓

VS Code

↓

Git

↓

GitHub Repository

↓

SSH into VMs

↓

Deploy using Docker Compose

The GitHub repository is the source of truth for all configurations and automation.
