<?php
    $servername = '118.139.178.119';
    $username = 'xfg1lnzh4jsj';
    $password = 'V!B05Tf!gdlW';
    $database = 'develxki_ibee';
    $conn = new mysqli($servername, $username, $password, $database);
if ($conn->connect_error) {
    die('Connection failed: ' . $conn->connect_error);
}
  $date = new DateTime("now", new DateTimeZone('Asia/Kolkata') );
  $currentdate = $date->format('Y-m-d H:i:s');

if(isset($_POST['ad_id'])){
	$sender = $conn -> real_escape_string($_POST['ad_id']);
	$subs_name = $conn -> real_escape_string($_POST['ad_name']);
	$subs_email = $conn -> real_escape_string($_POST['ad_email']);

    $max_count_sql = "SELECT MAX(id) as high FROM usr_tb;";
	$max_count_result = $conn -> query($max_count_sql);

    $row = $max_count_result -> fetch_assoc();
    $maxCount = "iba".(int)$row['high'] + 1;

	$insert_usr_sql = "INSERT INTO `usr_tb`(`usr_id`, `usr_nme`, `email`, `login_date`) 
	VALUES ('$maxCount','$subs_name','$subs_email','$currentdate') ";
	if ($conn->query($insert_usr_sql) === TRUE) {
		echo "T";
	} 
	else {
		echo "N";
	}
}
?>