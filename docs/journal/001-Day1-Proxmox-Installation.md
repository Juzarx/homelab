# Day 1 - Proxmox Installation

**Date:** 2026-06-16

**Objective:** Install Proxmox VE.

**Status:** Completed

**Related documents:**
- [Roadmap](..\roadmap.md)
- [Architecture](../architecture.md)
- [Proxmox Downloads](https://www.proxmox.com/en/downloads/proxmox-virtual-environment)
- [Rufus](https://rufus.ie/en/)

## Steps

- Downloaded the Proxmox VE ISO.
- Downloaded Rufus.
- Created bootable USB drive using Rufus.
- Install Proxmox VE on the 500 gb SSD.
- Configure root user and password.
- Rebooted the system.
- Accessed the Proxmox web interface form my main PC.
- Configured a DHCP reservation on the ISP router to keep a fixed IP address.
- updated and upgraded the system using `apt upgrade` and `apt update`.

## Notes

The installation process was smoother than I expected. Next step is to configure SSH access and the creation of the Virtual Machines.