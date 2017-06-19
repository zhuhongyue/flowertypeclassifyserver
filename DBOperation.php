<?php

class DBOperation{

         private $host = 'localhost';
         private $user = 'root';
         private $db = 'flowerdatabase';
         private $pass = 'balabala';
         private $conn;

public function __construct() {
        $this -> conn = new PDO("mysql:host=".$this -> host.";dbname=".$this -> db, $this -> user, $this -> pass);

}

public function checkExist($name){
    $sql = 'SELECT COUNT(*) from flower WHERE name =:name';
    $query = $this -> conn -> prepare($sql);
    $query -> execute(array('name' => $name));
    if($query){
        $row_count = $query -> fetchColumn();
        if ($row_count == 0){
            return false;
        } else {
            return true;
        }
    } else {
        return false;
    }
}

public function getDescription($name) {

    $sql = 'SELECT * FROM flower WHERE name = :name';
    $query = $this -> conn -> prepare($sql);
    $query -> execute(array(':name' => $name));
    if($query && $this->checkExist($name)){
	$data = $query -> fetchObject();
	$des = $data -> description;
    	return $des;
    }else{
	return "not exist in database";
    }
}
public function getWeb($name){
    $sql = 'SELECT * FROM flower WHERE name = :name';
    $query = $this -> conn -> prepare($sql);
    $query -> execute(array(':name' => $name));
    if($query && $this->checkExist($name)){
        $data = $query -> fetchObject();
        $web = $data -> web;
        return $des;
    }else{
        return "not exist in database";
    }


}



}




