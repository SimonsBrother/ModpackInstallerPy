from pathlib import Path

from core import preparation as prep
from core import organisation as org
from core import constants
from guis import make_preparation_gui, make_modpack_data_path_gui, show_error, show_conclusion, get_custom_mc_folder

# Manual prep
make_preparation_gui().mainloop()

# Check for custom installation
user_has_custom_mc_folder, custom_mc_folder = get_custom_mc_folder()
if user_has_custom_mc_folder:
    # Use custom folder
    mc_folder = custom_mc_folder
else:
    # Determine default mc folder
    mc_folder = prep.determine_default_mc_folder(prep.determine_os())

# Get modpack data path
mp_data_path_gui, mp_data_path = make_modpack_data_path_gui()
mp_data_path_gui.mainloop()

mp_data_path = mp_data_path.get()
if mp_data_path != constants.UNSET:
    try:
        # Organise
        org.backup_existing_key_items(mc_folder)
        org.delete_existing_key_folders(mc_folder)
        org.copy_key_folders(Path(mp_data_path), mc_folder)

        show_conclusion(str(mc_folder))

    except Exception as e:
        show_error(e)
