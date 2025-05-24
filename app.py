import streamlit as st
import pandas as pd

st.title("Investment Model Assumptions")

st.markdown("Adjust the assumptions below to see how they impact the valuation.")

# Sidebar inputs
st.sidebar.header("Assumptions")
total_supply = st.sidebar.slider("Total Supply ($B)", 5.0, 35.0, 20.0, step=1.0)
supply_staked = st.sidebar.slider("Supply Staked (%)", 30, 70, 50, step=1)
average_yield = st.sidebar.slider("Average Yield (%)", 5, 12, 8, step=1)
margin = st.sidebar.slider("Margin (%)", 60, 95, 80, step=1)
multiple = st.sidebar.slider("Multiple", 10, 35, 25, step=1)

# Calculations
gross_revenues = (total_supply * (supply_staked / 100) * (average_yield / 100))
net_revenues = gross_revenues * (margin / 100)
valuation = net_revenues * multiple
potential = valuation / total_supply

# Display output
results = {
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
st.dataframe(pd.DataFrame([results]))
