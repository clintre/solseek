#!/usr/bin/env python3
import gi
import sys
import socket
import subprocess
import os
import time

gi.require_version('Gtk', '3.0')
gi.require_version('AyatanaAppIndicator3', '0.1')

from gi.repository import Gtk, Gio
from gi.repository import AyatanaAppIndicator3 as appindicator

# Global variable to hold the socket so it isn't garbage collected
_lock_socket = None

def enforce_single_instance():
    """Ensures only one instance of the tray icon is running."""
    global _lock_socket
    _lock_socket = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
    try:
        _lock_socket.bind('\0solseek_update_notifier_lock')
    except socket.error:
        sys.exit(0)

def open_solseek(menu_item):
    env = os.environ.copy()
    if "DISPLAY" not in env:
        env["DISPLAY"] = ":0"

    try:
        subprocess.Popen(
            ["systemd-run", "--user", "--scope", "xdg-terminal-exec", "solseek"],
            env=env,
            start_new_session=True
        )
    except Exception as e:
        print(f"Failed to launch terminal: {e}")

    # Give systemd-run half a second to register the new scope before quitting
    time.sleep(0.5)

    # Safely close the tray icon
    Gtk.main_quit()

def main():
    # 1. Check for existing instances before building the UI!
    enforce_single_instance()

    # Initialize the Indicator using the native system theme
    indicator = appindicator.Indicator.new(
        "solseek-update-notifier",
        "software-update-available-symbolic",
        appindicator.IndicatorCategory.APPLICATION_STATUS
    )
    indicator.set_label("Updates Available", "")
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)

    # Build the dropdown menu
    menu = Gtk.Menu()
    
    # Label item
    item_update = Gtk.MenuItem(label="Updates Available")
    item_update.connect("activate", open_solseek)
    menu.append(item_update)
        
    # Action item
    item_update2 = Gtk.MenuItem(label="Open Solseek")
    item_update2.connect("activate", open_solseek)
    menu.append(item_update2)
    
    # Dismiss item
    item_dismiss = Gtk.MenuItem(label="Dismiss")
    item_dismiss.connect("activate", lambda _: Gtk.main_quit())
    menu.append(item_dismiss)
    
    menu.show_all()
    indicator.set_menu(menu)

    # Start the blocking Gtk loop to keep the icon alive in the tray
    Gtk.main()

if __name__ == "__main__":
    main()
