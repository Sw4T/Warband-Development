# Warband Module Development 

_Actually developping_ : **Random Academy Brawl** - A MP Mod for Mount&Blade Warband where you fight with many differents classes, weapons and stuff but in a totally random way. We're aiming to release a version with deathmatch implemented over little maps and some basic random stuff like positioning or weapons.

We are looking for some map-makers, scripters, 3D designers who want to make this a *real garbage*...

***

## Developers

- Swatosj - Editing, Resources content, Scripting 
- Marmoutte - Scripting
- Zixelle - Modeling, Texturing, Scenes

***

## How to get involved and/or play the mod ?

1. Download Python 2.7.X and add ";C:/Python27" (or your install path) to the PATH variable of Windows 
2. Get the module system directory from this repository and copy it where you want
3. Copy the Native module folder and rename it
4. Copy the content of the "Module folder to copy" inside the created module
4. Change the variable _export_dir_ of the _module_info.py_ file to the path of this copied folder
5. Execute _compile.bat_
6. Run the game by launching the created module


***

## Supported match types 

_Deathmatch_, _Team Deathmatch_

***

We are using the native module system to create the mod and some tools :
- [openBRF](http://www.mbrepository.com/file.php?id=1466) - Open .brf files to preview/import/exports everything like meshes, textures...
- [Morghs M&B WB-WFAS Editor](https://drive.google.com/file/d/1cC2UVnQXdsMFxt7PepGbCWtNcOau4CiA/view) - GUI to add/edit troops, items, parties...
- [MABLE](http://www.mbrepository.com/file.php?id=2659) - GUI to edit module_items.py

[W.R.E.C.K](http://forums.taleworlds.com/index.php/topic,325102.0.html) and [WSE](http://forums.taleworlds.com/index.php/topic,324890.0.html) are already integrated within the module system

***

A great tutorial about starting to mod and code in Warband is available in [PDF](http://www.freewebs.com/jikbyond/40kTut/M&B%20Module%20System%20Doc2-3.pdf) or [HTML](http://forums.taleworlds.com/index.php/board,12.0.html)

Tutorial about scripting in warband: http://forums.taleworlds.com/index.php/topic,142422.0.html

Tutorial about handling multiplayer events: https://forums.taleworlds.com/index.php/topic,94854.0.html

Importing items from mods: https://www.youtube.com/watch?v=JHUd-Pp-SSw
