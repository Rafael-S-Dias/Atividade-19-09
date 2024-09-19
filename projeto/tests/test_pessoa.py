import pytest
from projeto.models.pessoa import Pessoa
from projeto.models.enums.sexo import Sexo

@pytest.fixture
def pessoa_valida():
    pessoa1 = Pessoa("Fuboca", 23, Sexo.MASCULINO)
    return pessoa1

def test_pessoa_nome_valido(pessoa_valida):
    assert pessoa_valida._nome == "Fuboca"

def test_pessoa_idade_valida(pessoa_valida):   
    assert pessoa_valida._idade == 23
    
def test_pessoa_idade_negativa(pessoa_valida):  
    pessoa_valida._set_idade(-1)
    assert pessoa_valida._idade == 0