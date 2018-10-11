# Auto Open Notes - a Sublime Text 3 Plugin

When a new window is opened with a single folder:
1. A `.sublime.autoopen` file is looked for.  If it exists, each file listed in the file is then opened
2. Otherwise it'll look for a `notes.txt`, then `readme.md`, then `readme` files and opens the first


## To Install

    cd "$HOME/Library/Application Support/Sublime Text 3/Packages/auto_open_notes/notes.txt"
    git clone https://github.com/noahcoad/auto_open_notes.git


## To Use

    mkdir ~/tmp
    echo hello world > ~/tmp/notes.txt
    subl ~/tmp


## See Also

Check out my other Sublime Text 3 plugins:
* [Open URL](https://github.com/noahcoad/open-url)
* [Google Spell Check](https://github.com/noahcoad/google-spell-check)


## The sweet flow...
Combined with the [Open URL](https://github.com/noahcoad/open-url) plugin ... create a projects.txt file that you put lines in for each project folder.  Then just open this projects.txt file, put the cursor over a line, ctrl+u to "open url" to that folder, and bamn, the folder is opened and the appropriate notes/readme file is opened automatically.
