<img src="/demo/solseek-logo.png" align="left" width="64"/>

# Solseek
## A TUI Package Manager for Solus

solseek is a simple terminal user interface which allows you to browse, search, and manage packages from the Solus packages. Packages can be installed, reinstalled, updated, verified, and removed through the interface.

Note: This is a work in progress!

<p align="center">Click image below to see a short demo video</p>

[![See it in Action](https://raw.githubusercontent.com/clintre/solseek/main/demo/demo_thumb.png)](https://www.youtube.com/watch?v=qAFCz32Buvw)


## Features
  - Select and install multiple packages at once
  - View package details
  - Manage system updates for installed tools such as; eopkg, flatpak, snap, distrobox, and fwupd
  - Verify all packages installed by eopkg
  - View and export installed packages for eopkg and flatpak (all and/or user installed)
  - View system configurations

## Planned
  - Official package in the Solus repo
  - Ability to search and install/uninstall flatpaks
  - Update checks and notifications
  - Additional languages (looking for help on this)

## Requirements
  - [Solus](https://getsol.us/)
  - [eopkg](https://github.com/getsolus/eopkg)
  - [fzf](https://github.com/junegunn/fzf)

## Installation
  - Requirements: git and make
```
sudo eopkg it git
sudo eopkg it make
```
  - Install Steps
```
git clone https://github.com/clintre/solseek.git
cd ./solseek/package
sudo make install
```

## Inspirations from other distro tools
  - [pacseek](https://github.com/moson-mo/pacseek)
  - [dnfseek](https://github.com/OmarHesham2356/dnfseek)
