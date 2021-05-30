"""
    AUTHOR: GAUTAM CHANDRA SAHA
    DATE & TIME: 30/05/21 AT 6:08 PM

"""

from flask import Flask, jsonify, request, render_template

stores = [
    {
        "name": "J c Saha Store",
        "items": [
            {"name": "dal", "price": 100},
            {"name": "oil", "price": 200},
            {"name": "rice", "price": 300},
        ]
    },
    {
        "name": "D c Saha Store",
        "items": [
            {"name": "biscuit", "price": 40},
            {"name": "drinks", "price": 50},
            {"name": "dry fruits", "price": 600},
        ]

    }
]


def main():
    app = Flask(__name__)
    port = 5000

    # create the end points
    @app.route('/')
    def home():
        f"Welcome to our store! Goto http://127.0.0.1:{port}/store"

        return render_template("index.html")

    # POST for /store
    @app.route('/store', methods=["POST"])
    def create_store():
        request_data = request.get_json()
        new_store = {
            "name": request_data["name"],
            "items": []
        }
        stores.append(new_store)

        return jsonify(new_store)

    # GET for /store
    @app.route('/store')
    def get_stores():
        return jsonify({"stores": stores})

    # GET for /store/<string:name>
    @app.route('/store/<string:name>')
    def get_store(name):
        for store in stores:
            if store["name"] == name:
                return jsonify(store)

        return jsonify({'ERROR': 'Store not found'})

    # POST for /store/<string:name>/item
    @app.route('/store/<string:name>/item', methods=["POST"])
    def create_item_for_store(name):
        request_data = request.get_json()

        for store in stores:
            if name == store["name"]:
                new_item = {
                    "name": request_data["name"],
                    "price": request_data["price"],
                }
                store["items"].append(new_item)
                return jsonify(store)

        return jsonify({'ERROR': 'Store not found'})

    # GET for /store/<string:name>/item
    @app.route('/store/<string:name>/item')
    def get_item_from_store(name):
        for store in stores:
            if store["name"] == name:
                return jsonify(store["items"])

        return jsonify({'ERROR': 'Store not found'})

    # run the app on port
    app.run(port=port)


if __name__ == '__main__':
    main()
