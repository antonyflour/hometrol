<?php
include_once 'functionCheckLogin.php';
include_once 'functionHTTP.php';

$code_login = login_check($mysqli);	
if($code_login <1) {
        header('Location: index.php');
}

$mac = $_REQUEST['mac'];
$numero_pin = $_REQUEST['pin'];

?>

<html>
  <head>
    <meta name="viewport" content="width=device-width">
    <title><?php echo "PIN ".$numero_pin ?></title>
    <link rel="stylesheet" href="css/style_first.css"> 
  </head>
  <body>

	 <div class="container">
 	 <div id="div-first">
    	<h3><?php echo "PIN ".$numero_pin ?></h3>
    	<fieldset>	
	<?php
    
    $curl = http_get("http://localhost:8080/shield/".$mac."/pin/".$numero_pin);
    $resp = curl_exec($curl);
    $curl_info = curl_getinfo($curl);
    curl_close($curl);
    if($curl_info['http_code']==200){
    	$pin = json_decode($resp,true);
    	$tipo = $pin['tipo'];
      $usato = $pin['usato'];
      $nome = $pin['nome_pin'];
      echo "mac: ".$mac." numero pin: ".$numero_pin." nome: ".$nome." tipo: ".$tipo." usato: ".$usato;
    }
    else{
      echo "Impossibile recuperare le informazioni del pin";
    }
	?>
	<br>
	<table align=center border=0 cellpadding=3>
	<tr>
    <td><button onClick="location.assign('generalSettings.php');">Impostazioni</button>
    <td><button onClick="location.assign('formAddShield.php');">Aggiungi Scheda</button>
		<td><button onClick="location.assign('logout.php');">Logout</button>
	</table>
    </fieldset>
  </div>
  </div>

  </body>

</html>
