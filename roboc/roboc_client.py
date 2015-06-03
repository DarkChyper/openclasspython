#!/usr/bin/python3.4
# -*- coding: utf8 -*-

from roboc_client_class import *
from roboc_client_interf import *

network = Network()

#datasend = DataSend()
datareceive = DataReceive()

#datasend.start()
datareceive.start()

fenetre = Tk()
interface = Interface(fenetre)

interface.mainloop()

#datasend.join()
datareceive.join()

network.deco()

interface.destroy()
