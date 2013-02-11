import sys
from collections import defaultdict

import sublime
import sublime_plugin

PYTHON_3 = 0x030000F0

class HideTabsEventListener(sublime_plugin.EventListener):

    _show_tabs = defaultdict(bool)

    if sys.hexversion > PYTHON_3:
        def on_new_async(self, view):
            self.toggle_tabs()
    else:
        def on_new(self, view):
            self.toggle_tabs()

    def on_close(self, view):
        self.toggle_tabs()

    if sys.hexversion > PYTHON_3:
        def on_clone_async(self, view):
            self.toggle_tabs()
    else:
        def on_clone(self, view):
            self.toggle_tabs()

    if sys.hexversion > PYTHON_3:
        def on_activated_async(self, view):
            self.toggle_tabs()
    else:
        def on_activated(self, view):
            self.toggle_tabs()

    if sys.hexversion > PYTHON_3:
        def on_deactivated_async(self, view):
            self.toggle_tabs()
    else:
        def on_deactivated(self, view):
            self.toggle_tabs()

    def toggle_tabs(self):
        window = sublime.active_window()
        if not window:
            return

        num_of_views = len(window.views())
        if num_of_views > 1:
            self.show_tabs = True
        elif num_of_views < 2:
            self.show_tabs = False

    def _get_show_tabs(self):
        window = sublime.active_window()
        return HideTabsEventListener._show_tabs[window.id()]
    def _set_show_tabs(self, show):
        window = sublime.active_window()
        if self.show_tabs != show:
            window.run_command('toggle_tabs')
        HideTabsEventListener._show_tabs[window.id()] = show
    show_tabs = property(_get_show_tabs, _set_show_tabs)
