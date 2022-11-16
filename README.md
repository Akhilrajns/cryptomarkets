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

Install all the required packages for development/testing

```
    python -m pip install -r requirement-dev.txt
```

Rename the `sample.env` to `.env` and update the file with the original values

To start the application
```
    python -m main.py
```
To run the unit tests

```
    $ pytest
```
