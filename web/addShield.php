<?php
include_once 'functionCheckLogin.php';
include_once 'functionHTTP.php';

$code_login = login_check($mysqli);	
if($code_login <1) {
        header('Location: index.php');
}

$ip = $_REQUEST['ip'];
$port = $_REQUEST['port'];


$payload['ip_shield'] = $_REQUEST['ip'];
$payload['port_shield'] = $_REQUEST['port'];

	$curl = http_post("http://localhost:8080/shield", "application/json", json_encode($payload));
	$resp = curl_exec($curl);
	$curl_info = curl_getinfo($curl);
	curl_close($curl);
	if($curl_info['http_code']==200){
		echo "<html><head></head><body><script>alert('Configurazione completata correttamente');location.assign('index.php');</script></body></html>";
	}
	else{
		echo "<html><head></head><body><script>alert('errore: ".$curl_info['http_code']."');location.assign('index.php');</script></body></html>";
	}
?>
