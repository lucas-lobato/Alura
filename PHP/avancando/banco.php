<?php

function myPrint(string $mensagem)
{
    echo ($mensagem . PHP_EOL);
}

function sacar(array $conta, float $valorASacar) : array
{
    if($valorASacar > $conta['saldo']){
       myPrint('Voce nao pode sacar esse valor');
    } else {
        $conta['saldo'] -= $valorASacar;
    }
    return $conta;
}

$contasCorrentes = [
    '123.456.789-10' => [
        'titular' => 'Maria',
        'saldo' => 10000
    ],

    '123.456.789-11' => [
        'titular' => 'Alberto',
        'saldo' => 3000
    ],

    '123.456.789-12' => [
        'titular' => 'Vinicius',
        'saldo' => 100
    ]
];

foreach ($contasCorrentes as $cpf => $conta){
    myPrint($cpf. " " . $conta['titular']);
}