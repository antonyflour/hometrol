<?php

	include_once 'functionHTTP.php';

	$curl = http_get("http://localhost:8080/shield/90-A2-DA-10-21-A9");
	$resp = curl_exec($curl);
	$curl_info = curl_getinfo($curl);
	curl_close($curl);
	if($curl_info['http_code']==200){
			echo $resp;
			echo "<br><br>";
			$shields = json_decode($resp,true);
			if( !empty($shields)){
				$output_pin = json_decode($shields['output_pin'],true);
				foreach($output_pin as $pin){
					echo $pin['nome_pin'].":".$pin['stato']."<br>";
				}
				
				$input_pin = json_decode($shields['input_pin'],true);
				foreach($input_pin as $pin){
					echo $pin['nome_pin'].":".$pin['stato']."<br>";
				}
				/*foreach($shields as $shield){
				echo $shield['mac'];
				echo $shield['nome'];
				echo "<br>";
				}
				*/
			}
			else{
				echo "nessuna scheda";
			}
		}
		else{
			echo "nessuna risposta";
			
		}

?>

