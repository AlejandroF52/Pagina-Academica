from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required
from . import shop_bp
from ..models import Product
from ..extensions import db

@shop_bp.route('/shop')
@login_required
def shop():
    products = Product.query.all()
    return render_template('shop.html', products=products)

@shop_bp.route('/shop/add', methods=['GET', 'POST'])
@login_required
def add_product():
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        price = request.form.get('price')
        image_url = request.form.get('image_url')

        # Validaciones básicas
        if not name or not price or not image_url:
            flash('Por favor, completa todos los campos obligatorios.', 'warning')
            return redirect(url_for('shop.add_product'))

        new_product = Product(
            name=name,
            description=description,
            price=float(price),
            image_url=image_url
        )
        db.session.add(new_product)
        db.session.commit()
        flash('Producto agregado correctamente.', 'success')
        return redirect(url_for('shop.shop'))

    return render_template('add_product.html')

@shop_bp.route('/shop/delete/<int:product_id>', methods=['POST'])
@login_required
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    flash('Producto eliminado correctamente.', 'success')
    return redirect(url_for('shop.shop'))

@shop_bp.route('/shop/update/<int:product_id>', methods=['GET', 'POST'])
@login_required
def update_product(product_id):
    product = Product.query.get_or_404(product_id)
    if request.method == 'POST':
        product.name = request.form['name']
        product.description = request.form['description']
        product.price = float(request.form['price'])
        product.image_url = request.form['image_url']
        db.session.commit()
        flash('Producto actualizado correctamente.', 'success')
        return redirect(url_for('shop.shop'))
    return render_template('update_product.html', product=product)
