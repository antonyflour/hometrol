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
    <title>Eventi registrati</title>
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

                        <li><a href="#">Aggiungi Evento</a></li>
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
        <h3>Eventi registrati</h3>
        <fieldset>
            <?php

            ###
            ### GET SHIELDS
            ###
            try{
                $events = getEvents();
                if (empty($events)) {
                    echo " Nessun evento registrato ";
                }
                else{
                    echo "<table border=1 align=center cellpadding=5 cellspacing=0>";
                    echo "<tr class='boldtr'><td>ID<td>INTERVALLO RIPETIZIONE<td>ABILITATO<td>ULTIMA ESECUZIONE";
                    foreach($events as $event){
                        $id = $event->getId();
                        $interval = $event->getRepetitionInterval();
                        $enabled = $event->getEnabled();
                        $lastExecTime = $event->getLastExecTime();
                        echo "<br>";
                        echo "<tr><td>".$id."<td>".$interval."<td>".$enabled."<td>".$lastExecTime;
                    }
                }
                echo "</table>";
            }
            catch (Exception $e){
                echo $e->getMessage();
            }

            ?>
        </fieldset>
    </div>
</div>

</body>

</html>
