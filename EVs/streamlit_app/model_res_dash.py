import streamlit as st
import datetime
from utils import get_data, data_subset, data_plot
from PIL import Image


def data_plot(data, fields, together):
    if together:
        data_charts = data.groupby("time_frame").mean()[fields]
    else:
        data_charts = data.groupby(["time_frame", "model_name"]).mean()[fields].unstack()
        data_charts.columns = data_charts.columns.get_level_values(1)

    return data_charts


def gen_app():
    source = get_data()
    # print(source)
    specific_date = source["date_time"].min() + datetime.timedelta(days=7)
    source = source[source["date_time"] > specific_date]
    poss_locs = list(source["model_name"].unique())

    st.title("Model Results")
    st.write("Visualisation of model statistics")

    st.markdown('<p style="font-family:sans-serif; color:Black; font-size: 30px;"><b>Impact of incentivisation on different customer profiles</b></p>', unsafe_allow_html=True)
    # with st.sidebar:
    col1, col2, col4 = st.columns(3)  # col3,
    with col1:
        if st.checkbox("All Customer profiles", value=True):
            locs = ["All"]
        else:
            locs = [st.multiselect("Customer profiles", poss_locs, poss_locs[0])][0]
    with col2:
        together = st.radio("Aggregated", [True, False], index=1)
    with col4:
        timeframe = [st.radio("Timeframe", ["all", "day", "hour", "weekday", "weekend"], index=0,)]
        if timeframe == ["day"]:
            specific_date = st.date_input(
                "Date",
                value=source["date_time"].min(),
                min_value=source["date_time"].min(),
                max_value=source["date_time"].max(),
            )

    # Original time series chart. Omitted `get_chart` for clarity
    data = data_subset(source, locs, timeframe, specific_date)
    col1, col4 = st.columns(2)  # col2, col3,
    with col1:
        st.write("Energy Load caused by all agents combined")
        data["charge_load_rep"] = data["charge_load"] / data["rep_agents"]
        st.line_chart(data_plot(data, ["charge_load_rep"], together))
    with col4:
        if not together:
            st.write("Percent of EVs moving in IoW")
            st.line_chart(data_plot(data, ["av_moving"], together) * 100)
        else:
            st.write("Position of EVs on IoW by percentage")
            st.line_chart(data_plot(data, ["av_moving", "av_home", "av_work", "av_random", "av_CP"], together) * 100)

    col1, col4 = st.columns(2)  # col2, col3,
    with col1:
        st.write("Number of representative agents")
        st.line_chart(data_plot(data, ["rep_agents"], together))
    with col4:
        st.write("Price of Charging for Agents")
        st.line_chart(data_plot(data, ["price"], together))

    st.markdown('<p style="font-family:sans-serif; color:Black; font-size: 30px;"><b>Impact of changing the number of charging stations</b></p>', unsafe_allow_html=True)
    st.write("20 vs 57 Charging points")
    col1, col2 = st.columns(2) 
    with col1:
        image = Image.open('../Data/resources/CP_20.png')
        st.image(image, caption='20 charging stations')
    with col2:
        image = Image.open('../Data/resources/CP_57.png')
        st.image(image, caption='57 charging stations')

    col1, col2 = st.columns(2) 
    with col1:
        image = Image.open('../Data/resources/CP_20_1.png')
        st.image(image, caption='20 charging stations')
    with col2:
        image = Image.open('../Data/resources/CP_57_1.png')
        st.image(image, caption='57 charging stations')



