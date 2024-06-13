import webbrowser
import tkinter as tk
from pathlib import Path
from tkinter import ttk
from tkinter import messagebox, filedialog

import mip.core.preparation as prep
import mip.core.constants as constants


modpack_url = "csladsmodpack.ddns.net"


# Mostly copied from https://stackoverflow.com/questions/14910858/how-to-specify-where-a-tkinter-window-opens
def centre_root(root: tk.Tk):
    ws = root.winfo_screenwidth()  # width of the screen
    hs = root.winfo_screenheight()  # height of the screen

    w = 800  # width for the Tk root
    h = 650  # height for the Tk root

    # calculate x and y coordinates for the Tk root window
    x = int((ws / 2) - (w / 2))
    y = int((hs / 2) - (h / 2))

    # set the dimensions of the screen
    # and where it is placed
    root.geometry(f"+{x}+{y}")


def make_prepare_gui() -> tk.Tk:
    """ Creates the GUI for guiding the user to preparing the modpack, and returns the root. """
    root = tk.Tk()
    root.wm_title("ModpackInstaller(Py) - preparation")
    centre_root(root)
    frm = ttk.Frame(root, padding=10)
    frm.grid()

    # Step 1
    tk.Label(frm, justify=tk.CENTER,
             text="1. Download the modpack from the link below (just click the 'Download' button).").grid(column=0,
                                                                                                          row=0)

    # Download link
    mp_link = tk.Label(frm, text=modpack_url, fg="lightblue", cursor="hand")
    mp_link.grid(column=0, row=1)
    mp_link.bind("<Button-1>", lambda e: webbrowser.open_new("http://" + modpack_url))

    # Step 2
    ttk.Label(frm, justify=tk.CENTER,
              text="2. Find where you downloaded the file, and unzip it. If you don't know, read the article below.").grid(
        column=0, row=3)

    # Unzip link
    unzip_link = tk.Label(frm, text="How to unzip files", fg="lightblue", cursor="hand")
    unzip_link.grid(column=0, row=4)
    unzip_link.bind("<Button-1>", lambda e: webbrowser.open_new("https://www.wikihow.com/Unzip-a-File"))

    # Step 3
    ttk.Label(frm, justify=tk.CENTER,
              text="3. This step and the next can be skipped if you've done this before.\n"
                   "From the unzipped contents, find 'forge-1.20.1-47.2.0-installer.jar', and\n"
                   "double click the file. (You may need to right click it and press open)").grid(column=0, row=5)

    # Step 4
    ttk.Label(frm, justify=tk.CENTER,
              text="4. In the Forge Installer that will open, you just need to press OK.\n"
                   "The 'Install client' option should be selected by default.\n"
                   "Forge might take a minute to install, press OK once it's done.").grid(column=0, row=6)

    # Next button
    next_btn = tk.Button(frm, text="Next")
    next_btn.grid(column=0, row=7)
    next_btn.bind("<Button-1>", lambda e: root.destroy())

    return root


def make_modpack_data_path_gui() -> tuple[tk.Tk, tk.StringVar]:
    """ Creates the GUI for guiding the user through the organisation process, returning the root and the path to the modpack data. """
    root = tk.Tk()
    root.wm_title("ModpackInstaller(Py) - organisation")
    centre_root(root)
    frm = ttk.Frame(root, padding=10)
    frm.grid()

    tk.Label(frm, justify=tk.CENTER,
             text="In the unzipped csladsmodpack folder, there should be a folder called 'modpack_data'.\n"
                  "Press the button below and select the folder.").grid(column=0, row=0)

    modpack_data_path = tk.StringVar()
    modpack_data_path.set(constants.UNSET)

    def get_modpack_data(e):
        selected_path = filedialog.askdirectory(mustexist=True)
        try:
            prep.check_modpack_data_folder(Path(selected_path))
            modpack_data_path.set(selected_path)
            root.destroy()
        except FileNotFoundError:
            messagebox.showwarning("Bad format", "The selected folder is in the wrong format. You probably picked the wrong folder.")

    # Select modpack data button
    mp_data_btn = tk.Button(frm, text="Select modpack data")
    mp_data_btn.grid(column=0, row=1)
    mp_data_btn.bind("<Button-1>", get_modpack_data)

    return root, modpack_data_path


def show_error(error: Exception):
    messagebox.showerror("Error occurred.", f"An error occurred. Details: \n\n\n {error}")
    exit(1)


def show_conclusion(mc_folder: str):
    messagebox.showinfo("Install complete", "Installation complete.\n"
                                            "Previously installed modpacks have been backed up.\n"
                                            "This may take up storage over time, so feel free to remove "
                                            f"any backups you do not want to keep. The backups folder "
                                            f"({constants.REQUIRED_ITEMS_BACKUP_DIR_NAME}) can be found at the minecraft "
                                            f"folder ({mc_folder}).")
