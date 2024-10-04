# fixxx_dashboard.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
day_df = pd.read_csv('day.csv')
hour_df = pd.read_csv('hour.csv')

# Streamlit Dashboard Title
st.title("Bike Sharing Analysis Dashboard")
st.write("### Analyzing Hourly, Seasonal, and Yearly Usage Patterns")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Explore:", [
    "Hourly Usage Distribution",
    "Seasonal Usage Patterns",
    "Yearly Monthly Trends Comparison"
])

# Question 1: Hourly Usage Distribution
if page == "Hourly Usage Distribution":
    st.subheader("1. Hourly Usage Distribution by Casual and Registered Users")
    
    # Group data by hour and calculate average usage
    hour_df['hour'] = hour_df['hr']
    hourly_usage = hour_df.groupby('hour')[['casual', 'registered']].mean()
    
    st.write("### Average Hourly Usage")
    st.line_chart(hourly_usage)

# Question 2: Seasonal Usage Patterns
elif page == "Seasonal Usage Patterns":
    st.subheader("2. Seasonal Usage Patterns for Casual and Registered Users")
    
    # Aggregate data by season and sum usage for each user type
    seasonal_usage = day_df.groupby('season')[['casual', 'registered']].sum()
    
    st.write("### Total Usage by Season")
    st.bar_chart(seasonal_usage)

    if st.checkbox("Show raw seasonal data"):
        st.write(seasonal_usage)

# Revised Question 3: Yearly Monthly Trends Comparison
elif page == "Yearly Monthly Trends Comparison":
    st.subheader("3. Monthly Trends Comparison for 2011 and 2012")
    
    # Convert 'yr' to actual years and group data by year and month
    day_df['year'] = day_df['yr'].apply(lambda x: 2011 + x)
    monthly_trends = day_df.groupby(['year', 'mnth'])[['casual', 'registered']].sum().unstack(level=0)
    
    st.write("### Monthly Usage Trends Comparison (2011 vs 2012)")
    
    # Plot trends for casual and registered users
    fig, ax = plt.subplots()
    monthly_trends['casual'].plot(ax=ax, label="Casual Users")
    monthly_trends['registered'].plot(ax=ax, label="Registered Users")
    ax.set_title("Monthly Usage Trends for 2011 and 2012")
    ax.set_xlabel("Month")
    ax.set_ylabel("Total Usage")
    plt.legend(title="User Type")
    st.pyplot(fig)

    if st.checkbox("Show raw monthly trends data"):
        st.write(monthly_trends)

# Running the app
# Use `streamlit run fixxx_dashboard.py` to start the dashboard
