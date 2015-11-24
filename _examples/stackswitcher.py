#!/usr/bin/env python3

from gi.repository import Gtk

class StackSwitcher(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_default_size(400, 300)
        self.connect("destroy", Gtk.main_quit)

        grid = Gtk.Grid()
        self.add(grid)

        stack = Gtk.Stack()
        stack.set_hexpand(True)
        stack.set_vexpand(True)
        grid.attach(stack, 0, 1, 1, 1)

        stackswitcher = Gtk.StackSwitcher()
        stackswitcher.set_stack(stack)
        grid.attach(stackswitcher, 0, 0, 1, 1)

        for page in range(1, 4):
            label = Gtk.Label("Stack Content on Page %i" % (page))
            name = "label%i" % page
            title = "Page %i" % page
            stack.add_titled(label, name, title)

window = StackSwitcher()
window.show_all()

Gtk.main()
