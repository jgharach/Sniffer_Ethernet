<!DOCTYPE html> 
<html lang="fr"> 
<head> 
    <meta charset="utf-8" />
    <title>Thales</title> 
</head> 
<body>
    <?php
    include('base.php');
    $sql = "SELECT COLUMN_NAME
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_SCHEMA = 'thales' AND TABLE_NAME = 'trame' AND COLUMN_NAME NOT IN ('id_trame', 'num_test')
    ORDER BY ORDINAL_POSITION";
    $req = $bd->prepare($sql);
    $req->execute();
    $recup_nom_champs = $req->fetchall(PDO::FETCH_ASSOC);
    $req->closeCursor();
    $nom_champs = [];
    foreach ($recup_nom_champs as $key => $val){
        array_push($nom_champs, "{$val['COLUMN_NAME']}");       
    }
    echo "$nom_champs[0]";
    $sql = "SELECT framedate, MID, bench_3, bench_5, framesize, mac_dest, mac_src, field_1, field_2, field_3, field_4, field_5, field_6, field_7, src_ip, dest_ip, field_9, field_10, field_11, field_14, field_16, field_17, field_18, field_20, field_21, field_23, field_25, field_26, field_28, field_29, field_30, field_32, packet_date, mac_sender, sender_ip, mac_target, target_ip
    FROM trame
    WHERE num_test = 1";
    $req = $bd->prepare($sql);
    $req->execute();
    $trame = $req->fetchall(PDO::FETCH_ASSOC);
    $req->closeCursor();
    foreach ($trame as $key => $val){
        echo "<p>{$val['framedate']}</p>";
    }       
    ?> 
</body> 
 </html>