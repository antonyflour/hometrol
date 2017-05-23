<?php
include_once 'functionCheckLogin.php';
include_once 'functionHTTP.php';
include_once 'stub/stub.php';

$code_login = login_check($mysqli);
if($code_login <1) {
    header('Location: index.php');
}
?>

<html>
<head>
    <meta name="viewport" content="width=device-width">
    <title>Schede collegate</title>
    <link rel="stylesheet" href="css/style_first.css">
    <link href="css/header_and_menu.css" rel="stylesheet" type="text/css" media="screen">
    <script src='http://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js'></script>

</head>
<body>


<!-- HEADER E MENU -->
<div id="container">
    <header>
                <div class="menu">
                    <div class="closeButton"><a class="icon-close"><div id="divButtonClose">&nbsp;</div></a></div>
                    <ul>

                        <li><a href="#">Aggiungi Scheda</a></li>
                        <li><a href="eventsView.php">Eventi</a></li>
                        <li><a href="#">Impostazioni</a></li>
                        <li><a href="#">Logout</a></li>

                    </ul>
                </div>
                <div id="menuButton"><a class="icon-menu"><div id="divButtonMenu">&nbsp;</div></a></div>
        <div id="divHeader"><img id="logo" src="img/icon/main_icon_conscritta.png" /></div>
    </header>
</div>
<script type="text/javascript" src="js/menu_animation.js"></script>


<div class="container">
    <div id="div-first">
        <h3>Schede collegate</h3>
        <fieldset>
            <?php

            ###
            ### GET SHIELDS
            ###
            try{
                $shields = getShields();
                if (empty($shields)) {
                    echo " Non ci sono schede collegate ";
                }
                else{
                    echo "<table border=1 align=center cellpadding=5 cellspacing=0>";
                    echo "<tr class='boldtr'><td>MAC<td>NOME<td>IP<td>PORTA";
                    foreach($shields as $shield){
                        $mac = $shield->getMac();
                        $nome = $shield->getNome();
                        $ip = $shield->getIp();
                        $port = $shield->getPort();
                        echo "<br>";
                        echo "<tr><td><a href='shieldAdmin.php?mac=".$mac."'>".$mac."</a><td class='boldtd'>".$nome."<td>".$ip."<td>".$port;
                    }
                }
                echo "</table>";
            }
            catch (Exception $e){
                echo $e->getMessage();
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
