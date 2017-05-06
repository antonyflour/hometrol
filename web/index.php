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
        $("#username").val(value);
        $("#div-username").hide();
        $("#h3title").text("Inserisci password per: "+value);
        $("#div-password").show();
    }

    function back() {
        $("#div-password").hide();
        $("#div-username").show();
        $("#h3title").text("Accedi come:");
    }

</script>

<!-- HEADER E MENU -->
<div id="container">
    <header>
        <div id="divHeader"><img id="logo" src="img/icon/main_icon_conscritta.png" /></div>
    </header>
</div>
<script type="text/javascript" src="js/menu_animation.js"></script>

<div class="container">
    <div id="login-form">
        <h3 id="h3title">Accedi come: </h3>
        <fieldset>
            <form action="processLogin.php" method="POST" name="login_form" id="login_form">
                <input name = "username" type="hidden" id="username">
                <div align="center" id="div-username">
                    <input type="button" value="ADMIN" onclick="setUsername('admin')">
                    <br>
                    <input type="button" value="USER" onclick="setUsername('user')">
                </div>

                <div align="center" id="div-password">
                    <input type="password" name="password" required value="Password" onBlur="if(this.value=='')this.value='Password'" onFocus="if(this.value=='Password')this.value='' ">
                    <input type="submit" value="Login" onclick="formhash(this.form, this.form.password);" />
                    <input type="button" value="Indietro" onclick="back();" />
                </div>

                <script> $("#div-password").hide(); </script>
            </form>
        </fieldset>
    </div>
</div>
</body>
</html>
