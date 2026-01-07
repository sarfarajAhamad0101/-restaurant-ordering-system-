menu = {
    "Pizza": 80,
    "Red Pasta": 60,
    "White Pasta": 55,
    "Salad": 70,
    "Burger": 60
}

print("🍽️ Welcome to Our Restaurant 🍽️")
print("\n----- MENU -----")
for item, price in menu.items():
    print(f"{item}: Rs{price}")
print("----------------")

order_total = 0
ordered_items = []

while True:
    item = input("\nEnter item name to order: ").title()
    
    if item in menu:
        order_total += menu[item]
        ordered_items.append(item)
        print(f"✅ {item} added to your order")
    else:
        print("❌ Item not available")

    choice = input("Do you want to add another item? (Yes/No): ").title()
    if choice != "Yes":
        break

print("\n🧾 ----- BILL -----")
for item in ordered_items:
    print(f"{item}: Rs{menu[item]}")

print("------------------")
print(f"💰 Total Amount: Rs{order_total}")
print("🙏 Thank you for visiting!")
