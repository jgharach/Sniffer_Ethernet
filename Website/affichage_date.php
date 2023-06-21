<?php
include('base.php');
$test = $_GET['test'];
$sql = "SELECT date_execution FROM test WHERE nom_test = '$test'";
$req = $bd->prepare($sql);
$req->execute();
$date = $req->fetchall(PDO::FETCH_ASSOC);
$req->closeCursor();
?>
<!DOCTYPE html> 
<html lang="fr"> 
<head> 
    <meta charset="utf-8" />
    <title>Sniffer Ethernet</title> 
    <link rel="stylesheet" href="http://localhost/Website/CSS/page.css"> 
</head> 
<body>
    <header><img src="http://localhost/Website/Image/Thales_Alenia_Space_Logo.svg.png" height="100"></img></header>
    <h2>Affichage des dates d'exécutions</h2>    
    <?php
        for($i=0 ; $i<count($date); $i++){
            $url = "http://localhost/Website/Website/afficher_trame.php?test=$test&date={$date[$i]['date_execution']}";
            echo "<a href='$url'>{$date[$i]['date_execution']}</a> <br>";
        }
     ?>
</body> 
 </html>