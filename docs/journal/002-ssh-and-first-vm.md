# Day 2 - SSH and first VM

**Date:** 2026-06-19

**Objective:** Install Ubuntu Server as the infrastructure VM on proxmox. Access proxmox and the Infrastructure VM via SSH

**Status:** Completed

**Related documents:**
- [Roadmap](../roadmap.md)
- [Architecture](../architecture.md)
- [Day 1](./001-Day1-Proxmox-Installation.md)
- [Ubuntu Server download](https://ubuntu.com/download/server)

## SSH to Proxmox using an SSH key pair:

- Access Proxmox using `ssh root@YourProxmoxIP` and inserting the password.
- Create an SSH key pair on the local machine using `ssh-keygen -t ed25519 -C "AnyIdentifierYouLike"`
- On a powershell terminal we use `Get-Content $HOME\.ssh\id_ed25519.pub` and copy the public key
- Now in the proxmox terminal we use `mkdir -p ~/.ssh` to create the .ssh folder if it does not exist
- Change the permissions on the folder to execute, read and write for the owner with `chmod 700 ~/.ssh`
- Open the ssh keys file with `nano ~/.ssh/authorized_keys`
- Paste the key gotten on powershell previously
- Use `ctrl + O` and `Enter` to save the changes and `ctrl + X` to exit the file
- Change the file permissions to read and write only by the owner with `chmod 600 ~/.ssh/authorized_keys`
- Test the configuration with: `ssh root@YourProxmoxIP`. If no password is requested, the key authentication is working correctly.

## Installing Ubuntu Server VM on Proxmox:

- Access Proxmox web interface using the url http://YourProxmoxIP:8006
- Download the Ubuntu server ISO on https://ubuntu.com/download/server
- Upload the ISO on the Proxmox interface Datacenter > yourNode(Usually pve) > local > ISO images > upload
- Select create VM
- Name it, I used the name InfrastructureVM
- Select the OS, in this case Ubuntu Server
- Select machine as q35 to emulate a modern chipset.
- Select OVMF instead of SeaBIOS to get a virtual UEFI (Better for compatibility)
- Using 2 CPU cores, 32GB SSD, 2GB RAM, use Network VirtIO and enable guest agent.
- Follow the steps on screen to install the OS
- Fix the IP with the DHCP reservation on your router configuration
- Reboot the VM
- Enter your credentials
- Use `sudo apt update` and `sudo apt upgrade -y` to update all the packages
- Use:

  `sudo apt install qemu-guest-agent curl git -y`

  to install:

  - **qemu-guest-agent**: Allows Proxmox to communicate with the VM.
  - **curl**: Tool used to make HTTP requests and download scripts.
  - **git**: Version control system used for GitHub repositories.



## SSH to the infrastructure using a SSH key pair:

- Access the VM using `ssh YourUser@YourVMIP` and inserting the password.
- On a powershell terminal we use `Get-Content $HOME\.ssh\id_ed25519.pub` and copy the public keys
- Now in the VM terminal we use `mkdir -p ~/.ssh` to create the .ssh folder if it does not exist
- Change the permissions on the folder to execute, read and write for the owner with `chmod 700 ~/.ssh`
- Open the ssh keys file with `nano ~/.ssh/authorized_keys`
- Paste the key gotten on powershell previously
- Use `ctrl + O` and `Enter` to save the changes and `ctrl + X` to exit the file
- Change the file permissions to read and write only by the owner with `chmod 600 ~/.ssh/authorized_keys`
- Test the configuration with: `ssh YourUser@YourVMIP`. If no password is requested, the key authentication is working correctly.


## Lessons learned

- SSH key authentication is safer and more convenient than password authentication.
- qemu-guest-agent improves the integration between Proxmox and the VM.
- Using DHCP reservations is easier to maintain than configuring static IPs inside each VM.
- Modern VM settings such as q35, OVMF and VirtIO provide better compatibility and performance.
- It's okay to use the same SSH key pair on proxmox and all VMs.

