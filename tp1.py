#! /usr/bin/env python


def genGrid(nRows, nCols):
    ''' (int, int) -> list of list of chars {{grid}}

    Generates and returns a grid of nRows by nCols. Every element on the inner
    lists is a whitespace character.

    '''
    g = [] # Output grid
    for r in range(nRows): # Create each row one by one.
        row = []           # Rows cannot be aliases of each others.
        for c in range(nCols):
            row.append(' ')
        g.append(row)
    return g



def displayGrid(g):
    ''' (grid) -> NoneType

    Display the grid to standard output. The grid must be surrounded by '+'
    symbols.

    '''
    print '- ' * len(g[0]) # Header and footer for better visualization
    for row in g: # For each row
        for col in row: # print every column with no newline
            print col,
        print           # Print newline at the end of the row
    print '- ' * len(g[0])



def genX(size):
    ''' (int) -> grid

    Returns a X graphics of size size.

    >>> displayGrid(genX(3))
    - - - 
    *   *
      *  
    *   *
    - - - 
    >>> displayGrid(genX(4))
    - - - - 
    *     *
      * *  
      * *  
    *     *
    - - - - 
    >>> displayGrid(genX(5))
    - - - - - 
    *       *
      *   *  
        *    
      *   *  
    *       *
    - - - - - 
    '''
    g = genGrid(size, size)
    for i in range(size):
        g[i][i] = '*'           # Draw Upper Left to Lower Right line
        g[i][size-1 - i] = '*'  # Draw Lower Left to Upper Right line
    return g



def genUpperRightTriangle(size):
    '''

    >>> displayGrid(genUpperRightTriangle(7))
    - - - - - - - 
    * * * * * * *
      * * * * * *
        * * * * *
          * * * *
            * * *
              * *
                *
    - - - - - - - 
    '''
    g = genGrid(size, size)
    n = len(g)
    for i in range(n):  # Iterate over each row
        for j in range(i, n): # Every column starting from the row number to
             g[i][j] = '*'    # the end of the row is painted.
    return g



def genUpperCenterTriangle(size):
    '''

    >>> displayGrid(genUpperCenterTriangle(7))
    - - - - - - - 
    * * * * * * *
      * * * * *  
        * * *    
          *      
    <BLANKLINE>
    <BLANKLINE>
    <BLANKLINE>
    - - - - - - - 
    '''
    g = genGrid(size, size)
    n = len(g)
    for i in range(n / 2 + 1):
        for j in range(i, n - i): # The range to paint diminishes from one unit
             g[i][j] = '*'        # on the left and on the right as we go down.
    return g



def horizontalFlip(g):
    '''

    >>> displayGrid(horizontalFlip(genUpperRightTriangle(4)))
    - - - - 
          *
        * *
      * * *
    * * * *
    - - - - 
    '''
    out = []
    for i in range(len(g)-1, -1, -1): # Iterate in reverse over the rows
        out.append(list(g[i]))  # list() call to avoid aliasing issues.
    return out



def merge(g1, g2):
    ''' (grid, grid) -> grid

    Returns a new grid that is g1 overlayed on top of g2.

    Precondition: g1 and g2 have the same dimensions.

    >>> displayGrid(
    ...     merge(
    ...         genUpperCenterTriangle(5),
    ...         horizontalFlip(genUpperCenterTriangle(5))
    ...     )
    ... )
    - - - - - 
    * * * * *
      * * *  
        *    
      * * *  
    * * * * *
    - - - - - 
    '''
    out = []
    nRows, nCols = len(g1), len(g1[0])
    for i in range(nRows):
        sub = []
        for j in range(nCols):
            if g1[i][j] == '*' or g2[i][j] == '*':
                sub.append('*')
            else:
                sub.append(' ')
        out.append(sub)
    return out



def vConcat(g1, g2):
    ''' (grid, grid) -> grid

    Returns a vertical concatenation of g1 and g2.

    Precondition: g1 and g2 have the same number of columns.

    >>> displayGrid(vConcat(genX(3), genX(3)))
    - - - 
    *   *
      *  
    *   *
    *   *
      *  
    *   *
    - - - 
    '''
    out = []
    for row in g1:
        out.append(list(row))
    for row in g2:
        out.append(list(row))
    return out



def hConcat(g1, g2):
    ''' (grid, grid) -> grid

    Returns an horizontal concatenation of g1 and g2.

    Precondition: g1 and g2 have the same number of rows.

    >>> displayGrid(hConcat(genX(3), genX(3)))
    - - - - - - 
    *   * *   *
      *     *  
    *   * *   *
    - - - - - - 
    '''
    out = []
    for row in range(len(g1)):
        sub = []
        for col in g1[row]:
            sub.append(col)
        for col in g2[row]:
            sub.append(col)
        out.append(sub)
    return out




def hConcatMulti(g, n):
    ''' (grid, int) -> grid

    Repeat the pattern in g n times horizontally.

    >>> displayGrid(hConcatMulti(genX(3), 3))
    - - - - - - - - - 
    *   * *   * *   *
      *     *     *  
    *   * *   * *   *
    - - - - - - - - - 
    >>> displayGrid(hConcatMulti(genX(3), 4))
    - - - - - - - - - - - - 
    *   * *   * *   * *   *
      *     *     *     *  
    *   * *   * *   * *   *
    - - - - - - - - - - - - 
    '''
    out = g
    for i in range(1, n):
        out = hConcat(out, g)
    return out



def vConcatMulti(g, n):
    ''' (grid, int) -> grid

    Repeat the pattern in g n times vertically.

    >>> displayGrid(vConcatMulti(genX(3), 3))
    - - - 
    *   *
      *  
    *   *
    *   *
      *  
    *   *
    *   *
      *  
    *   *
    - - - 
    '''
    out = g
    for i in range(1, n):
        out = vConcat(out, g)
    return out



def hvConcatMulti(g, nRows, nCols):
    ''' (grid, int, int) -> grid

    Repeat the pattern in grid g nRows times vertically and nCols times
    horizontally.

    >>> displayGrid(hvConcatMulti(genX(3), 3, 4))
    - - - - - - - - - - - - 
    *   * *   * *   * *   *
      *     *     *     *  
    *   * *   * *   * *   *
    *   * *   * *   * *   *
      *     *     *     *  
    *   * *   * *   * *   *
    *   * *   * *   * *   *
      *     *     *     *  
    *   * *   * *   * *   *
    - - - - - - - - - - - - 
    '''
    out = vConcatMulti(g, nRows)
    out = hConcatMulti(out, nCols)
    return out



if __name__ == '__main__':
    import doctest
    res = doctest.testmod()
    print res











