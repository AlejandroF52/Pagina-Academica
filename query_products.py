from app import create_app
from app.models import Product

def query_products():
    products = Product.query.all()
    return [(p.id, p.name, p.price, p.image_url) for p in products]

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        products = query_products()
        for product in products:
            print(product)
