#!/usr/bin/env python
# coding: utf-8

# In[3]:


import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Netflix Dashboard", layout="wide")

st.title("📺 Netflix Movies & TV Shows Dashboard")

# Load public dataset directly from GitHub
DATA_URL = "https://raw.githubusercontent.com/USERNAME/REPO/main/netflix_titles.csv"

@st.cache_data
def load_data():
    return pd.read_csv("https://raw.githubusercontent.com/USERNAME/REPO/main/netflix_titles.csv")

df = load_data()

st.subheader("Dataset Preview")
st.dataframe(df.head())

# Sidebar filters
st.sidebar.header("Filters")

type_filter = st.sidebar.multiselect(
    "Select Type",
    options=df["type"].unique(),
    default=df["type"].unique()
)

country_filter = st.sidebar.multiselect(
    "Select Country (optional)",
    options=df["country"].dropna().unique(),
    default=[]
)

filtered_df = df[df["type"].isin(type_filter)]

if country_filter:
    filtered_df = filtered_df[filtered_df["country"].isin(country_filter)]

st.subheader("Filtered Dataset")
st.dataframe(filtered_df.head())

# Visualization 1 — Count by Type
st.subheader("Count of Movies vs TV Shows")
fig_type = px.bar(
    df["type"].value_counts().reset_index(),
    x="index",
    y="type",
    labels={"index": "Type", "type": "Count"},
    title="Movies vs TV Shows"
)
st.plotly_chart(fig_type, use_container_width=True)

# Visualization 2 — Releases Over Time
st.subheader("Releases Over Time")
df_year = df.dropna(subset=["release_year"])
fig_year = px.histogram(
    df_year,
    x="release_year",
    nbins=30,
    title="Content Releases by Year"
)
st.plotly_chart(fig_year, use_container_width=True)

# Visualization 3 — Rating Distribution
st.subheader("Rating Distribution")
fig_rate = px.bar(
    df["rating"].value_counts().reset_index(),
    x="index",
    y="rating",
    labels={"index": "Rating", "rating": "Count"},
    title="Distribution of Ratings"
)
st.plotly_chart(fig_rate, use_container_width=True)


