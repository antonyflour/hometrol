<?php
	include_once 'functionCheckLogin.php';
	include_once 'functionHTTP.php';
	$code_login = login_check($mysqli);	
	if($code_login <1) {
		header('Location: index.php');
	}
	$mac = $_REQUEST['mac'];
	
	
	$curl = http_delete("http://localhost:8080/shield/".$mac);
	$resp = curl_exec($curl);
	$curl_info = curl_getinfo($curl);
	curl_close($curl);
	if($curl_info['http_code']==200){
		header('Location: firstAdmin.php'); 
	}
	else{
		echo "<html><head></head><body><script>alert('impossibile rimuovere la scheda');</script></body></html>";
	}
	  
?>
