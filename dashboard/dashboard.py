import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn.preprocessing import StandardScaler
import streamlit as st
import warnings
warnings.filterwarnings("ignore")

# Title
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

# Input dari pengguna menggunakan Streamlit
st.sidebar.header("Filter Tanggal")
start_date = st.sidebar.date_input("Tanggal Mulai", value=pd.to_datetime("2021-01-01").date())
end_date = st.sidebar.date_input("Tanggal Akhir", value=pd.to_datetime("2021-12-31").date())

# Pastikan konversi tanggal menggunakan pd.to_datetime()
start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

# Filter data berdasarkan rentang tanggal
orders['order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp'])
filtered_orders = orders[(orders['order_purchase_timestamp'] >= start_date) &
                         (orders['order_purchase_timestamp'] <= end_date)]

# Tampilkan data yang difilter
st.write(f"Menampilkan data dari {start_date.date()} hingga {end_date.date()}:")
st.dataframe(filtered_orders)

st.write("Start Date:", start_date, type(start_date))
st.write("End Date:", end_date, type(end_date))

# Pertanyaan 1: Metode pembayaran yang paling banyak digunakan
st.header("Pertanyaan 1: Metode Pembayaran yang Paling Banyak Digunakan")
payment_count = payments['payment_type'].value_counts().reset_index()
payment_count.columns = ['payment_type', 'count']

st.write("Jumlah penggunaan tiap metode pembayaran:")
st.dataframe(payment_count)

most_used_payment = payment_count.iloc[0]
st.write(f"Metode pembayaran yang paling banyak digunakan adalah **{most_used_payment['payment_type']}** dengan jumlah **{most_used_payment['count']}** kali.")

# Visualisasi Pertanyaan 1
st.subheader("Visualisasi: Metode Pembayaran yang Paling Banyak Digunakan")
fig_payment = px.bar(payment_count, x='payment_type', y='count', color='payment_type', 
                     title="Metode Pembayaran yang Paling Banyak Digunakan")
st.plotly_chart(fig_payment)

# Pertanyaan 2: Daerah dengan jumlah pelanggan terbanyak
st.header("Pertanyaan 2: Daerah dengan Jumlah Pelanggan Terbanyak")
customer_city_count = customers['customer_city'].value_counts().reset_index()
customer_city_count.columns = ['customer_city', 'count']

st.write("Jumlah pelanggan per kota:")
st.dataframe(customer_city_count)

most_popular_city = customer_city_count.iloc[0]
st.write(f"Kota dengan jumlah pelanggan terbanyak adalah **{most_popular_city['customer_city']}** dengan total pelanggan **{most_popular_city['count']}**.")

# Visualisasi Pertanyaan 2
st.subheader("Visualisasi: Kota dengan Jumlah Pelanggan Terbanyak")
fig_city = px.bar(customer_city_count.head(10), x='customer_city', y='count', 
                  color='customer_city', title="10 Kota dengan Jumlah Pelanggan Terbanyak")
st.plotly_chart(fig_city)

# Pertanyaan 3: Analisis tambahan - Total transaksi per bulan
st.header("Pertanyaan 3: Total Transaksi Per Bulan")
filtered_orders['order_month'] = filtered_orders['order_purchase_timestamp'].dt.to_period('M')
monthly_sales = filtered_orders.groupby('order_month').size().reset_index(name='count')

st.write("Total transaksi per bulan:")
st.dataframe(monthly_sales)

fig_monthly_sales = px.line(monthly_sales, x='order_month', y='count', title="Total Transaksi Per Bulan")
st.plotly_chart(fig_monthly_sales)

# (Opsional) RFM Analysis
st.header("(Opsional) RFM Analysis")
recent_date = filtered_orders['order_purchase_timestamp'].max()
rfm_data = filtered_orders.groupby('customer_id').agg({
    'order_purchase_timestamp': lambda x: (recent_date - x.max()).days,
    'order_id': 'count',
    'order_approved_at': 'sum'
}).reset_index()
rfm_data.columns = ['customer_id', 'Recency', 'Frequency', 'Monetary']
st.write("Hasil RFM Analysis:")
st.dataframe(rfm_data.head())
