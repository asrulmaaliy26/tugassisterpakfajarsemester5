<?php 
$json_url = "https://www.googleapis.com/youtube/v3/channels?part=snippet, statistics&id=UCx7zc0MyoSdDSQXvq5Gl8gg&key=AIzaSyC-IpGE2nkQsstBu4KAOEV2u5v2Qxcud8E";
$json = file_get_contents($json_url);
$data = json_decode($json);

print_r($data);
?>