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
graph TD

User[Your PC / Phone]

TS[Tailscale]

subgraph Infra["Infrastructure VM"]
    Homepage[Homepage]
    Traefik[Traefik]
    Prometheus[Prometheus]
    Grafana[Grafana]
end

subgraph Media["Media VM"]
    Nextcloud[Nextcloud]
    Books[Audiobookshelf]
    Music[Navidrome]
end

User --> TS

TS --> Traefik
TS --> Homepage

Homepage -. Links .-> Traefik

Traefik --> Nextcloud
Traefik --> Books
Traefik --> Music
Traefik --> Grafana

Prometheus --> Grafana
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

