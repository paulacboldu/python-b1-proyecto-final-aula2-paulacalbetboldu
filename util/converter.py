from abc import ABC, abstractmethod
from users import Cashier, Customer
from products import Hamburger, Soda, Drink, HappyMeal

class Converter(ABC):
  @abstractmethod
  def convert(self, dataFrame, *args) -> list:
    pass  
  def print(self, objects):
    for item in objects:
      print(item.describe())

class CashierConverter(Converter):
  def convert(self, dataFrame):
    cashiers = []
    for _, row in dataFrame.iterrows():
      cashier = Cashier(
        name=row["name"],
        dni=row["dni"],
        age=int(row["age"]),
        timeTable=row["timetable"],
        salary=float(row["salary"])
      )
      cashiers.append(cashier)
    return cashiers

class CustomerConverter(Converter):
  def convert(self, dataFrame):
    customers = []
    for _, row in dataFrame.iterrows():
      customer = Customer(
        name=row["name"],
        dni=row["dni"],
        age=int(row["age"]),
        email=row["email"],
        postalCode=row["postalcode"]
      )
      customers.append(customer)
    return customers

class ProductConverter(Converter):
  def convert(self, dataFrame, product_type: str):
    products = []

    for _, row in dataFrame.iterrows():
      if product_type == "hamburger":
        product = Hamburger(row["id"], row["name"], float(row["price"]))
      elif product_type == "soda":
        product = Soda(row["id"], row["name"], float(row["price"]))
      elif product_type == "drink":
        product = Drink(row["id"], row["name"], float(row["price"]))
      elif product_type == "happy_meal":
        product = HappyMeal(row["id"], row["name"], float(row["price"]))
      else:
        raise ValueError("Unknown product type")

      products.append(product)

    return products