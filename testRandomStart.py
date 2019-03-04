import unittest
from main_wrapping import Grid
import time

class testPulsar(unittest.TestCase):

    def test1(self):
        g = Grid(30)
        g.randomStart()
    
        g.print()
        while True:
            time.sleep(0.3)
            g.tickGrid()
            g.print()
    

if __name__ == '__main__':
    unittest.main()
