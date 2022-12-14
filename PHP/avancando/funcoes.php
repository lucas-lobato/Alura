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

function exibeConta(array $conta)
{
    ['titular' => $titular, 'saldo' => $saldo] = $conta;
    echo "<li>Titular: $titular. Saldo: $saldo</li>";
}