<?php
    $servername = '118.139.178.119';
    $username = 'xfg1lnzh4jsj';
    $password = 'V!B05Tf!gdlW';
    $database = 'develxki_ibee';
    $conn = new mysqli($servername, $username, $password, $database);
if ($conn->connect_error) {
    die('Connection failed: ' . $conn->connect_error);
}
$sql = "SELECT * FROM usr_tb";
$result = $conn->query($sql);

// Fetch data
$data = array();
if ($result->num_rows > 0) {
    while($row = $result->fetch_assoc()) {
        $data[] = $row;
    }
}

// Close connection
$conn->close();

// Output data in JSON format
echo json_encode($data);
?>

