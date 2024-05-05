# Camille's Harmony Toolkit, AKA umbratools
## A set of tools to make life easier.

### What is it ?
This is a toolkit I developped in python to quicken my workflow in Linux, and I decided to make it possible to expand upon it by implementing a plugin system. 
The toolkit is still in it's infancy, so some features may not work as well as they should, and I'm open to any feedback. Some features could/will be removed or changed, as I have picked this toolkit's development back up, with a few things in mind.


### What it do ?
* Conversion to/from ASCII, hexadecimal and binary
* checksum calculation (md5, sha1, sha256)
* youtube video/audio download
* qr code generation (output to file in .png form, and to terminal as ASCII art)
* quarantine directory management (basically, a read-write only, root only directory to deal with sus files)
* metadata removal using exiftool
* redirecting output to clipboard (may not be compatible with your OS)
* type analysis (whether it's ASCII, hexadecimal or binary, using regex)
* secure file deletion (multiple passes with encryption and rewrite of the file with junk data)
* system-wide integrity check (needs some polishing though)
* scorched-earth-strategy (wipe the computer as thoroughly as possible ; may be deleted/changed to a plugin later, due to how dangerous it is, even with the failsafes implemented)
* a few easter eggs, like converting regular text to "uwu"-like text, a weird (but working) cipher, and braille
* rather good plugin system using python3

### How do I install it ?
Currently, the best (and only) way of installing the toolkit is to clone it's github repo, and either create a link to the "umbratools" file or move it to somewhere on your path. Plugins and config are automatically generated under `$HOME/.harmonytoolkit/`.
There are plans to include it on the AUR and on pip, but it will take some time as life tends to get in the way, and I do this as a hobby/side project, you know

To clone the repo, ensure you have `git` installed (`git --version`), then run the following command :
```bash
git clone https://github.com/TheDarkWolfer/Camille-s-Harmony-Toolkit
```
And if you want it on your path, you can do the following :
```bash
cd Camille-s-Harmony-Toolkit
ln -s ./umbratools /usr/local/bin/umbratools
```

Another thing you may want to do is shorten the name to an alias, like so :
```bash
echo "alias cht='umbratools'" >> ~/.zshrc | ~/.bashrc #Choose depending on the shell you use
```
