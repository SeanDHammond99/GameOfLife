import unittest
from main import Grid
import time

class testPulsar(unittest.TestCase):

    def test1(self):
        g = Grid(20)
        g.setCell(14,11)
        g.setCell(15,11)
        g.setCell(12,12)
        g.setCell(17,12)
        g.setCell(11,13)
        g.setCell(11,14)
        g.setCell(17,14)
        g.setCell(11,15)
        g.setCell(12,15)
        g.setCell(13,15)
        g.setCell(14,15)
        g.setCell(15,15)
        g.setCell(16,15)
        
    
    
        g.print()
        while True:
            time.sleep(0.1)
            g.tickGrid()
            g.print()
    

if __name__ == '__main__':
    unittest.main()
