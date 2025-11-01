# E-Commerce Product Recommendation System

**Live Demo:** [http://ec2-54-82-115-45.compute-1.amazonaws.com:5000/](http://ec2-54-82-115-45.compute-1.amazonaws.com:5000/)
**Tech Stack:** Flask • Python • Pickle • AWS EC2

---

## Project Overview

This project is a **Hybrid Product Recommendation System** that combines **content-based filtering** and **collaborative filtering** to recommend products to users. It is built using **Flask** as a lightweight backend framework and deployed on **AWS EC2**.

The app dynamically displays random products, and upon selecting a product, it shows detailed information along with top recommended items that users are likely to co-purchase or find similar.

---

## Features

**Hybrid Recommendation Engine** – Combines collaborative and content-based methods.
**Dynamic Product Display** – Shows random products on the home page.
**Product Details Page** – Displays description, price, and related recommendations.
**Auto Image Handling** – Uses placeholder images dynamically for each product.
**AWS EC2 Hosted** – Easily accessible public demo.

---

## Recommendation Logic

### Hybrid Recommendation Formula

[
\text{Hybrid Score} = \alpha \times \text{Content Score} + (1 - \alpha) \times \text{Collaborative Score}
]

* **Content-based filtering:** Recommends items similar in description or attributes.
* **Collaborative filtering:** Recommends items often bought or viewed together.
* **Alpha (α):** Balances both methods (default = 0.5).

---

## Project Structure

```
 ecom-recommender/
│
├── models/
│   ├── co_purchase.pkl          # Collaborative filtering data
│   ├── content.pkl              # Content similarity data
│   └── products.pkl             # Product information data
│
├── static/
│   └── images/
│       └── placeholders/        # Placeholder product images
│
├── templates/
│   ├── index.html               # Homepage layout
│   └── product.html             # Product details & recommendations page
│
├── app.py                       # Main Flask application
└── README.md                    # Project documentation
```

---

## Installation & Setup

### 1️ Clone the Repository

```bash
git clone https://github.com/yourusername/ecom-recommender.git
cd ecom-recommender
```

### 2️ Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate       # (Linux/Mac)
venv\Scripts\activate          # (Windows)
```

### 3️ Install Dependencies

```bash
pip install flask
```

### 4️ Add Model Files

Place your `co_purchase.pkl`, `content.pkl`, and `products.pkl` files inside the `models/` folder.

### 5️ Run the Application

```bash
python app.py
```

Visit your local app at:
 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## ☁️ Deployment on AWS EC2

### Steps Summary:

1. Launch an EC2 instance (Ubuntu or Amazon Linux).
2. SSH into the instance.
3. Install Python and Flask:

   ```bash
   sudo apt update
   sudo apt install python3-pip -y
   pip3 install flask
   ```
4. Upload your project files to the EC2 instance using `scp` or Git.
5. Run your Flask app:

   ```bash
   python3 app.py
   ```
6. Open port **5000** in your EC2 security group.
7. Access your app using your EC2 public URL:
   **[http://ec2-xx-xx-xx-xx.compute-1.amazonaws.com:5000/](http://ec2-xx-xx-xx-xx.compute-1.amazonaws.com:5000/)**

---

## Example Routes

| Route                     | Description                            |
| ------------------------- | -------------------------------------- |
| `/`                       | Displays 25 random products            |
| `/product/<product_name>` | Shows details and recommended products |

---

## Screenshots

** Home Page**
Displays random products with images.

**Product Details Page**
Shows product description, price, and hybrid recommendations.

---

## Tech Stack

| Layer         | Technology                      |
| ------------- | ------------------------------- |
| Backend       | Flask (Python)                  |
| Model Storage | Pickle (.pkl)                   |
| Hosting       | AWS EC2                         |
| Frontend      | HTML, CSS (via Flask templates) |

---

## Author

**Gaikwad Om**
📧 [gaikwadom465@gmail.com](mailto:gaikwadom465@gmail.com)
🌐 [LinkedIn](https://www.linkedin.com/in/om-gaikwad-a70421310/)
