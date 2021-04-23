# emaillab

Test driven development ["TDD"] of an email client.

<!-- TOC -->

- [emaillab](#emaillab)
  - [TL;DR](#tldr)
  - [Project](#project)
  - [Project Structure](#project-structure)
  - [Test Driven Development](#test-driven-development)
  - [Usage](#usage)

<!-- /TOC -->

## TL;DR

![Example Usage](demo.gif)

## Project

Create a CLI tool that we can use to easily send an email via SMTP. The CLI checks if the config file `emaillab.yml` exists. Otherwise it will prompt the user to create a new config file, and asks the user for these required fields (unless specified otherwise):

1. user name
2. user email
3. user password
4. smtp url (default: smtp.gmail.com)
5. smtp port (default: 465)
6. addressee to
7. addressee subject
8. addressee body (type | for multi line)
9. addressee attachment (optional)

---
## Project Structure
     emaillab/                        <-- Root of your project
       |- .gitignore                  <-- GitHub ignore 
       |- demo.gif                    <-- GIF example usage used by README.md
       |- Makefile                    <-- Make 
       |- Pipfile                     <-- Pipenv 
       |- Pipfile.lock                <-- Pipenv lock 
       |- README.md                   <-- GitHub README markdown 
       +- src/
          +- emaillab/                <-- Holds any business logic
             |- __init__.py
             |- config.py             <-- Python module to create or load config
             |- emaillab.py           <-- Python module to compose email and interface with smtplib
             |- main.py               <-- Python module to demo the modules
       +- tests/                      <-- Holds any automated tests
          |- test_config.py           <-- Python script to test cli.py

---
## Test Driven Development

For this project, we're using `pytest` as our testing framework. We wrote a line in our `Makefile` that utilizes the `pytest`.

The file `test_config.py` ensures that our `config` module works as expected.

## Usage

To use the CLI tool.

```bash
python src/emaillab/main.py
```

To use these modules within your Python script.

```python
from emaillab import config, emaillab
```