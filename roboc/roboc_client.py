#!/usr/bin/python3.4
# -*- coding: utf8 -*-

from roboc_client_class import *

network = Network()

datasend = DataSend()

datasend.start()

datasend.join()

network.deco()
