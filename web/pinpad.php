
<!DOCTYPE html>
<html>
    <head>
	<meta name="viewport" content="width=device-width">
        <title>Login</title>
        <link rel="stylesheet" href="css/style_pinpad.css" />
        <script type="text/JavaScript" src="js/sha512.js"></script> 
        <script type="text/JavaScript" src="js/forms.js"></script> 
        <script src="js/pinpad.js"></script>
        <script src='http://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js'></script>
        
    </head>
    <body>
	<div class="container">
	<div id="pinpad-div">
	<h3>Raspuino System</h3>
	<fieldset>
		
		<form action='/processLoginPincode.php' method='post' name='PINform' id='PINform' autocomplete='off' draggable='true'>
			<table border="0" align="center">
				<tr>
					<td colspan="3" style="padding-bottom: 20px;"><input id='PINbox' type='password' value='' name='PINbox' disabled/>
				</tr>
				<tr>
				
					<td><input type='button' class='PINbutton' name='1' value='1' id='1' onClick=addNumber(this); />
					<td><input type='button' class='PINbutton' name='2' value='2' id='2' onClick=addNumber(this); />
					<td><input type='button' class='PINbutton' name='3' value='3' id='3' onClick=addNumber(this); />
				</tr>
				<tr>
					<td><input type='button' class='PINbutton' name='4' value='4' id='4' onClick=addNumber(this); />
					<td><input type='button' class='PINbutton' name='5' value='5' id='5' onClick=addNumber(this); />
					<td><input type='button' class='PINbutton' name='6' value='6' id='6' onClick=addNumber(this); />
				</tr>
				<tr>
					<td><input type='button' class='PINbutton' name='7' value='7' id='7' onClick=addNumber(this); />
					<td><input type='button' class='PINbutton' name='8' value='8' id='8' onClick=addNumber(this); />
					<td><input type='button' class='PINbutton' name='9' value='9' id='9' onClick=addNumber(this); />
				</tr>
				<tr>
					<td><input type='button' class='PINbutton clear' name='-' value='clear' id='-' onClick=clearForm(this); />
					<td><input type='button' class='PINbutton' name='0' value='0' id='0' onClick=addNumber(this); />
					<td><input type='button' class='PINbutton enter' name='+' value='enter' id='+' onClick=submitForm(PINbox); />
				</tr>
			</table>
		</form>
	
	</fieldset>
	</div>
	</div>
    </body>
</html>
