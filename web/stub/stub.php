<?php
/**
 * Created by PhpStorm.
 * User: anton
 * Date: 02/05/2017
 * Time: 19:54
 */

include_once dirname(__DIR__).'../functionHTTP.php';
include_once dirname(__DIR__).'../commons/urls.php';
include_once dirname(__DIR__).'../model/json_decoder.php';

function getShields() {
    try{
        $resp = http_get(URL_GET_SHIELDS);
        $shields = json_decode_shields_array($resp);
        return $shields;
    } catch (Exception $e){
        throw new Exception("Impossibile recuperare le schede");
    }
}

function getShield($mac) {
    try{
        $resp = http_get(URL_GET_SHIELD.$mac);
        $shield = json_decode_shield($resp);
        return $shield;
    } catch (Exception $e){
        throw new Exception("Impossibile recuperare la scheda");
    }
}

