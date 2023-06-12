#pragma once
#include <string>
#include "Cpf.hpp"

class Funcionario
{
public:
	
private:
	Cpf cpf;
	std::string nome;
	float salario;
public:
	Funcionario(Cpf cpf, std::string nome, float salario);
};

