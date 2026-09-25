# XkeyboardSwitchFix

Small X11 utility that fixes keyboard layout switching. It listens for hotkeys
globally and switches the active XKB layout through
[xkblayout-state](https://github.com/smduzan/xkblayout-state), whose source is
vendored in this repository.

Useful when your desktop environment's layout-switch shortcut is unreliable
(e.g. inside some Electron apps or on certain keyboard configurations).

## Hotkeys

| Keys                       | Action                     |
| -------------------------- | -------------------------- |
| `Ctrl + Shift` (left)      | previous layout (`set -1`) |
| `Ctrl + Shift` (right)     | next layout (`set +1`)     |

## Requirements

- Linux with X11 (`libX11` for `xkblayout-state`, `python-xlib`/`evdev` for input listening)
- [uv](https://docs.astral.sh/uv/) for Python environment management (Python >= 3.10)

## Quick start

```sh
uv sync        # create .venv and install dependencies
./src/run.sh   # start the hotkey listener
```

`run.sh` resolves the project root automatically, so it can be started from
any directory.

## Layout tool

`src/xkblayout-state` is a prebuilt binary. To build it from the vendored
source (requires a C++ compiler and X11 development headers):

```sh
cd xkblayout-state
make
cp xkblayout-state ../src/
```

Check the available layouts and switch manually with the tool directly:

```sh
./src/xkblayout-state print "%n"   # print layout names
./src/xkblayout-state set +1        # switch to the next layout
```

## How it works

`src/main.py` runs a `pynput` keyboard listener. `src/hk.py` provides the
`HK` hotkey class: a callback fires once every key of the combination has
been pressed and the last one is released. Raw modifier codes reported by the
backend are normalized via the keymap in `main.py`.

## Autostart

Add a desktop entry or session autostart entry pointing to the absolute path
of `src/run.sh`.

## Project layout

```
pyproject.toml      # uv-managed project (deps + dev group)
uv.lock             # locked dependency versions
src/
  main.py           # listener entry point
  hk.py             # hotkey logic
  run.sh            # start via uv
  xkblayout-state   # prebuilt layout tool binary
xkblayout-state/    # C++ source of the layout tool (make)
```
