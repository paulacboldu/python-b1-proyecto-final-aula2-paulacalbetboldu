import pandas as pd
from users import Cashier, Customer
from products import Hamburger, Soda
from orders import Order
from util.converter import CashierConverter, CustomerConverter, ProductConverter
from util.file_manager import CSVFileManager


def test_order_total_two_products():
    # --- 1. Llegim CSV ---
    cashier_df = CSVFileManager("data/cashiers.csv").read()
    customer_df = CSVFileManager("data/customers.csv").read()
    hamburgers_df = CSVFileManager("data/hamburgers.csv").read()
    sodas_df = CSVFileManager("data/sodas.csv").read()

    # --- 2. Convertim ---
    cashier = CashierConverter().convert(cashier_df)[0]
    customer = CustomerConverter().convert(customer_df)[0]

    product_converter = ProductConverter()
    hamburgers = product_converter.convert(hamburgers_df, "hamburger")
    sodas = product_converter.convert(sodas_df, "soda")

    # Agafem productes concrets (com a l’exemple)
    h1 = next(p for p in hamburgers if p.id == "H1")
    g1 = next(p for p in sodas if p.id == "G1")

    # --- 3. Preparem l'ordre ---
    order = Order(cashier, customer)
    order.add(h1)
    order.add(g1)

    # --- 4. Assertions finals---
    assert len(order.products) == 2
    assert order.calculateTotal() == 12.3


def test_order_show_output(capsys):
    # --- Preparació ---
    cashier_df = CSVFileManager("data/cashiers.csv").read()
    customer_df = CSVFileManager("data/customers.csv").read()
    hamburgers_df = CSVFileManager("data/hamburgers.csv").read()
    sodas_df = CSVFileManager("data/sodas.csv").read()

    cashier = CashierConverter().convert(cashier_df)[0]
    customer = CustomerConverter().convert(customer_df)[0]

    product_converter = ProductConverter()
    products = []
    products += product_converter.convert(hamburgers_df, "hamburger")[:1]
    products += product_converter.convert(sodas_df, "soda")[:1]

    order = Order(cashier, customer)
    for product in products:
        order.add(product)

    # --- Execució ---
    order.show()

    # --- Captura de la sortida ---
    captured = capsys.readouterr().out

    # --- Asserts clau ---
    assert "Hello : Customer - Name:" in captured
    assert "Was attended by : Cashier - Name:" in captured
    assert "Product - Type:" in captured
    assert "Total price :" in captured
