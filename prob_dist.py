import pandas as pd
import numpy as np

# -------------------------------
# Step 1: Load Dataset
# -------------------------------
df = pd.read_csv("multi_source_dataset.csv")

# -------------------------------
# Step 2: Define Source Credibility Priors
# -------------------------------
source_credibility = {
    "Forbes": 0.95,
    "Wikipedia": 0.9,
    "NewsSite": 0.85,
    "BlogX": 0.5,
    "RandomSite": 0.3
}

# -------------------------------
# Step 3: Compute Source Frequency Agreement
# -------------------------------
def compute_frequency_score(df):
    freq_score = {}
    for source in df["source"].unique():
        agreements = 0
        total = 0
        
        for entity in df["entity"].unique():
            subset = df[df["entity"] == entity]
            majority_value = subset["value"].mode()[0]
            source_values = subset[subset["source"] == source]["value"]
            
            if len(source_values) > 0:
                total += 1
                if source_values.values[0] == majority_value:
                    agreements += 1
        
        freq_score[source] = agreements / total if total > 0 else 0
    return freq_score

frequency_score = compute_frequency_score(df)

# -------------------------------
# Step 4: Compute Reliability Score
# -------------------------------
alpha, beta = 0.6, 0.4

reliability = {}

for source in df["source"].unique():
    C = source_credibility.get(source, 0.5)
    F = frequency_score.get(source, 0.5)
    reliability[source] = alpha * C + beta * F

# -------------------------------
# Step 5: Probability Estimation
# -------------------------------
def compute_probabilities(entity_name, attribute_name):
    subset = df[
        (df["entity"] == entity_name) & 
        (df["attribute"] == attribute_name)
    ]
    
    total_weight = sum(reliability[s] for s in subset["source"])
    
    value_prob = {}
    for value in subset["value"].unique():
        sources = subset[subset["value"] == value]["source"]
        weight_sum = sum(reliability[s] for s in sources)
        value_prob[value] = weight_sum / total_weight
    
    return value_prob

# -------------------------------
# Example
# -------------------------------
entity_name = "Person_0"
attribute_name = "age"
probs = compute_probabilities(entity_name,attribute_name)

print(f"Probability Distribution for {entity_name}:")
for k, v in probs.items():
    print(f"{k} -> {round(v, 4)}")


# sample output :-----

# Probability Distribution for Person_0:
# 49 -> 0.8872
# 94 -> 0.1128