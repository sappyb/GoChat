<?php

$host = "127.0.0.1";
$port = 2004;

$output="datatatatatatta" ;

$socket1 = socket_create(AF_INET, SOCK_STREAM,0) or die("Could not create socket\n");

socket_connect ($socket1 , $host,$port ) ;

socket_write($socket1, $output, strlen ($output)) or die("Could not write output\n");

socket_close($socket1) ;


?>
