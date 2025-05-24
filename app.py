import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Investment Model Assumptions")

st.markdown("Adjust the assumptions below to see how they impact the valuation.")

# Sidebar inputs with help tooltips
st.sidebar.header("Assumptions")
total_supply = st.sidebar.slider(
    "Total Supply ($B)", 5.0, 35.0, 20.0, step=1.0,
    help="Total token supply expected in circulation (in billions)"
)
supply_staked = st.sidebar.slider(
    "Supply Staked (%)", 20, 100, 50, step=1,
    help="Percentage of the total supply that is staked to earn savings rate"
)
average_yield = st.sidebar.slider(
    "Average Yield (%)", 3, 15, 8, step=1,
    help="Annual average yield given to stakers (in percent)"
)
margin = st.sidebar.slider(
    "Margin (%)", 60, 95, 80, step=1,
    help="Net margin as a percentage of gross revenues"
)
multiple = st.sidebar.slider(
    "Multiple", 10, 50, 25, step=1,
    help="Revenue multiple used for valuation purposes"
)

# Current numbers for comparison
current_data = {
    "Total Supply ($B)": 18,
    "Supply Staked (%)": 52,
    "Average Yield (%)": 7,
    "Margin (%)": 78,
    "Gross Revenues ($B)": round(18 * 0.52 * 0.07, 2),
    "Net Revenues ($B)": round((18 * 0.52 * 0.07) * 0.78, 2),
    "Multiple": 22,
    "Valuation ($B)": round(((18 * 0.52 * 0.07) * 0.78) * 22, 2),
    "Potential (x)": round((((18 * 0.52 * 0.07) * 0.78) * 22) / 18, 2)
}

# Calculations for user input
gross_revenues = (total_supply * (supply_staked / 100) * (average_yield / 100))
net_revenues = gross_revenues * (margin / 100)
valuation = net_revenues * multiple
potential = valuation / total_supply

# Display output
model_results = {
    "Total Supply ($B)": total_supply,
    "Supply Staked (%)": supply_staked,
    "Average Yield (%)": average_yield,
    "Margin (%)": margin,
    "Gross Revenues ($B)": round(gross_revenues, 2),
    "Net Revenues ($B)": round(net_revenues, 2),
    "Multiple": multiple,
    "Valuation ($B)": round(valuation, 2),
    "Potential (x)": round(potential, 2)
}

st.subheader("Results")
st.markdown("**Current Data vs Your Model**")
st.dataframe(pd.DataFrame([current_data, model_results], index=["Current", "Your Model"]))

# Visualization
st.subheader("Visual Comparison")
fig, ax = plt.subplots()
labels = list(model_results.keys())[-3:]
current_vals = [current_data[label] for label in labels]
model_vals = [model_results[label] for label in labels]

x = range(len(labels))
ax.bar([i - 0.2 for i in x], current_vals, width=0.4, label='Current')
ax.bar([i + 0.2 for i in x], model_vals, width=0.4, label='Your Model')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylabel("$B or x")
ax.legend()
st.pyplot(fig)
