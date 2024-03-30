import random
from datetime import datetime, timedelta

# Define the categories
categories = [
    "Enforced Ceiling Category",
    "Office Supplies from Office Depot",
    "Tech Gadgets from Best Buy",
    "Groceries from Trader Joe's",
    "All other Walmart spend",
    "Dining Out",
    "Gasoline",
    "Home Improvement from Home Depot",
    "Clothing from Macy's",
    "Entertainment",
    "Travel Expenses",
    "Healthcare",
    "Pet Supplies"
]

# Define the start and end dates
start_date = datetime(2018, 11, 1)
end_date = datetime(2023, 12, 31)

# Calculate the number of days between start and end dates
total_days = (end_date - start_date).days

# Create a dictionary to hold the total spend per category
total_spend = {category: 0 for category in categories}

# Ensure "Enforced Ceiling Category" totals $25,000
total_spend["Enforced Ceiling Category"] = 25000

# Generate random spend amounts for other categories
for category in categories:
    if category != "Enforced Ceiling Category":
        total_spend[category] = random.randint(1000, 50000)

# Generate the expense report
expense_report = []
current_date = start_date
while current_date <= end_date:
    for category in categories:
        # Randomly decide if there was spend on this category on this day
        if random.choice([True, False]):
            # Generate a random spend amount for the day
            daily_spend = round(random.uniform(5, 500), 2)
            # Ensure we don't exceed the total spend for the category
            if total_spend[category] - daily_spend >= 0:
                total_spend[category] -= daily_spend
                expense_report.append({
                    "Date": current_date.strftime("%Y-%m-%d"),
                    "Category": category,
                    "Amount ($)": daily_spend
                })
    # Move to the next day
    current_date += timedelta(days=1)

# Print the expense report
for entry in expense_report:
    print(f"{entry['Date']}, {entry['Category']}, {entry['Amount ($)']}")
    