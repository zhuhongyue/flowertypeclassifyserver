
<?php
#just for test in local
require_once 'function.php';
$fun = new Functions();
$file_path = "oxford102/data/jpg/image_08186.jpg";
$result = array("result" => "success","msg" => $fun -> typeclassify($file_path));
$str = $result["msg"];
echo $str;
echo "\n";
preg_match_all('/[a-z]+/ ',$str,$match);
$str =  implode(" ",$match[0]);
echo $str;
echo "\n";
echo $fun -> checkdatabase($str);
echo "\n";


