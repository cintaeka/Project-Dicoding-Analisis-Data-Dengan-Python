import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn.preprocessing import StandardScaler
import streamlit as st
import warnings
warnings.filterwarnings("ignore")

# Judul aplikasi
st.title("Analisis Data Pelanggan dan Pertanyaan Bisnis")

# Load datasets
orders = pd.read_csv('https://raw.githubusercontent.com/cintaeka/Dicoding-BelajarAnalisisDataDenganPython/refs/heads/main/Data/orders_dataset.csv') 
customers = pd.read_csv('https://raw.githubusercontent.com/cintaeka/Dicoding-BelajarAnalisisDataDenganPython/refs/heads/main/Data/customers_dataset.csv') 
geolocation = pd.read_csv('https://raw.githubusercontent.com/cintaeka/Dicoding-BelajarAnalisisDataDenganPython/refs/heads/main/Data/geolocation_dataset.csv') 
items = pd.read_csv('https://raw.githubusercontent.com/cintaeka/Dicoding-BelajarAnalisisDataDenganPython/refs/heads/main/Data/order_items_dataset.csv') 
payments = pd.read_csv('https://raw.githubusercontent.com/cintaeka/Dicoding-BelajarAnalisisDataDenganPython/refs/heads/main/Data/order_payments_dataset.csv') 
reviews = pd.read_csv('https://raw.githubusercontent.com/cintaeka/Dicoding-BelajarAnalisisDataDenganPython/refs/heads/main/Data/order_reviews_dataset.csv') 
products = pd.read_csv('https://raw.githubusercontent.com/cintaeka/Dicoding-BelajarAnalisisDataDenganPython/refs/heads/main/Data/products_dataset.csv') 
sellers = pd.read_csv('https://raw.githubusercontent.com/cintaeka/Dicoding-BelajarAnalisisDataDenganPython/refs/heads/main/Data/sellers_dataset.csv') 
category = pd.read_csv('https://raw.githubusercontent.com/cintaeka/Dicoding-BelajarAnalisisDataDenganPython/refs/heads/main/Data/product_category_name_translation.csv') 

# Konversi tanggal untuk orders
orders['order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp'])

# Filter interaktif berdasarkan tanggal
st.sidebar.header("Filter Data")
start_date = st.sidebar.date_input("Tanggal Mulai", value=orders['order_purchase_timestamp'].min().date())
end_date = st.sidebar.date_input("Tanggal Akhir", value=orders['order_purchase_timestamp'].max().date())

if start_date > end_date:
    st.sidebar.error("Tanggal Mulai tidak boleh lebih besar dari Tanggal Akhir.")
else:
    filtered_orders = orders[(orders['order_purchase_timestamp'].dt.date >= start_date) & (orders['order_purchase_timestamp'].dt.date <= end_date)]

# Filter interaktif lainnya (contoh: metode pembayaran)
payment_types = payments['payment_type'].unique()
selected_payment_type = st.sidebar.multiselect("Metode Pembayaran", options=payment_types, default=payment_types)
filtered_payments = payments[payments['payment_type'].isin(selected_payment_type)]

# Pertanyaan 1: Metode pembayaran yang paling banyak digunakan
st.header("Pertanyaan 1: Metode Pembayaran yang Paling Banyak Digunakan")
payment_count = filtered_payments['payment_type'].value_counts().reset_index()
payment_count.columns = ['payment_type', 'count']

st.write("Jumlah penggunaan tiap metode pembayaran:")
st.dataframe(payment_count)

if not payment_count.empty:
    most_used_payment = payment_count.iloc[0]
    st.write(f"Metode pembayaran yang paling banyak digunakan adalah **{most_used_payment['payment_type']}** dengan jumlah **{most_used_payment['count']}** kali.")
else:
    st.write("Tidak ada data yang sesuai dengan filter.")

# Pertanyaan 2: Daerah dengan jumlah pelanggan terbanyak
st.header("Pertanyaan 2: Daerah dengan Jumlah Pelanggan Terbanyak")
customer_city_count = customers['customer_city'].value_counts().reset_index()
customer_city_count.columns = ['customer_city', 'count']

st.write("Jumlah pelanggan per kota:")
st.dataframe(customer_city_count)

most_popular_city = customer_city_count.iloc[0]
st.write(f"Kota dengan jumlah pelanggan terbanyak adalah **{most_popular_city['customer_city']}** dengan total pelanggan **{most_popular_city['count']}**.")

# Visualisasi interaktif dengan Plotly
st.header("Visualisasi Interaktif")
st.subheader("Distribusi Pesanan Berdasarkan Tanggal")
order_distribution = filtered_orders['order_purchase_timestamp'].dt.date.value_counts().reset_index()
order_distribution.columns = ['Tanggal', 'Jumlah Pesanan']
order_distribution = order_distribution.sort_values('Tanggal')

fig = px.bar(order_distribution, x='Tanggal', y='Jumlah Pesanan', title="Distribusi Pesanan")
st.plotly_chart(fig)
