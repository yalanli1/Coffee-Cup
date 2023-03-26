from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# describe a coffee cup as an object
# refer to https://www.homegrounds.co/different-coffee-cup-types/
class CoffeeCup:
    def __init__(self, type, size, material, function):
        self.type = type  # e.g. classic mug, travel mug, demitasse, tumbler
        self.size = size  # i.e. measured in oz
        self.material = material  # e.g. ceramic, glass, steel, paper, stoneware
        self.function = function  # e.g. pour-over, retain-heat, double-walled, vintage, cup+plate, personalized

    # use getattr() instead of getters
    
 
# Examples of coffee cups
coffee_cups = [
    CoffeeCup("classic mug", 8, "ceramic", "pull-over"),
    CoffeeCup("travel mug", 15, "plastic", "portable"),
    CoffeeCup("demitasse", 3.4, "ceramic", "pull-over"),
    CoffeeCup("espersso cup", 4, "glass", "double-walled"),
    CoffeeCup("tumbler", 20, "steel", "retain-heat")
]

from flask import Flask

app = Flask(__name__)

# prints all coffee cups
@app.route('/all_cups', methods=['GET'])
def get_all_coffee_cups():
    ret_cups = {}
    for i, c in enumerate(coffee_cups):
        ret_cups[i] = {
            'type': c.type,
            'size': c.size,
            'material': c.material,
            'function': c.function
        }
    return ret_cups

# find a coffee cup by a property
@app.route('/find_cups/<key>=<value>', methods=['GET'])
def find_coffee_cups(key, value):
    ret_cups = {}
    for i, c in enumerate(coffee_cups):
        if getattr(c, key) == value:
            ret_cups[i] = {
                'type': c.type,
                'size': c.size,
                'material': c.material,
                'function': c.function
            }
    return ret_cups

# add a new coffee cup
@app.route('/add_cup', methods=['POST'])
def add_coffee_cup():
    cup = CoffeeCup(request.args.get("type"), request.args.get("size"), request.args.get("material"), request.args.get("function"))
    coffee_cups.append(cup)
    return jsonify({
        'message': 'Successfully created a new coffee cup! Use /all_cups to check the existing cups',
        'data': {
            'type': cup.type,
            'size': cup.size,
            'material': cup.material,
            'function': cup.function
        }
    })


if __name__ == '__main__':
    app.run(debug=True, port=5000)