from fdmgmt.utils import utils

import json
from flask import Flask, request, jsonify

app = Flask(__name__)
db_utils = utils.DatabaseUtils()

@app.route('/v1/items', methods=['GET'])
def get_all_items():
    table_name = request.args.get('table_name')
    if table_name:
        items = db_utils.get_all_items(table_name)
        return items
    else:
        return jsonify({'error': 'missing params'}), 400

@app.route('/v1/item', methods=['GET'])
def get_item():
    data = request.get_json()
    if data:
        items = db_utils.get_item(table_name=data.get('table_name'), 
                                item_key=data.get('item_key'), 
                                item_value=data.get('item_value'))
        return jsonify(items)
    else:
        return jsonify({'error': 'Invalid JSON data in request'}), 400

@app.route('/v1/delete_item', methods=['DELETE'])
def delete_item():
    data = request.get_json()
    if data:
        ok = db_utils.delete_item(table_name=data.get('table_name'), 
                                item_key=data.get('item_key'), 
                                item_value=data.get('item_value'))
        if ok:
            return jsonify({'OK': 'Delete item success'}), 200
        else:
            return jsonify({'error': 'Delete item Failed'}), 400
    else:
        return jsonify({'error': 'Invalid JSON data in request'}), 400

if __name__ == '__main__':
    app.run(debug=True, host='103.69.195.147', port=5000)
