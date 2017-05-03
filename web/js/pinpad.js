
function addNumber(e){
	var v = $( "#PINbox" ).val();
	$( "#PINbox" ).val( v + e.value );
}
function clearForm(e){
	$( "#PINbox" ).val( "" );
}
function submitForm(e) {
	if (e.value == "") {
		alert("Enter a PIN");
	} else {

		$("#PINbox").removeAttr("disabled");
		formhash(document.getElementById('PINform'), e);
	};
};
