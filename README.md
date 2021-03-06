# Eventex


Sistema de eventos encomendado pela Morena.

[![Build Status](https://travis-ci.org/Riverfount/wttd.svg?branch=master)](https://travis-ci.org/Riverfount/wttd) 
[![Code Health](https://landscape.io/github/Riverfount/wttd/master/landscape.svg?style=flat)](https://landscape.io/github/Riverfount/wttd/master)
[![Coverage Status](https://coveralls.io/repos/github/Riverfount/wttd/badge.svg?branch=master)](https://coveralls.io/github/Riverfount/wttd?branch=master)

## Como desenvolver?

1. Clone o repositório;
2. Crie um _virtualenv_ com Python 3.6.1;
3. Ative o _virtualenv_;
4. Instale as dependências;
5. Configure a instância de desenvolvimento com o _.env_;
6. Execute os testes.

```console
git clone git@github.com:Riverfount/wttd.git
cd wttd
python -m virtualenv .wttd
source .wttd/bin/activate
pip install -r requiremets-dev.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy?

1. Crie uma instância no Heroku;
2. Envie as configurações para o Heroku;
3. Defina uma SECRET_KEY para a instância;
4. Defina DEBUG=False;
5. Configure o serviço de e-mail;
6. Envie o código para o Heroku.

```console
heroku create minhainstancia
# Para executar o configu:push se necessário instale o plugin push do Heroku
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# configuro o e-mail (dependerá de sua instância)
git push heroku master --force
```