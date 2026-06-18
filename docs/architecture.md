# Architecture

## Physical Host

HP Probook 440 G5

* Intel i7 8th Gen
* 16 GB RAM
* 500 GB SSD
* 1 TB HDD

Runs:

* Proxmox VE

---

## Physical Architecture

```mermaid
graph TD

Internet[Internet]
Router[ISP Router]
Proxmox[Proxmox Host]

Infra[Infrastructure VM]
Media[Media VM]
Games[Games VM]

Internet --> Router
Router --> Proxmox

Proxmox --> Infra
Proxmox --> Media
Proxmox --> Games
```

## Services Architecture

```mermaid
graph LR

User[Your PC / Phone]

TS[Tailscale]

Infra[Infrastructure VM]

Traefik[Traefik]

Media[Media VM]

Nextcloud[Nextcloud]
Books[Audiobookshelf]
Music[Navidrome]

Grafana[Grafana]
Prometheus[Prometheus]

User --> TS

TS --> Infra

Infra --> Traefik

Infra --> Grafana
Infra --> Prometheus

Traefik --> Media
Traefik --> Grafana

Media --> Nextcloud
Media --> Books
Media --> Music
```

## Games Architecture

```mermaid
graph LR

Friends/Me

Tailscale

GamesVM[Games VM]

Minecraft

ProjectZomboid

Satisfactory

Friends/Me --> Tailscale

Tailscale --> GamesVM

GamesVM --> Minecraft
GamesVM --> ProjectZomboid
GamesVM --> Satisfactory
```

