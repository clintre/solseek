<img src="/demo/solseek-logo.png" align="left" width="64"/>

# Solseek
## A TUI Package Manager for Solus

🌟[Features](#features) 📑[Requirements & Installation](#requirements) 📗[Usage](https://github.com/clintre/solseek/wiki) 💪[Contributing](#contributing)

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

## Known Limitations / Issues
  - Currently only in English and French
  - Some minor navigation issues around using fzf for the UX. [example](https://github.com/clintre/solseek/issues/15) (not fzf fault, this is outside of its original design)

## Planned
  - Additional languages (looking for help on this)
  - Recipes for common installs on Solus (Nvidia, Distrobox, etc)

## Requirements & Installation
Moved to [Wiki](https://github.com/clintre/solseek/wiki#getting-started)

## Usage
Moved to [Wiki](https://github.com/clintre/solseek/wiki)

## Contributing
The biggest need right now is the language files. If you are not as familiar with git commands on your computer, I have created a guide so you can use the Github website to make changes easily.
- [Correcting Language Files](https://github.com/clintre/solseek/discussions/13)
- Adding language file guide coming, but if you are familiar with Github, copy the en directory and contents and translate.

## Credits
Solus and eopkg! Solseek uses eopkg natively to handle the packaging information and interaction. 
There was no need to write some system to extract the data as the Solus team has done a wonderful job already with eopkg and it allows me to simply wrap this tool around the strengths of it.
    
## Inspirations from other distro tools
  - [pacseek](https://github.com/moson-mo/pacseek) - Overall concept
  - [dnfseek](https://github.com/OmarHesham2356/dnfseek) - Using fzf for handling the UI/UX
