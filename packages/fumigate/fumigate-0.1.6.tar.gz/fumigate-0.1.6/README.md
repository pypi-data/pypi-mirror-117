Fumigate

A small demo library to help in NLP's most tedious task text cleaning.

Installation
pip install -i https://test.pypi.org/simple/ fumigate
#Get started
How to fumigate(clean) your text data

    1.  from fumigate import Fumes

    2. Instantiate a Fumes object
        fumes = Fumes()

    3. Call the purge method
        result = fumes.purge(<text>)