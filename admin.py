import matplotlib.pyplot as plt
import pandas as pd

# Sample data for maize production in Kenya (in 1000 metric tonnes)
data = {
    'Year': list(range(2010, 2021)),
    'Maize_Production': [3200, 3400, 3100, 3700, 3900, 4000, 4200, 4100, 4300, 4500, 4700]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Create the plot
fig, ax1 = plt.subplots(figsize=(10, 6))

# Bar chart (Maize Production)
ax1.bar(df['Year'], df['Maize_Production'], color='skyblue', label='Maize Production (Bar)', alpha=0.7)

# Line chart (on the same axis)
ax1.plot(df['Year'], df['Maize_Production'], color='darkblue', marker='o', label='Maize Production (Line)', linewidth=2)

# Labels and title
ax1.set_xlabel('Year')
ax1.set_ylabel('Production (1000 metric tonnes)')
ax1.set_title('Maize Production in Kenya (2010–2020)')
ax1.legend(loc='upper left')
ax1.grid(True, linestyle='--', alpha=0.5)

# Show the plot
plt.tight_layout()
plt.show()
