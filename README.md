# 📊 Pricing & Discount Analysis

> Analyze pricing and discount effectiveness to identify profit leakage and support data-driven pricing decisions.

---

## 📌 Project Overview

This project analyzes the financial performance of **Global Superstore**, a multinational retail company, to evaluate pricing and discount strategies. Using SQL, Python, Excel, and Looker Studio, the analysis transforms raw transaction data into business insights and recommendations that support the company's goal of improving profitability.
---

## 🎯 Business Questions

This project aims to answer the following questions:

- How do discounts affect profit margins?
- Which product sub-categories generate high sales but low profitability?
- At what discount level does profitability begin to decline?
- Is the current discount strategy effective across different customer segments? :contentReference[oaicite:2]{index=2}

---

## ⚙️ Workflow

Data Extraction → Data Preprocessing → Exploratory Data Analysis (SQL) → Dashboard Development (Looker Studio) → Business Insights & Recommendations. :contentReference[oaicite:3]{index=3}

---

## 📈 Key Findings

- Discounts above **20%** significantly reduce profitability.
- Several high-sales sub-categories (Tables, Bookcases, Supplies, and Fasteners) consistently generate low or negative profit.
- Losses are driven not only by discount policies but also by low product margins.
- Similar profit issues are observed across all customer segments, indicating a product-level rather than customer-level problem. :contentReference[oaicite:4]{index=4}

---

## 💡 Recommendations

- Limit discounts above **20%**, especially for low-margin products.
- Review product costs (COGS) and pricing strategies for unprofitable sub-categories.
- Apply different discount strategies based on product profitability instead of using a uniform discount policy. :contentReference[oaicite:5]{index=5}

---

## 📂 Repository Structure

```text
data/
sql/
python/
dashboard/
presentation/
```

---

## 📁 Dataset

The project uses the original dataset containing **more than 50,000 rows**.

Due to GitHub's file preview limitation, the dataset cannot be displayed directly in the browser. Please download **`RevoU Dataset.csv`** from the `data` folder to view the complete dataset.
