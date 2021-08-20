<?php
$host = 'db';
$user = 'MYSQL_USER';
$pass = 'MYSQL_PASSWORD';
$database = 'MYSQL_DATABASE';
$conn = new mysqli($host, $user, $pass, $database);
$data = json_decode(file_get_contents('php://input'), true);
$sql = 'INSERT INTO `links` (url) VALUES ("'.$data["url"].'")';

if ($result = $conn->query($sql)) {
    echo 'Success!';
}
?>
