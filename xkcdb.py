#!/usr/bin/env python3
import gi
import xkcd
import math

gi.require_version("Gtk","3.0")
from gi.repository import Gtk

comic = xkcd.Comic(91)
comic.download(output="/tmp/",outputFile="xkcd.png")
class myWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="XKCD Browser")
        self.box = Gtk.VBox()
        self.image = Gtk.Image()
        self.image_area = Gtk.Box()
        self.button = Gtk.Button(label="Click Here")
        self.box.add(self.image_area)
        self.box.add(self.button)
        self.image.set_from_file('/tmp/xkcd.png')
        self.image_area.add(self.image)
        self.image_area.show_all()
        #self.button.connect ("clicked", self.update_image)
        self.add(self.box)
    #def on_button_clicked (self, widget):
    #    comic.show()

    #def update_image (widged, data=None):
    #    image = Gtk.Image()
    #    image_area = Gtk.Box()
    #    image.set_from_file('/tmp/xkcd.png')
    #    image_area.add(image)
    #    image_area.show_all()

win = myWindow()
win.connect("delete-event", Gtk.main_quit)
#win.add(box)
win.show_all()
Gtk.main()
