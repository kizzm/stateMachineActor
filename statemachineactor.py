# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 20:29:34 2017

@author: swill_000
"""

import pykka
import tkinter as tk

class instrumentBackend( pykka.ThreadingActor ):
    
    def __init__( self, *args, **kwargs ):
        super( instrumentBackend, self ).__init__()
        
    def on_receive( self, message ):
        if message.get( 'command' ) =='start':
            pass
        elif message.get( 'command' ) =='stop':
            pass
        elif message.get( 'command' ) =='send':
            self.send()
            
    def send( self ):
        pass
    
class instrumentFrontend( pykka.ThreadingActor ):
    
    def __init__( self, *args, **kwargs ):
        super( instrumentFrontend, self ).__init__()
        
    def on_receive( self, message ):
        if message.get( 'command' ) == 'start':
            pass
        elif message.get( 'command' ) == 'stop':
            pass
#        elif message.get( 'command' ) == '':
#            pass
            
class myApp( tk.Tk ):
    
    def __init__( self, content, text, *args, **kwargs ):
        tk.Tk.__init__( self, *args, **kwargs )
        
        container = tk.Frame( self )        
        container.pack( side='top', fill='both', expand=True )
        container.grid_rowconfigure( 0, weight=1 )
        container.grid_columnconfigure( 0, weight=1 )
        
        self.frames={}
        
        for F in content:
            frame = F( container, self, text )
            self.frames[F] = frame
            frame.grid( row=0, column=0, sticky='nsew' )
            
        self.show_frame( content[0] )
        
    def show_frame( self, cont ):
        self.frames[cont].tkraise()

        
class StartPage( tk.Frame ):
    
    def __init__( self, parent, controller, text ):
        tk.Frame.__init__( self, parent )
        
        label = tk.Label( self, variable='Start Page' )
        label.pack( pady=10, padx=10 )
        