from pathlib import Path

import mip.core.preparation as prep

modpack_data_folder = Path("/Users/calebhair/Downloads/modpack resources/modpack data")
nonexistent_path = Path("/Users/calebhair/nothing")


def tests():
    # Manual tests
    os = prep.determine_os()
    mc_folder = prep.determine_default_mc_folder(os)
    print(f"OS: {os}")
    print(f"Default MC folder: {mc_folder}")

    # check_folder_exists tests
    prep.check_folder_exists(mc_folder)
    try:
        # Test nonexistent path
        prep.check_folder_exists(nonexistent_path)
        raise Exception("Nonexistent path did not raise exception when checked.")
    except FileNotFoundError:
        pass

    # check_modpack_data_folder tests
    prep.check_modpack_data_folder(modpack_data_folder)
    try:
        # Test wrong folder
        prep.check_modpack_data_folder(modpack_data_folder / "config")
        raise Exception("Incorrect folder did not raise exception.")
    except FileNotFoundError:
        pass


if __name__ == "__main__":
    tests()
