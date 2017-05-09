<?php

function http_get($url) {
    $curl = curl_init();
    curl_setopt_array($curl, array(
        CURLOPT_RETURNTRANSFER => 1,
        CURLOPT_URL => $url,
        CURLOPT_USERAGENT => 'Raspberry',
        CURLOPT_TIMEOUT => 5));
    $resp = curl_exec($curl);
    $curl_info = curl_getinfo($curl);
    curl_close($curl);
    if($curl_info['http_code']==200) {
        return $resp;
    }
    else {
        throw new Exception("HTTP GET Exception");
    }
}

function http_post($url, $content_type, $content) {
    $curl = curl_init();
    curl_setopt_array($curl, array(
        CURLOPT_RETURNTRANSFER => 1,
        CURLOPT_POST => 1,
        CURLOPT_URL => $url,
        CURLOPT_USERAGENT => 'Raspberry',
        CURLOPT_TIMEOUT => 5,
        CURLOPT_HTTPHEADER => array('content-type: '.$content_type),
        CURLOPT_POSTFIELDS => $content));
    return $curl;
}

function http_delete($url){
    $curl = curl_init();
    curl_setopt_array($curl, array(
        CURLOPT_RETURNTRANSFER => 1,
        CURLOPT_CUSTOMREQUEST => "DELETE",
        CURLOPT_URL => $url,
        CURLOPT_USERAGENT => 'Raspberry',
        CURLOPT_TIMEOUT => 5));
    $resp = curl_exec($curl);
    $curl_info = curl_getinfo($curl);
    curl_close($curl);
    if($curl_info['http_code']==200) {
        return $resp;
    }
    else {
        throw new Exception("HTTP GET Exception");
    }
}

?>

