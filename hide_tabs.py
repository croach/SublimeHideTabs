"""
This plugin manages hiding/showing tabs according to the number of open views
"""

import sys
from collections import defaultdict

import sublime
import sublime_plugin


def sublime_text_3():
    """Returns True if this is Sublime Text 3
    """
    try:
        return int(sublime.version()) >= 3000
    except ValueError:
        return sys.hexversion >= 0x030000F0


class HideTabsEventListener(sublime_plugin.EventListener):

    # Holds the tabs visibility for each of the currently open windows
    _tabs_visibility = defaultdict(bool)

    # Use the async versions of the event handlers available in Sublime Text 3
    if sublime_text_3():
        def on_new_async(self, view):
            self.update_tabs_visibility()

        def on_clone_async(self, view):
            self.update_tabs_visibility()

        def on_activated_async(self, view):
            self.update_tabs_visibility()

        def on_deactivated_async(self, view):
            self.update_tabs_visibility()

    # Otherwise, just use the synchronous versions if this is Sublime Text 2
    else:
        def on_new(self, view):
            sublime.set_timeout(self.update_tabs_visibility, 200)

        def on_clone(self, view):
            sublime.set_timeout(self.update_tabs_visibility, 200)

        def on_activated(self, view):
            sublime.set_timeout(self.update_tabs_visibility, 200)

        def on_deactivated(self, view):
            sublime.set_timeout(self.update_tabs_visibility, 200)

    # There is no async version of on_close, so just use the regular one
    def on_close(self, view):
        self.update_tabs_visibility()

    def update_tabs_visibility(self):
        """Show/hide tabs based on the number of views in the active window
        """
        window = sublime.active_window()
        if not window:
            return

        # Loop through all of the groups (split windows), and if any have
        # more than one view, show tabs, otherwise, hide them
        for i in range(window.num_groups()):
            if len(window.views_in_group(i)) > 1:
                self.tabs_visible = True
                break
        else:
            self.tabs_visible = False

    def _get_tabs_visible(self):
        window = sublime.active_window()
        return HideTabsEventListener._tabs_visibility[window.id()]
    def _set_tabs_visible(self, visible):
        window = sublime.active_window()
        if self.tabs_visible != visible:
            window.run_command('toggle_tabs')
        HideTabsEventListener._tabs_visibility[window.id()] = visible
    tabs_visible = property(_get_tabs_visible, _set_tabs_visible)
