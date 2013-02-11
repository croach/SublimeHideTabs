# Sublime Hide Tabs

Sublime Text plugin to manage hiding and showing tabs depending on how many views are in the active window.

## Installation

The easiest way to install the Hide Tabs plugin is with [Package Control][package_control]. If you don't have it installed, you can always do the following:

1. Either download (and unzip) the [zip file][zip_file] or clone the repository
2. Move the unzipped (or cloned) directory into the [Packages folder][packages_folder] for your platform

#### To find the Packages folder

1. Open Sublime Text
2. Open the python console `` Ctrl-` ``
3. Type the following into the python console:

    ```
    >>> import sublime
    >>> sublime.packages_path()
    ```

## Usage

To use the Hide Tabs plugin, you must first make sure that the tabs are hidden by default. Anytime the hide/show functionality gets "out of whack", just run through the following steps:

1. Open up Sublime Text (and close all tabs, if any, that are open)
2. Select *View > Hide Tabs*
3. Quit Sublime Text (to make sure your new preferences are saved)


[package_control]: http://wbond.net/sublime_packages/package_control
[zip_file]: https://github.com/croach/SublimeHideTabs/archive/master.zip
[packages_folder]: #to-find-the-packages-folder
