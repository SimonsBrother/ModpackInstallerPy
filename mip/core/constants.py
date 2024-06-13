from enum import Enum

# Names of folders and files necessary for the modpack to work.
REQUIRED_MODPACK_ITEMS = ["mods", "config", "shaderpacks", "scripts", "options.txt"]

# Name of the backups directory for existing key items in the mc folder.
REQUIRED_ITEMS_BACKUP_DIR_NAME = "mip_key_items_backup"


class OperatingSystem(Enum):
    MAC = "macOS"
    WINDOWS = "Windows"
