# Auto Open Notes - a Sublime Text 3 Plugin

When a new window is opened with a single folder:
1. A `.sublime.autoopen` file is looked for in the folder.  If it exists, each file listed in the file is then opened.
2. Otherwise it'll look for a `notes.txt`, `readme.md`, `readme.txt`, then `readme` files in that order and opens the first it finds.


## To Install
Use WBond's [Package Control](https://packagecontrol.io/)


## To Use
Try having a notes.txt or readme.md file in a folder and opening that folder in sublime.

    mkdir ~/tmp
    echo hello world > ~/tmp/notes.txt
    subl ~/tmp


## See Also
Check out my other Sublime Text 3 plugins:
* [Open URL](https://github.com/noahcoad/open-url)
* [Google Spell Check](https://github.com/noahcoad/google-spell-check)


## The sweet flow...
Combined with the [Open URL](https://github.com/noahcoad/open-url) plugin ... create a projects.txt file that you put lines in for each project folder.  Then just open this projects.txt file, put the cursor over a line, ctrl+u to "open url" to that folder, and bamn, the folder is opened and the appropriate notes/readme file is opened automatically.


## Random Thoughts
Should this be renamed to "Auto Open Readme"?  bc most people use readme files instead of notes? 


## Backlog
Improvement ideas for contributing and improving...

* Add to [Package Control](https://packagecontrol.io/docs/submitting_a_package)
* Move default set of files to open (like notes.txt, readme.txt, etc) to a settings file that the user can override


## Acknowledgments 
Shout out to [@josiahcoad](https://github.com/josiahcoad) for code reviewing and improvement ideas!