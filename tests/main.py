"""
This file is used to test that the installation of the contract decorator was
successful.  It will be used to test the package installed on test.pypi.org
and pypi.org.
"""

from contract import contract, checktype

if __name__ == "__main__":
    class Simple(object):
        @contract({'a': [checktype(int)]})
        def check_me(self, a):
            pass


    simple = Simple()
    simple.check_me(101)
    print('Successfully used the contract decorator')
