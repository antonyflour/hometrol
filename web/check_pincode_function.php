<?php
include_once 'dbConnect.php';

function checkPincode($username, $pin, $mysqli) {
    // Using prepared statements means that SQL injection is not possible. 
    if ($stmt = $mysqli->prepare("SELECT pin  FROM users WHERE username = ? LIMIT 1")) {
        $stmt->bind_param('s', $username);  // Bind "$email" to parameter.
        $stmt->execute();    // Execute the prepared query.
        $stmt->store_result();
	 
        // get variables from result.
        $stmt->bind_result($pin_found);
        $stmt->fetch();

        if ($stmt->num_rows == 1) {
                // Check if the password in the database matches
                // the password the user submitted. 
                if ($pin_found == $pin) {
                    return true;
                } else {
                    // Password is not correct
                    return false;
                }
        } else {
            // No user exists.
            return false;
        }
    }
}

?>

