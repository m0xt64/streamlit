# This script is intended to be run using Streamlit.
# Install the needed packages using:
# pip install streamlit plotly

import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.title("SKY: Investment Model")

st.markdown("Adjust the assumptions to see how they impact the valuation.")

# Sidebar inputs with help tooltips
st.sidebar.header("Assumptions")
total_supply = st.sidebar.slider(
    "Total Supply ($B)", 5.0, 35.0, 20.0, step=1.0,
    help="Total token supply expected in circulation (in billions)"
)
supply_staked = st.sidebar.slider(
    "Supply Staked (%)", 20, 100, 50, step=1,
    help="Percentage of the total supply that is staked earning savings rate"
)
average_yield = st.sidebar.slider(
    "Average Yield (%)", 3, 15, 8, step=1,
    help="Annual average yield given to stakers (in percent)"
)
margin = st.sidebar.slider(
    "Margin (%)", 60, 95, 80, step=1,
    help="Percent of net revenue (after savings) going to Sky vs Stars. Currently 100/0, but expected to shift to 80/20 based on Spark data."
)
multiple = st.sidebar.slider(
    "Multiple", 10, 50, 25, step=1,
    help="Revenue multiple used for valuation purposes"
)

# You can customize these current values as needed
# Current numbers for comparison
current_supply = 6  # in $B
current_staked = 45  # %
current_yield = 4.5    # %
current_gross =  0.290 # in $B
current_net = 0.180 # in $B
current_valuation = 1.1 # in $B
current_margin = 100 # %
current_potential = 0
current_multiple = 8 # in x

current_data = {
    "Total Supply ($B)": current_supply,
    "Supply Staked (%)": current_staked,
    "Average Yield (%)": current_yield,
    "Margin (%)": current_margin,
    "Gross Revenues ($B)": current_gross,
    "Net Revenues ($B)": current_net,
    "Multiple": current_multiple,
    "Valuation ($B)": current_valuation,
    "Potential (x)": current_potential
}

# Calculations for user input
gross_revenues = total_supply * (average_yield / 100) 
net_revenues = gross_revenues * (1-(supply_staked / 100)) * (margin / 100)
valuation = net_revenues * multiple
potential = valuation / current_valuation

# Model results
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

# Show data
st.subheader("Results")
st.markdown("**Current Data vs Your Model**")
st.dataframe(pd.DataFrame([current_data, model_results], index=["Current", "Your Model"]))

# Display upside potential sentence
st.markdown(f"Based on your inputs, the upside potential is: **{round(potential, 2)}x**")

# Plot visual comparison
st.subheader("Visual Comparison")
labels = ["Total Supply ($B)", "Net Revenues ($B)", "Valuation ($B)"]
current_vals = [current_data[label] for label in labels]
model_vals = [model_results[label] for label in labels]

fig = go.Figure(data=[
    go.Bar(name='Current', x=labels, y=current_vals),
    go.Bar(name='Your Model', x=labels, y=model_vals)
])
fig.update_layout(barmode='group', yaxis_title="$B")
st.plotly_chart(fig)
