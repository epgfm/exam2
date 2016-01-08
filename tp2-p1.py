#! /usr/bin/env python

from tp1 import *


def invert(g):
    ''' (grid) -> grid

    Returns an inverted version of g.

    >>> displayGrid(invert(genX(3)))
    - - - 
      *  
    *   *
      *  
    - - - 
    '''



def rotateClockWise90(g):
    ''' (grid) -> grid

    Returns a version of g rotated 90 degrees clockwise.

    >>> g0 = genUpperRightTriangle(3) ; displayGrid(g0)
    - - - 
    * * *
      * *
        *
    - - - 
    >>> g1 = rotateClockWise90(g0) ; displayGrid(g1)
    - - - 
        *
      * *
    * * *
    - - - 
    >>> g2 = rotateClockWise90(g1) ; displayGrid(g2)
    - - - 
    *    
    * *  
    * * *
    - - - 
    >>> g3 = rotateClockWise90(g2) ; displayGrid(g3)
    - - - 
    * * *
    * *  
    *    
    - - - 
    '''



def paintAlternateLines(g):
    ''' (grid) -> NoneType

    Change g so that every other line is painted.

    >>> g = genGrid(5, 8) ; paintAlternateLines(g) ; displayGrid(g)
    - - - - - - - - 
    * * * * * * * *
    <BLANKLINE>
    * * * * * * * *
    <BLANKLINE>
    * * * * * * * *
    - - - - - - - - 
    '''



def paintGrid(nRows, nCols):
    ''' (grid) -> NoneType

    Returns a graphic reprensentation of a grid.

    >>> g = paintGrid(5, 8) ; displayGrid(g)
    - - - - - - - - 
    * * * * * * * *
    *   *   *   *  
    * * * * * * * *
    *   *   *   *  
    * * * * * * * *
    - - - - - - - - 
    '''






if __name__ == '__main__':
    import doctest
    res = doctest.testmod()
    print res



