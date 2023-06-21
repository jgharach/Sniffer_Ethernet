<?php
    session_start();
    $test = $_SESSION['test'];
    $date = $_SESSION['date'];
    include('base.php');
    $sql = "SELECT id_test FROM test WHERE nom_test = '$test' AND date_execution = '$date'";
    $req = $bd->prepare($sql);
    $req->execute();
    $id_test = $req->fetchall(PDO::FETCH_ASSOC);
    $req->closeCursor();
    $id_test = $id_test[0]['id_test'];
    $_SESSION['id_test'] = $id_test; 
    $sql = "SELECT framedate, MID, bench_3, bench_5, framesize, mac_dest, mac_src, field_1, field_2, field_3 , field_4 , field_5 , field_6 , field_7 , src_ip, dest_ip, field_9, field_10, field_11, field_14, field_16 , field_17, field_18, field_20 , field_21 , field_23, field_25 , field_26 , field_28 , field_29 , field_30 ,field_32, packet_date, mac_sender,sender_ip ,mac_target,target_ip FROM trame WHERE num_test = '$id_test'";
    $req = $bd->prepare($sql);
    $req->execute();
    $trame = $req->fetchall(PDO::FETCH_ASSOC);
    $req->closeCursor();
    $nom_champ = array_keys($trame[0]);
    $_SESSION['nom_champ'] = $nom_champ;
    $nbr_champ = count($nom_champ);
    $trame = array_map('array_values', $trame);
    $nbr_trame = count($trame); 
    $nbr_trame_affi = $_POST['trame'];
?>
<!DOCTYPE html> 
<html lang="fr"> 
<head> 
    <meta charset="utf-8">
    <link rel="stylesheet" href="http://localhost/Website/CSS/page.css"> 
    <title>Sniffer Ethernet</title> 
</head> 
<body>
<table>
        <?php
        $position_label = [];
        echo '<form method="POST" action="modified.php?nbr_trame_affi=' . $nbr_trame_affi . '">';
        if ($nbr_trame == 0){
            echo "La base de données est vide !";
        }
        elseif (0 < $nbr_trame_affi && $nbr_trame_affi <= $nbr_trame){
            echo "<tr>";
            for ($i = 0; $i < $nbr_champ; $i++) {
                echo "<th>{$nom_champ[$i]}</th>";
            }
            echo "</tr>";
            for ($j = 0; $j < $nbr_trame_affi; $j++) {
                echo "<tr>";
                for ($i = 0; $i < $nbr_champ; $i++) {
                    echo "<td>";
                    if (stripos($trame[$j][$i], "MID") !== false || stripos($trame[$j][$i], "ordi") !== false || stripos($trame[$j][$i], "label") !== false){
                        echo "<input type='text' name='label[]' value='{$trame[$j][$i]}'>";
                        array_push($position_label, [$j,$i]);
                    }
                    else {
                        echo $trame[$j][$i];
                    }
                    echo "</td>";
                }
                echo "</tr>";
            }
        }
        else{
            echo "Impossible : sélectionner un nombre entre 1 et {$nbr_trame} pour les trames que vous voulez affichez";
        }
        $_SESSION['position_label'] = $position_label;
        ?> 
</table>
<br>
<?php
if (0 < $nbr_trame_affi && $nbr_trame_affi <= $nbr_trame){
    echo '<button  type="submit">Modification des labels</button></form>';
    echo '<p>Supprimer toutes les trames de la base de données :</p>';
    echo '<form method="POST" action="supprimer.php">
    <button type="submit">Supprimer</button>
    </form>';
}
?>
</body>
</html>