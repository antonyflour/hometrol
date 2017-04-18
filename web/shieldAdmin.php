<?php
include_once 'functionCheckLogin.php';
include_once 'functionHTTP.php';

$code_login = login_check($mysqli);	
if($code_login <1) {
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
		echo "<head><meta name='viewport' content='width=device-width'><title>".$nome_scheda."</title><link rel='stylesheet' href='css/style_shield.css'><script type='text/JavaScript' src='js/change_state.js'></script> </head>";
  	echo "<body><div class='container' align=center><div id='shield-div'><h3>".$nome_scheda."</h3><fieldset>";
		
		//costruisco la tabella html 
		echo "<table border=1 align=center cellpadding=5 cellspacing=0>";
    echo "<tr class='boldtr'><td colspan=6>INPUT";
    echo "<tr class='boldtr'><td>N.<td>NOME<td>USATO<td>TIPO<td colspan=2>STATO";
		
		//recupero i pin di input
		$input_pins = json_decode($shield['input_pin'],true);
		foreach($input_pins as $pin){
			$input_status = $pin['stato'];
			$numero_pin = $pin['numero_pin'];
			$nome = $pin['nome_pin'];
			$usato = $pin['usato'];
			$input_type = $pin['in_mode'];
			
			if($input_status == 1){
				if($input_type == "NL"){
					$str_status="ON";
				}
				else{
					$str_status="OFF";
				}
			}
			else{
				if($input_type=="NL"){
					$str_status="OFF";
				}
				else{
					$str_status="ON";
				}
			}
			echo "<tr>";
			echo "<td>".$numero_pin."<td class='boldtd'><a href='pinView.php?mac=".$mac."&pin=".$numero_pin."'>".$nome."</a><td> ".$usato."<td>".$input_type;
			if($str_status=="OFF"){
				echo "<td colspan=2 class='offtd'>";
			}
			else{
				echo "<td colspan=2 class='ontd'>";
			}
			echo $str_status;
		}
		
		//tabella html
		echo "<tr class='boldtr'><td colspan=6>OUTPUT";
    echo "<tr class='boldtr'><td>N.<td>NOME<td>USATO<td>TIPO<td>STATO<td>AZIONE";
		
		//recupero i pin di output
		$output_pins = json_decode($shield['output_pin'],true);
		foreach($output_pins as $pin){
			$output_status = $pin['stato'];
			$numero_pin = $pin['numero_pin'];
			$nome = $pin['nome_pin'];
			$usato = $pin['usato'];
			$out_mode = $pin['out_mode'];
			
			if($out_mode=="HL"){
				if($output_status == 1){
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
			echo "<td>".$numero_pin."<td class='boldtd'><a href='pinView.php?mac=".$mac."&pin=".$numero_pin."'>".$nome."</a><td>".$usato."<td>".$out_mode;
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
			echo "<td align=center><button onClick='changeState(\"".$mac."\",".$numero_pin.",".$cmd_azione.")'>".$str_azione."</button>";
							
		}
		
		//concludo la tabella
		echo "</table>";
		echo "<br><br>";
		echo "<table align=center><tr>";
		echo "<td><button onClick=\"location.assign('shieldSettings.php?mac=".$mac."&nome=".$nome_scheda."')\">Impostazioni Scheda</button>";
		echo "</table>";
	}
	else{
		echo "<div align=center>Impossibile recuperare la scheda</div>";

	}

?>
	<br>
	<table align=center>
	<tr>
	<td><button onClick="location.assign('firstAdmin.php')">Torna a Schede</button>
	<td><button onClick="location.assign('deleteShield.php?mac=<?php echo $mac ?>')">Elimina scheda</button></td></tr>
	</table>
	</fieldset>
 	</div>
</div>
</body>
</html>
