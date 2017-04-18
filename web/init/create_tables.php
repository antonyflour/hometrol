<?php
	include_once '../connectionConfig.php'; 
	
	$mysqli = new mysqli(HOST, USER, PASSWORD);
	
	$database_ok=false;
	if ($stmt = $mysqli->prepare("CREATE DATABASE ".DATABASE.";")) {
		if($stmt->execute()){
			$database_ok=true;
		}
	}

	
	$mysqli = new mysqli(HOST, USER, PASSWORD, DATABASE);

	
	//create users table
	$users_table_ok=false;
	if ($stmt = $mysqli->prepare("CREATE TABLE users(
															 username VARCHAR(50) PRIMARY KEY,
															 password VARCHAR(128) NOT NULL);")) {
					if($stmt->execute()){
						$users_table_ok=true;
					}
	}
	
	//create sessions table
	$sessions_table_ok=false;
	if ($stmt = $mysqli->prepare("CREATE TABLE sessions(
															 key_cookie VARCHAR(50) PRIMARY KEY,
															 user VARCHAR(50) NOT NULL,
															 isadmin VARCHAR(3) NOT NULL,
															 creation_date DATE NOT NULL,
															 creation_time TIME NOT NULL,
															 FOREIGN KEY (user) REFERENCES users(username)
																	ON UPDATE CASCADE
																	ON DELETE CASCADE);")) {
					if($stmt->execute()){
						$sessions_table_ok=true;
					}
	}
	
	
	//insert 'admin' user 
	$insert_admin_ok=false;
	if ($stmt = $mysqli->prepare("INSERT INTO users (username, password) VALUES (?, ?);")) {
					$username="admin";
					$hashed_pass = hash("sha512","admin");
					$stmt->bind_param("ss",$username, $hashed_pass);
					if($stmt->execute()){
						$insert_admin_ok=true;
					}
	}
	
	//insert 'user' user 
	$insert_user_ok=false;
	if ($stmt = $mysqli->prepare("INSERT INTO users (username, password) VALUES (?, ?);")) {
					$username="user";
					$hashed_pass = hash("sha512","user");
					$stmt->bind_param("ss",$username, $hashed_pass);
					if($stmt->execute()){
						$insert_user_ok=true;
					}
	}
	
	
	if($database_ok==true){
		echo "database created: ok<br>";
	}
	else{
		echo "database created: error<br>";
	}
	
	if($users_table_ok==true){
		echo "users table: ok<br>";
	}
	else{
		echo "users table: error<br>";
	}

	if($sessions_table_ok==true){
		echo "sessions table: ok<br>";
	}
	else{
		echo "sessions table: error<br>";
	}
	
	if($insert_admin_ok==true){
		echo "insert admin: ok<br>";
	}
	else{
		echo "insert admin: error<br>";
	}
	
	if($insert_user_ok==true){
		echo "insert user: ok<br>";
	}
	else{
		echo "insert user: error<br>";
	}
?>