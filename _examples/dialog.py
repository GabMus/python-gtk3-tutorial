#!/usr/bin/env python3

from gi.repository import Gtk

class Dialog(Gtk.Dialog):
    def __init__(self):
        Gtk.Dialog.__init__(self)
        self.set_title("Dialog")
        self.set_default_size(400, 300)
        self.add_button("OK", Gtk.ResponseType.OK)
        self.add_button("Cancel", Gtk.ResponseType.CANCEL)
        self.connect("response", self.on_response)

        label = Gtk.Label("This is a Dialog example.")
        self.vbox.add(label)

        self.show_all()

    def on_response(self, dialog, response):
        if response == Gtk.ResponseType.OK:
            print("OK button clicked")
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel button clicked")
        else:
            print("Dialog closed")

        dialog.destroy()

dialog = Dialog()
dialog.run()
