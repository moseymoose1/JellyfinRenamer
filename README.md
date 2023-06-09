**JellyfinRenamer**

Python script that parses existing file names for season and episode terms and renames all files in a specified folder to match Jellyfin's naming convention. Supports [tags] and double episodes and part numbers. Files must have the episode pattern SXXEXX somewhere in the original filename. Most downloaded files have this pattern somewhere, so use it to tidy up downloaded seasons to work with Jellyfin or organise your files.

**Instructions**
1. Execute the run.bat file.
2. Copy the folder path from windows by right clicking on the address bar in explorer, ENTER.
3. List any tags you wish to add to the file names superated by ; e.i. 2160p;HDR (this will apply to all files in the folder) Dont not add [brakets] for your tags, the script will add them automatically.
4. If you do not wish to add any tags, just hit ENTER with no values provided.

*The run.bat should always be kept in the* ***same folder*** *as the JellyFinRename.py as the batch file will always look for the script in the current directory.*
