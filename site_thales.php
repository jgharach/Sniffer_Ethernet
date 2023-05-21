<!DOCTYPE html> 
<html lang="fr"> 
<head> 
    <meta charset="utf-8" />
    <title>Thales</title> 
</head> 
<body> 
    <?php
        include('base.php');
        $sql = "SELECT nom_test FROM test";
        $req = $bd->prepare($sql);
        $req->execute();
        $nom_test = $req->fetchall();
        $req->closeCursor();
        echo $nom_test
    ?>
</body> 
 </html>