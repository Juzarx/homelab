# Closing laptop lid suspended Proxmox despite HandleLidSwitch=ignore — 2026-07-29

**Service:** proxmox host
**Duration:** ~30 min

## What happened
Needed the Proxmox host to keep running with the lid closed, since the
screen light interferes with sleep. Set `HandleLidSwitch=ignore` in
`/etc/systemd/logind.conf` and restarted systemd-logind, but closing the
lid still suspended the whole host, taking every VM down with it.

## Root cause
The line was added correctly, but never uncommented. `logind.conf` ships
with every setting present but commented out (`#HandleLidSwitch=ignore`)
as a reference showing the default value, not an active config. Editing
a commented line without removing the `#` has no effect at all, systemd
just keeps using its actual default.

Confirmed with:
```bash
systemctl show systemd-logind -p HandleLidSwitch
```
which showed nothing meaningful until the `#` was removed, after which
it correctly reported `HandleLidSwitch=ignore`.

Also ruled out acpid as a possible cause (interferes with lid handling
on some distros) before finding the real issue, it wasn't even installed.

## Fix
Uncommented the relevant lines in `/etc/systemd/logind.conf`:
```
HandleLidSwitch=ignore
HandleLidSwitchExternalPower=ignore
HandleLidSwitchDocked=ignore
```
Restarted systemd-logind, confirmed with `systemctl show` that the
setting was actually active this time.

## Lesson learned
Systemd config files often ship fully commented out as documentation of
defaults, not a live config. Adding a value on an already-commented line
silently does nothing, always verify a systemd setting actually took
effect with `systemctl show <service> -p <Property>` rather than trusting
that saving the file was enough.