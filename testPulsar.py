import unittest
from main import Grid
import time

class testPulsar(unittest.TestCase):

    def test1(self):
        g = Grid(20)
        #g.randomStart()
        g.setCell(3,1)
        g.setCell(4,1)
        g.setCell(5,1)
        g.setCell(9,1)
        g.setCell(10,1)
        g.setCell(11,1)
        g.setCell(1,3)
        g.setCell(6,3)
        g.setCell(8,3)
        g.setCell(13,3)
        g.setCell(1,4)
        g.setCell(6,4)
        g.setCell(8,4)
        g.setCell(13,4)
        g.setCell(1,5)
        g.setCell(6,5)
        g.setCell(8,5)
        g.setCell(13,5)
        g.setCell(3,6)
        g.setCell(4,6)
        g.setCell(5,6)
        g.setCell(9,6)
        g.setCell(10,6)
        g.setCell(11,6)
        g.setCell(3,8)
        g.setCell(4,8)
        g.setCell(5,8)
        g.setCell(9,8)
        g.setCell(10,8)
        g.setCell(11,8)
        g.setCell(3,13)
        g.setCell(4,13)
        g.setCell(5,13)
        g.setCell(9,13)
        g.setCell(10,13)
        g.setCell(11,13)
        g.setCell(1,9)
        g.setCell(6,9)
        g.setCell(8,9)
        g.setCell(13,9)
        g.setCell(1,10)
        g.setCell(6,10)
        g.setCell(8,10)
        g.setCell(13,10)
        g.setCell(1,11)
        g.setCell(6,11)
        g.setCell(8,11)
        g.setCell(13,11)
        
    
    
        g.print()
        while True:
            time.sleep(0.5)
            g.tickGrid()
            g.print()
    

if __name__ == '__main__':
    unittest.main()
          
