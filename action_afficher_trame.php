<?php
    session_start();
    $_SESSION['test'] = $_GET['test'];
    $_SESSION['date'] = $_GET['date'];
?>
<!DOCTYPE html> 
<html lang="fr"> 
<head> 
    <meta charset="utf-8" />
    <title>SAE23</title> 
</head> 
<body>
     
    <form action="affichage_trame.php" method="post">
    <p>Sélectionner le nombre de trames que vous voulez afficher : <input type="text" name="trame" /></p>
    <p><input type="submit" value="Confirmer"></p>
    </form>
</body> 
 </html>
