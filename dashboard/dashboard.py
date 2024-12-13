import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn.preprocessing import StandardScaler
import streamlit as st
import warnings
warnings.filterwarnings("ignore")

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

# Pertanyaan 1: Metode pembayaran yang paling banyak digunakan
st.header("Pertanyaan 1: Metode Pembayaran yang Paling Banyak Digunakan")
payment_count = payments['payment_type'].value_counts().reset_index()
payment_count.columns = ['payment_type', 'count']

st.write("Jumlah penggunaan tiap metode pembayaran:")
st.dataframe(payment_count)

most_used_payment = payment_count.iloc[0]
st.write(f"Metode pembayaran yang paling banyak digunakan adalah **{most_used_payment['payment_type']}** dengan jumlah **{most_used_payment['count']}** kali.")

# Pertanyaan 2: Daerah dengan jumlah pelanggan terbanyak
st.header("Pertanyaan 2: Daerah dengan Jumlah Pelanggan Terbanyak")
customer_city_count = customers['customer_city'].value_counts().reset_index()
customer_city_count.columns = ['customer_city', 'count']

st.write("Jumlah pelanggan per kota:")
st.dataframe(customer_city_count)

most_popular_city = customer_city_count.iloc[0]
st.write(f"Kota dengan jumlah pelanggan terbanyak adalah **{most_popular_city['customer_city']}** dengan total pelanggan **{most_popular_city['count']}**.")
