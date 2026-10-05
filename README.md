<img src="https://raw.githubusercontent.com/clintre/solseek/main/demo/solseek-logo.png" align="left" width="64"/>

# Solseek
## A TUI Package Manager for Solus
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](LICENSE)

🌟[Features](#features) 📑[Requirements & Installation](https://codeberg.org/clintre/solseek/wiki#getting-started) 📗[Wiki](https://codeberg.org/clintre/solseek/wiki) 💪[Contributing](#contributing) 

Solseek is a terminal user interface that allows you to browse, search, and manage packages and drivers for Solus and Flatpak. Packages can be installed, reinstalled, updated, verified, and removed through the interface. It is built around the native tools ( bash, eopkg, flatpak, etc.) to avoid complications.

[<img src="https://codeberg.org/clintre/solseek/raw/branch/main/demo/demo_thumb.png" width="640px" align="center" style="width: 640px; height: auto" />](https://codeberg.org/clintre/solseek/raw/branch/main/demo/demo_thumb.png)

<hr id="features">

## Features
  - Complete app store similar to Discover or Gnome Software
  - Works as a desktop app or from a terminal
  - Navigate and use with keyboard and/or mouse
  - Select and install multiple packages at once
  - Manage system updates for installed tools such as; eopkg, flatpak, snap, distrobox, and fwupd
  - Rollback system to help issues brought on by updates or installs
  - Driver manager for Nvidia and printer drivers (more coming)
  - Verify all packages
  - View and export installed packages for eopkg and flatpak (all and/or user installed)
  - Recall (rollback) system package actions
  - Update notification service (even when not running)
  - View system configurations
  - Quick update both system packages and flatpak using `solseek up`
  - Theme Support

## Language Support
  - English
  - French
  - German
  - Polish
  - Portuguese
  - Slovenian
  - Spanish
  - Ukrainian

<hr>

## Known Limitations / Issues
  - Limited Language support
  - Limited Snap support. Only updates, no list or searching. Full Snap support is not planned at this time.

<hr>

## Planned
| Feature | Info | Delivery |
| ----------- | ----------- | ----------- |
| **Additional Languages** | Looking for translators | 🔃 |
| **Recipes** | Common configs & tools | 1.? |
| **moss support** | AerynOS & future Solus | 2.x |

<hr>

## Contributing
The biggest need right now is the language files. If you are not as familiar with git commands on your computer, I have created a guide so you can use the Github website to make changes easily.
- Adding language file guide coming, but if you are familiar with Github, copy the en directory and contents and translate.

<hr>

## Credits
Solus and eopkg! Solseek uses eopkg natively to handle the packaging information and interaction. 
There was no need to write some system to extract the data as the Solus team has done a wonderful job already with eopkg and it allows me to simply wrap this tool around the strengths of it.

<hr>

## Inspirations from other distro tools
  - [pacseek](https://github.com/moson-mo/pacseek) - Overall concept
  - [topgrade](https://github.com/topgrade-rs/topgrade) - Update flow
