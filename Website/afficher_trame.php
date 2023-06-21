<?php
    session_start();
    $_SESSION['test'] = $_GET['test'];
    $_SESSION['date'] = $_GET['date'];
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
    <form action="affichage_trame.php" method="post">
    <p>Sélectionner le nombre de trames que vous voulez afficher : <input type="text" name="trame" /></p>
    <p><input type="submit" value="Confirmer"></p>
    </form>
</body> 
 </html>
