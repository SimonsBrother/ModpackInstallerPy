# TODO Test everything on windows
from pathlib import Path

import mip.core.preparation as prep
import mip.core.organisation as org
import mip.core.constants as constants
from guis import make_prepare_gui, make_modpack_data_path_gui, show_error, show_conclusion

# Manual prep
make_prepare_gui().mainloop()

# Get modpack data path
mp_data_path_gui, mp_data_path = make_modpack_data_path_gui()
mp_data_path_gui.mainloop()
mp_data_path = mp_data_path.get()
if mp_data_path == constants.UNSET:
    exit()

try:
    # Determine mc folder, currently uses default
    default_mc_folder = prep.determine_default_mc_folder(prep.determine_os())

    # Organise
    org.backup_existing_key_items(default_mc_folder)
    org.delete_existing_key_folders(default_mc_folder)
    org.copy_key_folders(Path(mp_data_path), default_mc_folder)

    show_conclusion(str(default_mc_folder))

except Exception as e:
    show_error(e)

