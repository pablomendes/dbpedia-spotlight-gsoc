<?php

$query = $_GET["query"];

$format = "json";
$url = 'http://dbpedia.org/sparql?'
      .'query='.urlencode($query)
      .'&format='.$format;

echo($query);
$json = request($url);

$array = json_decode($json,TRUE);

function request($url){

   // is curl installed?
   if (!function_exists('curl_init')){
      //$opts = array(
	  //  'http'=>array(
	  //    'method'=>"GET",
	  //    'header'=>"Accept-content: en\r\n"
	  //  )
	  //);
	  //$context = stream_context_create($opts);

	  // Open the file using the HTTP headers set above
	  //$file = file_get_contents($url, false, $context);
	  return file_get_contents($url);
      //die('CURL is not installed!');
   }

   // get curl handle
   $ch= curl_init();

   // set request url
   curl_setopt($ch,
      CURLOPT_URL,
      $url);

   // return response, don't print/echo
   curl_setopt($ch,
      CURLOPT_RETURNTRANSFER,
      true);

   /*
   Here you find more options for curl:
   http://www.php.net/curl_setopt
   */

   $response = curl_exec($ch);

   curl_close($ch);

   return $response;
}

?>