# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 23:10:19 2017

@author: swill_000
"""

import tkinter as tk
import time

class myClockApp( tk.Tk ):
    def __init__( self, content ):
        tk.Tk.__init__( self )

        container = tk.Frame( self )
        container.pack( side='top', fill='both', expand=True )
        container.grid_rowconfigure( 0, weight=1 )
        container.grid_columnconfigure( 0, weight=1 )
        
        self.frames={}

        for F in content:
            frame = F( container, self )
            self.frames[F] = frame
            frame.grid( row=0, column=0, sticky='nsew' )
            
        self.mainloop()
        
    def show_frame( self, cont ):
        self.frames[ cont ].tkraise()
        
class ClockPage( tk.Frame ):
    
    def __init__( self, parent, controller ):
        tk.Frame.__init__( self, parent )
        self.clock = tk.Label( self, text='' )
#        self.clock.grid( row=0, column=0, sticky='nsew' )
        self.clock.pack()
        self.update_page()
        
    def update_page( self ):
        now = time.strftime('%H:%M:%S')
        self.clock.configure( text=now )
        self.master.after( 100, self.update_page )
        
class TripleStatBar( tk.Frame ):
    def __init__( self, parent, controller ):
        tk.Frame.__init__( self, parent )
        self._statframes = dict()
        self.statlabels = dict()
        for i in range(3):
#            print(type(i))
            self._statframes[i] = tk.Frame( self, parent )
            self._statframes[i].grid( row=0, column=i, sticky='ew' )
            self.statlabels[i] = tk.Label( self, text='Label{}'.format(i) )
            self.statlabels[i].grid()
            
        self.update_page()
            
    def update_page( self ):
        now = dict()
        for i,e in enumerate( [ '%H','%M','%S' ] ):
#            print(type(i))
            now = time.strftime( e )
            self.statlabels[i].configure( text=now )
            self.master.after( 100, self.update_page )
            
tstAPP = myClockApp( [ ClockPage ] )