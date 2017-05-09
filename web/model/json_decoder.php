<?php
/**
 * Created by PhpStorm.
 * User: anton
 * Date: 02/05/2017
 * Time: 21:19
 */

include_once 'shield.php';
include_once 'pin.php';
include_once 'evento.php';
include_once 'pinStateAlterationCondition.php';
include_once 'emailNotifyAction.php';

function json_decode_shields_array($json_string){
    $tot_assoc_array = json_decode($json_string, true);

    $shields = array();

    foreach($tot_assoc_array as $assoc_array){

        array_push($shields, json_decode_shield($assoc_array));
    }

    return $shields;
}

function json_decode_shield($json_string){
    //se l'argomento è la stringa json la decodifico, altrimenti utilizzo direttamente come array associativo
    if(is_array($json_string))
        $assoc_array = $json_string;
    else
        $assoc_array = json_decode($json_string, true);

    $mac = $assoc_array['mac'];
    $nome_shield = $assoc_array['nome'];
    $ip = $assoc_array['ip'];
    $port = $assoc_array['port'];

    $input_pins_array = json_decode_pins_array($assoc_array['input_pin']);

    $output_pins_array = json_decode_pins_array($assoc_array['output_pin']);

    return new Shield($mac, $nome_shield, $ip, $port, $input_pins_array, $output_pins_array);
}

function json_decode_pins_array($json_string){
    $pins = json_decode($json_string,true);
    $pins_array = array();

    foreach($pins as $pin){
        $numero_pin = $pin['numero_pin'];
        $tipo = $pin['tipo'];
        $nome = $pin['nome_pin'];
        $usato = $pin['usato'];
        $out_mode = $pin['out_mode'];
        $in_mode = $pin['in_mode'];
        $input_status = $pin['stato'];

        array_push($pins_array, new Pin($numero_pin, $tipo, $nome, $usato, $out_mode, $in_mode, $input_status));
    }

    return $pins_array;
}

function json_decode_events_array($json_string){
    $tot_assoc_array = json_decode($json_string, true);

    $events = array();

    foreach($tot_assoc_array as $assoc_array){

        array_push($events, json_decode_event($assoc_array));
    }

    return $events;
}

function json_decode_event($json_string){
    //se l'argomento è la stringa json la decodifico, altrimenti utilizzo direttamente come array associativo
    if(is_array($json_string))
        $assoc_array = $json_string;
    else
        $assoc_array = json_decode($json_string, true);

    $id = $assoc_array['id'];
    $interval = $assoc_array['repetitionInterval'];
    $enabled = $assoc_array['enabled'];
    $lastExecTime = $assoc_array['last_exec_time'];

    $condition_type = $assoc_array['condition_type'];
    $action_type = $assoc_array['action_type'];

    $condition = NULL;
    if($condition_type == PinStateAlterationCondition::class){
        $condition = json_decode_pinStateAlterationCondition($assoc_array['condition']);
    }

    $action = NULL;
    if($action_type == EmailNotifyAction::class){
        $action = json_decode_emailNotifyAction($assoc_array['action']);
    }

    return new Evento($id, $enabled, $lastExecTime, $interval, $condition, $action);
}

function json_decode_pinStateAlterationCondition($json_string){
    if(is_array($json_string))
        $assoc_array = $json_string;
    else
        $assoc_array = json_decode($json_string, true);

    $id = $assoc_array['id'];
    $mac = $assoc_array['mac_shield'];
    $pin = $assoc_array['pin_number'];
    $expected_state = $assoc_array['expected_state'];

    return new PinStateAlterationCondition($id, $mac, $pin, $expected_state);
}

function json_decode_emailNotifyAction($json_string){
    if(is_array($json_string))
        $assoc_array = $json_string;
    else
        $assoc_array = json_decode($json_string, true);

    $id = $assoc_array['id'];
    $email = $assoc_array['email'];
    $msg = $assoc_array['msg'];

    return new EmailNotifyAction($id, $email, $msg);

}