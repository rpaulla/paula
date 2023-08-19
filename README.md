# Guia de Instalação

## Entrar no ambiente virtualenv

### Windows

```
.venv\Scripts\activate
```


### Linux

```
source .venv/bin/activate
```

## Instalar as dependências

```
pip install requirements.txt
```

## copia o .env.example e renomeia para .env

## Rode o script secret_key.py

```
python3 secret_key.py
```

## Agora, copie a SECRET_KEY que foi gerada no terminal e coloque no seu arquivo .env

# Agora, você já pode rodar a aplicação

```
python3 manage.py runserver
```

