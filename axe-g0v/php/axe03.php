<?php
$url="http://axe-level-1.herokuapp.com/lv3/";
$jsonData = array();

$tuples = fetchContent($url);
foreach($tuples as $t)
	$jsonData[] = $t;

for($i=0; $i<75; $i++) {
	$tuples = fetchContent($url . "?page=next");
	foreach($tuples as $t)
		$jsonData[] = $t;
	echo "page $i done\n";
}
echo json_encode($jsonData, JSON_UNESCAPED_UNICODE);
?>

<?php
function fetchContent($url) {
	$tuples = array();
	$ch=curl_init();
	curl_setopt($ch,CURLOPT_URL,$url);
	curl_setopt($ch,CURLOPT_HEADER,false);
	curl_setopt($ch, CURLOPT_COOKIE, "PHPSESSID=aaa");
	curl_setopt($ch,CURLOPT_RETURNTRANSFER,1);
	$result = curl_exec($ch);
	$dom = new DOMDocument();
	@$dom->loadHTML($result);
	$xpath = new DOMXPath($dom);
	$trs = $xpath->query("//table[@class='table']/tr[position()>1]");
	foreach($trs as $tr) {
		$tds = $tr->childNodes;
		$tuple = array(
			"town" =>$tds->item(0)->nodeValue,
			"village" =>$tds->item(2)->nodeValue,
			"name" =>$tds->item(4)->nodeValue
		);
		$tuples[] = $tuple;
	}
	return $tuples;

}
?>
