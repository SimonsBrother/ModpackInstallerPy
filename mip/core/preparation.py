""" Everything to do with getting information needed for organisation, and checking the validity of inputs. """

from pathlib import Path
import getpass  # For getting the current username, used for inferring the default location of the Minecraft folder.
import sys  # For getting platform, which is for getting the default Minecraft folder.

from . import constants


def determine_os() -> constants.OperatingSystem:
    """ Determines if the operating system is macOS or Windows, returning an OperatingSystem value. Raises Exception if on any other platform. """
    os = sys.platform
    match os:
        case "darwin":
            return constants.OperatingSystem.MAC
        case "win32":
            return constants.OperatingSystem.WINDOWS
        case _:
            raise Exception("Unsupported operating system. Must be using Windows or macOS.")


def determine_default_mc_folder(os: constants.OperatingSystem):
    """ Determines the path of the default Minecraft folder based on the OS. If an invalid OS value is passed, an Exception is thrown. If the Minecraft path does not exist, a FileNotFoundError is thrown. """
    match os:
        case constants.OperatingSystem.MAC:
            # The default location depends on the username.
            default_mc_path = Path(f"/Users/{getpass.getuser()}/Library/Application Support/minecraft")
        case constants.OperatingSystem.WINDOWS:
            default_mc_path = Path(f"/Users/{getpass.getuser()}/AppData/Roaming/.minecraft")
        case _:
            raise Exception(f"Unsupported OS somehow passed into function determining default folder: {os}")

    check_folder_exists(default_mc_path)

    return default_mc_path


def check_folder_exists(path: Path):
    """ Raises FileNotFoundError is the path given does not exist. """
    if not path.exists():
        raise FileNotFoundError(f"The Minecraft directory does not exist at that location: {path}")


def check_modpack_data_folder(modpack_data_path: Path):
    """ Ensures that each item in required_modpack_items is present in the path provided. """
    contents = [item.name for item in modpack_data_path.iterdir()]
    for required_item in constants.REQUIRED_MODPACK_ITEMS:
        if required_item not in contents:
            raise FileNotFoundError(f"Missing required item: {required_item}. Check you're using the right directory.")
