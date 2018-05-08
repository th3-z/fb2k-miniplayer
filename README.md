# fb2k-mini-player
A tiny Foobar 2000 controller for Windows that can sit above other applications in borderless-fullscreen mode.

### Installation
* Install Foobar 2000 COM automation plugin: https://hydrogenaud.io/index.php/topic,39946.0.html
  - **Close Foobar 2000 before installation**
* Run the release executable
* Colours, and transparency can be configured in `config.ini`

### Usage
* Left-click album art - focus Foobar 2000
* Right-click album art - close fb2k-mini-player
* Middle-click-hold - move fb2k-mini-player
* Ctrl + C - copy track information to clipboard

### Build requirements
* pywin32
* pillow
* mutagen
* cx_freeze
* python 3.x

### Building
Run `build.bat`
