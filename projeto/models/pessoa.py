from projeto.models.enums.sexo import Sexo

class Pessoa:
    def __init__(self, nome : str, idade: int, sexo: Sexo) -> None:
        self._nome = self._verificar_nome(nome)
        self._idade = self._verificar_idade(idade)
        self._sexo = sexo

    def _verificar_nome(self, valor):
        self._verificar_nome_tipo_invalido(valor)

        self._nome = valor
        return self._nome 
    
    def _verificar_idade(self, valor):
        self._verificar_idade_tipo_invalido(valor)
        self._verificar_idade_negativa(valor)
        self._verificar_idade_maior_130(valor)

        self._idade = valor
        return self._idade 

    def _verificar_nome_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("O nome deve ser um texto!")
        
    def _verificar_idade_tipo_invalido (self, valor):
        if not isinstance(valor, int):
            raise TypeError("A idade deve ser número inteiro!")

    def _verificar_idade_negativa (self, valor):
        if valor < 0:
            raise ValueError("A idade não pode ser negativa!")

    def _verificar_idade_maior_130 (self, valor): 
        if valor > 130:
            raise ValueError("A idade não pode ser maior que 130 anos!")

    def __str__(self) -> str:
        return(
                f"\nNome: {self._nome}"
                f"\nIdade: {self._idade}"
                f"\nSexo: {self._sexo}"

        )