# globalshop.py
from flask import Flask, request, jsonify
import pandas as pd
user_behavior = pd.read_csv('user_behavior.csv')
purchase_history = pd.read_csv('purchase_history.csv')

from surprise import SVD, Dataset, Reader

# Load data into a Surprise dataset
reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(user_behavior[['user_id', 'product_id', 'rating']], reader)

# Train the SVD model
model = SVD()
trainset = data.build_full_trainset()
model.fit(trainset)

def get_recommendations(user_id, n=5):
    predictions = []
    for product_id in purchase_history['product_id'].unique():
        prediction = model.predict(user_id, product_id)
        predictions.append((int(product_id), float(prediction.est)))
    recommendations = sorted(predictions, key=lambda x: x[1], reverse=True)[:n]
    return recommendations

app = Flask(__name__)

@app.route('/recommendations/<int:user_id>', methods=['GET'])
def recommendations(user_id):
    n = int(request.args.get('n', 5))
    recs = get_recommendations(user_id, n)
    return jsonify(recs)

@app.route('/')
def index():
    return 'GlobeShop Recommendation System'

if __name__ == '__main__':
    app.run(debug=True, port=5001)