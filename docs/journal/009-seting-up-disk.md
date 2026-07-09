# Day 9 - Disk and nextcloud set up

**Date:** 2026-07-07

**Objective:** Set up the HDD storage disk and deploy nextcloud

**Status:** Pending

**Related documents:**
- [Roadmap](../roadmap.md)
- [Architecture](../architecture.md)
- [Day 8](./008-creating-and-setting-up-media-vm.md)

## Disk set up
- Checked if the disk shows up in the VM with `lsblk`
- Partitioned the disk with `sudo fdisk /dev/sdb`
- Inside fdisk used `n` to create a new partition
- Pressed enter through the defaults.
- Used `w` to write changes and exit.
- Used `sudo mkfs.ext4 /dev/sdb1` to format the disk as ext4.
- Created the mounting point with `sudo mkdir -p /mnt/media`.
- Mounted the disk with `sudo mount /dev/sdb1 /mnt/media`.
- Made it persist across the reboots with sudo `blkid /dev/sdb1`.
- Copied the UUID and edited the fstab file on `sudo nano /etc/fstab`.
- Added the line `UUID=my-uuid-here  /mnt/media  ext4  defaults  0  2`.
- Tested if it works without rebooting with
    ```bash
    sudo umount /mnt/media
    sudo mount -a
    df -h /mnt/media 
    ```
- It works just fine.
- Created the nextcloud folder `sudo mkdir -p /mnt/media/nextcloud`.
- Created the grimmory folder `sudo mkdir -p /mnt/media/grimmory`.
- Gave my user owner permissions with `sudo chown -R $USER:$USER /mnt/media`.
- Ran `df -h /mnt/media` again to verify it worked.

## Power outage and unstable internet connection
- A power outage occurred.
- Once power was back it was not stable and kept going out.
- Internet connection was off for most part of the day once power was stable again.
- Decided to end the day here.