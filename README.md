<img src="https://raw.githubusercontent.com/clintre/solseek/main/demo/solseek-logo.png" align="left" width="64"/>

# Solseek
## A TUI Package Manager for Solus

🌟[Features](#features) 📑[Requirements & Installation](https://github.com/clintre/solseek/wiki#getting-started) 📗[Wiki](https://github.com/clintre/solseek/wiki) 💪[Contributing](#contributing)

Solseek is a simple terminal user interface that allows you to browse, search, and manage packages and drivers for Solus and Flatpak. Packages can be installed, reinstalled, updated, verified, and removed through the interface. It is built around the native tools ( bash, eopkg, flatpak, etc.) to avoid complications.

📽️ [Click here](https://youtu.be/MT7w6rZLmt0) or image below to see a short demo video.

[![See it in Action](https://raw.githubusercontent.com/clintre/solseek/main/demo/demo_thumb.png)](https://youtu.be/MT7w6rZLmt0)

<hr id="features">

## Features
  - Complete app store similar to Discover or Gnome Software
  - Works as a desktop app or from terminal
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

## Language Support
  - English
  - French
  - German
  - Polish
  - Slovenian
  - Spanish
  - Brazil Portuguese

<hr>

## Known Limitations / Issues
  - Limited Language support
  - Limited Snap support. Only updates, no list or searching. Full Snap support is not planned at this time.

<hr>

## Planned
| Feature | Info | Delivery |
| ----------- | ----------- | ----------- |
| **Additional Languages** | Looking for translators | 🔃 |
| **Recipes** | Looking for translators | 1.? |
| **moss support** | AerynOS & future Solus | 1.? |
| **tmux support** | Enhance UX | 2.x |

<hr>

## Contributing
The biggest need right now is the language files. If you are not as familiar with git commands on your computer, I have created a guide so you can use the Github website to make changes easily.
- [Adding or Correction Language Files](https://github.com/clintre/solseek/discussions/13)
- Adding language file guide coming, but if you are familiar with Github, copy the en directory and contents and translate.

<hr>

## Credits
Solus and eopkg! Solseek uses eopkg natively to handle the packaging information and interaction. 
There was no need to write some system to extract the data as the Solus team has done a wonderful job already with eopkg and it allows me to simply wrap this tool around the strengths of it.

<hr>

## Inspirations from other distro tools
  - [pacseek](https://github.com/moson-mo/pacseek) - Overall concept
  - [dnfseek](https://github.com/OmarHesham2356/dnfseek) - Using fzf for handling the UI/UX
