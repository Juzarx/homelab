# Roadmap

## Phase 1 - Foundations

**Goal:** Prepare the host and networking.

- [x] Install Proxmox VE
- [x] Configure DHCP reservation on ISP router
- [ ] Configure SSH access
- [ ] Configure SSH keys
- [ ] Install Tailscale on Proxmox
- [x] Create GitHub repository
- [ ] Complete documentation

**Skills:**
- Linux
- Networking
- SSH
- Proxmox

---

## Phase 2 - Infrastructure VM

**Goal:** Create the management environment.

### VM Specs

- Ubuntu Server
- 2 vCPU
- 2 GB RAM
- 30 GB Disk

### Services

- [ ] Install Docker
- [ ] Install Docker Compose
- [ ] Install Tailscale
- [ ] Deploy Homepage
- [ ] Deploy Traefik

**Skills:**
- Docker
- Reverse Proxy
- Linux Administration

---

## Phase 3 - Media VM

**Goal:** Deploy personal services.

### VM Specs

- Ubuntu Server
- 4 vCPU
- 4 GB RAM
- 100 GB Disk

### Services

- [ ] Deploy Nextcloud
- [ ] Deploy Audiobookshelf
- [ ] Deploy Navidrome
- [ ] Configure persistent volumes
- [ ] Configure backups

**Skills:**
- Docker Compose
- Persistent Storage
- Volume Management

---

## Phase 4 - Games VM

**Goal:** Host dedicated game servers.

### VM Specs

- Ubuntu Server
- 4 vCPU
- 6 GB RAM
- 100 GB Disk

### Services

- [ ] Install Docker
- [ ] Install Tailscale
- [ ] Deploy Minecraft Server
- [ ] Deploy Project Zomboid Server
- [ ] Deploy Satisfactory Dedicated Server
- [ ] Configure backups

**Skills:**
- Docker
- Game Server Administration
- Networking

---

## Phase 5 - Monitoring

**Goal:** Monitor the homelab.

### Services

- [ ] Deploy Prometheus
- [ ] Deploy Grafana
- [ ] Install Node Exporter
- [ ] Monitor containers
- [ ] Monitor VMs
- [ ] Create dashboards

**Skills:**
- Monitoring
- Metrics
- Observability

---

## Phase 6 - Automation

**Goal:** Automate repetitive tasks.

### Python Scripts

- [ ] Backup scripts
- [ ] Health checks
- [ ] Container monitoring
- [ ] Service restart scripts

**Skills:**
- Python
- Automation
- Linux Scripting

---

## Phase 7 - CI/CD

**Goal:** Automate workflows.

### GitHub Actions

- [ ] Validate Docker Compose files
- [ ] Run Python checks
- [ ] Deploy containers automatically
- [ ] Create CI pipelines

**Skills:**
- GitHub Actions
- CI/CD

---

## Phase 8 - Infrastructure as Code

**Goal:** Provision infrastructure automatically.

### Terraform

- [ ] Learn Terraform fundamentals
- [ ] Configure Proxmox provider
- [ ] Provision VMs automatically

**Skills:**
- Terraform
- Infrastructure as Code

---

## Phase 9 - Kubernetes Lab

**Goal:** Learn container orchestration.

### Kubernetes Lab VM

- [ ] Install k3s
- [ ] Learn Helm
- [ ] Deploy sample applications
- [ ] Explore GitOps

**Skills:**
- Kubernetes
- Helm
- GitOps