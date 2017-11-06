<?php
	date_default_timezone_set('Asia/Kolkata');
	//error_reporting(0);
	$con = mysqli_connect("localhost","YOUR_USERNAME","YOUR_PASSWORD") or die("Cannot establish a connection to localhost");
	mysqli_select_db($con,"arachnis_ptproject") or die("Cannot select the DB");
?>
