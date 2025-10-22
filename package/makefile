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

	@echo "✅ solseek installation complete."

uninstall:
	@echo "Removing solseek from $(BINDIR)..."
	@rm -f $(DESTDIR)$(BINDIR)/$(SCRIPT)

	@echo "Removing solseek data files from $(DATADIR)..."
	@rm -rf $(DESTDIR)$(DATADIR)/$(DATA_FOLDER)

	@echo "🗑️ solseek uninstallation complete."
