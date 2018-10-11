#
# Automatically opens notes files when a new window is created with a single folder
# 
# https://www.sublimetext.com/docs/3/api_reference.html#sublime_plugin.EventListener
# ~/code/prjs/sublime
# backup:
# zip -r ~/code/prjs/sublime/auto_open_notes/backup.zip "/Users/ncoad/Library/Application Support/Sublime Text 3/Packages/auto_open_notes"
#
# place a ".sublime.autoopen" file in a folder with a file name per line to
# list the files that should automatically be opened when this folder is opened

import sublime, sublime_plugin
import os.path

window_markers = []
files = ['notes.txt', 'readme.md', 'readme']

class auto_open_notes(sublime_plugin.EventListener):
	def on_new_async(self, view):
		global window_markers                                    # track state across events
		if view and view.window():                               # ensure window is live
			w = view.window()                                      # keep reference to this window
			wid = str(w.id())                                      # get id of the window to prevent re-opening file
			if wid not in window_markers:                          # if this window hasn't had a default open yet
				window_markers.append(wid)                           # keep track we've already tried to open a file for this window
				if len(w.views()) == 0:                              # make sure window has more than one view
					for folder in w.folders():                         # for autoopen files, check each folder in the project
						autoopen = os.path.join(folder, '.sublime.autoopen')
						if os.path.exists(autoopen):                     # if an autoopen file exists, open each file listed in there
							for line in [x.strip() for x in open(autoopen).readlines() if len(x) > 0 and x[0:1] != "#"]:        # get a file name on each line, ignore lines starting with "#"
								file = os.path.join(folder, line)            # use project folder as base
								if os.path.exists(file):                     # check to see if the file exists
									w.open_file(file)                          # open it
						else:                                            # if there isn't a .sublime.autoopen file, then check the defaults
							if len(w.folders()) == 1:                      # make sure window has exactly one folder
								for x in files:                              # check each type of file supported
									file = os.path.join(w.folders()[0], x)     # look for file in the main folder
									if os.path.exists(file):                   # if it exists
										w.open_file(file)                        # open the file 
										return                                   # and we're done