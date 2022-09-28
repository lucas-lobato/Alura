<?php

$notasBimestre1 = [
    'vinicius' => 10,
    'lobato' => 9,
    'lucas' => 8,
    'luana' => 7,
    'rosa' => 6,
    'maria' => 5
];

$notasBimestre2 = [
    'vinicius' => 10,
    'lobato' => 10,
    'lucas' => 8,
    'luana' => 8,
    'rosa' => 6,
    'amanda' => 5
];

var_dump(array_diff($notasBimestre1, $notasBimestre2));
var_dump(array_diff_key($notasBimestre1, $notasBimestre2));
var_dump(array_diff_assoc($notasBimestre1, $notasBimestre2));