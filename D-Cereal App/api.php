<?php
class User {
	public $name;

	function set_name($name) {
		$this->name = $name;
	}

	function get_name() {
		return $this->name;
	}
}

class User2 {
	public $name;
	function set_name($name) {
		$this->name = $name;
	}

	function get_name() {
		return eval($this->name);
	}
}

set_error_handler("err_handler", E_ALL);
$err = '';
function err_handler($errno, $errstr) {
	global $err;
	$err .= $errstr."\n";
}
$json = file_get_contents('php://input');
$input = json_decode($json, true);
$data = array();
if(isset($input['name'])) {
	$userobj = new User();
	$userobj->set_name($input['name']);
	$data['body'] = base64_encode(serialize($userobj));
}
elseif(isset($input['userdata'])) {
	$userobj = unserialize(base64_decode($input['userdata']));
	$name = $userobj->get_name();
	if(isset($input['debug'])) {
		if($input['debug'] === "true") {
			$data['debug'] = $err;
		}
	}
	$data['body'] = "Hello, " . $name . "<br>";
}

$data['statuscode'] = http_response_code();
$data['headers'] = array();
$data['headers']['Access-Control-Allow-Origin'] = '*';
header('Content-Type: application/json; charset=utf-8');
echo json_encode($data);
?>