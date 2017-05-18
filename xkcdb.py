#!/usr/bin/env python3
import gi
import xkcd
gi.require_version("Gtk","3.0")
from gi.repository import Gtk

comic = xkcd.Comic(90)
class myWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="XKCD Browser")

        self.button = Gtk.Button(label="Click Here")
        self.button.connect ("clicked", self.on_button_clicked)
        self.add(self.button)

    def on_button_clicked (self, widget):
        comic.show()

win = myWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
