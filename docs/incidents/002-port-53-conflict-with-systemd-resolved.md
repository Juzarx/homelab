# Port 53 conflict with systemd-resolved — 2026-06-26
**Service:** Pi-hole
**Down for:** ~10 min

## What happened
While trying to create the container the next error showed up:
`failed to set up container networking: driver failed programming external connectivity on endpoint pihole (7b079c7ac43dd0b4022779b390d0eb60d6a1b75bd8682fea8b3dcebc2160a18e): failed to bind host port 0.0.0.0:53/tcp: address already in use`
Meaning there is a conflict with port 53, a common issue in Ubuntu with systemd-resolved.

## Fix
Disabling the stub listener
### Steps
- Enter `sudo nano /etc/systemd/resolved.conf`
- Find the lines, uncomment and set them with `DNS=8.8.8.8` `DNSStubListener=no`.
- Update `resolv.conf` using `sudo rm /etc/resolv.conf` to remove current `resolv.conf` file, and create a new one pointing to the corrected one with `sudo ln -s /run/systemd/resolve/resolv.conf /etc/resolv.conf`.
- Restart the service with `sudo systemctl restart systemd-resolved` for the changes to take effect.
- Verify if port 53 is free now with `sudo ss -tulnp | grep :53`

## Lesson learned
- The port 53 is by default occupied by the systemd-resolved on Ubuntu.
- We need a DNS so we use the google one 8.8.8.8.