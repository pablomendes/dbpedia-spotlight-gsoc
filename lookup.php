<?php
/**
 *
 * @author pablomendes
 */
$keyword = $_GET["QueryString"];
$simple = file_get_contents ("http://lookup.dbpedia.org/api/search.asmx/KeywordSearch?QueryString=$keyword");
$xml = simplexml_load_string($simple);
$json = json_encode($xml);
$array = json_decode($json,TRUE);

$results = $array["Result"];
$output = array();
foreach ($results as $r) {
  $output[] = array("URI"=>$r["URI"],"Label"=>$r["Label"]);
}
header("Content-type: application/json");
echo json_encode($output);
?>