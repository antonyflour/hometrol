<?php
include_once 'functionCheckLogin.php';
include_once 'functionHTTP.php';

$code_login = login_check($mysqli);	
if($code_login <0) {
        header('Location: index.php');
}

$mac = $_REQUEST['mac'];
$curl = http_get("http://localhost:8080/shield/".$mac);
$resp = curl_exec($curl);
$curl_info = curl_getinfo($curl);
curl_close($curl);
if($curl_info['http_code']==200){
	$shield = json_decode($resp,true);
	$mac = $shield['mac'];
  $nome_scheda = $shield['nome'];
		
	//costruisco l'intestazione della pagina
	echo "<html>";
	echo "<head><meta name='viewport' content='width=device-width'><title>".$nome_scheda."</title><link rel='stylesheet' href='css/style_shield.css?".(date('l jS \of F Y h:i:s A'))."'><script type='text/JavaScript' src='js/change_state.js'></script> </head>";
  echo "<body><div class='container' align=center><div id='shield-div'><h3>".$nome_scheda."</h3><fieldset>";
			
	//costruisco la tabella html
	echo "<table border=1 align=center cellpadding=5 cellspacing=0>";
	echo "<tr class='boldtr'><td colspan=3>DISPOSITIVI";
	echo "<tr class='boldtr'><td>NOME<td>STATO<td>AZIONE";

	//recupero le informazioni sui pin di input
	$input_array=array();
	$input_pins = json_decode($shield['input_pin'],true);
	foreach($input_pins as $pin){
		$input_status = $pin['stato'];
		$numero_pin = $pin['numero_pin'];
		$nome = $pin['nome_pin'];
		$usato = $pin['usato'];
		$input_type = $pin['in_mode'];
			
		if($usato=="YES" or $usato=="SI"){
			$tmp_array=array();
			$tmp_array["type"] = "I";
			$tmp_array["input_pin"]=$numero_pin;
			$tmp_array["input_type"]=$input_type;
			$tmp_array["input_status"]=$input_status;
								
			$input_array[$nome]=$tmp_array;
		}
	}
						
	//recupero le informazioni sui pin di output	
	$output_array=array();
	$output_pins = json_decode($shield['output_pin'],true);
	foreach($output_pins as $pin){
		$output_status = $pin['stato'];
		$numero_pin = $pin['numero_pin'];
		$nome = $pin['nome_pin'];
		$usato = $pin['usato'];
		$out_mode = $pin['out_mode'];
			
		if($usato=="YES" or $usato=="SI"){
			$tmp_array=array();
			$tmp_array["type"] = "O";
			$tmp_array["output_pin"]=$numero_pin;
			$tmp_array["output_mode"]=$out_mode;
			$tmp_array["output_status"]=$output_status;
			$output_array[$nome]=$tmp_array;
		}
	}
						
	$dispositivi=array();
	//analizzo l'array dei pin di input
	foreach($input_array as $key => $value){
		$dispositivo=array();
		$dispositivo["type"]="I";
		$dispositivo["input_pin"]=$value["input_pin"];
		$dispositivo["input_type"]=$value["input_type"];
		$dispositivo["input_status"]=$value["input_status"];
	
		//se tra i pin di output è presente un pin con lo stesso nome ($key)
		if($output_array[$key]!=null){
			$dispositivo["type"]="IO";
			$output_info=$output_array[$key];
			$dispositivo["output_pin"]=$output_info["output_pin"];
			$dispositivo["output_mode"]=$output_info["output_mode"];
			$dispositivo["output_status"]=$output_info["output_status"];
		  unset($output_array[$key]);
		}
	
		$dispositivi[$key]=$dispositivo;
	}
						
	//analizzo l'array dei pin di output rimasti
	foreach($output_array as $key => $value){
		$dispositivo=array();
		$dispositivo["type"]="O";
		$dispositivo["output_pin"]=$value["output_pin"];
		$dispositivo["output_mode"]=$value["output_mode"];
		$dispositivo["output_status"]=$value["output_status"];
		$dispositivi[$key]=$dispositivo;
	}
						
	//ordino in base al nome
	ksort($dispositivi);
	
	//costruisco la tabella
	foreach($dispositivi as $key => $dispositivo){
							
		//dispositivo che ha sia pin di input che di output
		if($dispositivo["type"]=="IO"){
			if($dispositivo["input_status"]==1){
				if($dispositivo["input_type"]=="NL"){
					$str_status="ON";
				}
				else{
					$str_status="OFF";
				}
			}
			else{
				if($dispositivo["input_type"]=="NL"){
					$str_status="OFF";
				}
				else{
					$str_status="ON";
				}
			}
		
			if($dispositivo["output_mode"]=="HL"){
				if($str_status=="ON"){
					$str_azione="SPEGNI";
					$cmd_azione=0;
				}
				else{
					$str_azione="ACCENDI";
					$cmd_azione=1;
				}
			}
			else{
				$str_azione="TOGGLE";
				$cmd_azione=2;
			}
			
			echo "<tr>";
			echo "<td class='boldtd'>".$key;
			
			if($str_status=="OFF"){
				echo "<td class='offtd'>";
			}
			else if($str_status=="ON"){
				echo "<td class='ontd'>";
			}
			
			echo $str_status;
			echo "<td align=center><button onClick='changeState(\"".""."\","."".",".$dispositivo["output_pin"].",".$cmd_azione.")'>".$str_azione."</button>";
								
		}
		
		//dispositivo che ha solo un pin di input
		elseif($dispositivo["type"]=="I"){
			if($dispositivo["input_status"]==1){
				if($dispositivo["input_type"]=="NL"){
					$str_status="ON";
				}
				else{
					$str_status="OFF";
				}
			}
			else{
				if($dispositivo["input_type"]=="NL"){
					$str_status="OFF";
				}
				else{
					$str_status="ON";
				}
			}
			
			echo "<tr>";
			echo "<td class='boldtd'>".$key;
			
			if($str_status=="OFF"){
				echo "<td class='offtd' colspan='2'>";
			}
			else if($str_status=="ON"){
				echo "<td class='ontd' colspan='2'>";
			}
			echo $str_status;
		}
		
		//dispositivo che ha solo un pin di output
		elseif($dispositivo["type"]=="O"){
			if($dispositivo["output_mode"]=="HL"){
				if($dispositivo["output_status"]==1){
					$str_status="ON";
					$str_azione="SPEGNI";
					$cmd_azione=0;
				}
				else{
					$str_status="OFF";
					$str_azione="ACCENDI";
					$cmd_azione=1;
				}
			}
			else{
				$str_status = "ND";
				$str_azione="TOGGLE";
				$cmd_azione=2;
			}
		
			echo "<tr>";
			echo "<td class='boldtd'>".$key;
			
			if($str_status=="OFF"){
				echo "<td class='offtd'>";
			}
			else if($str_status=="ON"){
				echo "<td class='ontd'>";
			}
			else{
				echo "<td>";
			}
			
			echo $str_status;
			echo "<td align=center><button onClick='changeState(\"".$mac."\",".$dispositivo["output_pin"].",".$cmd_azione.")'>".$str_azione."</button>";
		}
	}
						
	//concludo la tabella
	echo "</table>";

}
else{
	echo "<div align=center>Impossibile recuperare la scheda</div>";
}

?>
	<br>
		<table class='tablebutton'>
			<tr>
				<td><button onClick="location.assign('/firstUser.php');">Indietro</button>
				<td></td>
				<td><button onClick="location.reload();">Ricarica</button>
		</table>
	</fieldset>
 	</div>
</div>
</body>
</html>
