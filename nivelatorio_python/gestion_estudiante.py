import datetime


product_fields = ["title", "author", "category", "price", "stock"]
products = {}  # Diccionario para productos 
sales = []     # Lista para ventas 

# Funciones auxiliares 
def generate_product_id():
    # Genera un ID único para el producto 
    return f"P{len(products) + 1:03d}"

def validate_positive_float(prompt):
    # Valida que sea un número positivo flotante
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                raise ValueError("Debe ser un número positivo")
            return value
        except ValueError as e:
            print(f"Error: {e}")

def validate_positive_int(prompt):
    # Valida que sea un entero positivo 
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                raise ValueError("Debe ser un número entero positivo ")
            return value
        except ValueError as e:
            print(f"Error: {e}")

# Gestión de inventario 
def add_product():
    print("\n--- Agregar producto ---")
    product_id = generate_product_id()
    title = input("Título : ")
    author = input("Autor : ")
    category = input("Categoría : ")
    price = validate_positive_float("Precio : ")
    stock = validate_positive_int("Cantidad en stock : ")

    products[product_id] = {
        "title": title,
        "author": author,
        "category": category,
        "price": price,
        "stock": stock
    }
    print(f"Producto '{title}' agregado con ID: {product_id} ")

def update_product():
    print("\n--- Actualizar producto ---")
    pid = input("Ingrese el ID del producto : ")
    if pid in products:
        print(f"Actualizando '{products[pid]['title']}'  ")
        products[pid]["price"] = validate_positive_float("Nuevo precio : ")
        products[pid]["stock"] = validate_positive_int("Nuevo stock : ")
        print("Producto actualizado.")
    else:
        print("Producto no encontrado ")

def delete_product():
    print("\n--- Eliminar producto ---")
    pid = input("ID del producto : ")
    if pid in products:
        del products[pid]
        print("Producto eliminado.")
    else:
        print("Producto no encontrado ")

def list_products():
    print("\n--- Lista de productos  ---")
    if not products:
        print("No hay productos registrados")
    else:
        for pid, p in products.items():
            print(f"{pid}: {p['title']} por {p['author']} | {p['category']} | ${p['price']} | Stock: {p['stock']}")

# Registro de ventas 
# validar que el id si esta 
def register_sale():
    print("\n--- Registrar venta ")
    customer = input("Nombre del cliente : ")
    list_products()
    pid = input("ID del producto : ")
    if pid not in products:
        print("ID no válido")
        return

    product = products[pid]
    quantity = validate_positive_int("Cantidad : ")
    if quantity > product["stock"]:
        print("¡Stock insuficiente!")
        return

    discount = validate_positive_float("Descuento (%) [0 si no aplica] : ")

    date = datetime.datetime.now().strftime("%Y-%m-%d")
    total_price = product["price"] * quantity
    discounted_price = total_price * (1 - discount / 100)

    # Registrar venta 
    sales.append({
        "customer": customer,
        "product_id": pid,
        "title": product["title"],
        "author": product["author"],
        "quantity": quantity,
        "price": product["price"],
        "discount": discount,
        "date": date,
        "net_price": discounted_price
    })

    # Actualizar stock 
    product["stock"] -= quantity

    print(f"Venta registrada: {quantity} x {product['title']} con {discount}% de descuento.")

def view_sales():
    print("\n--- Historial de ventas ---")
    if not sales:
        print("No hay ventas registradas ")
    else:
        for s in sales:
            print(f"{s['date']} | {s['customer']} compro {s['quantity']} x {s['title']} por ${s['net_price']:.2f} (Descuento: {s['discount']}%)")

# Modulo de reportes 
def top_3_products():
    print("\n--- Top 3 productos más vendidos ---")
    stats = {}
    for s in sales:
        stats[s["product_id"]] = stats.get(s["product_id"], 0) + s["quantity"]
    top = sorted(stats.items(), key=lambda x: x[1], reverse=True)[:3]
    for pid, qty in top:
        print(f"{products[pid]['title']} - {qty} vendidos ")

def sales_by_author():
    print("\n--- Ventas por autor ---")
    authors = {}
    for s in sales:
        authors[s["author"]] = authors.get(s["author"], 0) + s["net_price"]
    for author, total in authors.items():
        print(f"{author}: ${total:.2f}")

def calculate_revenue():
    print("\n--- Ingresos  ---")
    gross = sum(s["price"] * s["quantity"] for s in sales)
    net = sum(s["net_price"] for s in sales)
    print(f"Ingreso bruto : ${gross:.2f}")
    print(f"Ingreso neto (después de descuentos): ${net:.2f}")

# Menu principal 
def main_menu():
    while True:
        print("\n----Sistema de Librería ----")
        print("1. Agregar producto ")
        print("2. Actualizar producto ")
        print("3. Eliminar producto ")
        print("4. Listar productos ")
        print("5. Registrar venta ")
        print("6. Ver ventas ")
        print("7. Top 3 más vendidos ")
        print("8. Ventas por autor ")
        print("9. Reporte de ingresos ")
        print("0. Salir ")
        choice = input("Elige una opcion: ")

        try:
            match choice:
                case "1": add_product()
                case "2": update_product()
                case "3": delete_product()
                case "4": list_products()
                case "5": register_sale()
                case "6": view_sales()
                case "7": top_3_products()
                case "8": sales_by_author()
                case "9": calculate_revenue()
                case "0":
                    print("¡Hasta pronto! ")
                    break
                case _: print("Opción inválida ")
        except Exception as e:
            print(f"Ocurrió un error inesperado : {e}")

# Datos iniciales 
def preload_products():
    sample = [
        {"title": "Python 101", "author": "John Smith", "category": "Programming", "price": 25.99, "stock": 10},
        {"title": "Digital Marketing", "author": "Alice Brown", "category": "Business", "price": 19.99, "stock": 15},
        {"title": "Data Science Basics", "author": "Jane Doe", "category": "Data", "price": 30.00, "stock": 8},
        {"title": "AI Revolution", "author": "Dr. Tech", "category": "Technology", "price": 40.50, "stock": 5},
        {"title": "History of Art", "author": "L. Vinci", "category": "Art", "price": 22.75, "stock": 12}
    ]
    for p in sample:
        pid = generate_product_id()
        products[pid] = p

# Ejecución principal
if __name__ == "__main__":
    preload_products()  # Cargar productos iniciales
    main_menu()         # Iniciar menú 