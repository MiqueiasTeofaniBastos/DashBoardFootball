# DashBoardFootball - Futebol Hoje API

Esse projeto é uma aplicação Flask simples que consome uma API de partidas de futebol e mostra os jogos marcados para o dia atual, junto com o placar dos mesmos.

## Setup

Para rodar essa aplicação na sua máquina local, siga os passos abaixo:

**1.** Clone o repositório para a sua máquina

```bash
git clone https://github.com/MiqueiasTeofaniBastos/DashBoardFootball.git
```

**2.** Mude para o diretório que contém o código do projeto

```bash
cd DashBoardFootball
```

**3.** Crie um ambiente virtual e o ative:

```bash
python3 -m venv venv
source venv/bin/activate
```

**4.** Instale as dependências necessárias:

```bash
pip install -r requirements.txt
```

**5.** Exporte as variáveis de Ambiente

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
```

**6.** Rodar a aplicação

```bash
flask run
```
Depois de rodar o último comando acima, você deverá ver que o servidor está rodando em `http://127.0.0.1:5000/`.

## Uso

Abra o navegador e acesse `http://127.0.0.1:5000/` para ver quais jogos estão ocorrendo hoje e o atual placar deles.
