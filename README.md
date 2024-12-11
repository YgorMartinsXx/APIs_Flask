
# Desenvolvimento e manipulaçao de APIs

Este repositório é direcionado a quem, assim como eu, gosta do desenvolvimento de APIs. Em cada seção deste repositório você poderá entender os fundamentos e estrututras básicas de uma API.




## Requisitos

- Python 3.13.0
- Flask 3.0.3
- Flask-Cors 5.0.0
- jsonify 0.5
- requests 2.32.3
- PostMan(Somente para testes)

```bash
  pip install python
  pip install flask
  pip install flask-cors
  pip install jsonify
  pip install requests
```
    
## Instruções

Para este projeto é recomendado o uso do PostMan, para que assim seja possivel testar as APIs criadas.

Toda API criada neste projeto está com uma *Porta* e um *Host* já definidos.

Se atente somente a URL a ser inserida no PostMan pois a porta pode e deve mudada de acordo com o projeto:

    http://localhost:5002/


## Documentação

### Retorna todos os alunos
Seguindo o Host e a Porta apresentada no projeto "04.Flask":

#### retorna todos os alunos

```http
  GET /alunos
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `alunos` | `string` | endPoint padrao definido no Model |

#### aluno():

retorna todos os alunos.

### Retorna um aluno

```http
  GET /alunos/29
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `int` | **Obrigatório**. O ID do aluno que você quer |

#### aluno_por_id():

Recebe um numero (ID do aluno definido no Json criado) e retorna o aluno detentor do ID.

