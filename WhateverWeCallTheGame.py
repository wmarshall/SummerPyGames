#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#       WhateverWeCallTheGame.py
#       
#       Copyright Contributors
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 3 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.
#       
#       
import pygame, objects, levels,os,menus
pygame.init()
def testfunc():
    pass
def main():
    #texture=pygame.image.load("assets/mortHead.png")
    testobj=objects.Object("assets"+os.sep+"mortHead.png")
    level =levels.Level(1,1)
    screen = pygame.display.set_mode([800,600])
    testmenu=menus.Menu(dict([["test",testfunc]]))
    while True:
        testmenu.draw()
        pygame.display.flip()
    return 0

if __name__ == '__main__':
	main()

