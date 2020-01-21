# -*- coding: utf-8 -*-
"""
GameEventData.py

Contains functions for generating dataframes, dictionaries ,lists, etc. that
are used to determine event outcomes (e.g., pitch results, what happens once
a ball is hit, base runner management). 

Module and functions called by baseball_main.py

Create November 30, 2019
"""

import pandas as pd
import numpy as np


def BuildPitchResultDataFrame():
    '''
    '''
    
    # Build pitch-result lookup dataframe:

    r1 = [1,2,3,4,5,6,7,2,3,4,5,6,7,3,4,5,6,7,4,5,6,7,5,6,7,6,7,7]
    r2 = [1,1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,4,4,4,4,5,5,5,6,6,7]

    PitchResult = ['BallHit','Strike!','Ball','Strike!','FoulBall','Strike!','Strike!','BallHit',
       'Ball','FoulBall','Strike!','Strike!', 'Strike!','BallHit','FieldingError','Strike!',
       'Ball','Ball','Hit by Pitch','FoulBall','BallHit','Strike!','Strike!','Ball',
       'Ball','BallHit','Ball','Strike!']

    DFhdr = ['Roll_1','Roll_2','PitchResult','HitResult']

    HitResult = ['HomeRun!','Single','GndOut','FlyOut',
             'FlyOut',
             'GndOut',
             'Single',
             'GndOut',
             'FoulOut',
             'GndOut',
             'FlyOut',
             'FlyOut', 
             'Double',
             'FlyOut',
             'GndOut',
             'Single',
             'Double',
             'GndOut',
             'FoulOut',
             'GndOut',
             'Triple',
            'GndOut',
            'FlyOut',
            'Single',
            'FlyOut',
            'Home Run',
            'GndOut',
            'FlyOut']

    df = pd.DataFrame(np.column_stack([r1,r2,PitchResult,HitResult]), columns=DFhdr)
    df = df.astype({'Roll_1':'int8','Roll_2':'int8','PitchResult':'str','HitResult':'str'}).copy()
    
    return(df)