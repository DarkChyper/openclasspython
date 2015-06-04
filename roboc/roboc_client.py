#!/usr/bin/python3.4
# -*- coding: utf8 -*-

from roboc_client_class import *
from roboc_client_interf import *

fenetre = Tk()
interface = Interface(fenetre)

network = Network()

#datasend = DataSend()
datareceive = DataReceive()
majprincipal = MajPrincipal()

#datasend.start()
datareceive.start()
majprincipal.start()

interface.mainloop()
interface.destroy()

#datasend.join()
datareceive.join()
majprincipal.join()

network.deco()


