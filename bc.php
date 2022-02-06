<?php
$fp = fsockopen('unix:///tmp/echo.sock', -1, $errno, $errstr, 30);
if (!$fp) {
  echo "$errstr ($errno)<br />\n";
} else {
  while (!feof($fp)) {
    echo fgets($fp, 4096);
  }
  fclose($fp);
}
?>
