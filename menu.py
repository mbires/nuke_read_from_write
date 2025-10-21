# -*- coding: utf-8 -*-

import nuke

menu = nuke.menu("Nuke").addMenu("BiresTools")
menu.addCommand("Read From Write", "import read_from_write; read_from_write.readFromWrite()", "Shift+R")
