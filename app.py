from chalice import Chalice

app = Chalice(app_name='aws-lambda-endpoint')

list = [
    {
        "name": "Maça",
        "price": "1.99"
    },
    {
        "name": "Morango",
        "price": "3.99"
    }
]


@app.route('/products', methods=['GET'])
def products():
    return list
