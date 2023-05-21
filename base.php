<?php
try {
        $bd = new PDO ("mysql:host=localhost;dbname=thales"/*identifiant isis*/,"root"/*identifiant isis*/,"brKMEbR?f@hLY885"/*mot de passe de la base perso*/);
        $bd->exec('SET NAMES utf8');

} catch (Exception $e) {
        die ("Erreur: Connexion à la base impossible");
}
?>