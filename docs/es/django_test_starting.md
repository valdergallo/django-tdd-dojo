The tests ensures consistency of the code in future modifications

- Implementation errors of new features
- Corrections or changes to existing application
- Ensures the consistency of a story or task
- Can be used as documentation
- Prevents reversal code
- DO NOT fix bugs
- NOT AVOID BUGS

## What should I test

- **URLs**

    May be tested to avoid errors URL and the URL to ensure that still exists
    and is returning always some necessary values, and thus test Views.

- **Forms**

    The forms are the abstraction of Models, it is up to them to validate
    information before being saved. Therefore it is important to test your
    validations

- **Models**

    Only in cases where there is some kind of validation or alteration. In
    this case it is possible to use only the full_clean method to validate
    the fields.

- **Managers**

    In this case the database should contain data, fixtures and validated results

- **Templatetags**

    All templatetag needs to be validated and do requisisções to the database

- **The Validators**

    Validators are useful for reusing validaçãos a form.

- **Admin**

    Some people are testing the application in the Admin to ensure that it is
    registered in the Admin.
