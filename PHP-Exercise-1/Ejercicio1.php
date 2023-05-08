<?php
$votos = array();
for ($i = 0; $i < 5000; $i++) {
    array_push($votos, rand(1, 30));
}
$votosordenados = array_count_values($votos);
arsort($votosordenados);
foreach ($votosordenados as $x => $x_value) {
    echo "Candidato N°" . $x . " tiene " . $x_value . " votos" . "<br>";
}
?>