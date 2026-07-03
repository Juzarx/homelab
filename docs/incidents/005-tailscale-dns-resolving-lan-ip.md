# Tailscale DNS resolving LAN IP instead of Tailscale IP — 2026-07-02

**Service:** tailscale / pihole / homepage
**Duration:** ~1 hour

## What happened
After setting up Tailscale and adding my phone to the tailnet, I could
connect to the tunnel but `homepage.home` would not load on mobile data.
Requesting the VM's Tailscale IP directly returned a 404, which was
expected since no Host header was set. But the hostname itself never
loaded at all, not even a 404.

## Root cause
Traced through several possibilities before finding the real one:

- Checked Android's Private DNS setting, was already off, not the cause.
- Checked for a MagicDNS conflict in the Tailscale admin console,
  MagicDNS and the custom nameserver were both configured correctly,
  not the cause.
- Checked if the nameserver IP in the Tailscale admin console matched
  the VM's actual Tailscale IP, it matched, not the cause.
- Ran `nslookup homepage.home` against the Tailscale nameserver from
  both PC and phone, both resolved successfully.

The actual issue: Pi-hole was answering DNS queries with the VM's LAN
IP, not its Tailscale IP. On my PC this worked fine since it's on the
same LAN. On my phone using mobile data, that LAN IP is not reachable
at all, since Tailscale only routes to a device's own Tailscale IP by
default, not its entire local network.

## Fix
Instead of changing every Pi-hole DNS record to point to the Tailscale
IP, configured the VM as a Tailscale subnet router so the whole LAN
subnet becomes reachable through the tailnet:

- Enabled IP forwarding on the VM by adding `net.ipv4.ip_forward = 1`
  to `/etc/sysctl.conf` and reloading with `sysctl -p`.
- Advertised the LAN subnet with
  `sudo tailscale up --advertise-routes=<LAN_SUBNET>/24`.
- Approved the advertised route in the Tailscale admin console, routes
  stay disabled by default until manually approved.

With this in place, Pi-hole can keep answering with LAN IPs and any
device on the tailnet, including the phone on mobile data, can now
reach them through the VM acting as a gateway.

## Lesson learned
DNS resolving correctly does not guarantee the resolved address is
actually reachable from where the request is coming from. A LAN IP is
only reachable from Tailscale if the network itself is being routed
through the tailnet, not just the individual device.

## Security note
Advertising the LAN subnet makes every device on the home network
reachable to anything already inside the tailnet, not just the homelab
VM. Acceptable for a personal tailnet with only my own devices. Will
need to revisit with Tailscale ACLs before inviting friends, so they
only reach the specific services meant for them and nothing else.