<?php
$sock = stream_socket_client('unix:///tmp/echo.sock', $errno, $errst);
$type = 'Hello';
fwrite($sock, $type);
$response = fread($sock, 1024);
fclose($sock);
?>
