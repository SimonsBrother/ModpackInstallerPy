from pathlib import Path

import mip.core.preparation as prep
import mip.core.organisation as org

mc_folder = prep.determine_default_mc_folder(prep.determine_os())
modpack_data_folder = Path("/Users/calebhair/Downloads/modpack resources/modpack data")


def manual_tests():
    """ These tests perform some part of the organisation process, and wait for enter to be pressed in the terminal. """
    input("Press enter to backup existing key items.")
    org.backup_existing_key_items(mc_folder)

    input("Press enter to delete existing key items.")
    org.delete_existing_key_folders(mc_folder)

    input("Press enter to copy modpack data to mc folder.")
    org.copy_key_folders(modpack_data_folder, mc_folder)


if __name__ == "__main__":
    manual_tests()
