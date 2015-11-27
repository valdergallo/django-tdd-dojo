def calc(x, y):
    """
    Test calc function with doctest
    to execute: python -m doctest -v python_file.py

    >>> calc(1,2)
    3
    >>> calc(2,3)
    1
    >>> calc(1,3)
    4
    """
    soma = x + y
    return soma


# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()
