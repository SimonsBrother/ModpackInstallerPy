""" Everything to do with putting modpack resources in the right location. """
import shutil
from pathlib import Path
from datetime import datetime

import mip.core.constants as constants


def backup_existing_key_items(mc_folder: Path):
    """ Generates a backup of the key items that exist in the mc folder. """
    # First, create the path to the backups directory
    backup_dir_path = mc_folder / constants.REQUIRED_ITEMS_BACKUP_DIR_NAME
    # Make the name of the backup, based on the current time TODO make it a version number or something
    specific_backup_dir_name = str(datetime.now()).replace('-', '_').replace(':', '_').replace('.', '_')
    # Create the path to the specific backup directory
    specific_backup_dir_path = backup_dir_path / specific_backup_dir_name

    # Create the specific backup directory
    specific_backup_dir_path.mkdir(parents=True)

    # Copy the required items to the backup directory
    for item in constants.REQUIRED_MODPACK_ITEMS:
        item_path = mc_folder / item
        # Check that the item exists before trying to back it up
        if item_path.exists():
            if item_path.is_dir():
                # Create directory for storing the contents of the key directory
                item_backup_path = specific_backup_dir_path / item
                item_backup_path.mkdir()
                shutil.copytree(item_path, item_backup_path, dirs_exist_ok=True)
            else:
                # Copy the file
                shutil.copy(item_path, specific_backup_dir_path)


def delete_existing_key_folders(mc_folder: Path):
    """ Removes the key items that exist in the mc folder. """
    # Delete the required items from the mc folder
    for item in constants.REQUIRED_MODPACK_ITEMS:
        item_path = mc_folder / item
        # Check that the item exists before trying to delete it
        if item_path.exists():
            # Use shutil.rmtree for directories, otherwise for files use Path().unlink
            if item_path.is_dir():
                shutil.rmtree(item_path)
            else:
                item_path.unlink()


def copy_key_folders(modpack_data_path: Path, mc_folder: Path):
    shutil.copytree(modpack_data_path, mc_folder, dirs_exist_ok=True)
