# Why I chose Proxmox — 2026-06-17

## Context
I needed somewhere to run my homelab services on an old HP laptop.
The main options were installing Docker directly on the machine or
adding a hypervisor layer first.

## Decision
Proxmox gives me a virtualization layer between the hardware and my
services. I can run one or more Ubuntu VMs on top of it and manage
everything through a web UI.

## Why not bare metal Docker
Running Docker directly on the laptop means one bad config can affect
the whole machine. With Proxmox I can snapshot a VM before doing
something risky, roll back if I break it, and the host stays untouched.
It also mirrors how isolation works in real enterprise environments,
which is part of why I'm building this homelab.