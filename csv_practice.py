# REFLECTION QUESTIONS
#
#1.  Python can automate the process of reading and saving data.
# This is very useful when the same steps need to be done a lot of times or
# with bigger amounts of data. Excel is more visual and makes it easier to
# see data and use spreadsheets.
#
# 2. A business could use append mode to track their daily sales in the report.
# Every time someone makes a report, Python can add the date and total
# sales to a log file without deleting the old records. This helps the person
# keep their history of sales.

import csv
from datetime import datetime

# EXERCISE 2: Read and print raw rows
print("\n--- EXERCISE 2 ---")

with open("data/sales.csv", "r", newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)


# EXERCISE 3: Skip the header
print("\n--- EXERCISE 3 ---")

with open("data/sales.csv", "r", newline="") as file:
    reader = csv.reader(file)

    header = next(reader)
    print("Header:", header)

    for row in reader:
        print(row)


# EXERCISE 4: Compute totals
print("\n--- EXERCISE 4 ---")

total_revenue = 0

with open("data/sales.csv", "r", newline="") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])

        total = price * quantity
        total_revenue += total

        print(f"{product}: {quantity} units × ${price:.2f} = ${total:.2f}")

print(f"\nTotal revenue: ${total_revenue:.2f}")


# EXERCISE 5: Filter and write
print("\n--- EXERCISE 5 ---")

original_count = 0
written_count = 0

with open("data/sales.csv", "r", newline="") as infile:
    reader = csv.reader(infile)
    next(reader)

    with open("data/cleaned.csv", "w", newline="") as outfile:
        writer = csv.writer(outfile)

        writer.writerow(["Product", "Price", "Qty", "Total"])

        for row in reader:
            original_count += 1

            product = row[0]
            price = float(row[1])
            quantity = int(row[2])

            total = price * quantity

            if total > 100:
                writer.writerow([product, price, quantity, total])
                written_count += 1

print(f"Rows written: {written_count}")
print(f"Original rows: {original_count}")


# EXERCISE 6: csv.DictReader
print("\n--- EXERCISE 6 ---")

dict_total_revenue = 0

with open("data/sales.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        total = price * quantity
        dict_total_revenue += total

        print(f"{product}: ${total:.2f}")

print(f"Total revenue using DictReader: ${dict_total_revenue:.2f}")

# csv.reader uses column positions, such as row[0], and is useful for simple CSV files.
# DictReader uses column names, making the code easier to understand when working with named columns.


# EXERCISE 7: Sales summary by product
print("\n--- EXERCISE 7 ---")

sales_summary = {}

with open("data/sales.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        total = price * quantity

        if product in sales_summary:
            sales_summary[product] += total
        else:
            sales_summary[product] = total

for product in sorted(sales_summary):
    print(f"{product}: ${sales_summary[product]:.2f}")

# EXERCISE 8: Create a run log
print("\n--- EXERCISE 8 ---")

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("data/run_log.txt", "a") as log_file:
    log_file.write(f"{timestamp} - Total revenue: ${total_revenue:.2f}\n")

print("Run logged successfully.")
