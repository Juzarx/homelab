# Why I chose Tailscale — 2026-06-17

## Context
I need a way to connect to my services outside my LAN. 

## Decision
Tailscale is a WireGuard-based VPN that creates a private network between
my devices without exposing any ports to the internet. It's easier and
safer than port forwarding.

## Why not Port Forwarding
In my region is common for ISPs to use CGNAT and to get an static and unique IP address is hard and expensive.
Also securitywise, tailscale is way easier to manage than port forwarding.