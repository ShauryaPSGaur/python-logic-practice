"""
Shopping Bill Calculator

This program calculates the final bill based on:
- Product price
- Quantity
- Discount rules:
    > 10000  → 20% discount
    > 5000   → 10% discount
    Otherwise → No discount
"""

# Take user input
product_price = float(input("Enter Product Price: "))
quantity = int(input("Enter Quantity: "))

# Calculate total
total = product_price * quantity

# Initialize discount rate
discount_rate = 0

# Apply discount rules
if total > 10000:
    discount_rate = 0.20
elif total > 5000:
    discount_rate = 0.10

# Calculate discount and final bill
discount_amount = total * discount_rate
final_bill = total - discount_amount

# Display result
print("\n------ BILL SUMMARY ------")
print("Original Total :", total)
print("Discount       :", discount_amount)
print("Final Bill     :", final_bill)
print("---------------------------")
