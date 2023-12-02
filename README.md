<h1 align="center">
    <img src="utils/img/bitmap.png" alt="Poupy" width="150"/>
    <br>
</h1>

<p align="center"><strong>Manage your personal budget.</strong></p>

<p align="center">
  <a href="https://github.com/henriquesebastiao/poupy">
    <img src="https://img.shields.io/badge/Status-development-red" alt="Development status" />
  </a>
  <a href="https://github.com/henriquesebastiao/poupy/actions/workflows/ci.yml">
    <img src="https://github.com/henriquesebastiao/poupy/actions/workflows/ci.yml/badge.svg" alt="CI status"/>
  </a>
  <a href="https://github.com/henriquesebastiao/poupy/blob/main/LICENSE">
    <img alt="LICENSE" src="https://img.shields.io/github/license/henriquesebastiao/poupy"/>
  </a>
</p>

<p align="center">
  <img src="utils/img/screenshot.png" alt="Preview"/>
</p>

Poupy is a webapp that allows you to create and manage your own personal budget.
It is a simple and intuitive application that allows you to manage your expenses and income, and also allows you to
create your own categories and subcategories.

## How to execute the project?
```shell
git clone https://github.com/henriquesebastiao/poupy.git
cd poupy
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
Now you must open the project in the browser:
```
http://localhost:8000/
```


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

