#!/usr/bin/env python3
import gi
import xkcd
from random import SystemRandom

gi.require_version("Gtk","3.0")
from gi.repository import Gtk

rand = SystemRandom()

class myWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="XKCD Browser")

        #self.cur_comic stores the number of the latest comic
        self.cur_comic=xkcd.getLatestComicNum()

        #image display
        self.image = Gtk.Image()
        self.image_area = Gtk.Box()

        self.image.set_from_file('/tmp/xkcd.png')
        self.image_area.set_center_widget(self.image)
        self.image_area.show_all()

        #random button
        self.rand_btn = Gtk.Button.new_with_label("random")
        self.rand_btn.connect ("clicked", self.on_random_clicked)
        #next button
        self.nxt_btn = Gtk.Button.new_with_label(">")
        self.nxt_btn.connect("clicked", self.on_nxt_clicked)
        if self.cur_comic == xkcd.getLatestComicNum():
            self.nxt_btn.set_sensitive(False)
        #fast next button
        self.fst_nxt_btn = Gtk.Button.new_with_label(">>")
        self.fst_nxt_btn.connect("clicked", self.on_fst_nxt_clicked)
        latest = xkcd.getLatestComicNum()
        if self.cur_comic > latest - 5:
            self.fst_nxt_btn.set_sensitive(False)
        #previous button
        self.prv_btn = Gtk.Button.new_with_label("<")
        self.prv_btn.connect("clicked", self.on_prv_clicked)
        #fast previous button
        self.fst_prv_btn = Gtk.Button.new_with_label("<<")
        self.fst_prv_btn.connect("clicked", self.on_fst_prv_clicked)

        #organise buttons ~~~~~~~~~~~~~~~~~
        self.main_box = Gtk.VBox()
        self.main_box.add(self.image_area)
        self.button_box = Gtk.HButtonBox()
        self.button_box.set_homogeneous(False)

        self.button_box.pack_start(self.fst_prv_btn, False, True, 0)
        self.button_box.pack_start(self.prv_btn, False, True, 0)
        self.button_box.pack_start(self.rand_btn, False, True, 0)
        self.button_box.pack_start(self.nxt_btn, False, True, 0)
        self.button_box.pack_start(self.fst_nxt_btn, False, True, 0)
        self.main_box.add(self.button_box)

        self.add(self.main_box)

        #initialise ~~~~~~~~~~~~~~~~~~~~~~~
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

    def on_nxt_clicked(self, button):
        self.cur_comic += 1
        self.update_image()

    def on_fst_nxt_clicked(self, button):
        self.cur_comic += 5
        self.update_image()
        
    def on_prv_clicked(self, button):
        self.cur_comic -= 1
        self.update_image()

    def on_fst_prv_clicked(self, button):
        self.cur_comic -= 5
        self.update_image()

    def on_random_clicked(self, button):
        self.cur_comic=rand.randint(1,xkcd.getLatestComicNum())
        self.update_image()

    #Whenever we want to update the comic displayed we'll use this
    def update_image(self):
        xkcd.getComic(self.cur_comic).download(output='/tmp/',outputFile='xkcd.png')
        self.image.set_from_file('/tmp/xkcd.png')

        latest = xkcd.getLatestComicNum()
        if self.cur_comic == latest:
            self.nxt_btn.set_sensitive(False)
        elif self.cur_comic < latest:
            self.nxt_btn.set_sensitive(True)

        if self.cur_comic > latest - 5:
            self.fst_nxt_btn.set_sensitive(False)
        elif self.cur_comic <= latest - 5:
            self.fst_nxt_btn.set_sensitive(True)


comic = xkcd.getLatestComic()
comic.download(output="/tmp/",outputFile="xkcd.png")
Display = myWindow()
Gtk.main()
