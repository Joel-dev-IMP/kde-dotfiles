# KDE Dotfiles

This repository contains important Dotfiles that I'm using for my current KDE setup.
I wanted to make the configuration as similar as possible to my previous i3/Sway/Hyprland-Setups, but I decided not to use Krohnkite, because it felt relatively glitchy.
Instead, I focused on getting the look and feel similar to my prior setups and compensate for the lack of a tiling window manager by configuring intuitive shortcuts for arranging windows quickly.

**Contents:**

- Keyboard Shortcuts: `kglobalshortcutsrc`
- KDE Theme/Settings: `kdeglobals`, `klaunchrc`, `ksplashrc`, `kwinrc`, `plasma_workspace.notifyrc`, `plasma-org.kde.plasma.desktop-appletsrc`, `plasmanotifyrc`, `plasmarc`, `plasmashellrc`
- KRunner Settings: `krunnerrc`
- Kitty Configuration: `kitty/`

**Installation:**
Download/clone the repository and run `./install.py` to copy all files into `~/.config/`.
Log out and log back in to load the configuration changes.
Certain settings might not take effect, even though they are configured in the Dotfiles, so you might have to do the following steps after installation:

- Change the Desktop wallpaper
- Change the filter for files shown on the desktop
- Add the scripts from `~/.config/kdedefaults/scripts/` as shortcuts in `Settings > Keyboard > Shortcuts > Add New > Command or Script`

If you want to use Kitty as your terminal, refer to the [kitty documentation](https://sw.kovidgoyal.net/kitty/binary/) for installation instructions.
Fedora users can install kitty with `sudo dnf install kitty`.

## Keyboard Shortcuts

**Window & Desktop Management**

Exactly like in my previous configs, `Meta + 1` through `Meta + 0` allow **switching between desktops** 1 to 10.\
**Moving the active window to a specific desktop** can be done using `Meta + Shift + 1` through `Meta + Shift + 0`.

Unlike i3, KDE does not bind Desktops to screens.
Therefore, switching desktops is not sufficient to switch between screens, and additional shortcuts for switching between screens have been added:\
`Meta + F1` and `Meta + F2` allow **switching to screen** 1/2 (and moving the mouse there).
Note that moving the mouse to the target screen is done with a workaround that requires a window to be on the target screen!\
**Moving the active window to a screen** can be done with `Meta + Shift + F1` and `Meta + Shift + F2`.

`Meta + F` maximizes windows (keeping the top bar), `Meta + F11` toggles windows full-screen (hiding the top bar).\
`Meta + Q` closes windows (instead of `Alt + F4`).

Window tiling needs to be done manually, but it uses similar shortcuts to i3:\
`Meta + Shift + H/J/K/L` move windows to the left/bottom/top/right and switching focus between windows can be done using `Meta + L/H`.\
Unfortunately, KDE does not have a concept of "Moving the focus to the left window", because it is not a tiling window manager.
Instead, these shortcuts behave like `Alt + Tab`/`Alt + Shift + Tab` (which is a common shortcut in different operating systems that cycles through all windows (on the current desktop) ordered by "most recently focused").

Since `Meta + L` is no longer available as shortcut for locking the screen, `Meta + E` now locks the screen and `Meta + Shift + E` logs out the current user.

**Application Launches**

- `Meta + Return` launches a terminal (Kitty)
- `Meta + D` opens the application launcher (KRunner).
- `Meta + S` opens the system settings

## KDE Theme/Settings

I've disabled the bounce animation at the cursor when applications open, disabled the splash screen when logging in, added custom wallpapers and added 10 desktops.
KRunner has been configured to open in the center of the screen, similar to dmenu/rofi/wofi.
A lot of notifications have been disabled, for example when plugging in a new USB stick.
Similar to the previous configs, there is a top bar with the desktops on the left, a calendar widget in the center and system control widgets on the right.
Apart from that, the theme and settings are pretty much unmodified.

## Kitty Configuration

The configuration for kitty uses the [JetBrainsMono Nerd Font](https://github.com/ryanoasis/nerd-fonts/releases/download/v3.5.1/JetBrainsMono.zip), which you need to install separately (into `~/.fonts/`).
