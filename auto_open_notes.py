#
# Automatically opens notes files when a new window is created with a single folder
#
# place a ".sublime.autoopen" file in a folder with a file name per line to
# list the files that should automatically be opened when this folder is opened
# that will override tring to open the default notes.txt, readme.md, readme files
#
# https://github.com/noahcoad/auto_open_notes
#
# Yes I use tabs.  Set to 2 spaces.  Looks so weird on github, right?!  I mean 8 spaces?!? seriously?
# 

import sublime
import sublime_plugin
import os.path

# keep track of all windows we've run on
window_markers = []

# default list of files to look for to open
# TODO: move to a user config file
files = ['notes.txt', 'readme.md', 'readme.txt', 'readme']

class auto_open_notes(sublime_plugin.EventListener):
  def on_new_async(self, view):

    # expect to open default files, if we don't find a .sublime.autoopen file
    autoopen_defaults = True

    # track state across events
    global window_markers

    # view and window are live
    if view and view.window():

      # keep reference to this window
      w = view.window()

      # get id of the window to prevent re-opening file
      wid = str(w.id())

      # only autoopen a window once
      if wid not in window_markers:

        # keep track we've already tried to open a file for this window
        window_markers.append(wid)
        
        # make sure window has more than one view
        if len(w.views()) == 0:

          # for autoopen files, check each folder in the project
          for folder in w.folders():
            autoopen = os.path.join(folder, '.sublime.autoopen')
            
            # if an autoopen file exists, open each file listed in there
            if os.path.exists(autoopen):

              # a .sublime.autoopen file was found, so don't open notes.txt etc by default
              autoopen_defaults = False

              # get a file name on each line, ignore lines starting with "#"
              for line in [x.strip() for x in open(autoopen).readlines() if len(x) > 0 and x[0:1] != "#"]:
                # use project folder as base for relative paths
                # TODO: also support absolute path resolution
                file = os.path.join(folder, line)

                # check to see if the file exists and open it
                if os.path.exists(file):                     
                  w.open_file(file)

          # if there isn't a .sublime.autoopen file, then check the defaults
          if autoopen_defaults:

            # make sure window has exactly one folder
            if len(w.folders()) == 1:

              # check each type of file supported
              for x in files:

                # look for file in the main folder
                file = os.path.join(w.folders()[0], x)

                # if it exists, open the file and we're done
                if os.path.exists(file):                     
                  w.open_file(file)
                  return