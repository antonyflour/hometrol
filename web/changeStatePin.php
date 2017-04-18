<?php
include_once 'functionCheckLogin.php';
include_once 'functionHTTP.php';

$admin_code = login_check($mysqli);
if ($admin_code >=0) {
	$mac = $_REQUEST['mac'];
	$pin = $_REQUEST['pin'];
	$stato = $_REQUEST['stato'];
	
	$payload['stato'] = $stato;
	$curl = http_post("http://localhost:8080/shield/".$mac."/pin/".$pin."/state", "application/json", json_encode($payload));
	$resp = curl_exec($curl);
	$curl_info = curl_getinfo($curl);
	curl_close($curl);
	if($curl_info['http_code']==200){
		http_response_code(200);
	}
	else{
		http_response_code(405);
	}
}else{
	http_response_code(405);
}

?>
