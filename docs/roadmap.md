# Roadmap

## Phase 1 - Foundations

**Goal:** Prepare the host and networking.

- [x] Install Proxmox VE
- [x] Configure DHCP reservation on ISP router
- [x] Configure SSH access
- [x] Configure SSH keys
- [x] Create GitHub repository
- [X] Complete documentation

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
- 32 GB Disk

### Services
- [x] Install Docker
- [x] Deploy Traefik
- [X] Deploy Pi-hole
- [x] Deploy Homepage
- [x] Install Tailscale

**Skills:**
- Docker
- Reverse Proxy
- DNS
- Linux Administration

---

## Phase 3 - Media VM

**Goal:** Deploy personal services.

### VM Specs

- Ubuntu Server
- 4 vCPU
- 4 GB RAM
- 64 GB SSD
- 750 GB HDD

### Services
- [x] Install Docker
- [x] Install Tailscale
- [x] Deploy Nextcloud
- [x] Deploy Grimmory
- [x] Deploy Navidrome
- [x] Configure persistent volumes
- [x] Configure backups

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
- [ ] Install lm-sensors on all VMs
- [ ] Import Node Exporter community dashboard in Grafana
- [ ] Install Node Exporter on Infra VM
- [ ] Install Node Exporter on Media VM
- [ ] Install Node Exporter on Games VM
- [ ] Monitor containers
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

> This phase is exploratory — tackle it after the rest of the homelab is stable and running.

### Kubernetes Lab VM

- [ ] Install k3s
- [ ] Learn Helm
- [ ] Deploy sample applications
- [ ] Explore GitOps

**Skills:**
- Kubernetes
- Helm
- GitOps