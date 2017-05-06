function formhash(form, password) {
    // Create a new element input, this will be our hashed password field. 
    var p = document.createElement("input");
 
    // Add the new element to our form. 
    p.name = "pass";
    p.type = "hidden";
    p.value = hex_sha512(password.value);
    form.appendChild(p); // added this
    // Make sure the plaintext password doesn't get sent. 
    password.value = "";
    // Finally submit the form.
    form.submit();
}
