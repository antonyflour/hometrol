<?php
include_once 'functionCheckLogin.php';
include_once 'functionHTTP.php';

$code_login = login_check($mysqli);	
if($code_login <0) {
        header('Location: index.php');
}
?>

<html>
  <head>
    <meta name="viewport" content="width=device-width">
    <title>Schede collegate</title>
    <link rel="stylesheet" href="css/style_first.css"> 
  </head>
  <body>

	 <div class="container">
 	 <div id="div-first">
    	<h3>Schede collegate</h3>
    	<fieldset>	
	<?php
  
    ###
    ### GET SHIELDS
    ###
    $curl = http_get("http://localhost:8080/shields");
		$resp = curl_exec($curl);
		$curl_info = curl_getinfo($curl);
		curl_close($curl);
		if($curl_info['http_code']==200){
			$shields = json_decode($resp,true);
        if (empty($shields)) {
          echo " Non ci sono schede collegate ";
        }
        else{
          echo "<table class='tableuser' border=1 align=center cellpadding=5 cellspacing=0>";
          echo "<tr class='boldtr'><td>NOME";
          foreach($shields as $shield){
            $mac = $shield['mac'];
            $nome = $shield['nome'];
            echo "<tr><td><a href='shieldUser.php?mac=".$mac."'>".$nome;
          }            
        }
		echo "</table>";
	}
	else{
		echo "Impossibile recuperare le schede";
	}
	?>
	<br>
	<table align=center border=0 cellpadding=3>
	<tr>
    <td><button onClick="location.assign('generalSettings.php');">Impostazioni</button>
		<td><button onClick="location.assign('logout.php');">Logout</button>
	</table>
  </div>
  </div>

  </body>

</html>
