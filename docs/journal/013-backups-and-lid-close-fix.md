# Day 13 - Backups and preventing sleep on lid close

**Date:** 2026-07-29

**Objective:** Set up scheduled backups and stop the host from sleeping when the lid closes

**Status:** Completed

**Related documents:**
- [Roadmap](../roadmap.md)
- [Architecture](../architecture.md)
- [Day 12](./012-deploying-navidrome.md)
- [Incident-007](../incidents/007-lid-close-suspending-proxmox.md)

## Checking disk space for backups
- Worried the HDD didn't have enough room for backups plus the future Minecraft server.
- Checked real usage on the Proxmox host with `df -h /hdd` instead of trusting the 750gb allocated to the disk, since it's qcow2 with thin provisioning.
- Confirmed actual usage was still low, plenty of room.

## Setting up Proxmox backups
- Went to Datacenter > Backup > Add.
- Set storage to hdd1-storage, schedule for 3am, mode snapshot, compression zstd.
- Set retention to keep last 3 backups.
- Ran the job manually first with Run now to confirm it worked before trusting the schedule.
- Backup completed successfully.

## Preventing the laptop from sleeping on lid close
- Set `HandleLidSwitch=ignore` in `/etc/systemd/logind.conf`, restarted systemd-logind, lid close still suspended the host.
- Checked ACPI directly with `journalctl -k | grep -i lid`, confirmed the lid switch was detected correctly.
- Checked `/proc/acpi/wakeup`, nothing related to lid.
- Suspected acpid might be interfering, checked with `systemctl status acpid`, it wasn't even installed.
- Ran `systemctl show systemd-logind | grep -i handle`, got nothing useful back.
- Checked `/etc/systemd/logind.conf` directly and realized the line was never actually uncommented, still had the `#` in front of it.
- Uncommented `HandleLidSwitch=ignore`, `HandleLidSwitchExternalPower=ignore` and `HandleLidSwitchDocked=ignore`.
- Restarted systemd-logind again.
- Verified with `systemctl show systemd-logind -p HandleLidSwitch`, showed ignore correctly this time.
- Closed the lid, waited a minute, checked services from another device, still up. Worked.
- Documented the whole thing on [Incident-007](../incidents/007-lid-close-suspending-proxmox.md).

## BIOS settings
- Entered BIOS with F10 on boot.
- Turned on battery health / battery care mode to avoid keeping the battery at 100% all the time.
- Looked for a lid close setting in BIOS, only found wake on lid open, nothing about closing it, makes sense since lid close is handled by the OS not the firmware.

## Notes
- Systemd config files ship fully commented out by default, editing a commented line does nothing until the `#` is removed. Always verify with `systemctl show` instead of trusting the file was saved correctly.