#!/usr/bin/env python3
import gi
import xkcd
from random import SystemRandom

gi.require_version("Gtk","3.0")
from gi.repository import Gtk

rand = SystemRandom()
number = 0 #Default

class myWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="XKCD Browser")

        #self.cur_comic stores the number of the latest comic
        self.cur_comic=xkcd.getLatestComicNum()

        self.main_box = Gtk.VBox()

        self.image = Gtk.Image()
        self.image_area = Gtk.Box()

        self.rand_btn = Gtk.Button.new_with_label("Random XKCD")

        self.image.set_from_file('/tmp/xkcd.png')
        self.image_area.add(self.image)
        self.image_area.show_all()

        self.rand_btn.connect ("clicked", self.on_random_clicked)

        self.main_box.add(self.image_area)
        self.main_box.add(self.rand_btn)
        self.add(self.main_box)

        self.nxt_btn = Gtk.Button.new_with_label("Next Comic")
        self.nxt_btn.connect("clicked", self.on_next_clicked)
        self.main_box.pack_start(self.nxt_btn, True, True, 0)

        self.prv_btn = Gtk.Button.new_with_label("Previous Comic")
        self.prv_btn.connect("clicked", self.on_prv_clicked)
        self.main_box.pack_start(self.prv_btn, True, True, 0)

    #    button = Gtk.Button.new_with_mnemonic("_Open")
    #    button.connect("clicked", self.on_open_clicked)
    #    self.main_box.pack_start(button, True, True, 0)

        self.close_btn = Gtk.Button.new_with_mnemonic("_Close")
        self.close_btn.connect("clicked", self.on_close_clicked)
        self.main_box.pack_start(self.close_btn, True, True, 0)

        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

    def on_next_clicked(self, button):
        if self.cur_comic
            self.nxt_btn.set_sensitive(False)
        else:
            self.cur_comic+=1
        self.update_image()

    def on_prv_clicked(self, button):
        self.cur_comic+=-1
        self.update_image()

    def on_random_clicked(self,button):
        self.cur_comic=rand.randint(1,xkcd.getLatestComicNum())
        self.update_image()

    def on_close_clicked(self, button):
        Gtk.main_quit()

    #Whenever we want to update the comic displayed we'll use this
    def update_image(self):
        xkcd.getComic(self.cur_comic).download(output='/tmp/',outputFile='xkcd.png')
        self.image.set_from_file('/tmp/xkcd.png')

comic = xkcd.getLatestComic()
comic.download(output="/tmp/",outputFile="xkcd.png")

myWindow()
Gtk.main()
