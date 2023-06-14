<!DOCTYPE html> 
<html lang="fr"> 
<head> 
    <meta charset="utf-8" />
    <title>SAE23</title> 
</head> 
<body>
    <?php
    include('base.php');
    $test = $_GET['test'];
    $date = $_GET['date'];
    $sql = "SELECT id_test FROM test WHERE nom_test = '$test' AND date_execution = '$date'";
    $req = $bd->prepare($sql);
    $req->execute();
    $id_test = $req->fetchall(PDO::FETCH_ASSOC);
    $req->closeCursor();
    $id_test = $id_test[0]['id_test'];
    $sql = "SELECT framedate, MID, bench_3, bench_5, framesize, mac_dest, mac_src, field_1, field_2, field_3 , field_4 , field_5 , field_6 , field_7 , src_ip, dest_ip, field_9, field_10, field_11, field_14, field_16 , field_17, field_18, field_20 , field_21 , field_23, field_25 , field_26 , field_28 , field_29 , field_30 ,field_32, packet_date, mac_sender,sender_ip ,mac_target,target_ip FROM trame WHERE num_test = '$id_test'";
    $req = $bd->prepare($sql);
    $req->execute();
    $trame = $req->fetchall(PDO::FETCH_ASSOC);
    $req->closeCursor();
    $nom_champ = array_keys($trame[0]);
    $trame = array_map('array_values', $trame);
    ?> 
    <table>
            <?php   
            for ($i=0; $i<count($nom_champ); $i++){
                echo "<tr><td>{$nom_champ[$i]}</td></tr>";
                for ($j=0; $j<count($trame); $j++){
                    echo "<tr><td>{$trame[$j][$i]}</td></tr>";
                }
            }            
         ?>
    </table>
</body> 
 </html>