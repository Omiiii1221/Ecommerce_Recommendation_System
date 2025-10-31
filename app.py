from flask import Flask, render_template, url_for # type: ignore
import pickle
import os

app = Flask(__name__)

MODEL_PATH = r"C:\Users\gaikw\Downloads\e_com_data.csv\models"

with open(f"{MODEL_PATH}/co_purchase.pkl", "rb") as f:
    collab_df = pickle.load(f)

with open(f"{MODEL_PATH}/content.pkl", "rb") as f:
    content_df = pickle.load(f)

with open(f"{MODEL_PATH}/products.pkl", "rb") as f:
    products = pickle.load(f)

PLACEHOLDER_DIR = os.path.join(app.static_folder, 'images', 'placeholders')
PLACEHOLDER_IMAGES = [] # Initializing an empty list

try:
    if os.path.exists(PLACEHOLDER_DIR):
        # allowed image extensions
        allowed_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.webp')
        PLACEHOLDER_IMAGES = [
            f for f in os.listdir(PLACEHOLDER_DIR)
            if os.path.isfile(os.path.join(PLACEHOLDER_DIR, f)) and f.lower().endswith(allowed_extensions)
        ]
except Exception as e:
    print(f"Error scanning placeholder directory: {e}")

if not PLACEHOLDER_IMAGES:
    print("Warning: No placeholder images found or directory is missing. Using default image.")


def hybrid_recommend(product_name, top_n=5, alpha=0.5):
    if product_name not in content_df.index or product_name not in collab_df.columns:
        return []

    content_scores = content_df[product_name]
    collab_scores = collab_df[product_name]

    hybrid_scores = alpha * content_scores + (1 - alpha) * collab_scores
    hybrid_scores = hybrid_scores.drop(product_name, errors='ignore') 
    top_products = hybrid_scores.sort_values(ascending=False).head(top_n)
    return list(top_products.index)

def get_image_path(product_name):
    if PLACEHOLDER_IMAGES:
        image_index = hash(product_name) % len(PLACEHOLDER_IMAGES)
        image_filename = PLACEHOLDER_IMAGES[image_index]
        return url_for("static", filename=f"images/placeholders/{image_filename}")
    else:
        return url_for("static", filename="images/default.jpg")


@app.route("/")
def index():
    unique_products = products["Description"].drop_duplicates().sample(n=25).tolist()
    products_list = [{"name": p, "img": get_image_path(p)} for p in unique_products]
    return render_template("index.html", products=products_list)

@app.route("/product/<product_name>")
def product_detail(product_name):
    recommendations = hybrid_recommend(product_name, top_n=5)
    rec_data = [{"name": r, "img": get_image_path(r)} for r in recommendations]
    details = {
        "name": product_name,
        "img": get_image_path(product_name),
        "price": round(abs(hash(product_name)) % 999 + 99, 2), 
        "desc": f"Discover the excellent quality of the {product_name}. This item is a customer favorite, known for its durability and unique design. Perfect for enhancing your daily life or as a thoughtful gift."
    }
    return render_template("product.html", details=details, recommendations=rec_data)


if __name__ == "__main__":
    app.run(debug=True)