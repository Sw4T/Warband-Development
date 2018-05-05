# Point export_dir to the folder you will be keeping your module
# Make sure you use forward slashes (/) and NOT backward slashes (\)



# Several possible variants for export_dir variable:

# Warband being installed to C:/Games
export_dir = "D:/Steam/steamapps/common/MountBlade Warband/Modules/Truand Brawl 0.1"

# Warband being installed to default path on Windows XP or Vista
#export_dir = "C:/Programs Files/Mount&Blade Warband/Modules/Native/"

# Warband being installed to default path on Windows 7+
#export_dir = "C:/Programs Files (x86)/Mount&Blade Warband/Modules/Native/"

# Likely paths for Steam Warband installation:
#export_dir = "C:/Programs Files/Steam/steamapps/common/Mount&Blade Warband/Modules/Native/"
#export_dir = "C:/Programs Files (x86)/Steam/steamapps/common/Mount&Blade Warband/Modules/Native/"



###################################
#   W.R.E.C.K. Compiler Options   #
###################################


# Change this line to select where compiler will generate ID_* files. Use None instead of the string to completely suppress generation of ID_* files.
# ONLY DO THIS WHEN YOU HAVE COMPLETELY REMOVED ID_* FILE DEPENDENCIES IN MODULE SYSTEM!
# Default value: "ID_%s.py"

#write_id_files = "ID_%s.py"    # default vanilla-compatible option
#write_id_files = "ID/ID_%s.py" # will put ID_* files in ID/ subfolder of module system's folder
write_id_files = None          # will suppress generation of ID_*.py files


# Set to True to display compiler performance information at the end of compilation. Set to False to suppress.
# Default value: False

show_performance_data = True



##########################
#   W.R.E.C.K. Plugins   #
##########################

#import plugin_ms_extension
#import plugin_presentations
