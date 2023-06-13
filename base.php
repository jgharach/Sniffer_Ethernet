<?php
try {
        $bd = new PDO ("mysql:host=localhost;dbname=gj200498"/*identifiant isis*/,"gj200498"/*identifiant isis*/,"gj2004987503"/*mot de passe de la base perso*/);
        $bd->exec('SET NAMES utf8');

} catch (Exception $e) {
        die ("Erreur: Connexion à la base impossible");
}
?>