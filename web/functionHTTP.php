<?php

function http_get($url) {
    $curl = curl_init();
		curl_setopt_array($curl, array(
    		CURLOPT_RETURNTRANSFER => 1,
    		CURLOPT_URL => $url,
				CURLOPT_USERAGENT => 'Raspberry',
				CURLOPT_TIMEOUT => 5));
    return $curl;
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
    return $curl;
}

?>

