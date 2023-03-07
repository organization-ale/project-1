# APIException

O django rest framework tem em sua estrutura uma classe para customizar exeções chamada APIException, onde ela nos traz uma certa agilidade para se levantar erros e retornar em sua response de forma legível sem a necessidade de utilizar o try except.

## Exemplo

Vamos supor que em nossa aplicação queremos levantar um erro caso seja passado um ```age``` negativo e queremos tratá-lo retornando uma mensagem adequada. Para isso customizaremos esse tipo de erro criando uma classe ```NegativeAgeError``` herdando de ```APIException``` em um arquivo chamado **exceptions.py**.

```python
from rest_framework.exceptions import APIException

class NegativeAgeError(APIException):
    status_code = 400
    default_detail = "O campo 'age' não pode ser negativo"
```

OBS:
- **status_code**: Atributo vindo da herança utilizado para setar o status code.
- **default_detail**: Atributo vindo da herança utilizado para definir a mensagem de erro.

dasdsadsada