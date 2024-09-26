import json
import os
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

# Database connection
engine = create_engine('postgresql://ricardo:3136@localhost/library')
Base = declarative_base()

# Define the CreditCardExpense class (new table)


class CreditCardExpense(Base):
    __tablename__ = 'credit_card_expenses'
    id = Column(Integer, primary_key=True)
    purchase_date = Column(String, nullable=False)
    card_name = Column(String, nullable=False)
    card_last_digits = Column(Integer, nullable=False)
    category = Column(String, nullable=False)
    description = Column(String, nullable=False)
    installment = Column(String, nullable=True)
    value_usd = Column(Float, nullable=False)
    exchange_rate = Column(Float, nullable=False)
    value_brl = Column(Float, nullable=False)


# Create session
Session = sessionmaker(bind=engine)
session = Session()


def run():
    # Create the table if it doesn't exist
    Base.metadata.create_all(engine)

    # Define the path to the JSON file
    json_file_path = os.path.expanduser(
        '~/code/statistic/src/credit_card/json/2024-04.json')

    # Load the JSON data (assuming it's a list of dictionaries)
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    # Loop through the list of expenses and insert each into the database
    for expense_data in data:

        if expense_data["Descrição"] == "Inclusao de Pagamento    ":
            continue

        expense = CreditCardExpense(
            purchase_date=expense_data["Data de Compra"],
            card_name=expense_data["Nome no Cartão"],
            card_last_digits=expense_data["Final do Cartão"],
            category=expense_data["Categoria"],
            description=expense_data["Descrição"],
            installment=expense_data["Parcela"],
            value_usd=expense_data["Valor (em US$)"],
            exchange_rate=expense_data["Cotação (em R$)"],
            value_brl=expense_data["Valor (em R$)"]
        )
        session.add(expense)

    # Commit the session to save all the data
    session.commit()

    # Query and print all expenses
    expenses = session.query(CreditCardExpense).all()
    for expense in expenses:
        print(
            f'Expense: {expense.description}, Value (BRL): {expense.value_brl}, Purchase Date: {expense.purchase_date}')

    # Close the session
    session.close()


run()
