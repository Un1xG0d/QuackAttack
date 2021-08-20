<!DOCTYPE html>
<head>
    <style type="text/css">
    table.blueTable {
      width: 100%;
      text-align: center;
      font-size: 48px;
  }
  table.blueTable td, table.blueTable th {
    border: 1px solid #000000;
  }
  table.blueTable thead {
      background: #0B6FA4;
  }
  table.blueTable thead th {
      font-weight: bold;
      color: #FFFFFF;
      text-align: center;
  }
</style>
</head>
<body>
    <center>
        <table class="blueTable">
            <thead>
                <tr>
                    <th>Credential Dump URLs</th>
                </tr>
            </thead>
            <tbody>
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
                    echo "<tr><td><a href='" . $link->url . "'>" . $link->url . "</a></td><tr>";
                }
                ?>
            </tbody>
        </table>
    </center>
</body>