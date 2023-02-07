import streamlit as st
import agent_app
import model_res_dash
import new_run
import new_run_live
import taxi_driver_dashboard
import altair as alt
from streamlit_option_menu import option_menu
from PIL import Image

st.set_page_config(layout="wide")
logo = Image.open(r"./branding/cap_logo.png")
st.image(logo, width=130)

choose = option_menu(
    "E-UK : Dashboards for policy makers",
    ["Live Run", "Model Results", "New Model Run", "Taxi driver dashboard"],
    icons=["shuffle", "bar-chart", "node-plus"], 
    menu_icon="app-indicator",
    default_index=0,
    orientation="horizontal",
    styles={
        "icon": {"color": "orange", "font-size": "25px"},
    },
)

if choose == "Live Run":
    new_run_live.gen_app()
elif choose == "Model Results":
    model_res_dash.gen_app()
elif choose == "Taxi driver dashboard":
    taxi_driver_dashboard.gen_app()
else:
    new_run.gen_app()
