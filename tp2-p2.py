#! /usr/bin/env python

from tp1 import *

def leftSide(g, n):
    ''' (grid, int) -> grid

    Return the left part of g (split at the nth column)

    Precondition: 0 <= n < len(grid)

    >>> g = leftSide(genX(5), 3) ; displayGrid(g)
    - - - 
    *    
      *  
        *
      *  
    *    
    - - - 
    '''



def rightSide(g, n):
    ''' (grid, int) -> grid

    Return the right part of g (split at the nth column)

    Precondition: 0 <= n < len(grid)

    >>> g = rightSide(genX(5), 3) ; displayGrid(g)
    - - 
      *
    *  
    <BLANKLINE>
    *  
      *
    - - 
    '''



def locateRightMost(g):
    ''' (grid) -> int

    >>> g1 = leftSide(genX(5), 3) ; g2 = genGrid(5, 3) ; g3 = hConcat(g1, g2)
    >>> displayGrid(g3)
    - - - - - - 
    *          
      *        
        *      
      *        
    *          
    - - - - - - 
    >>> locateRightMost(g3)
    2
    '''



def shiftRight(g):
    ''' (grid) -> grid

    >>> g1 = leftSide(genX(5), 3) ; g2 = genGrid(5, 3) ; g3 = hConcat(g1, g2)
    >>> displayGrid(g3)
    - - - - - - 
    *          
      *        
        *      
      *        
    *          
    - - - - - - 
    >>> g4 = shiftRight(g3) ; displayGrid(g4)
    - - - - - - 
          *    
            *  
              *
            *  
          *    
    - - - - - - 
    '''





if __name__ == '__main__':
    import doctest
    res = doctest.testmod()
    print res



