# cryptomarkets
API to list the crypto market updates

# Prerequisties

Python 3.7 +

Setup Virtual env(WIndows)

```
    C:\Program Files\Python310>python.exe -m venv D:\projects\env\venv
```

To Activate the Virtual env
```
    cd D:\projects\env\venv
    $ source Scripts/activate
```

Install all the required packages for application

```
    python -m pip install -r requirements.txt
```

Install all the required packages for development with testing and linting packages

```
    python -m pip install -r requirement-dev.txt
```

Rename the `sample.env` to `.env` and update the file with the original values

To start the application
```
    python -m main.py
```

To run the unit tests with coverage

```
    $ python -m coverage run -m pytest tests
```

To generate the HTML reports of coverage
```
    python -m coverage html
```
# Swagger URL:

You will be able to view the swagger [URL](http://localhost:8000/docs) http://0.0.0.0:8000/docs
