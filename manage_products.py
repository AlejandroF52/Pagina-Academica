from app import create_app, db
from app.models import Product

def add_product(name, description, price, image_url):
    app = create_app()
    with app.app_context():
        # (opcional) podrías verificar si ya existe un producto con ese nombre
        existing_product = Product.query.filter_by(name=name).first()
        if existing_product:
            print(f"El producto '{name}' ya existe.")
            return False
        
        new_product = Product(
            name=name,
            description=description,
            price=price,
            image_url=image_url
        )

        db.session.add(new_product)
        db.session.commit()
        print(f"Producto '{name}' agregado correctamente.")
        return True

if __name__ == "__main__":
    name = input("Nombre del producto: ")
    description = input("Descripción: ")
    
    while True:
        try:
            price = float(input("Precio (ej: 49.99): "))
            break
        except ValueError:
            print("❌ Precio inválido. Inténtalo de nuevo.")
    
    image_url = input("URL de la imagen: ")
    add_product(name, description, price, image_url)
