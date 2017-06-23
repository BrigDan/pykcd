#!/usr/bin/env python3
import gi
import xkcd
from random import SystemRandom

gi.require_version("Gtk","3.0")
from gi.repository import Gtk

rand = SystemRandom()

def getRandomComic():
    number = rand.randint(1,xkcd.getLatestComicNum())
    return xkcd.Comic(number)

class myWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="XKCD Browser")

        self.main_box = Gtk.VBox()

        self.image = Gtk.Image()
        self.image_area = Gtk.Box()


        self.image.set_from_file('/tmp/xkcd.png')
        self.image_area.add(self.image)
        self.image_area.show_all()

        self.button = Gtk.Button(label="random xkcd")

        self.main_box.add(self.image_area)
        self.main_box.add(self.button)
        self.add(self.main_box)

        self.button.connect ("clicked", self.update_image)
        self.main_box.pack_start(button, True, True, 0)
        button = Gtk.Button.new_with_label("Click Me")
        button.connect("clicked", self.on_click_me_clicked)
        self.main_box.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_mnemonic("_Open")
        button.connect("clicked", self.on_open_clicked)
        self.main_box.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_mnemonic("_Close")
        button.connect("clicked", self.on_close_clicked)
        self.main_box.pack_start(button, True, True, 0)

    def on_click_me_clicked(self, button):
        print("\"Click me\" button was clicked")

    def on_open_clicked(self, button):
        print("\"Open\" button was clicked")

    def on_close_clicked(self, button):
        print("Closing application")
        Gtk.main_quit()

    def update_image(win,butt):
        getRandomComic().download(output='/tmp/',outputFile='xkcd.png')
        win.image.set_from_file('/tmp/xkcd.png')

comic = xkcd.getLatestComic()
comic.download(output="/tmp/",outputFile="xkcd.png")

win = myWindow()
win.connect("delete-event", Gtk.main_quit)
#win.add(box)
win.show_all()
Gtk.main()
