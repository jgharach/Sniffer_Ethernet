<?php
session_start();
include('base.php');
$id_test = $_SESSION['id_test'];
$sql = "DELETE FROM trame WHERE num_test = '$id_test'";
$req = $bd->prepare($sql);
$req->execute();
header("Location: http://localhost/Website/Website/affichage_trame.php");
exit();
?>
