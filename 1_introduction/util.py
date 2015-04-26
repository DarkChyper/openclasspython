#!/usr/bin/env python3
# coding: utf-8

import os

def pause():
    if os.name == "nt":
        os.system("pause")

if __name__ == "__main__":
    pause()