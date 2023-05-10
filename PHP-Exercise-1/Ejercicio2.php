<?php
$estudiantes = array();

function generate_random_name($first_names, $last_names) {
    $first_name = $first_names[array_rand($first_names)];
    $last_name = $last_names[array_rand($last_names)];
    return $first_name . ' ' . $last_name;
}

$first_names = ['Emma', 'Olivia', 'Ava', 'Isabella', 'Sophia', 'Mia', 'Charlotte', 'Amelia', 'Harper', 'Evelyn', 'Abigail', 'Emily', 'Elizabeth', 'Mila', 'Ella', 'Avery', 'Sofia', 'Camila', 'Aria', 'Scarlett', 'Victoria', 'Madison', 'Luna', 'Grace', 'Chloe', 'Penelope', 'Layla', 'Riley', 'Zoey', 'Nora','Lily','Eleanor','Hannah','Lillian','Addison','Aubrey','Ellie','Stella','Natalie','Zoe','Leah'];
$last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez','Hernandez','Lopez','Gonzalez','Wilson','Anderson','Taylor','Thomas','Jackson','White','Harris','Martin','Thompson','Garcia','Martinez','Robinson','Clark','Rodriguez','Lewis','Lee','Walker'];

for ($i = 0; $i < 6500; $i++) {
    $estudiantes[$i] = array(
        rand(2000000, 3000000),
        generate_random_name($first_names, $last_names),
        round(rand(0, 50) / 10, 1),
        rand(10, 68),
        rand(1980, 2023)
    );
}
$codigo_carrera = 12;

echo "Ingrese el código de la carrera a listar (los codigos de carreras van de 10 a 68): " .$codigo_carrera."<br>";

$estudiante_por_carreras = array_filter($estudiantes, function ($estudiante) use ($codigo_carrera) {
    return $estudiante[3] == $codigo_carrera;
});
$estudiante_por_promedios = array_filter($estudiante_por_carreras, function ($estudiante) {
    return $estudiante[2] >= 4;
});

echo "Código y nombre de los estudiantes de la carrera " . $codigo_carrera . " con promedio acumulado igual o mayor a 4:" ."<br>"."<br>";

foreach ($estudiante_por_promedios as $estudiante) {
    echo "CÓDIGO: " . $estudiante[0] . ", NOMBRE: " . $estudiante[1] . ", PROMEDIO: " . $estudiante[2] . ", AÑO DE INGRESO: " . $estudiante[4] ."<br>";
}

echo "<br>"."Total de estudiantes: " . count($estudiante_por_promedios)."<br>";

$estudiantes_antes_1990 = array_filter($estudiantes, function ($estudiante) {
    return $estudiante[4] < 1990;
});
$estudiantes_condicionales = array_filter($estudiantes_antes_1990, function ($estudiante) {
    return $estudiante[2] < 3.3 && $estudiante[2] > 2.7;
});

echo "<br>"."Código y nombre de los estudiantes que ingresaron antes de 1990 y están condicionales:"."<br>"."<br>";

foreach ($estudiantes_condicionales as $estudiante) {
    echo "CÓDIGO: " . $estudiante[0] . ", NOMBRE: " . $estudiante[1] . ", PROMEDIO: " . $estudiante[2] . ", AÑO DE INGRESO: " . $estudiante[4] ."<br>";
}
?>