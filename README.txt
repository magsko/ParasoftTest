#**Parabank Test Suite**


The goal of this project was to practice setting up a testing environment with Selenium and Python and practicing my test automation skills.

## About
The test object of the project is [Parabank](https://parabank.parasoft.com/parabank/index.htm) a demo web banking app by Parasoft.


The project uses Page Object Model (POM) to organize the code.
It is written in python, uses Selenium for browser automation,
pytest for test management and pytest-html for reporting results.


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install selenium
brew cask install chromedriver
pip install -U pytest
pip install Faker
```

## To run
```bash
pytest --html=report.html
```



## License
[MIT](https://choosealicense.com/licenses/mit/)
