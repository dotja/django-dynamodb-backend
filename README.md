# Django with a DynamoDB backend

An example project for using Django with DynamoDB on the backend.


## Steps:

### Spin up a DynamoDB docker container
```docker run -p 8000:8000 -d amazon/dynamodb-local```


### Create a DynamoDB table
```python dynamodb_migrator.py```

### View the database table
```aws dynamodb list-tables --endpoint-url http://localhost:8000```

### Run the Django project
```python manage.py runserver 8080```

### Show database table content
```aws dynamodb scan --table-name my-table --endpoint-url http://localhost:8000```

