<?php
/**
 * Created by PhpStorm.
 * User: anton
 * Date: 02/05/2017
 * Time: 19:54
 */

include_once 'functionHTTP.php';
include_once 'urls.php';
include_once 'json_decoder.php';

function getShields() {
    try{
        $resp = http_get(URL_GET_SHIELDS);
        $shields = json_decode_shields_array($resp);
        return $shields;
    } catch (Exception $e){
        throw new Exception("Impossibile recuperare le schede");
    }
}

