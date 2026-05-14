# ⚽ Bernardo Silva Performance Analytics Dashboard

A football analytics project analyzing Bernardo Silva’s performance from 2017/18 to 2025/26 using Python, Streamlit, and Plotly.

---

live demo: https://bernardo-silva-performance-analytics-dashboard-jswjrw5rkyrij3v.streamlit.app/

## 📊 Project Overview

This dashboard evaluates:
- Goal and assist trends
- Expected vs actual performance (xG/xA)
- Creative output (key passes, xA per 90)
- Minutes vs productivity relationship
- Career progression and role evolution

---
## What the data revealed

🎨 1. Creative evolution is not linear — it is cyclical
Peak creative volume (key passes per 90) occurred in 2018/19 and 2019/20 (2.24–2.32 kp90)
After a tactical dip, he showed a strong creative resurgence in 2023/24 (2.25 kp90 + 8.53 xA)
Recent seasons show a slight reduction in volume but stable output

👉 Insight: His creativity does not decline permanently — it re-adjusts based on role

🎯 2. He consistently converts chances at expected levels
Across multiple seasons, goals closely tracked xG
Example:
2023/24 → 6 goals vs 4.10 xG (overperformance)
2024/25 → 4 goals vs 4.79 xG (slight under, but stable)
Assists also closely followed xA trends
2023/24 → 9 assists vs 8.53 xA

👉 Insight: He is a highly efficient and predictable performer, not reliant on randomness.

🧠 3. His best seasons came in different “versions” of himself
2018–2020: Peak volume creator (high kp90, balanced goals + assists)
2020–2022: Tactical adjustment phase (lower volume, stable efficiency)
2023/24: Creative resurgence + highest assist output (9 assists)
2024–2026: Stabilization phase with controlled output

👉 Insight: He has multiple peak identities, not a single prime.

⏱️ 4. Minutes played do not define output
Even in seasons with varying minutes, productivity per 90 remained stable
High involvement even when rotated
No clear dependency between minutes and efficiency

👉 Insight: He is a system player, not a volume-dependent performer

⚖️ 5. His attacking contribution is role-driven, not form-driven
Early career = balanced scorer + creator
Mid career = deeper creative playmaker
Recent years = hybrid role with controlled attacking output

👉 Insight: His performance is shaped more by tactical instructions than decline

## 🧠 Key Insights

- Consistent elite-level creative midfielder
- Strong alignment between expected and actual output
- Multiple performance peaks across career
- High tactical adaptability across roles

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Pandas
- Plotly
- Excel dataset

---
## Project Structure
bernardo-silva-analytics/
│
├── app21.py
├── data/
│   └── player-groups (6).xlsx
│
├── assets/
│   └── bernardo.jpg
│
├── requirements.txt
├── README.md
└── .gitignore

## 📈 Features

- Interactive season filtering
- KPI performance summary
- Career trend analysis
- Efficiency (xG vs goals, xA vs assists)
- Minutes vs productivity analysis

---

## 🚀 How to Run Locally

```bash
pip install -r requirements.txt
streamlit run app21.py

## Dashboard Preview
<img width="1599" height="772" alt="image" src="https://github.com/user-attachments/assets/530d494e-5e91-4328-a178-1adb0559e851" />


## Author
Stephen Yaw Ayamah
Football Data Analyst Portfolio Project
