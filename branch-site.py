# diagram.py
from diagrams import Diagram
from diagrams.custom import Custom


with Diagram("Branch Site", show=False):
    router = Custom("Router", "./generic-icons/router.jpg")
    switch = Custom("Switch", "./generic-icons/switch 01.jpg")
    pc = Custom("PC", "./generic-icons/host.jpg")

    router >> switch >> pc
