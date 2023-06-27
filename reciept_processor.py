from flask import Flask, jsonify, request
import uuid
import re
import math
from datetime import datetime

app = Flask(__name__)

receipts = {}

@app.route('/receipts/process', methods=['POST'])
def process_receipts():

    receipt = request.get_json()
    receipt_id = str(uuid.uuid4())
    points = evaluate_points(receipt)

    receipts[receipt_id] = {
        'receipt': receipt,
        'points': points
    }

    return jsonify({'id': receipt_id})


@app.route('/receipts/<receipt_id>/points', methods=['GET'])
def get_points(receipt_id):

    receipt_data = receipts.get(receipt_id)

    if not receipt_data:
        return jsonify({'error': 'Receipt Does not Exist !!'}), 404
    
    points = receipt_data['points']

    return jsonify({'points': points})


def evaluate_points(receipt):

    points = 0

    points += len(re.sub('[^a-zA-Z0-9]', '', receipt['retailer']))

    if float(receipt['total']) == round(float(receipt['total'])):
        points += 50

    if math.isclose(float(receipt['total']) % 0.25, 0):
        points += 25

    points += (len(receipt['items']) // 2) * 5

    for item in receipt['items']:

        trimmedLength = len(item['shortDescription'].strip())

        if trimmedLength % 3 == 0:
            price = float(item['price'])
            itemPoints = math.ceil(price * 0.2)
            points += itemPoints

    purchaseDate = datetime.strptime(receipt['purchaseDate'], '%Y-%m-%d')

    if purchaseDate.day % 2 != 0:
        points += 6

    purchaseTime = datetime.strptime(receipt['purchaseTime'], '%H:%M')
    afternoonStart = datetime.strptime('14:00', '%H:%M')
    afternoonEnd = datetime.strptime('16:00', '%H:%M')

    if afternoonStart < purchaseTime < afternoonEnd:
        points += 10

    return points

if __name__ == '__main__':
    app.run(host='0.0.0.0')