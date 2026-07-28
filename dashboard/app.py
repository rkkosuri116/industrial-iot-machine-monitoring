import streamlit as st
import sys
import os
import pandas as pd

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

from database.db_connection import get_connection

st.set_page_config(
    page_title="Factory Machine Dashboard",
    page_icon="🏭",
    layout="wide"
)

st.title("🏭 Factory Machine Monitoring Dashboard")

connection = get_connection()

query = """
SELECT *
FROM machine_data
ORDER BY timestamp DESC
LIMIT 20;
"""

df = pd.read_sql(query, connection)
connection.close()

if df.empty:
    st.warning("No machine data available.")
    st.stop()

latest = df.iloc[0]

col1, col2, col3, col4 = st.columns(4)

col1.metric("🌡 Temperature", f"{latest['temperature']:.2f} °C")
col2.metric("⚙ RPM", int(latest["rpm"]))
col3.metric("⚡ Power", f"{latest['power']:.2f} kW")
col4.metric("📈 Vibration", f"{latest['vibration']:.2f} mm/s")

st.success(f"Machine Status: {latest['status']}")

st.subheader("Latest Machine Data")
st.dataframe(df, use_container_width=True)

st.subheader("Temperature Trend")
st.line_chart(df.set_index("timestamp")["temperature"])

st.subheader("RPM Trend")
st.line_chart(df.set_index("timestamp")["rpm"])

st.subheader("Power Trend")
st.line_chart(df.set_index("timestamp")["power"])

st.subheader("Vibration Trend")
st.line_chart(df.set_index("timestamp")["vibration"])