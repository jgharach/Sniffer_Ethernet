<?php
session_start();
include('base.php');
$id_test = $_SESSION['id_test'];
$nom_champ = $_SESSION['nom_champ'];
$label = $_POST['label'];
$position_label = $_SESSION['position_label'];
$sql = "SELECT id_trame FROM trame WHERE num_test = '$id_test'";
$req = $bd->prepare($sql);
$req->execute();
$id_trame = $req->fetchall(PDO::FETCH_ASSOC);
$req->closeCursor();
for ($i=0; $i<count($position_label); $i++){
    for ($j=0; $j<count($id_trame); $j++){
        if ($id_trame[$j]['id_trame'] == $position_label[$i][0]){
            $sql = "UPDATE trame SET {$nom_champ[$position_label[$i][1]]} = '$label[$i]' WHERE $id_trame = '$position_label[$i][0]'";
            $req = $bd->prepare($sql);
            $req->execute();
        }
    }
}
header("Location: http://localhost/Website/Website/affichage_trame.php");
exit();
?> 