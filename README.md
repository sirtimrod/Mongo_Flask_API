# Mongo_Flask_API


### Requests examples with curl
```bash
# GET request that finds a product by name and parameter
curl -i --location --request GET 'http://127.0.0.1:5000/products' --header 'Content-Type: application/json' --data-raw '{"name": "Macbook PRO", "parameters": {"colore":"grey"}}'

# GET request that finds a product by parameter
curl -i --location --request GET 'http://127.0.0.1:5000/products' --header 'Content-Type: application/json' --data-raw '{"parameters": {"weight":0.12}}'

# GET request that finds a product by name
curl -i --location --request GET 'http://127.0.0.1:5000/products' --header 'Content-Type: application/json' --data-raw '{"name": "iPhone 12"}'

# GET request that finds a product by id
curl -i --location --request GET 'http://127.0.0.1:5000/details' --header 'Content-Type: application/json' --data-raw '{"id": "612e5a59df66d2ab0a02adc4"}'

# POST request that creates new product in DB
curl -i --location --request POST 'http://127.0.0.1:5000/create' --header 'Content-Type: application/json' --data-raw '{"name": "Samsung", "description": "Some new text", "parameters": {"wight": 0.333}}'
```
