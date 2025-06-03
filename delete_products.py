from app import create_app, db
from app.models import Product

def delete_product(product_id):
    app = create_app()
    with app.app_context():
        product = Product.query.get(product_id)
        if not product:
            print(f"❌ Producto con ID {product_id} no encontrado.")
            return False

        confirm = input(f"¿Estás seguro de eliminar el producto '{product.name}'? (s/n): ").strip().lower()
        if confirm != 's':
            print("❌ Operación cancelada.")
            return False

        db.session.delete(product)
        db.session.commit()
        print(f"✅ Producto '{product.name}' eliminado.")
        return True

if __name__ == "__main__":
    try:
        product_id = int(input("ID del producto a eliminar: "))
        delete_product(product_id)
    except ValueError:
        print("❌ ID inválido.")
