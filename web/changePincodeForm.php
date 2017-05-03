<?php
include_once 'functionCheckLogin.php';

$code_login = login_check($mysqli);	
if($code_login !=0) {
        header('Location: /index.php');
}
?>

<!DOCTYPE html>
<html>
	<head>
		<meta name="viewport" content="width=device-width">
		<title>Cambia Password</title>

		<link rel="stylesheet" href="css/style_form_change_password.css" />
		<link rel="stylesheet" href="css/style_pinpad.css" />

		<script src="js/changePIN.js"></script>
		<script type="text/JavaScript" src="js/sha512.js"></script>
		<script src="js/pinpad.js"></script>
		<script src='http://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js'></script>

		<script>
			var password;
			var pincode1;
			var pincode2;

		</script>
		
	</head>
	<body>
		<div class="container">
			<div id="changepass-form">
				<h3>Passo 1 : Inserisci la password attuale</h3>
				<fieldset id='fieldsetPassword'>
					<form action="/changePincode.php" method="post" name="change_form" id="change_form">
						<input type="hidden" name="username" value="">
						<table align=center border=0 cellpadding=5>
							<tr>
								<td>Inserisci password</td><td>
								<input type="password" id="pass">
								</td>
							<tr>
								<td colspan=2>
								<input type="button" value="Cambia" onclick="hidePassword()">
								</td>
						</table>
					</form>
				</fieldset>
			</div>

			<div id="pinpad-div">
				<h3 id = 'h3pinpad'>Passo 2 : inserisci PIN</h3>
				<fieldset>

					<form name='PINform' id='PINform' autocomplete='off' draggable='true'>
						<table border="0" align="center">
							<tr>
								<td colspan="3" style="padding-bottom: 20px;">
								<input id='PINbox' type='password' value='' name='PINbox' disabled/>
							</tr>
							<tr>

								<td>
								<input type='button' class='PINbutton' name='1' value='1' id='1' onClick=addNumber(this); />
								<td>
								<input type='button' class='PINbutton' name='2' value='2' id='2' onClick=addNumber(this); />
								<td>
								<input type='button' class='PINbutton' name='3' value='3' id='3' onClick=addNumber(this); />
							</tr>
							<tr>
								<td>
								<input type='button' class='PINbutton' name='4' value='4' id='4' onClick=addNumber(this); />
								<td>
								<input type='button' class='PINbutton' name='5' value='5' id='5' onClick=addNumber(this); />
								<td>
								<input type='button' class='PINbutton' name='6' value='6' id='6' onClick=addNumber(this); />
							</tr>
							<tr>
								<td>
								<input type='button' class='PINbutton' name='7' value='7' id='7' onClick=addNumber(this); />
								<td>
								<input type='button' class='PINbutton' name='8' value='8' id='8' onClick=addNumber(this); />
								<td>
								<input type='button' class='PINbutton' name='9' value='9' id='9' onClick=addNumber(this); />
							</tr>
							<tr>
								<td>
								<input type='button' class='PINbutton clear' name='-' value='clear' id='-' onClick=clearForm(this); />
								<td>
								<input type='button' class='PINbutton' name='0' value='0' id='0' onClick=addNumber(this); />
								<td>
								<input type='button' class='PINbutton enter' name='+' value='enter' id='+' onClick=insertPincode(); />
							</tr>
						</table>
					</form>

				</fieldset>
			</div>
			<script>
				$('#pinpad-div').hide();

				$('#change_form').on('keypress', function(e) {
					return e.which !== 13;
				});

			</script>

		</div>
	</body>
</html>
