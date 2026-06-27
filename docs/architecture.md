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

User["Your PC / Phone"]
TS[Tailscale]

subgraph Infra["Infrastructure VM"]
    Pihole["Pi-hole (DNS)"]
    Traefik[Traefik]
    Homepage[Homepage]
    Prometheus[Prometheus]
    Grafana[Grafana]
end

subgraph Media["Media VM"]
    Nextcloud[Nextcloud]
    Books[Audiobookshelf]
    Music[Navidrome]
end

User -->|DNS| Pihole
User --> TS
TS --> Traefik

Traefik --> Homepage
Traefik --> Grafana
Traefik --> Nextcloud
Traefik --> Books
Traefik --> Music

Homepage -.-> Nextcloud
Homepage -.-> Grafana
Homepage -.-> Books
Homepage -.-> Music

Prometheus --> Grafana
```

## Games Architecture

```mermaid
graph LR

Me["Friends / Me"]
Tailscale[Tailscale]
GamesVM[Games VM]
Minecraft[Minecraft]
ProjectZomboid[Project Zomboid]
Satisfactory[Satisfactory]

Me --> Tailscale
Tailscale --> GamesVM
GamesVM --> Minecraft
GamesVM --> ProjectZomboid
GamesVM --> Satisfactory
```

