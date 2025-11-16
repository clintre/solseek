<img src="/demo/solseek-logo.png" align="left" width="64"/>

# Solseek
## A TUI Package Manager for Solus

🌟[Features](#features) 📑[Requirements & Installation](#requirements) 📗[Usage](#usage)

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
  - Common package repair tools
  - Recipes for common installs on Solus (Nvidia, Distrobox, etc)

## Requirements
  - [Solus](https://getsol.us/)
  - [eopkg](https://github.com/getsolus/eopkg)
  - [fzf](https://github.com/junegunn/fzf)
  - [appstream](https://www.freedesktop.org/wiki/Distributions/AppStream/)

## Installation
```bash
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
### Config (version 0.3.3+)
If you need or will like to change settings.
```bash
mkdir -p ~/.config/solseek
cp /usr/share/solseek/config ~/.config/solseek/
nano ~/.config/solseek/config
```
Available Settings 
- Language [experimental] Currently only French "fr" and English "en" (default).
  - SS_LANG="en"
- Fastfetch (if installed) Options 0 = disabled, 1 = icons keys (default), 2 = text keys
  - SS_FASTFETCH=1
  - If you are not using a nerd font or having font rendering issues, setting this to 2 will work around the issue.
### Automated Update Checks
This is a temporary method to check for system and flatpak updates automatically.
This makes use of a login script.
Create the script...
```bash
mkdir -p ~/.scripts
nano ~/.scripts/solseek-uc.sh
```
Add the following...
```bash
#!/bin/sh

## Short delay after login
sleep 60

## Keep alive loop
while true
do

## Call solseek built-in update check for eopkg and flatpak
## This handles notifications as well
solseek -cu

## Check for updates every x seconds. Change to desired frequency
sleep 3600
done

exit 0
```
Make the script executable
```bash
chmod +x ~/.scripts/solseek-uc.sh
```
Add script to your autostart for your desktop.

## Credits
Solus and eopkg! Solseek uses eopkg natively to handle the packaging information and interaction. 
There was no need to write some system to extract the data as the Solus team has done a wonderful job already with eopkg and it allows me to simply wrap this tool around the strengths of it.
    
## Inspirations from other distro tools
  - [pacseek](https://github.com/moson-mo/pacseek) - Overall concept
  - [dnfseek](https://github.com/OmarHesham2356/dnfseek) - Using fzf for handling the UI/UX
