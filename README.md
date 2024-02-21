# How to run the project

## Alert
Firstly, you need to have installed **Python** and **Pip** to proceed with the next steps.


**Tip**: Test python in the terminal first with: 
```bash
python3 --version
```
or
```bash
python --version
```

### Use the shell commands below in sequence

Linux:
```bash
git clone https://github.com/JeanFurman/crudcodeleap.git
```
```bash
python3 -m venv venv
```
```bash
source venv/bin/activate
```
```bash
pip install -r requirements.txt
```
```bash
python3 crudcodeleap/manage.py makemigrations
```
```bash
python3 crudcodeleap/manage.py migrate --run-syncdb
```
```bash
python3 crudcodeleap/manage.py runserver
```

Windows:
```bash
git clone https://github.com/JeanFurman/crudcodeleap.git
```
```bash
python3 -m venv venv
```
```bash
cd venv/scripts
```
```bash
activate
```
```bash
cd ..
```
```bash
cd ..
```
```bash
pip install -r requirements.txt
```
```bash
python3 crudcodeleap/manage.py makemigrations
```
```bash
python3 crudcodeleap/manage.py migrate --run-syncdb
```
```bash
python3 crudcodeleap/manage.py runserver
```

## Endpoints

The endpoints for this application are as follows:

- `http://localhost:8000/careers/` - (GET/POST)

- `http://localhost:8000/careers/{id}/` - (GET/PUT/PATCH/DELETE)

With this payload example :

{
    "username": "String2Patch",
    "title": "String2",
    "content": "String2"
}

And if you want to run the tests, use: `python3 crudcodeleap/manage.py test crudcodeleap`
