Os testes garatem a consistência do código em futuras modificações

- Erros de implementação de novas funcionálidades
- Correções ou alteração em aplicação já existentes
- Garante a consistência de uma história ou tarefa
- Podem ser utilizados como documentação
- Evita reversão de código
- NÃO CORRIGEM BUGS
- NÃO EVITAM BUGS

## O que eu devo testar

- URLs

    Podem ser testadas para evitar erros de URL e para
    garantir que a URL ainda existe e está retornando sempre
    algum valores necessários, testando assim as Views.

- Forms

    Os forms são a abstração dos Models, cabe à eles validar informações
    antes de serem salvas. Sendo assim é importante testar suas validações

- Models
    Apenas em casos onde existe algum tipo de validação ou alteração.
    Nesse caso é possível se utilizar apenas do método full_clean
    para validar os campos.

- Managers

    Nesse caso a base deve conter dados, por fixtures e validados
    os resultados

- TemplateTags

    Toda TemplateTag precisa ser validada e não fazer requisisções
    ao banco de dados

- Validators

    Os validators são uteis para reutilizar as validaçãos de um form.

- Admin

    Algumas pessoas testam a existem do aplicativo no Admin, para garantir
    que ele está registrado no Admin.


-------------------------------------------------------------------------------

The tests ensures consistency of the code in future modifications

- Implementation errors of new features
- Corrections or changes to existing application
- Ensures the consistency of a story or task
- Can be used as documentation
- Prevents reversal code
- DO NOT fix bugs
- NOT AVOID BUGS

## What should I test

- URLs

    May be tested to avoid errors URL and the URL to ensure that still exists
    and is returning always some necessary values, and thus test Views.

- Forms

    The forms are the abstraction of Models, it is up to them to validate
    information before being saved. Therefore it is important to test your
    validations

- Models

    Only in cases where there is some kind of validation or alteration. In
    this case it is possible to use only the full_clean method to validate
    the fields.

- Managers

    In this case the database should contain data, fixtures and validated results

- Templatetags

    All templatetag needs to be validated and do requisisções to the database

- The Validators

    Validators are useful for reusing validaçãos a form.

- Admin

    Some people are testing the application in the Admin to ensure that it is
    registered in the Admin.
