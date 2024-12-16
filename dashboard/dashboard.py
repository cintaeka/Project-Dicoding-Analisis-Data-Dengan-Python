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
orders = pd.read_csv('../data/orders_dataset.csv', sep=';') 
customers = pd.read_csv('../data/customers_dataset.csv', sep=';') 
geolocation = pd.read_csv('../data/geolocation_dataset.csv') 
items = pd.read_csv('../data/order_items_dataset.csv', sep=';') 
payments = pd.read_csv('../data/order_payments_dataset.csv', sep=';') 
reviews = pd.read_csv('../data/order_reviews_dataset.csv') 
products = pd.read_csv('../data/products_dataset.csv', sep=';') 
sellers = pd.read_csv('../data/sellers_dataset.csv', sep=';') 
category = pd.read_csv('../data/product_category_name_translation.csv', sep=';') 


#filtering order_status
state = orders['order_status'].unique().tolist()
state = st.selectbox(
    label=("status orderan berdasarkan berdasarkan order_status"),
    options=state
)
filtered_data = orders[orders['order_status'] == state]
st.dataframe(filtered_data)

# Metode Pembayaran apa yang paling banyak digunakan?
st.subheader("Pembayaran yang paling banyak digunakan")
 
if 'payment_type' in payments.columns:
    # Hitung jumlah transaksi berdasarkan kolom payment_type
    payment_type_counts = payments['payment_type'].value_counts()
    
    # Streamlit UI
    st.title("Analisis Metode Pembayaran")
    st.subheader("Metode Pembayaran yang Paling Banyak Digunakan")

    # Buat grafik dengan Matplotlib
    fig, ax = plt.subplots(figsize=(8, 6))
    payment_type_counts.plot(kind='bar', color='skyblue', ax=ax)

    # Pengaturan grafik
    ax.set_title('Metode Pembayaran Paling Banyak Digunakan', fontsize=16)
    ax.set_xlabel('Jenis Pembayaran', fontsize=14)
    ax.set_ylabel('Jumlah Transaksi', fontsize=14)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, fontsize=12)

    # Tampilkan grafik di Streamlit
    st.pyplot(fig)
else:
    # Pesan error jika kolom payment_type tidak ditemukan
    st.error("Kolom 'payment_type' tidak ditemukan di file data.")

# di daerah mana yang paling banyak pelanggan?
if 'customer_state' in customers.columns:
    # Hitung jumlah pelanggan berdasarkan kolom customer_state
    customer_state_counts = customers['customer_state'].value_counts()
    
    # Streamlit UI
    st.title("Analisis Daerah Pelanggan")
    st.subheader("Daerah dengan Jumlah Pelanggan Terbanyak")

    # Buat grafik dengan Matplotlib
    fig, ax = plt.subplots(figsize=(8, 6))
    customer_state_counts.plot(kind='bar', color='skyblue', ax=ax)

    # Pengaturan grafik
    ax.set_title('Daerah yang Paling Banyak Pelanggan', fontsize=16)
    ax.set_xlabel('Daerah', fontsize=14)
    ax.set_ylabel('Jumlah Pelanggan', fontsize=14)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, fontsize=12)

    # Tampilkan grafik di Streamlit
    st.pyplot(fig)
else:
    # Pesan error jika kolom customer_state tidak ditemukan
    st.error("Kolom 'customer_state' tidak ditemukan di file data.")
