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
        $nom_tests = [];
        $url = "http://localhost/Website/affichage_trame.php";
        foreach ($nom_test as $key => $val){
            array_push($nom_tests, "{$val['nom_test']}");
        }
        echo "<a href='$url'>$nom_tests[0]</a> <br>";
        echo "<a href='$url'>$nom_tests[1]</a> <br>";
    ?>
</body> 
 </html>