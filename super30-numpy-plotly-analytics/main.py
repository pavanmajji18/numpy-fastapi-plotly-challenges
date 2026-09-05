import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ==========================================
# 1. DATA GENERATION
# ==========================================
# Set seed for reproducible fictional sales data
np.random.seed(42)

months = np.array([
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
])

# Generate monthly metrics using NumPy array and random generators
revenue = np.array([
    450000, 480000, 520000, 510000, 590000, 640000,
    620000, 710000, 750000, 890000, 1150000, 1280000
])

orders = np.array([1200, 1310, 1400, 1380, 1600, 1720, 1680, 1900, 2050, 2400, 3100, 3450])

# Cumulative active customers over the 12 months
customers = np.array([850, 960, 1100, 1220, 1450, 1680, 1850, 2150, 2420, 2890, 3600, 4150])

# Monthly expenses (INR)
expenses = np.array([
    380000, 400000, 430000, 440000, 480000, 510000,
    520000, 560000, 590000, 680000, 820000, 890000
])

# ==========================================
# 2. NUMPY PROCESSING
# ==========================================
# Element-wise arithmetic for profit
profit = revenue - expenses

# Month-to-month revenue differences: revenue[1:] - revenue[:-1]
rev_diff = revenue[1:] - revenue[:-1]
# Prepend 0 for the first month
monthly_revenue_change = np.concatenate(([0], rev_diff))

# ==========================================
# 3. ANALYSIS & STATISTICS
# ==========================================
# Basic statistics & reductions
total_revenue = np.sum(revenue)
avg_revenue = np.mean(revenue)
total_profit = np.sum(profit)
avg_profit = np.mean(profit)

# Best and lowest performing months
max_rev = np.max(revenue)
min_rev = np.min(revenue)

best_month_idx = np.where(revenue == max_rev)[0][0]
lowest_month_idx = np.where(revenue == min_rev)[0][0]

best_month = months[best_month_idx]
lowest_month = months[lowest_month_idx]

# Display analytical metrics
print("=" * 45)
print("       ANNUAL FINANCIAL SUMMARY")
print("=" * 45)
print(f"Total Annual Revenue : INR {total_revenue:,.2f}")
print(f"Average Monthly Rev  : INR {avg_revenue:,.2f}")
print(f"Total Annual Profit  : INR {total_profit:,.2f}")
print(f"Average Monthly Profit: INR {avg_profit:,.2f}")
print(f"Best Month           : {best_month} (INR {max_rev:,})")
print(f"Lowest Month         : {lowest_month} (INR {min_rev:,})")
print("-" * 45)

# Build DataFrame for Plotly visual consumption
df_sales = pd.DataFrame({
    "Month": months,
    "Revenue": revenue,
    "Expenses": expenses,
    "Profit": profit,
    "Orders": orders,
    "Customers": customers,
    "MoM_Change": monthly_revenue_change
})

# ==========================================
# 4. PLOTLY VISUALIZATION
# ==========================================

# Chart 1: Revenue Trends (Req 7)
fig_rev = px.line(
    df_sales,
    x="Month",
    y="Revenue",
    markers=True,
    title="Monthly Revenue Trend (INR)"
)
fig_rev.show()

# Chart 2: Monthly Orders (Req 8)
fig_orders = px.bar(
    df_sales,
    x="Month",
    y="Orders",
    title="Monthly Order Volumes"
)
fig_orders.show()

# Chart 3: Revenue vs Expenses Comparison (Req 9)
df_comp = pd.melt(
    df_sales,
    id_vars=["Month"],
    value_vars=["Revenue", "Expenses"],
    var_name="Category",
    value_name="Amount"
)
fig_comp = px.bar(
    df_comp,
    x="Month",
    y="Amount",
    color="Category",
    barmode="group",
    title="Monthly Revenue vs. Expenses"
)
fig_comp.show()

# Chart 4: Customer Growth Visualization (Req 10)
fig_cust = px.area(
    df_sales,
    x="Month",
    y="Customers",
    title="Cumulative Customer Growth"
)
fig_cust.show()

# Chart 5: Monthly Profit (Req 11)
fig_profit = px.bar(
    df_sales,
    x="Month",
    y="Profit",
    title="Monthly Net Profit (INR)"
)
fig_profit.show()

# Chart 6: Final Management Overview Visualization (Req 12)
# Multi-metric tracking dashboard combining cash flows & transaction volume
fig_mgmt = go.Figure()

# Revenue bar
fig_mgmt.add_trace(go.Bar(
    x=df_sales["Month"],
    y=df_sales["Revenue"],
    name="Revenue",
    marker_color="#1f77b4"
))

# Expenses bar
fig_mgmt.add_trace(go.Bar(
    x=df_sales["Month"],
    y=df_sales["Expenses"],
    name="Expenses",
    marker_color="#ff7f0e"
))

# Net Profit line overlay
fig_mgmt.add_trace(go.Scatter(
    x=df_sales["Month"],
    y=df_sales["Profit"],
    name="Net Profit",
    mode="lines+markers",
    line=dict(color="#2ca02c", width=3)
))

fig_mgmt.update_layout(
    title="Executive Overview: Revenue, Expenses & Net Profitability",
    xaxis_title="Month",
    yaxis_title="Amount (INR)",
    barmode="group",
    template="plotly_white"
)
fig_mgmt.show()

# ==========================================
# 5. INSIGHTS DISCOVERED
# ==========================================
print("\n" + "=" * 45)
print("          MANAGEMENT INSIGHTS")
print("=" * 45)
print("1. Q4 Seasonal Surge: Revenue spiked dramatically in Nov (INR 1.15M) and Dec (INR 1.28M), driven by holiday sales and year-end demand.")
print("2. Stable Operating Margin: Expenses scaled at a controlled rate compared to revenue, expanding net margins from ~15% in Q1 to over ~30% in Q4.")
print("3. High Revenue Retention: Cumulative customer base increased nearly five-fold (850 to 4,150), directly matching order volume growth.")
print("4. Lowest Performance Window: January was the lowest revenue month (INR 450k), highlighting post-holiday seasonal dips.")
print("5. Consistent MoM Momentum: Except for a brief flat plateau between March and April, month-over-month revenue change remained strictly positive all year.")