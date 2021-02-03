# Foobar 2000 Mini-Player

[![Downloads](https://img.shields.io/github/downloads/th3-z/fb2k-mini-player/total.svg)](https://img.shields.io/github/downloads/th3-z/fb2k-mini-player/total.svg)
[![GitHub license](https://img.shields.io/github/license/th3-z/fb2k-mini-player)](https://github.com/th3-z/fb2k-mini-player/blob/master/LICENSE)

A tiny Foobar 2000 controller for Windows that can sit above other applications
in borderless-fullscreen mode.

## User guide

### Installation

1. **Close Foobar 2000 before installing the COM automation plugin**
2. Install the Foobar 2000
   [COM automation plugin](https://hydrogenaud.io/index.php/topic,39946.0.html)
3. Extract the latest release zip
4. Run the executable `FoobarMiniplayer.exe`

### Usage

* Left-click album art - focus Foobar 2000
* Right-click album art - close fb2k-mini-player
* Middle-click-hold - move fb2k-mini-player
* Ctrl + C - copy track information to clipboard
* Settings can be configured in `config.conf`

### Settings

Foobar 2000 Mini-Player can be configured by editting the file `config.conf`.
Restart the program to apply your changes. The configuration options are of the
form `option = value`. The following options are available.

#### `position`

#### `col_bg`

#### `col_fg`

#### `alpha`

#### `album_art`

## Development

### Requirements

The following need to be installed before running the program from source.

* [Python3](https://www.python.org/downloads/)
* [Git](https://git-scm.com/downloads)
* [Foobar 2000](https://www.foobar2000.org/download)
* Foobar 2000 [COM automation plugin](https://hydrogenaud.io/index.php/topic,39946.0.html)
  (*close Foobar 2000 before running the installer*)

### Running

`command` denotes commands to be ran in git-bash.

1. Launch git-bash
2. Get the source code  -
   `git clone https://github.com/th3-z/fb2k-mini-player.git`
3. `cd fb2k-mini-player`
4. Install the Python requirements `pip install -r requirements.tx`
5. Launch Foobar 2000
6. Run `python FoobarMiniplayer.py`

### Building

After a successfully running the program it can be build with the command
`python setup.py build`.
