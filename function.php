<?php
require_once 'DBOperation.php';




#change all the path for yourself
class Functions{
private $db;
private $deploy;
private $caffemodel;
private $netmean;
private $home;
public function __construct(){
   $this->home = "/home/";
   $this->deploy = "oxford102/AlexNet/deploy.prototxt";
   $this->caffemodel = "oxford102/AlexNet/snapshot_iter_50000.caffemodel";
   $this->netmean =  "caffe/data/ilsvrc12/imagenet_mean.binaryproto";
   $this->lables = "oxford102/AlexNet/labels.txt";
   $this->filepath_default = "oxford102/data/jpg/image_08186.jpg";
   $this->array = "notcomplete";
   $this->ret = "notcomplete";
   $this->db = new DBOperation();

}



public function typeclassify($filepath){
   $array = "notcomplete";
   $ret = "notcomplete";
   $command = "caffe/build/examples/cpp_classification/classification.bin " .
                $this->deploy. ' ' .
                $this->caffemodel . ' ' .
                $this->netmean . ' ' .
                $this->lables .' ' .
                $this->filepath;
   exec($command,$array,$ret);
#   file_put_contents("log.txt", $array[1], FILE_APPEND); 
   if($ret != '0')return "fail in calssify : ".$ret;
   else return $array[1];
}

public function typeclassify_py($filepath){
   $command = "python oxford102/python/classify.py 2>&1 ".$filepath;
   try{
	exec("env ",$array1,$ret1);
	exec($command,$array,$ret);
   }catch(Exception $err){
	return $err;
   }
    if($ret != '0')return "fail in calssify :"." : ".implode("",$array1)." : ".$ret2." : ".implode('\n',$array);
    else  return $array[0]." : ".$ret;
}

public function checkdatabase($name){ 
    $db = $this -> db;
    if($db -> checkExist($name)){
	return $db -> getDescription($name) ;
    }else{
	return "not exist in database";	
    }
#   return "not complete";
}

public function checkdatabaseweb($name){
    $db = $this -> db;
    if($db -> checkExist($name)){
        return $db -> getWeb($name) ;
    }else{
        return "not exist in database";
    }



}

}
