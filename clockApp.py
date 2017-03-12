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
        self.clock.pack( pady=10, padx=10 )
        self.update_page()
        
    def update_page( self ):
        now = time.strftime('%H:%M:%S')
        self.clock.configure( text=now )
        self.master.after( 100, self.update_page )
        
tstAPP = myClockApp( [ ClockPage ] )