<img src="https://raw.githubusercontent.com/clintre/solseek/main/demo/solseek-logo.png" align="left" width="64"/>

# Solseek
## A TUI Package Manager for Solus

🌟[Features](#features) 📑[Requirements & Installation](https://github.com/clintre/solseek/wiki#getting-started) 📗[Wiki](https://github.com/clintre/solseek/wiki) 💪[Contributing](#contributing)

Solseek is a simple terminal user interface that allows you to browse, search, and manage packages for Solus and Flatpak. Packages can be installed, reinstalled, updated, verified, and removed through the interface. It is built around the native tools ( bash, eopkg, flatpak, etc.) to avoid complications.

⚠️ **Please note that until version 1.x this will be fast changing**

📽️ [Click here](https://youtu.be/MT7w6rZLmt0) or image below to see a short demo video.

[![See it in Action](https://raw.githubusercontent.com/clintre/solseek/main/demo/demo_thumb.png)](https://youtu.be/MT7w6rZLmt0)

## Features
  - Complete app store similar to Discover or Gnome Software
  - Select and install multiple packages at once
  - Manage system updates for installed tools such as; eopkg, flatpak, snap, distrobox, and fwupd
  - Verify all packages
  - View and export installed packages for eopkg and flatpak (all and/or user installed)
  - Recall (rollback) system package actions
  - Update notification service (even when not running)
  - View system configurations

## Known Limitations / Issues
  - Currently only in English, French, and Polish
  - Limited Snap support. Only updates, no list or searching. Full Snap support is not planned at this time.

## Planned
  - Additional languages (looking for help on this)
  - Recipes for common installs on Solus (Nvidia, Distrobox, etc)
  - moss support (AerynOS & future Solus)

## Contributing
The biggest need right now is the language files. If you are not as familiar with git commands on your computer, I have created a guide so you can use the Github website to make changes easily.
- [Adding or Correction Language Files](https://github.com/clintre/solseek/discussions/13)
- Adding language file guide coming, but if you are familiar with Github, copy the en directory and contents and translate.

## For Fun
Yeah never going to have a huge star history, this is just for fun.
[![Star History Chart](https://app.repohistory.com/api/svg?repo=clintre/solseek&type=Date&background=0D1117&color=62C3F8)](https://app.repohistory.com/star-history)

## Credits
Solus and eopkg! Solseek uses eopkg natively to handle the packaging information and interaction. 
There was no need to write some system to extract the data as the Solus team has done a wonderful job already with eopkg and it allows me to simply wrap this tool around the strengths of it.
    
## Inspirations from other distro tools
  - [pacseek](https://github.com/moson-mo/pacseek) - Overall concept
  - [dnfseek](https://github.com/OmarHesham2356/dnfseek) - Using fzf for handling the UI/UX
