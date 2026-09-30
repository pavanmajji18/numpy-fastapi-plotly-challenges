# Super30: NumPy + Plotly E-Commerce Analytics

An end-to-end high-performance data analytics and business intelligence pipeline built with **NumPy**, **Pandas**, and **Plotly**. This project demonstrates zero-loop vectorized financial computations, statistical reductions, and executive-level interactive data visualizations.

---

## 👤 Author Information

* **Author:** Pavan Kumar Majji
* **Project:** super30-numpy-plotly-analytics
* **LinkedIn:** [Pavan Kumar Majji](https://www.linkedin.com/in/pavan-kumar-majji-231303199/)
* **Repository:** [numpy-fastapi-plotly-challenges](https://github.com/pavanmajji18/numpy-fastapi-plotly-challenges/tree/main/super30-numpy-plotly-analytics)

---

## 🚀 Key Features

* **⚡ Vectorized Financial Analytics:** Uses NumPy arrays for fast, element-wise math (Net Profit, Month-over-Month Revenue Deltas, array concatenation).
* **📊 Statistical Reductions & Windowing:** Computes annual metrics, mean performance, and extracts peak/lowest performance months using `np.argmax` / `np.argmin` and `np.where`.
* **📈 Interactive BI Visualizations:** Generates interactive Plotly charts including Line, Bar, Grouped Bar, and Area charts.
* **💼 Executive Overview Dashboard:** Implements a combined multi-trace `plotly.graph_objects` chart overlaying cash flows (Revenue & Expenses) with Net Profitability trendlines.
* **💡 Automated Insights Engine:** Automatically prints key business takeaways and annual financial summaries to the console.

---

## 📁 Repository Structure

```text
super30-numpy-plotly-analytics/
├── main.py          # Main execution script (NumPy analytics + Plotly charts)
├── output.txt       # Execution log output
├── requirements.txt # Project dependencies (numpy, pandas, plotly)
└── README.md        # Project documentation
```

---

## 🛠️ Installation & Setup

1. **Clone or navigate to the repository directory:**
   ```bash
   cd super30-numpy-plotly-analytics
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 💻 How to Run

Execute the main script:
```bash
python main.py
```

Running the script will:
1. Print the **Annual Financial Summary** and **Management Insights** directly to the terminal.
2. Automatically launch **6 interactive Plotly visualizations** in your default web browser.

---

## 📊 Visualizations Generated

| # | Visual Title | Chart Type | Key Data Metrics |
|---|---|---|---|
| **1** | Monthly Revenue Trend | Line Chart with Markers | 12-Month revenue trajectory (INR 450k to 1.28M) |
| **2** | Monthly Order Volumes | Bar Chart | Order volume progression (1,200 to 3,450 orders) |
| **3** | Monthly Revenue vs. Expenses | Grouped Bar Chart | Side-by-side financial comparison per month |
| **4** | Cumulative Customer Growth | Area Chart | Active customer base growth (850 to 4,150) |
| **5** | Monthly Net Profit | Bar Chart | Net profitability distribution |
| **6** | Executive Overview | Combined Multi-Trace Dashboard | Grouped Revenue/Expenses bars overlaid with Net Profit line |

---

## 💡 Discoverable Business Insights

Based on the execution results:
1. **Q4 Seasonal Surge:** Revenue spiked dramatically in November (INR 1.15M) and December (INR 1.28M), driven by holiday demand.
2. **Expanding Margins:** Net operating margins expanded from ~15% in Q1 to over ~30% in Q4.
3. **High Customer Retention:** Active customer base grew nearly 5-fold (850 to 4,150), mirroring order volume acceleration.
4. **Post-Holiday Dips:** January marked the lowest revenue month (INR 450k), highlighting expected post-holiday seasonality.
5. **Positive MoM Momentum:** Month-over-month revenue changes remained positive across all quarters.

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).
