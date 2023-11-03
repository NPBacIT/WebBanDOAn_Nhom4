from fdmgmt.utils import utils

import json
from flask import Flask, request, jsonify
app = Flask(__name__)

db_utils = utils.DatabaseUtils()

@app.route('/v1/items', methods=['GET'])
def get_all_items():
    data = request.get_json()
    if data:
        payload = {
            'table_name': data.get('table_name')
        }
        if not payload:   
            return jsonify({'error': 'Missing required parameters'}), 400
        else:
            items = db_utils.get_all_items(table_name=data.get('table_name'))
            return jsonify(items)
    else:
        return jsonify({'error': 'table_name not provided in payload'}), 400

@app.route('/v1/item', methods=['GET'])
def get_item():
    data = request.get_json()
    if data:
        payload = {
            'table_name': data.get('table_name'),
            'item_key': data.get('item_key'),
            'item_value': data.get('item_value')
        }
        if not payload:   
            return jsonify({'error': 'Missing required parameters'}), 400
        else:
            items = db_utils.get_item(table_name=data.get('table_name'), 
                                    item_key=data.get('item_key'), 
                                    item_id=data.get('item_id'))
            return jsonify(items)
    else:
        return jsonify({'error': 'Invalid JSON data in request'}), 400

if __name__ == '__main__':
    app.run(debug=True, host='103.69.195.147', port=5000)
