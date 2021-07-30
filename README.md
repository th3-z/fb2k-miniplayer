# Foobar Miniplayer

[![Downloads](https://img.shields.io/github/downloads/th3-z/fb2k-mini-player/total.svg)](https://img.shields.io/github/downloads/th3-z/fb2k-mini-player/total.svg)
[![GitHub license](https://img.shields.io/github/license/th3-z/fb2k-mini-player)](https://github.com/th3-z/fb2k-mini-player/blob/master/LICENSE)

A tiny Foobar 2000 controller for Windows that can sit above other applications
in borderless-fullscreen mode.

## Features

* Distraction-free operation, a mere 187x40 pixels with optional transparency
* Maintains top-most focus, visible when using other applications including borderless-fullscreen games
* Album artwork display
* Common Foobar 2000 controls
* Customisable colours

## Downloads

The most recent release is `0.1.0`. A binary is provided on the releases page.

[Release 0.1.0](https://github.com/th3-z/fb2k-mini-player/releases/tag/0.1.0)

## User guide

### Installation

1. **Close Foobar 2000 before installing the COM automation plugin**.
2. Install the Foobar 2000
   [COM automation plugin](https://hydrogenaud.io/index.php/topic,39946.0.html).
2. Launch Foobar 2000.
3. Extract the latest release zip.
4. Run the executable `FoobarMiniplayer.exe`.

### Usage

Please refer to this diagram and the bullet points.

![Diagram of player](https://github.com/th3-z/fb2k-miniplayer/raw/master/.github/diagram.png)

0. Current album artwork. Left-click to **focus Foobar 2000**, right-click to **close Foobar Miniplayer**.
1. Shuffle button. Left-click to select a **random track**, this does not affect your playlist order.
2. Previous track button. Left-click to play the **previous track** in the playlist.
3. Play/Pause button. Left-click to **toggle playing/paused** state.
4. Next track button. Left-click to skip to the **next track** in the playlist.
5. Volume slider. Scroll or drag the bar to adjust the **volume**.
6. Current artist/song marquee.

* Holding middle mouse and dragging **moves the player**, the chosen position will be recalled at startup.
* Ctrl + C copies the current track information to your clipboard.

### Settings

Foobar 2000 Mini-Player can be configured by editting the file `config.conf`.
Restart the program to apply your changes. The configuration options are of the
form `option=value`. The following options are available.

#### `col_bg`

The player's background colour. Must be hex notation with a leading `#`. A [colour picker](https://duckduckgo.com/?q=colour+picker) can help you find the hex notation for your desired colour. e.g. `col_bg=#1b1b1b`

#### `col_fg`

The colour used for the player's buttons and text. Must be hex notation with a leading `#`. e.g. `col_fg=#ef810b`

#### `alpha` 

The player's transparency level, where `1.0` is opaque and `0.0` is completely transparent e.g. `alpha=0.8`

#### `prefer_external`

Setting this value to `1` will prefer external over internal album artwork when both exist. e.g. `prefer_external=1`

#### `position`

The on-screen location of the player upon launch. e.g. `position=400,600`.

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
