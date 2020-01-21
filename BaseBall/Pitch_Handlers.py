#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Game_Event_Handlers.py

Created on Sat Nov 30 16:53:01 2019

@author: Paul
"""

# Pitch Result Handlers:
def HandlePitch(df, p1, p2):
    if(p1 < p2): p1, p2 = p2, p1  # allows combinations, prevents permutations
         
    res = df.loc[(df['Roll_1'].values == p1) & (df['Roll_2'].values == p2)]

    if(res['PitchResult'].values == 'Strike!'):
        HandleStrikes()
            
    if(res['PitchResult'].values == 'Ball'):
        HandleBalls()
        print('Ball!!!')
        
    if(res['PitchResult'].values == 'BallHit'):
        HandleHitBall()
    #if(res['Result'].values == 'Single!') or (res['Result'].values == 'Double!!') or \
    #(res['Result'].values == 'Triple!!!') or (res['Result'].values == 'Home Run!!!!'):
    #self.HandleHitBall(res['Result'].values)
 
    if(res['PitchResult'].values == 'FoulBall'):
        HandleFoulBall()
            
    if(res['PitchResult'].values == 'Hit by Pitch'):
        print('Batter hit by pitched ball!!!')
        HandleHitByPitchError()
            
    if(res['PitchResult'].values == 'FieldingError'):
        print('Error!!!')
     

def HandleStrikes(self):
   s = self.GetStrikes()
   if(s < 2):
       self.SetStrikes(s+1)
       print('Strike')
   if(s == 2):
       self.SetStrikes(0)
       self.SetBalls(0)
       self.HandleOuts()
       print('Struck him out swinging!')                  
                  
def HandleBalls(self):
    b = self.GetBalls()
    if(b < 3):
        self.SetBalls(b+1)
    if(b == 3):
        # check for base runners
        print('Batter walks')
        self.SetBalls(0)
        self.SetStrikes(0)
                  
def HandleHitBall(self):
    #CheckBases()
    # reset balls and strikes
    self.SetBalls(0)
    self.SetStrikes(0)
    p1, p2 = np.random.randint(low=1, high=7, size=2)
        
    if(p1 < p2): p1, p2 = p2, p1  # allows combinations, prevents permutations
        
    res = df.loc[(df['Roll_1'].values == p1) & (df['Roll_2'].values == p2)]
        
    if(res['HitResult'].values == 'HomeRun!'):
        print('It is high! It is far! It is gone! A \'Judgian Blast!\'')
            
    if(res['HitResult'].values == 'Single'):
        self.on_base.ToggleBase
        print('Single')
        
    if(res['HitResult'].values == 'Double'):
        print('Double')
            
    if(res['HitResult'].values == 'Triple'):
        print('Triple')
            
    if(res['HitResult'].values == 'FlyOut'):
        self.HandleOuts()
        print('Batter Flies Out')
            
    if(res['HitResult'].values == 'GndOut'):
        self.HandleOuts()
        print('Batter Grounds Out')
            
    if(res['HitResult'].values == 'FoulOut'):
        self.HandleOuts()
        print('Pop Foul Caught, Batter Out')
            

def HandleFoulBall(self):
    print('Fouled out of play')
    s = self.GetStrikes()
    if(s < 2):
        self.SetStrikes(s+1)
        # add random option for fielder to catch some 
            
            
def HandleOuts(self):
           # check number of outs < 2 increment, 2 end inning half, increment inning, reset outs
            # reset balls,strikes, change batting and fielding teams (check for game end)
            outs = self.GetOuts()
            if(outs+1 == 3):
                print('Side retired')
                # change batting and fielding teams
                self.batting_team, self.fielding_team = self.fielding_team, self.batting_team
                self.SetOuts(0)
                
                if(self.GetInningHalf() == 'top'):
                    self.SetInningHalf('bottom')
                else:
                    self.SetInningHalf('top')
                    self.SetInning(self.GetInning()+1)
            else:
                self.SetOuts(self.GetOuts()+1)

    def HandleFieldingError(self):
        # check to see if base runners, if so advance them, call IncrementError, and report
        # else do nothing
        pass
    
    def HandleHitByPitchError(self):
        # check to see if base runners, if so advance them, call MoveRunners, and report
        # Batter to First Base
        # update runners on base
        
        # reset balls and strikes to 0
        self.SetBalls(0)
        self.SetStrikes(0)