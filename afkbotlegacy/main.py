# Version 1.0.0
# Modules
import os
import re
import requests
import secrets
import sys
import webbrowser
import customtkinter as ctk
from PIL import Image
from assets.config import press_keys

# Set theme
ctk.set_default_color_theme("blue")
ctk.set_appearance_mode("dark")

latest_version = None


# Check latest version using re search and request
def get_latest_version():
    global latest_version
    if latest_version is None:
        response = requests.get('https://github.com/gorouflex/afkbotlegacy/releases/latest')
        latest_version = re.search(r'releases/tag/(\d+\.\d+(\.\d+)?)', response.text).group(1)
    return latest_version


def open_releases():
    webbrowser.open("https://github.com/gorouflex/afkbotlegacy/releases/tag/1.0.0")


# This resource_path works only when compile from python to exe
def resource_path(relative_path):
    base_path = getattr(sys, '_MEI PASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


def open_github():
    webbrowser.open("https://www.github.com/gorouflex/afkbotlegacy")


def open_afk_github():
    webbrowser.open("https://www.github.com/gorouflex/afkbot")


# Info Window
class InfoWindow(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.open_github = None
        ctk.set_default_color_theme("green")
        self.geometry("250x290")
        self.label = ctk.CTkLabel(self, text="About AFKBot Legacy",
                                  font=ctk.CTkFont(size=19, weight="bold"))
        self.label.grid(padx=10, pady=5, sticky="nsew")
        self.resizable(False, False)
        icon_path = os.path.join(os.getcwd(), "assets", "app.ico")
        self.after(250, lambda: self.iconbitmap(icon_path))
        self.title('About')
        self.owner = ctk.CTkLabel(self, text="Main developer: GorouFlex", font=("", 15))
        self.owner.grid(padx=5, pady=2, sticky="nsew")
        self.contrib = ctk.CTkLabel(self, text="Sub-developer: NotchApple1703", font=("", 15))
        self.contrib.grid(padx=5, pady=2, sticky="nsew")
        self.afk_github_button = ctk.CTkButton(self, width=120, height=40, text="Similar repo",
                                               font=("", 16),
                                               corner_radius=5,
                                               command=open_afk_github)
        self.afk_github_button.grid(row=3, column=0, padx=60, pady=5, sticky="nsew")
        self.github_button = ctk.CTkButton(self, width=120, height=40, text="GitHub",
                                           font=("", 16),
                                           corner_radius=5,
                                           command=open_github)
        self.github_button.grid(row=4, column=0, padx=60, pady=5, sticky="nsew")
        self.releases_button = ctk.CTkButton(self, width=120, height=40, text="Changes logs",
                                             font=("", 16),
                                             corner_radius=5,
                                             command=open_releases)
        self.releases_button.grid(row=5, column=0, padx=60, pady=5, sticky="nsew")
        self.version_label = ctk.CTkLabel(self, width=200,
                                          text=f"Latest version on GitHub: {get_latest_version()}",
                                          font=ctk.CTkFont(size=14))
        self.version_label.grid(row=6, column=0, padx=5, pady=5, sticky="nsew")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)


# Main func
class Main(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("450x300")
        self.resizable(False, False)
        self.update_title()
        self.toplevel_window = None
        self.openinfowindow = None
        self.is_running = None
        self.window = self
        self.columnconfigure(0, weight=1)
        icon_path = os.path.join(os.getcwd(), "assets", "app.ico")
        self.iconbitmap(icon_path)
        self.bg_img = ctk.CTkImage(Image.open("assets/bg.png"), size=(500, 300))
        self.bg_label = ctk.CTkLabel(self, text="", image=self.bg_img)
        self.bg_label.grid(row=0, column=0, rowspan=4, sticky="nsew")

        self.start_button = ctk.CTkButton(self, width=150, height=50, text="Start", font=("", 19),
                                          corner_radius=6,
                                          background_corner_colors=("#9b9fff", "#5a77ff", "#94a2ff", "#c88bca"),
                                          command=self.start)
        self.start_button.grid(row=0, column=0)

        self.stop_button = ctk.CTkButton(self, width=150, height=50, text="Stop", font=("", 19),
                                         corner_radius=6,
                                         background_corner_colors=("#ff5a58", "#9375ef", "#d86151", "#005c23"),
                                         command=self.stop)
        self.stop_button.grid(row=1, column=0)

        self.github_button = ctk.CTkButton(self, width=150, height=50, text="About", font=("", 19),
                                           corner_radius=6,
                                           background_corner_colors=("#669927", "#015f24", "#89bc29", "#8ab628"),
                                           command=self.infowindow)
        self.github_button.grid(row=2, column=0)

        self.credit_label = ctk.CTkLabel(self, width=500, text="Version: 1.0.0", font=("", 16))
        self.credit_label.grid(row=3, column=0, sticky="s")

    def update_title(self):
        self.title(secrets.token_hex(14))
        self.after(1000, self.update_title)

    def start(self):
        self.is_running = True
        press_keys(self)

    def stop(self):
        self.is_running = False

    def infowindow(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = InfoWindow()
            self.toplevel_window.focus()
        else:
            self.toplevel_window.focus()


if __name__ == '__main__':
    app = Main()
    app.mainloop()
