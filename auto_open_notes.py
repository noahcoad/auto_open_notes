#
# Automatically opens notes files when a new window is created with a single folder
#
# place a ".sublime.autoopen" file in a folder with a file name per line to
# list the files that should automatically be opened when this folder is opened
# that will override tring to open the default notes.txt, readme.md, readme files
#
# https://github.com/noahcoad/sublime_auto_open_notes
#

import sublime, sublime_plugin
import os.path

window_markers = []
files = ['notes.txt', 'readme.md', 'readme.txt', 'readme']

class auto_open_notes(sublime_plugin.EventListener):
	def on_new_async(self, view):
		autoopen_defaults = True
		global window_markers                                    # track state across events
		if view and view.window():                               # ensure window is live
			w = view.window()                                      # keep reference to this window
			wid = str(w.id())                                      # get id of the window to prevent re-opening file
			if wid not in window_markers:                          # if this window hasn't had a default open yet
				window_markers.append(wid)                           # keep track we've already tried to open a file for this window
				if len(w.views()) == 0:                              # make sure window has more than one view
					for folder in w.folders():                         # for autoopen files, check each folder in the project
						autoopen = os.path.join(folder,                  # look for a .sublime.autoopnen file
							'.sublime.autoopen')                           # look for a .sublime.autoopnen file
						if os.path.exists(autoopen):                     # if an autoopen file exists, open each file listed in there
							autoopen_defaults = False                      # a .sublime.autoopen file was found, so don't open notes.txt etc by default
							for line in [x.strip()                         # process each file listed
								for x in open(autoopen).readlines()          # in the .sublime.autoopen file
									if len(x) > 0 and x[0:1] != "#"]:          # get a file name on each line, ignore lines starting with "#"
								file = os.path.join(folder, line)            # use project folder as base
								if os.path.exists(file):                     # check to see if the file exists
									w.open_file(file)                          # open it
					if autoopen_defaults:                              # if there isn't a .sublime.autoopen file, then check the defaults
						if len(w.folders()) == 1:                        # make sure window has exactly one folder
							for x in files:                                # check each type of file supported
								file = os.path.join(w.folders()[0], x)       # look for file in the main folder
								if os.path.exists(file):                     # if it exists
									w.open_file(file)                          # open the file 
									return                                     # and we're done


# p.s. Yes, I'm using hard tabs for indentation.  bite me =P
# set tabs to whatever level of indentation you like in your editor 
# for crying out loud, at least they're consistent here, and use 
# the ST3 command "Indentation: Convert to Spaces", which will convert
# to spaces if you really need to be part of the 'soft tabs only' crowd =)