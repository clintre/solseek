# Makefile for installing solseek

# --- Configuration ---

# Source directories
SRC_BIN=bin
SRC_SHARE=share

# Script and data folder names
SCRIPT=solseek
DATA_FOLDER=solseek

# Installation directories
PREFIX=/usr
BINDIR=$(PREFIX)/bin
DATADIR=$(PREFIX)/share
APPDIR=$(DATADIR)/applications
ICONDIR=$(DATADIR)/icons/hicolor/scalable/apps

# Phony targets are not files
.PHONY: install uninstall

# --- Targets ---

install:
	@echo "Installing solseek from $(SRC_BIN) to $(BINDIR)..."
	@install -d -m 755 $(DESTDIR)$(BINDIR)
	@install -m 755 $(SRC_BIN)/$(SCRIPT) $(DESTDIR)$(BINDIR)/$(SCRIPT)

	@echo "Installing solseek data files from $(SRC_SHARE) to $(DATADIR)..."
	@install -d -m 755 $(DESTDIR)$(DATADIR)
	@cp -r $(SRC_SHARE)/$(DATA_FOLDER) $(DESTDIR)$(DATADIR)/

	@echo "Installing desktop file to $(APPDIR)..."
	@install -d -m 755 $(DESTDIR)$(APPDIR)
	@install -m 644 $(SRC_SHARE)/applications/Solseek.desktop $(DESTDIR)$(APPDIR)/

	@echo "Installing icon file to $(ICONDIR)..."
	@install -d -m 755 $(DESTDIR)$(ICONDIR)
	@install -m 644 $(SRC_SHARE)/icons/hicolor/scalable/apps/solseek.svg $(DESTDIR)$(ICONDIR)/

	@echo "✅ solseek installation complete."

uninstall:
	@echo "Removing solseek from $(BINDIR)..."
	@rm -f $(DESTDIR)$(BINDIR)/$(SCRIPT)

	@echo "Removing solseek data files from $(DATADIR)..."
	@rm -rf $(DESTDIR)$(DATADIR)/$(DATA_FOLDER)

	@echo "Removing desktop file from $(APPDIR)..."
	@rm -f $(DESTDIR)$(APPDIR)/Solseek.desktop

	@echo "Removing icon file from $(ICONDIR)..."
	@rm -f $(DESTDIR)$(ICONDIR)/solseek.svg

	@echo "🗑️ solseek uninstallation complete."
