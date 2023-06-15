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
    $trame = array_map('array_values', $trame);
?>
<!DOCTYPE html> 
<html lang="fr"> 
<head> 
    <meta charset="utf-8" />
    <title>SAE23</title> 
    <style>
        input[type="text"] {
         max-width: 100%;
        }
    </style>
</head> 
<body>
<table>
        <?php
        try {
            $nbr_trame = count($trame); 
            $nbr_trame_affi = $_POST['trame'];
            if (0 < $nbr_trame_affi && $nbr_trame_affi <= $nbr_trame){
                echo "<tr>";
                for ($i = 0; $i < count($nom_champ); $i++) {
                    echo "<th>{$nom_champ[$i]}</th>";
                }
                echo "</tr>";
                for ($j = 0; $j < $nbr_trame_affi; $j++) {
                    echo "<tr>";
                    for ($i = 0; $i < count($nom_champ); $i++) {
                        echo "<td>";
                        if (stripos($trame[$j][$i], "MID") !== false || stripos($trame[$j][$i], "ordi") !== false || stripos($trame[$j][$i], "label") !== false){
                            echo "<label><input type='text' value='{$trame[$j][$i]}'></label>";
                        }
                        else {
                            echo $trame[$j][$i];
                        }
                        echo "</td>";
                    }
                    echo "</tr>";
                }
            }
            else {
                echo "Impossible : sélectionner un nombre entre 1 et {$nbr_trame} pour les trames que vous voulez affichez";
            }
        }
        catch (Exception $e) {
            echo "Les données du test sont vides";
        }
        ?> 
</table>
<form method="POST" action="supprimer.php">
    <input type="submit" value="Supprimer">
</form>
</body>
</html>