<img src="/demo/solseek-logo.png" align="left" width="64"/>

# Solseek
## A TUI Package Manager for Solus

[Features](#features) | [Requirements & Installation](#requirements) | [Usage](#usage)

Solseek is a simple terminal user interface that allows you to browse, search, and manage packages for Solus and Flatpak. Packages can be installed, reinstalled, updated, verified, and removed through the interface. It is built around the native tools ( bash, eopkg, flatpak, etc.) to avoid complications.

<p align="center">Click image below to see a short demo video</p>

[![See it in Action](https://raw.githubusercontent.com/clintre/solseek/main/demo/demo_thumb.png)](https://youtu.be/6WesNbTb_Sk)

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
  - Additional languages (looking for help on this)
  - Clean Package Cache
  - Common package repair tools
  - Recipes for common installs on Solus (Nvidia, Distrobox, etc)

## Requirements
  - [Solus](https://getsol.us/)
  - [eopkg](https://github.com/getsolus/eopkg)
  - [fzf](https://github.com/junegunn/fzf)
  - [appstream](https://www.freedesktop.org/wiki/Distributions/AppStream/)

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
    - <kbd>↓</kbd><kbd>↑</kbd> for navigation
    - <kbd>ENTER</kbd> to select menu entry
    - <kbd>ESC</kbd> or <kbd>CTRL</kbd>+<kbd>C</kbd> to go back
    - <kbd>SHIFT</kbd>+<kbd>TAB</kbd> to select multiple items (<kbd>ENTER</kbd> to execute action)
  - Mouse / Touchpad
    - Scroll up/down
    - Single left click to view entry
    - Double left click to execute/select entry
    - <kbd>CTRL</kbd>+left click to select multiple items 

## Credits
Solus and eopkg! Solseek uses eopkg natively to handle the packaging information and interaction. 
There was no need to write some system to extract the data as the Solus team has done a wonderful job already with eopkg and it allows me to simply wrap this tool around the strengths of it.
    
## Inspirations from other distro tools
  - [pacseek](https://github.com/moson-mo/pacseek)
  - [dnfseek](https://github.com/OmarHesham2356/dnfseek)
