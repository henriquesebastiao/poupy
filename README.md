<h1 align="center">
    <img src="project/utils/img/bitmap.png" alt="Poupy" width="150"/><br>
</h1>

<p align="center"><strong>Manage your personal budget.</strong></p>

<p align="center">
    <a href="https://github.com/henriquesebastiao/poupy/actions/workflows/ci.yml">
        <img src="https://github.com/henriquesebastiao/poupy/actions/workflows/ci.yml/badge.svg" alt="CI status"/>
    </a>
    <a href="https://codecov.io/gh/henriquesebastiao/poupy" > 
        <img src="https://codecov.io/gh/henriquesebastiao/poupy/graph/badge.svg?token=aoIdJEPHV5" alt="Codecov status"/> 
    </a>
    <a href="https://github.com/henriquesebastiao/poupy/blob/main/LICENSE">
        <img alt="LICENSE" src="https://img.shields.io/github/license/henriquesebastiao/poupy"/>
    </a>
</p>

<div align="center">Deploy: <a href="http://server.henriquesebastiao.com:8090/app/login">http://server.henriquesebastiao.com:8090/</a></div>

<div align="center">Demo user:</div>
<div align="center">User: <strong>test</strong></div>
<div align="center">Password: <strong>Test@123</strong></div>

<p align="center">
    <img src="project/utils/img/screenshot.png" alt="Preview"/>
</p>

Poupy is a webapp that allows you to create and manage your own personal budget.
It is a simple and intuitive application that allows you to manage your expenses and income, and also allows you to
create your own categories and subcategories.

## How to execute the project?

```shell
git clone https://github.com/henriquesebastiao/poupy.git
cd poupy
poetry install
export DEBUG="1"
python manage.py migrate
python manage.py runserver
```

Now you must open the project in the browser:

```
http://localhost:8000/
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

