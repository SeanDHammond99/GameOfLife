import unittest
from main import Grid
import time

class testPulsar(unittest.TestCase):

    def test1(self):
        g = Grid(20)
        g.setCell(5,3)
        g.setCell(4,4)
        g.setCell(5,4)
        g.setCell(6,4)
        g.setCell(3,5)
        g.setCell(4,5)
        g.setCell(5,5)
        g.setCell(6,5)
        g.setCell(7,5)
        g.setCell(3,12)
        g.setCell(4,12)
        g.setCell(5,12)
        g.setCell(6,12)
        g.setCell(7,12)
        g.setCell(4,13)
        g.setCell(5,13)
        g.setCell(6,13)
        g.setCell(5,14)
    
    
        g.print()
        while True:
            time.sleep(0.3)
            g.tickGrid()
            g.print()
    

if __name__ == '__main__':
    unittest.main()
