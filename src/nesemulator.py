from romLoader import romLoader
from cpu import cpu
import sys

class Console:

    def __init__(self):
        romPath = sys.argv[1]

        self.cartridge = romLoader(romPath)

        try:
            self.cartridge.load()
        except:
            print("Couldn't load NES cartridge")

        CPU = cpu(self.cartridge)
        CPU.run()

Console()
