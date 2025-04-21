<?php
try {
        $bd = new PDO ("mysql:host=localhost;dbname=thales","root","password");
        $bd->exec('SET NAMES utf8');

} catch (Exception $e) {
        die ("Erreur: Connexion à la base impossible");
}
?>
