# Employee application

This is a Python web application with Flask, managing employees.

* Language: Python 3
* Framework: Flask
* Web application
* VCS: GitHub

Employee entity has an id and a name.

This application has a HTML UI and a REST API.

Use Postgresql.

```sh
docker run -d -e POSTGRES_DB=employees -e POSTGRES_USER=employees  -e POSTGRES_PASSWORD=employees  -p 5432:5432  --name employees-postgres postgres
```

```python
print("Hello World")
```
