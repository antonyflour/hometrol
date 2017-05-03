<?php

include_once 'functionCheckLogin.php';
include_once 'log_function.php';

$code_login = login_check($mysqli);	

if($code_login != 0) {
	echo "<html><head></head><body><script>alert('Non sei loggato! Password non cambiata!'); location.assign('/index.php');</script></body></html>";
}

if(isset($_POST['password'], $_POST['pincode'])){
	
	if ($stmt = $mysqli->prepare("SELECT password FROM users WHERE username = 'user';")) {
  	
    	$stmt->execute();   
    	$stmt->store_result();
	
		//se l'utente non è stato trovato
    	if ($stmt->num_rows == 0) {
      		echo "<html><head></head><body><script>alert('Utente non trovato! Password non cambiata!'); location.assign('/index.php');</script></body></html>";
    	}
    	else{
    		//recupero la vecchia password
    		$stmt->bind_result($password);
      		$stmt->fetch();
      	
      		if($password==$_POST['password']){
       	 		
       		 	if ($stmt = $mysqli->prepare("UPDATE users SET pin = ? WHERE username = 'user';")) {
          			
          			$stmt->bind_param("s", $_POST['pincode']);
          			$stmt->execute();   
          			$stmt->store_result();
		  			event_log("Pincode cambiato da ".$_SERVER['REMOTE_ADDR']);
          		
          			//effettuo il logout
          			echo "<html><head></head><body><script>alert('Pincode cambiato con successo!'); location.assign('/logout.php');</script></body></html>";
        		}
        		else{
          			echo "<html><head></head><body><script>alert('Impossibile accedere al database per il cambio del pincode! Pincode non cambiato!'); location.assign('/index.php');</script></body></html>";
        		}
      		}
      		else{
        		echo "<html><head></head><body><script>alert('La password inserita non coincide con quella salvata nel database! Pincode non cambiato!'); location.assign('/index.php');</script></body></html>";
      		}
    	}
	}
	else{
    	echo "<html><head></head><body><script>alert('Impossibile accedere al database per il cambio del pincode! Pincode non cambiato!'); location.assign('/index.php');</script></body></html>";
	}
}
else{
    echo "<html><head></head><body><script>alert('Impossibile cambiare il pincode!'); location.assign('/index.php');</script></body></html>";
}

?>


