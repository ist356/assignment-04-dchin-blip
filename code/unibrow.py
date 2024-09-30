'''
Solution unibrow.py
'''
import pandas as pd
import streamlit as st
import pandaslib as pl

st.title("UniBrow")
st.caption("The Universal data browser")

# TODO Write code here to complete the unibrow.py
f = st.file_uploader("Upload File", type=["csv", "xlsx", "json"])
if f:
    f_type = pl.get_file_extension(f.name)
    df = pl.load_file(f, f_type)
    cols = pl.get_column_names(df)
    selected_cols = st.multiselect("Select columns", cols, default=cols)
    if st.toggle("Filter data"):
        st_cols = st.columns(2)
        text_cols = pl.get_columns_of_type(df, 'object')
        filter_col = st_cols[0].selectbox("Select column", text_cols)
        if filter_col:
            vals = pl.get_unique_values(df, filter_col)
            val = st_cols[1].selectbox("Select value", vals)
            df_show = df[df[filter_col] == val][selected_cols]
    else:
        df_show = df[selected_cols]

    st.dataframe(df_show)
    st.dataframe(df_show.describe())