# Warband-Development

_Actually developping_ : **Truand World** - A MP Mod for Mount&Blade Warband where you fight with many differents classes, weapons and stuff but in a totally random way.
***
## Coders

- Swatosj
- Marmoutte

***

We are using the native module system to create the mod and some tools :
- [openBRF](http://www.mbrepository.com/file.php?id=1466) - Open .brf files to preview/import/exports everything like meshes, textures...
- [Morghs M&B WB-WFAS Editor](http://mountandblade.mircon.de/wp/morghs-mb-wbwfas-editor/) - GUI to add/edit troops, items, parties...
- [MABLE](http://www.mbrepository.com/file.php?id=2659) - GUI to edit module_items.py

***

##How to get ready ?

1. Download Python 2.7 and add ";C:/Python27" (or your install path) to the PATH variable of Windows 
2. Fetch the module system directory from this repository
3. Change the export path in _module_info.py_ to the folder of your new mod (like the other example directory "Truand World 0.1" which is already compiled)
4. Execute _build_module.bat_ to compile all your files into your mod folder
5. Put your mod folder in your Modules directory and run it on Mount&Blade:Warband
