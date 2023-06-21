<?php
include('base.php');
$sql = "SELECT nom_test FROM test";
$req = $bd->prepare($sql);
$req->execute();
$nom_test = $req->fetchall(PDO::FETCH_ASSOC);
$req->closeCursor();
?>
<!DOCTYPE html> 
<html lang="fr"> 
<head> 
    <meta charset="utf-8">
    <link rel="stylesheet" href="http://localhost/Website/CSS/page.css">
    <title>Sniffer Ethernet</title> 
</head> 
<body> 
    <header><img src="http://localhost/Website/Image/Thales_Alenia_Space_Logo.svg.png" height="100"></img></header>
    <h2>Affichage des test</h2>
    <?php
        for($i=0 ; $i< count($nom_test); $i++){
            $url = "http://localhost/Website/Website/affichage_date.php?test={$nom_test[$i]['nom_test']}";        
            echo "<a href='$url'>{$nom_test[$i]['nom_test']}</a> <br>";
        };
    ?>
</body>
</html>