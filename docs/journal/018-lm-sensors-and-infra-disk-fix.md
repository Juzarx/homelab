# Day 18 - lm-sensors, infra disk fix and pihole data loss

**Date:** 2026-08-17

**Objective:** Install lm-sensors and node exporter on the proxmox host

**Status:** Completed

**Related documents:**
- [Roadmap](../roadmap.md)
- [Architecture](../architecture.md)
- [Day 17](./017-container-monitoring.md)
- [Node Exporter Github](https://github.com/prometheus/node_exporter)
- [Incident-009](../incidents/009-pihole-dns-records-lost-disk-full.md)

## Installing lm-sensors on proxmox
- Installed with `apt install lm-sensors -y`.
- Ran `sensors-detect`, accepted defaults.
- Confirmed real readings with `sensors`, cpu cores, chipset, nvme and battery all showing correctly.

## Installing node exporter on proxmox
- Downloaded the release with `wget` into `/tmp`.
- Extracted with `tar xvf`.
- Copied the binary to `/usr/local/bin/`.
- Created a dedicated system user with `useradd --no-create-home --shell /bin/false node_exporter`, so it doesn't run as root.
- Gave the user ownership of the binary with `chown`.
- Created a systemd service file at `/etc/systemd/system/node_exporter.service` with the `--collector.hwmon` flag to expose sensor data.
- Enabled and started it with `systemctl enable` and `systemctl start`.
- Verified with `curl localhost:9100/metrics | grep hwmon`, real temps showing.
- Added proxmox-host as a new job in prometheus.yaml.
- Confirmed it as UP in prometheus targets.
- Imported the hwmon dashboard in grafana with ID 24629, working correctly.

## Infra VM disk problem
- Same LVM under allocation issue as media and games VM, only part of the disk was actually usable.
- Confirmed with `vgs` and `lvs`, VG had free space not given to the logical volume.
- Fixed with `lvextend -l +100%FREE` and `resize2fs`, no proxmox side resize needed this time since the virtual disk was already the right size.
- Before fixing this, couldn't connect through vscode remote ssh and an apt upgrade failed with no storage space left.
- Ran `apt update` and `apt upgrade -y` again after fixing the disk, no more errors.

## DNS stopped working
- Could not reach any service by `.home` name, only by ip and port.
- Confirmed pihole itself was healthy, resolved google.com fine from inside the container.
- Confirmed port 53 was correctly owned by docker, no systemd-resolved conflict.
- Tested `nslookup grimmory.home` directly against pihole's ip, got non-existent domain.
- Realized all the local DNS records got wiped, likely from the disk being full earlier during the infra VM problem.
- Also lost the 2FA config for the homepage widget, adlists were untouched.
- Temporarily exposed pihole's port again since traefik routing depends on DNS which was the thing broken.
- Re-added all the DNS records pointing to the infra VM ip.
- Removed the temporary port again once `.home` names worked.
- Documented on [Incident-009](../incidents/009-pihole-dns-records-lost-disk-full.md).

## Notes
- A full boot disk isn't just a storage problem, it can cause real data loss on services trying to write during that window, not just failed installs.