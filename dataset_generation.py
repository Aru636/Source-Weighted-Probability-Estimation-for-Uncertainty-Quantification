import pandas as pd
import numpy as np
import random

# -------------------------------
# Configuration
# -------------------------------
num_entities = 500
attributes = ["children", "net_worth", "age", "country", "marital_status"]

sources = ["Forbes", "Wikipedia", "NewsSite", "BlogX", "RandomSite"]

# Credibility aligned with your SWPE model
source_noise_prob = {
    "Forbes": 0.02,
    "Wikipedia": 0.05,
    "NewsSite": 0.08,
    "BlogX": 0.20,
    "RandomSite": 0.35
}

# -------------------------------
# Helper Functions
# -------------------------------
def generate_true_value(attribute):
    if attribute == "children":
        return random.randint(0, 8)
    elif attribute == "net_worth":
        return random.randint(1, 200) * 1e6
    elif attribute == "age":
        return random.randint(30, 90)
    elif attribute == "country":
        return random.choice(["USA", "UK", "India", "Germany", "France"])
    elif attribute == "marital_status":
        return random.choice(["Married", "Single", "Divorced"])
    else:
        return None


def inject_noise(true_value, attribute):
    if attribute == "children":
        return random.randint(0, 12)
    elif attribute == "net_worth":
        return random.randint(1, 250) * 1e6
    elif attribute == "age":
        return random.randint(25, 95)
    elif attribute == "country":
        return random.choice(["USA", "UK", "India", "Germany", "France", "Canada"])
    elif attribute == "marital_status":
        return random.choice(["Married", "Single", "Divorced", "Widowed"])
    else:
        return true_value

# -------------------------------
# Generate Dataset
# -------------------------------
rows = []

for i in range(num_entities):
    entity_name = f"Person_{i}"
    
    for attr in attributes:
        true_value = generate_true_value(attr)
        
        for source in sources:
            noise_prob = source_noise_prob[source]
            
            if random.random() < noise_prob:
                value = inject_noise(true_value, attr)
            else:
                value = true_value
            
            rows.append({
                "entity": entity_name,
                "attribute": attr,
                "source": source,
                "value": value
            })

df = pd.DataFrame(rows)

# Save to CSV
df.to_csv("multi_source_dataset.csv", index=False)

print("Synthetic dataset generated successfully!")
print("Shape:", df.shape)