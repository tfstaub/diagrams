# diagram.py
from diagrams import Diagram
from diagrams.generic import network as NETWORK
from diagrams.generic import os as OS

with Diagram("Basic Site", show=False):
    router = NETWORK.Router("Router")
    switch = NETWORK.Switch("Switch")
    pc = OS.Windows("PC")

    router >> switch >> pc
