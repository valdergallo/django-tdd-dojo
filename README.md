## What To Test?

Another common setback for developers/designers new to testing is the question
of "what should (or shouldn't) I test?" While there are no hard & fast rules
here that neatly apply everywhere, there are some general guidelines I can offer
on making the decision:

If the code in question is a built-in Python function/library, don't test it.
Examples like the datetime library. If the code in question is built into Django,
don't test it. Examples like the fields on a Model or testing how the built-in
template.Node renders included tags.
If your model has custom methods, you should test that, usually with unit tests.
Same goes for custom views, forms, template tags, context processors, middleware,
management commands, etc. If you implemented the business logic, you should test
your aspects of the code. Another upfront question is "how far down do you go?"
Again, there's no right answer here, save for "where am I comfortable?" If you
start mumbling "yo dawg..." under your breath or humming the tune of the
INCEPTION theme, you know you've probably gone too far. :D


## When Should You Test?

Another point of decision is deciding whether to do test-first (a.k.a. Test
Driven Development) or test-after. Test-first is where you write the necessary
tests to demonstrate proper behavior of the code BEFORE you write the code to
solve the problem at hand. Test-after is when you've already written the code to
solve the problem, then you go back & create tests to make sure the behavior of
the code you wrote is correct.

This choice comes down to personal preference. An advantage of test-driven
development is that it forces you to not skimp on the tests & think about the
API up front. However, it feels very unnatural at first & if you have no
experience writing tests, you may be at a loss as to what to do. Test-after
feels more natural but can lead to weak tests if they're hurried & not given
the proper time/effort.

Something that is always appropriate, regardless of general style, is when you
get a bug report. ALWAYS create a test case first & run your tests. Make sure
it demonstrates the failure, THEN go fix the bug. If your fix is correct, that
new test should pass! It's an excellent way to sanity check yourself & is a
great way to get started with testing to boot.


## Types Of Testing

There are many different types of testing. The prominent ones this series will
cover are unit tests and integration tests.

Unit tests cover very small, highly-specific areas of code. There's usually
relatively few interactions with other areas of the software. This style of
testing is very useful on critical, complicated components, such as validation,
importing or methods with complex business logic.

Integration tests are at the opposite end of the spectrum. These tests usually
cover multiple different facets of the application working together to produce a
result. They ensure that data flow is right & often handle multiple user
interactions.

The main difference between these two types is not the tooling but the approach
and what you choose to test. It's also a very common thing to mix & match these
two types throughout your test suite as it is appropriate.

#### References

[Toast Drive TDD](http://toastdriven.com/blog/2011/apr/10/guide-to-testing-in-django/)

[Django Test](https://docs.djangoproject.com/en/1.8/topics/testing/tools/)

[Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

[Coding Dojo e TDD](https://alextercete.wordpress.com/2009/09/11/apresentacao-sobre-coding-dojo-e-tdd-na-chemtech/)

[DojoPuzzles](http://dojopuzzles.com/problemas/exibe/caixa-eletronico/)

[RealPython TDD with Django](https://realpython.com/blog/python/testing-in-django-part-1-best-practices-and-examples/)

[Python Test Tools](https://wiki.python.org/moin/PythonTestingToolsTaxonomy)

[TDD Django Tutorial Functional Tests](http://www.tdd-django-tutorial.com/tutorial/1/)
