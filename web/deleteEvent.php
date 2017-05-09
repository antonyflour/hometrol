<?php
include_once 'functionCheckLogin.php';
include_once 'stub/stub.php';

$code_login = login_check($mysqli);
if($code_login <1) {
    header('Location: index.php');
}
$event_id = $_REQUEST['event_id'];

try{
    $resp = deleteEvent($event_id);
    http_response_code(200);
}catch (Exception $e){
	http_response_code(403);
}


?>
