function submitNewPin(form, password, pincode) {
	var hashed_pass = hex_sha512(password);
	var hashed_pin = hex_sha512(pincode);

	form.append('<input type="hidden" name="password" id = "password"/>');
	form.append('<input type="hidden" name="pincode" id = "pincode"/>');
	$('#password').val(hashed_pass);
	$('#pincode').val(hashed_pin);
	form.submit();
}

function hidePassword() {
	if ($('#pass').val() != '') {
		password = $('#pass').val();
		$('#changepass-form').hide();
		$('#pinpad-div').show();
	} else {
		alert("Inserisci la password");
	}
}

function insertPincode() {
	if ($('#PINbox').val() != '') {
		if (pincode1 == null) {
			pincode1 = $('#PINbox').val();
			$('#PINbox').val("");
			$('#h3pinpad').text("Passo 3 : inserisci di nuovo il PIN");
		} else {

			pincode2 = $('#PINbox').val();
			if (pincode1 == pincode2) {
				submitNewPin($('#change_form'), password, pincode2);
			} else {
				alert("I due PIN non coincidono, ripeti la procedura!");
				location.assign('/changePincodeForm.php');
			}
		}
	} else {
		alert("Inserisci un PIN valido");
	}
}
