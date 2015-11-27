Os testes garatem a consistência do código em futuras modificações

- Erros de implementação de novas funcionálidades
- Correções ou alteração em aplicação já existentes
- Garante a consistência de uma história ou tarefa
- Podem ser utilizados como documentação
- Evita reversão de código
- NÃO CORRIGEM BUGS
- NÃO EVITAM BUGS

## O que eu devo testar

- **URLs**

    Podem ser testadas para evitar erros de URL e para
    garantir que a URL ainda existe e está retornando sempre
    algum valores necessários, testando assim as Views.

- **Forms**

    Os forms são a abstração dos Models, cabe à eles validar informações
    antes de serem salvas. Sendo assim é importante testar suas validações

- **Models**
    Apenas em casos onde existe algum tipo de validação ou alteração.
    Nesse caso é possível se utilizar apenas do método full_clean
    para validar os campos.

- **Managers**

    Nesse caso a base deve conter dados, por fixtures e validados
    os resultados

- **TemplateTags**

    Toda TemplateTag precisa ser validada e não fazer requisisções
    ao banco de dados

- **Validators**

    Os validators são uteis para reutilizar as validaçãos de um form.

- **Admin**

    Algumas pessoas testam a existem do aplicativo no Admin, para garantir
    que ele está registrado no Admin.
