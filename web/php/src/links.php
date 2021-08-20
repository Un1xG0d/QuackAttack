<?php
$host = 'db';
$user = 'MYSQL_USER';
$pass = 'MYSQL_PASSWORD';
$database = 'MYSQL_DATABASE';
$conn = new mysqli($host, $user, $pass, $database);
$sql = 'SELECT * FROM links';

if ($result = $conn->query($sql)) {
    while ($data = $result->fetch_object()) {
        $links[] = $data;
    }
}

foreach ($links as $link) {
    echo "<br>";
    echo $link->url;
    echo "<br>";
}
?>
