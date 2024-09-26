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

def test_pessoa_nome_tipo_invalido_mostrar_mensagem():  
    with pytest.raises(TypeError, match = "O nome deve ser um texto!"):
        Pessoa("111", 23, Sexo.MASCULINO)

def test_pessoa_idade_tipo_invalido_mostrar_mensagem():  
    with pytest.raises(TypeError, match = "A idade deve ser número inteiro!"):
        Pessoa("Fuboca", "23", Sexo.MASCULINO)

def test_pessoa_idade_negativa_mostrar_mensagem():  
    with pytest.raises(ValueError, match = "A idade não pode ser negativa!"):
        Pessoa("Fuboca", -23, Sexo.MASCULINO)

def test_pessoa_idade_maior_130_mostrar_mensagem():  
    with pytest.raises(ValueError, match = "A idade não pode ser maior que 130 anos!"):
        Pessoa("Fuboca", 135, Sexo.MASCULINO)


    