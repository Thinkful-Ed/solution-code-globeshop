# GlobeShop Recommendation System

This repository offers a product recommendation system using the Surprise library and Flask. The system suggests products to users based on:

- **User Ratings**: Historical ratings provided by users for various products.
- **Purchase History**: Records of products purchased by users over time.

## Installation

1. Clone this repository.

2. Navigate to the project directory:

   ```bash
   cd globeshop-recommendation-system
   ```

3. Set up a virtual environment (recommended). Depending on your OS, use one of the following:

   - macOS and Linux:
     ```bash
     python3 -m venv globeshop-recommendation-system-venv;
     source globeshop-recommendation-system-venv/bin/activate;
     ```

   - Windows:
     ```bash
     python -m venv globeshop-recommendation-system-venv
     .\globeshop-recommendation-system-venv\Scripts\activate
     ```

4. Install the required packages:

   ```bash
   pip install flask pandas surprise;
   ```

5. Run the API:

   ```bash
   python globalshop.py
   ```

   By default, the API will start on `http://127.0.0.1:5001`

## API Descriptions

1. Recommendation API (`globalshop.py`):

   - Get product recommendations for a specific user: `GET /recommendations/<user_id>`
   - Index page: `GET /`

## Dataset Descriptions

- **user_behavior.csv**: Contains user ratings for products.
  - Columns: `user_id`, `product_id`, `rating`

- **purchase_history.csv**: Contains records of user purchases.
  - Columns: `user_id`, `product_id`, `purchase_date`

## Notes

Ensure the dataset files (`user_behavior.csv` and `purchase_history.csv`) are in the same directory as the `globalshop.py` file before running the API.