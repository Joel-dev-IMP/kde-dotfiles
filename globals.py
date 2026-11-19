from pathlib import Path

SOURCE_PATH = Path(__file__).parent
TARGET_PATH = Path("~/.config").expanduser()

TEXT_FILES: list[Path] = [
    SOURCE_PATH / "kdedefaults" / "scripts" / "focus_screen_0.sh",
    SOURCE_PATH / "kdedefaults" / "scripts" / "focus_screen_1.sh",
    SOURCE_PATH / "kdeglobals",
    SOURCE_PATH / "kglobalshortcutsrc",
    SOURCE_PATH / "klaunchrc",
    SOURCE_PATH / "krunnerrc",
    SOURCE_PATH / "ksplashrc",
    SOURCE_PATH / "kwinrc",
    SOURCE_PATH / "plasma_workspace.notifyrc",
    SOURCE_PATH / "plasma-org.kde.plasma.desktop-appletsrc",
    SOURCE_PATH / "plasmanotifyrc",
    SOURCE_PATH / "plasmarc",
    SOURCE_PATH / "plasmashellrc",
]

BINARY_FILES: list[Path] = [
    SOURCE_PATH / "wallpapers" / "abstract_turquoise_wallpaper.png",
    SOURCE_PATH / "wallpapers" / "space_blue_wallpaper.png",
    SOURCE_PATH / "wallpapers" / "space_green_wallpaper.png",
]

KITTY_FILES: list[Path] = [
    SOURCE_PATH / "kitty" / "kitty.conf"
]
