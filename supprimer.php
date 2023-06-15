<?php
include('base.php');
session_start();
$id_test = $_SESSION['id_test'];
$sql = "DELETE FROM trame WHERE num_test = '$id_test'";
$req = $bd->prepare($sql);
if ($req->execute()){
    echo "Les données ont été supprimés avec succès !";
}
else {
    echo "Impossible de supprimer les données";
}
header("Location: http://localhost/Website/affichage_trame.php");
exit();
?>
