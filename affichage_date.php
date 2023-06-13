<!DOCTYPE html> 
<html lang="fr"> 
<head> 
    <meta charset="utf-8" />
    <title>SAE23</title> 
</head> 
<body> 
    <?php
        include('base.php');
        $test = $_GET['test'];
        $sql = "SELECT date_execution FROM test WHERE nom_test = '$test'";
        $req = $bd->prepare($sql);
        $req->execute();
        $date = $req->fetchall(PDO::FETCH_ASSOC);
        $req->closeCursor();
        for($i=0 ; $i<count($date); $i++){
            $url = "http://isis.unice.fr/~gj200498/acces/Website/affichage_trame.php?test=$test&date={$date[$i]['date_execution']}";
            echo "<a href='$url'>{$date[$i]['date_execution']}</a> <br>";
        }
     ?>
</body> 
 </html>