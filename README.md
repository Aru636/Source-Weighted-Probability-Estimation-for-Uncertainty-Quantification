# 📘 Source-Weighted Probability Estimation (SWPE)
### Quantifying Uncertainty in Web-Scraped Data for Probabilistic Data Mining

---

## 📌 Overview

Modern data mining applications increasingly rely on **web-scraped data** collected from multiple online sources. However, scraped data is often:

- Incomplete  
- Inconsistent  
- Duplicated  
- Conflicting  
- Noisy due to parsing errors  
- Influenced by varying source credibility  

Traditional probabilistic data mining assumes that uncertainty is already represented using probability distributions. However, it does **not clearly define how these probabilities are estimated from raw scraped data**.

This project proposes a **Source-Weighted Probability Estimation (SWPE) framework** that quantifies uncertainty at the data acquisition stage before applying probabilistic mining algorithms.

---

## 🎯 Problem Statement

When multiple sources provide conflicting values for the same entity attribute:

- How do we measure source reliability?
- How do we construct probability distributions from raw scraped data?
- How do we select the most credible value?
- How do we preserve uncertainty for downstream probabilistic mining?

This project addresses these challenges using a weighted reliability-based approach.

---

## 💡 Proposed Solution

The SWPE framework works as follows:

1. Assign credibility priors to sources  
2. Compute frequency-based agreement scores  
3. Calculate reliability score for each source  
4. Construct probability distributions per *(entity, attribute)*  
5. Select value if confidence exceeds threshold  

### Reliability Model

\[
R_s = \alpha C_s + \beta F_s
\]

Where:

- \(C_s\) = Credibility prior  
- \(F_s\) = Frequency agreement score  
- \(\alpha, \beta\) = Hyperparameters  

### Probability Estimation

\[
P(v \mid entity, attribute) =
\frac{\sum_{s \in S_v} R_s}
{\sum_{all\ sources} R_s}
\]

---

## 📂 Project Structure

```
├── dataset_generation.py     # Synthetic multi-source dataset generator
├── dataset.ipynb             # Dataset exploration notebook
├── multi_source_dataset.csv  # Generated dataset
├── prob_dist.py              # Source-weighted probability model
├── prob_dist.ipynb           # Probability analysis notebook
```


---

## 📊 Dataset Description

The synthetic dataset simulates real-world web scraping:

- 500 entities  
- 5 attributes per entity  
- 5 sources with different credibility levels  
- Controlled noise injection  

Each record follows the format:

| entity | attribute | source | value |

Example:

| entity    | attribute | source      | value |
|------------|------------|------------|--------|
| Person_0 | children | Forbes     | 4 |
| Person_0 | children | Wikipedia  | 4 |
| Person_0 | children | BlogX      | 3 |
| Person_0 | children | RandomSite | 9 |

---

## ⚙️ How It Works

### 1️⃣ Dataset Generation

Run:

```bash
python dataset_generation.py
```
### 2️⃣ Compute Probability Distribution

Run:
```
python prob_dist.py
```
Or use Jupyter Notebook:
```
jupyter notebook
```

🧪 Example Output
Probability Distribution for Person_0 (children):
```
4 -> 0.9134
3 -> 0.0612
9 -> 0.0254
```
