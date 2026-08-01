# Day 14 - Creating and setting up games VM

**Date:** 2026-07-31

**Objective:** Create and set up the games VM

**Status:** Completed

**Related documents:**
- [Roadmap](../roadmap.md)
- [Architecture](../architecture.md)
- [Day 13](./013-backups-and-lid-close-fix.md)
- [Docker Installation Guide](https://docs.docker.com/engine/install/ubuntu/)

## Creating the VM
- Selected create VM.
- Named the VM as games.
- Selected the OS in this case the previously downloaded Ubuntu server.
- Selected machine as q35 to emulate a modern chipset.
- Selected OVMF instead of SeaBIOS to get a virtual UEFI (Better for compatibility).
- Selected Network VirtIO and enable Qemu agent.
- On disk i assigned 64 gb of the ssd as the OS disk.
- Selected 1 socket and 4 cores for CPU.
- Selected the CPU type as host, better performance since there's no cluster to migrate between.
- Assigned 8 GB of RAM memory.
- Left network with the default values.
- Started the VM creation.
- Configure the OS with the GUI.
- Selected the SSD as installation disk.
- Noticed the installer only allocated 30gb to root, same LVM issue as media VM. Fixed it in the partitioner this time instead of resizing after.
- Checked the OpenSSH to install it.
- Created credentials.
- Rebooted the VM.
- Fixed the ip with with the router DHCP reservation.

## Set up
- Used `sudo apt update` and `sudo apt upgrade -y` to update all the packages
- Used:

  `sudo apt install qemu-guest-agent curl git -y`

  to install:

  - **qemu-guest-agent**: Allows Proxmox to communicate with the VM.
  - **curl**: Tool used to make HTTP requests and download scripts.
  - **git**: Version control system used for GitHub repositories.

## SSH Access to the Games VM
- Accessed the VM using `ssh MyUser@MyVMIP` and inserting the password.
- On powershell I used `Get-Content $HOME\.ssh\id_ed25519.pub` and copy the public keys
- In the VM terminal I used `mkdir -p ~/.ssh` to create the .ssh folder if it does not exist
- Changed the permissions on the folder to execute, read and write for the owner with `chmod 700 ~/.ssh`
- Opened the ssh keys file with `nano ~/.ssh/authorized_keys`
- Pasted the key gotten on powershell previously
- Used `ctrl + O` and `Enter` to save the changes and `ctrl + X` to exit the file
- Changed the file permissions to read and write only by the owner with `chmod 600 ~/.ssh/authorized_keys`
- Tested the configuration with: `ssh MyUser@MyVMIP`. If no password is requested, the key authentication is working correctly.
- It worked correctly.

## Docker Installation
- Used the next commands to add Docker's official GPG key:
 ```bash
sudo apt update
sudo apt install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
```
- Then used the next commands to add the repository to APT sources
```bash
sudo tee /etc/apt/sources.list.d/docker.sources <<EOF
Types: deb
URIs: https://download.docker.com/linux/ubuntu
Suites: $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}")
Components: stable
Architectures: $(dpkg --print-architecture)
Signed-By: /etc/apt/keyrings/docker.asc
EOF
sudo apt update
```
- Then installed Docker latest version using `sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin`.
- After installation we can verify Docker is running with  `sudo systemctl status docker` if Docker is not running we can start it with `sudo systemctl start docker`.
- Finally to verify the installation we run `sudo docker run hello-world`.
- After we verify docker is successfully installed we add the user to docker group with `sudo usermod -aG docker $USER` to avoid using sudo while configuring docker. Log out and reconnect for this to take effect.
- Created the docker network `games` with `sudo docker network create games`.
- Verified if media network was created with `sudo docker network ls`.

## Tailscale Installation
- Installed Tailscale with `curl -fsSL https://tailscale.com/install.sh | sh`.
- Start the client with `sudo tailscale up`.
- Used the link to log in and add the VM to my tailnet.
- Used `tailscale ip -4` to see my tailscale ip.


## Notes
- Next step is deploying the minecraft container.