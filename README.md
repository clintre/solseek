<img src="/demo/solseek-logo.png" align="left" width="64"/>

# Solseek
## A TUI Package Manager for Solus

[Features](#features) | [Requirements & Installation](#requirements) | [Usage](#usage)

Solseek is a simple terminal user interface that allows you to browse, search, and manage packages from the Solus packages. Packages can be installed, reinstalled, updated, verified, and removed through the interface. It is built around the native tools ( bash, eopkg, flatpak, etc.) to avoid complications. It uses the power of fzf for the ui/ux and filtering.

<p align="center">Click image below to see a short demo video</p>

[![See it in Action](https://raw.githubusercontent.com/clintre/solseek/main/demo/demo_thumb.png)](https://www.youtube.com/watch?v=qAFCz32Buvw)

## Features
  - Select and install multiple packages at once
  - View package details
  - Manage system updates for installed tools such as; eopkg, flatpak, snap, distrobox, and fwupd
  - Verify all packages installed by eopkg
  - View and export installed packages for eopkg and flatpak (all and/or user installed)
  - View system configurations

## Known Limitations
  - Currently only in English

## Planned
  - Ability to search and install/uninstall flatpaks [coming soon]
  - Update checks and notifications
  - Additional languages (looking for help on this)

## Requirements
  - [Solus](https://getsol.us/)
  - [eopkg](https://github.com/getsolus/eopkg)
  - [fzf](https://github.com/junegunn/fzf)

## Installation
```
sudo eopkg it solseek
```

## Usage
### Launching Solseek
  - Desktop menu entry Solseek
  - Terminal `solseek`
### Navigation
  - Keyboard
    - Arrow Keys for up/down navigation
    - [ENTER] to select menu entry
    - [ESC] or [CTRL]+[C] to go back
    - [SHIFT]+[TAB] to select multiple items ([ENTER] to execute action)
  - Mouse / Touchpad
    - Scroll up/down
    - Single left click to view entry
    - Double left click to execute/select entry
    - [CTRL]+left click to select multiple items 

## Credits
Solus and eopkg! Solseek uses eopkg natively to handle the packaging information and interaction. 
There was no need to write some system to extract the data as the Solus team has done a wonderful job already with eopkg and it allows me to simply wrap this tool around the strengths of it.
    
## Inspirations from other distro tools
  - [pacseek](https://github.com/moson-mo/pacseek)
  - [dnfseek](https://github.com/OmarHesham2356/dnfseek)
