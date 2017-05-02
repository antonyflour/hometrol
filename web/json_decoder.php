<?php
/**
 * Created by PhpStorm.
 * User: anton
 * Date: 02/05/2017
 * Time: 21:19
 */

function json_decode_shields_array($json_string){
    $assoc_array = json_decode($json_string, true);

    $shields = array();

    foreach($assoc_array as $field){
        $mac = $field['mac'];
        $nome = $field['nome'];
        $ip = $field['ip'];
        $port = $field['port'];

        array_push($shields, new Shield($mac, $nome, $ip, $port, NULL, NULL));
    }

    return $shields;
}

function json_decode_shield($json_string){
    $assoc_array = json_decode($json_string, true);
    $mac = $assoc_array['mac'];
    $nome = $assoc_array['nome'];
    $ip = $assoc_array['ip'];
    $port = $assoc_array['port'];

    return new Shield($mac, $nome, $ip, $port, NULL, NULL);
}