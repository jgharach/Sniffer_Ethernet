<!DOCTYPE html> 
<html lang="fr"> 
<head> 
    <meta charset="utf-8" />
    <title>SAE23</title> 
</head> 
<body> 
    <?php
        include('base.php');
        $sql = "SELECT nom_test FROM test";
        $req = $bd->prepare($sql);
        $req->execute();
        $nom_test = $req->fetchall(PDO::FETCH_ASSOC);
        $req->closeCursor();
        $url = "http://localhost/Website/affichage_trame.php";
        foreach ($nom_test as $key => $val){
            echo "<a href='$url'>{$val['nom_test']}</a><br>";
        }
    ?>
</body> 
 </html>