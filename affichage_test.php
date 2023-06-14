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
        for($i=0 ; $i< count($nom_test); $i++){
            $url = "http://localhost/Website/affichage_date.php?test={$nom_test[$i]['nom_test']}";        
            echo "<a href='$url'>{$nom_test[$i]['nom_test']}</a> <br>";
        };
    ?>
</body>
</html>