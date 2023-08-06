# fakedadosbr

**fakedadosbr** is a library to generate fake data to development and debug.

## Features

- Fake persons.
- Fake Companys.
- Fake vehicles.

## Installation

- Run `pip install fakedadosbr`

## Exxemple

```python
from fakedadosbr import fake_cidadao, fake_empresa, fake_veiculo

cidadao = fake_cidadao()
company = fake_empresa()
vehicle = fake_veiculo()

print(cidadao)
print(company)
print(vehicle)
```

### Console Output

```bash
foo@bar ~/
$ python fakedados_test.py
{'nome': 'Marcos Vinicius Manoel da Conceição', 'idade': 27, 'cpf': '34725101966', 'rg': '170814713', 'data_nasc': '19/02/1994', 'sexo': 'Feminino', 'signo': 'Aquário', 'mae': 'Isabelly Ayla Alícia', 'pai': 'Bernardo Tiago da Conceição', 'email': 'marcosviniciusmanoeldaconceicao__marcosviniciusmanoeldaconceicao@gtx.ag', 'senha': 'MWzTZ8QeEG', 'cep': '54315675', 'endereco': '4ª Travessa Ladeira da Igreja', 'numero': 529, 'bairro': 'Guararapes', 'cidade': 'Jaboatão dos Guararapes', 'estado': 'PE', 'telefone_fixo': '8136207327', 'celular': '81994178412', 'altura': '1,77', 'peso': 
65, 'tipo_sanguineo': 'O-', 'cor': 'laranja'}

{'nome': 'Bárbara e Anderson Entulhos Ltda', 'cnpj': '67656533000105', 'ie': '5129572770', 'data_abertura': '18/11/1994', 'site': 'www.barbaraeandersonentulhosltda.com.br', 'email': 'financeiro@barbaraeandersonentulhosltda.com.br', 'cep': '83215330', 'endereco': 'Rua Buenos Aires', 'numero': '564', 'cidade': 'Paranaguá', 'estado': 'PR', 'telefone_fixo': '4126336328', 'celular': '41989684238'}

{'marca': 'AM Gen', 'modelo': 'Hummer Open-Top 6.5 4x4 Diesel TB', 'ano': '1998', 'renavam': '41591742567', 'placa_veiculo': 'NBA7300', 'cor': 'Azul'}
```

## Upgrade

- Run `pip install fakedadosbr --upgrade`
