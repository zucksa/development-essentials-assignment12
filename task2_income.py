# Assignment 12 - Task 2
# NumPy arrays and income calculations

import numpy as np

months = [
    "Jan", "Feb", "Mar", "Apr", "May",
    "Jun", "Jul", "Aug", "Sep", "Oct"
]

# Income of 3 departments for 10 months (EUR)
income = np.array([
    [12000, 13500, 12800, 15000, 16000,
     15500, 17000, 18000, 17500, 19000],

    [9500, 10000, 11000, 10500, 12000,
     12500, 13000, 14000, 14500, 15000],

    [18000, 17500, 19000, 20000, 21000,
     22000, 21500, 23000, 24000, 25000]
])

print("--- Original Income ---")
print("Months:", months)
print(income)

print("\n--- Array Information ---")
print("Array type:", type(income))
print("Array shape:", income.shape)
print("Number of dimensions:", income.ndim)

# Tax calculation: 30%
tax_rate = 0.30
net_income = income * (1 - tax_rate)

print("\n--- Net Income After 30% Tax ---")
print(net_income)

print("\n--- Example Calculation ---")
print("Department 1, January income:", income[0, 0])
print("Tax rate:", tax_rate)
print("Net income:", net_income[0, 0])

# Updated tax rates and second quarter calculations

print("\n--- Updated Tax Rates ---")

tax_rates = np.full(10, 0.30)
tax_rates[4:7] = 0.40

print("Months:", months)
print("Tax rates (%):", tax_rates * 100)

print("\n--- Updated Net Income ---")

updated_net_income = income * (1 - tax_rates)
print(updated_net_income)

print("\n--- Second Quarter (Apr, May, Jun) ---")

q2_months = months[3:6]
q2_income = income[:, 3:6]
q2_net_income = updated_net_income[:, 3:6]

print("Months:", q2_months)

print("\nOriginal income for Q2:")
print(q2_income)

print("\nNet income for Q2:")
print(q2_net_income)

# Total net income for the second quarter
q2_totals = q2_net_income.sum(axis=1)

print("\n--- Total Net Income by Department for Q2 ---")

for department, total in enumerate(q2_totals, start=1):
    print(f"Department {department}: {total:.2f} EUR")


# Total net income for all 10 months
total_net_income = updated_net_income.sum(axis=1)

print("\n--- Total Net Income for 10 Months ---")

for department, total in enumerate(total_net_income, start=1):
    print(f"Department {department}: {total:.2f} EUR")
