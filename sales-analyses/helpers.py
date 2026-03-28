def calculate_total(quantity, price):
  """Calculate total for a single item"""
  return quantity * price

def format_currency(amount):
  """Formate number as currency"""
  return f"${amount:,.2f}"


calculate_total(5,89)
format_currency(calculate_total(5,89))