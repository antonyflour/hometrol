<?php
include_once 'dbConnect.php';
include_once 'check_pincode_function.php';
include_once 'functionSessionStart.php';
include_once 'log_function.php';

if(isset($_COOKIE['known_host'])){
	$username = "user";
	
	if ($stmt = $mysqli->prepare("SELECT pin  FROM users WHERE username = 'user' LIMIT 1")) {
    	$stmt->execute();    // Execute the prepared query.
        $stmt->store_result();
	 	// get variables from result.
        $stmt->bind_result($pin);
        $stmt->fetch();

        if ($stmt->num_rows == 1 and $pin!=null) {
        		
			if(isset($_POST['pass'])){
								
			$pincode = $_POST['pass']; // The hashed pincode.	 
	
			event_log("Tentato accesso da ".$_SERVER['REMOTE_ADDR']."\t tramite pinpad");

    			if (checkPincode($username, $pincode, $mysqli) == true) {
					event_log("Accesso consentito a ".$_SERVER['REMOTE_ADDR']."\t username: ".$username);
					sec_session_start($mysqli, $username, "NO");
					header('Location: /firstUser.php');
				}
				else{
					header('Location: /index.php');
				}
			}
			else{
				header('Location: /index.php');
			}	
							
		}
		else{
			header('Location: /index.php');
		}
	}
	else{
		header('Location: /index.php');
	}
}
else{
	header('Location: /index.php');
}

?>
