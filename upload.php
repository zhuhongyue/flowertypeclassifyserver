<?php

require_once 'function.php';
$fun = new Functions();

if($_SERVER['REQUEST_METHOD'] == 'GET'){echo "Upload API";}
else if ($_SERVER['REQUEST_METHOD'] == 'POST'){

    $file_path = "/var/www/html/FlowerTypeServer/loaddata/Flower";
     
    $file_path = $file_path . basename( $_FILES['uploaded_file']['name']);
    if(move_uploaded_file($_FILES['uploaded_file']['tmp_name'], $file_path)) {
	$type = $fun -> typeclassify($file_path);
	preg_match_all('/[a-z]+/ ',$type,$match);
	$type = implode(" ",$match[0]);;
	$result = array("result" => "success","msg" => $type,"info" => $fun -> checkdatabase($type),"web" => $fun -> checkdatabaseweb($type));
    } else{
        $result = array("result" => "error","msg" => "erro in save image","info" => "not complete");
    }

    echo json_encode($result);


}
?>

