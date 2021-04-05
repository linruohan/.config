<?php

header("content-type:text/html;charset=utf-8");
date_default_timezone_set("PRC");

$pImg=$_FILES['file123'];

//echo json_encode($pImg);
//echo '\n<br>';

//echo json_encode($_FILES);
//echo '\n<br>';

//echo '_REQUEST';
//echo json_decode($_REQUEST);
//echo '\n<br>';
//print_r($pImg);

$request_arg = 'request,:';
$request_arg .= json_encode($pImg);

foreach ($_REQUEST as $key => $value)
{
    $request_arg .=  $key.'='.$value.",";
}
$request_arg .=  "\n";

$myfile = fopen("file.txt", "a") or die("Unable to open file!");
fwrite($myfile, $request_arg);
fclose($myfile);

if($pImg['error']==UPLOAD_ERR_OK)
{
  //取得扩展名
  $extName=strtolower(end(explode('.',$pImg['name'])));
  $filename=date("Ymdhis").".".$extName;
  $dest="uploads/".$filename;
  move_uploaded_file($pImg['tmp_name'],$dest);
  echo "上传成功";
}
else
{
  echo "上传错误";
}
?>
