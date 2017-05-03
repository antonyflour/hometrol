<?php
include_once 'functionCheckLogin.php';

$admin_code = login_check($mysqli);
if ($admin_code >=0) {
    if($admin_code==1){
        header('Location: firstAdmin.php');
    }
    else{
        header('Location: firstUser.php');
    }
}
?>
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width">
    <title>Login</title>
    <link rel="stylesheet" href="css/style_login.css" />
    <link href="css/header_and_menu.css" rel="stylesheet" type="text/css" media="screen">
    <script type="text/JavaScript" src="js/sha512.js"></script>
    <script type="text/JavaScript" src="js/forms.js"></script>
    <script src='http://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js'></script>
    <!--<script type="text/javascript" src="js/jquery-1.11.1.min.js"></script>-->

</head>
<body>
<script>
    function setUsername(value) {
        $("#username").value = value;
        $("#div-username").hide();
        $("#h3title").text("Inserisci password per: "+value);
        $("#div-password").show();
    }

</script>

<!-- HEADER E MENU -->
<div id="container">
    <header>
<!--        <div class="menu">-->
<!--            <div class="closeButton"><a class="icon-close"><div id="divButtonClose">&nbsp;</div></a></div>-->
<!--            <ul>-->
<!---->
<!--                <li><a href="#">Home</a></li>-->
<!--                <li><a href="#">Running</a></li>-->
<!--                <li><a href="#">Percorsi</a></li>-->
<!--                <li><a href="#">Allenamenti</a></li>-->
<!--                <li><a href="#">Alimentazione</a></li>-->
<!--                <li><a href="#">Contattaci</a></li>-->
<!---->
<!--            </ul>-->
<!--        </div>-->
<!--        <div id="menuButton"><a class="icon-menu"><div id="divButtonMenu">&nbsp;</div></a></div>-->
        <div id="divHeader"><img id="logo" src="img/icon/smarthome_icon_conscritta.png" /></div>
    </header>
</div>
<script type="text/javascript" src="js/menu_animation.js"></script>

<div class="container">
    <div id="login-form">
        <h3 id="h3title">Accedi come: </h3>
        <fieldset>
            <form action="processLogin.php" method="post" name="login_form" id="login_form">
                <input type="hidden" id="username">
                <div align="center" id="div-username">
                    <input type="button" value="ADMIN" onclick="setUsername('admin')">
                    <br>
                    <input type="button" value="USER" onclick="setUsername('user')">
                </div>

                <div align="center" id="div-password">
                    <input type="password" name="password" required value="Password" onBlur="if(this.value=='')this.value='Password'" onFocus="if(this.value=='Password')this.value='' ">
                    <input type="button" value="Login" onclick="formhash(this.form, this.form.password);" />
                </div>

                <script> $("#div-password").hide(); </script>
            </form>
        </fieldset>
    </div>
</div>
</body>
</html>
