import numpy as np
import pandas as pd
import matplotlib as mpl
import seaborn as sns
import streamlit as st

# sidebar pada streamlit
st.sidebar.subheader("Data Pribadi")
st.sidebar.write("Nama: Muhammad Zaidane Aflah")
st.sidebar.write("Group: Bangkit ML-44")
st.sidebar.write("Gmail Bangkit: m200d4ky2067@bangkit.academy")

# pembacaan dataset dari file CSV
databike_day = "day.csv"  # Menggunakan path relatif

data_perhari = pd.read_csv(databike_day, delimiter=';')
df = pd.DataFrame(data_perhari)

# menampilkan beberapa baris pertama data
st.subheader("Berikut beberapa baris pertama dari dataset:")
st.write(data_perhari.head())

# menampilkan informasi tentang dataset
st.subheader("Informasi tentang dataset:")
st.write(data_perhari.info())

# menampilkan statistik deskriptif untuk kolom-kolom numerik
st.subheader("Berikut data statistik deskriptif untuk kolom-kolom numerik:")
st.write(data_perhari.describe())

# menampilkan jumlah nilai yang hilang dalam setiap kolom
st.subheader("Jumlah nilai yang hilang dalam setiap kolom:")
st.write(data_perhari.isnull().sum())

# menampilkan jumlah baris yang duplikat
st.subheader("Jumlah baris yang duplikat:")
st.write(data_perhari.duplicated().sum())


new_path_day = "new_day.csv"  # Nama file baru
data_perhari.to_csv(new_path_day, index=False)

# Menampilkan beberapa informasi dari dataset
print("Beberapa baris pertama dari dataset:")
print(df.head())
print("\nInformasi tentang dataset:")
print(df.info())
print("\nStatistik deskriptif untuk kolom-kolom numerik:")
print(df.describe())
print("\nJumlah nilai yang hilang dalam setiap kolom:")
print(df.isnull().sum())
print("\nJumlah baris yang duplikat:")
print(df.duplicated().sum())
print("Jumlah nilai yang hilang dalam setiap kolom:")
print(df.isnull().sum())

# Menghapus Kolom yang Tidak Diperlukan
df_clean = df.drop(['instant'], axis=1)

# Pengubahan Tipe Data
df_clean['dteday'] = pd.to_datetime(df_clean['dteday'], format="%d/%m/%Y")  # Mengubah tipe data kolom 'dteday' menjadi datetime

#Pembersihan data dengan menghapus baris dengan nilai 'cnt' yang dianggap sebagai outlier)
Q1 = df_clean['cnt'].quantile(0.25)
Q3 = df_clean['cnt'].quantile(0.75)
IQR = Q3 - Q1
data_bawah = Q1 - 1.5 * IQR
data_atas = Q3 + 1.5 * IQR
df_clean = df_clean[(df_clean['cnt'] > data_bawah) & (df_clean['cnt'] < data_atas)]

# menampilkan informasi tentang dataset yang telah dibersihkan
print("\nInformasi tentang dataset yang telah dibersihkan:")
print(df_clean.info())

# Drop kolom 'dteday' dari dataframe
df_clean = df.drop(columns=['dteday'])

# menampilkan visual data dari jumlah sepeda yang dipinjam (cnt)
st.subheader("Histogram Jumlah Sepeda yang Dipinjam (cnt):")
plt.figure(figsize=(10, 6))
sns.histplot(data_perhari['cnt'], bins=30, kde=True)
plt.title('Distribusi Penyewaan Sepeda')
plt.xlabel('Count')
plt.ylabel('Frequency')
st.pyplot(plt)

# menampilkan visual data dari jumlah sepeda yang dipinjam (cnt) berdasarkan musim (season)
st.subheader("Box Plot Jumlah Sepeda yang Dipinjam (cnt) Berdasarkan Musim (season):")
plt.figure(figsize=(10, 6))
sns.boxplot(x='season', y='cnt', data=data_perhari)
plt.title('Penyewaan Sepeda Berdasarkan Musim')
plt.xlabel('Season')
plt.ylabel('Count')
st.pyplot(plt)

# menampilkan visual data dari jumlah sepeda yang dipinjam (cnt) vs. temperatur (temp)
st.subheader("Scatter Plot Jumlah Sepeda yang Dipinjam (cnt) vs. Temperatur (temp):")
plt.figure(figsize=(10, 6))
sns.scatterplot(x='temp', y='cnt', data=data_perhari)
plt.title('Bike Rentals vs. Temperature')
plt.xlabel('Temperature')
plt.ylabel('Count')
st.pyplot(plt)

# menampilkan visual data darikorelasi antara fitur-fitur numerik
st.subheader("Korelasi Antara Fitur-Fitur Numerik:")
correlation_matrix = data_perhari[['temp', 'atemp', 'hum', 'windspeed', 'casual', 'registered', 'cnt']].corr()
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
st.pyplot(plt)

# menampilkan visual data dari line plot tren jumlah sepeda yang dipinjam per hari
st.subheader("Pertanyaan 1")
st.write(":Bagaimana tren jumlah sepeda yang dipinjam berubah seiring dengan waktu?")
st.subheader("Line Plot Tren Jumlah Sepeda yang Dipinjam per Hari:")
plt.figure(figsize=(12, 6))
plt.plot(data_perhari['dteday'], data_perhari['cnt'], marker='o', linestyle='-')
plt.title('Tren peminjaman sepeda per har')
plt.xlabel('Date')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.grid(True)
st.pyplot(plt)

# menampilkan visual data dari bar plot korelasi antara cuaca dan jumlah sepeda yang dipinjam
st.subheader("Pertanyaan 2")
st.write("Bagaimana korelasi antara cuaca (weathersit) dengan jumlah sepeda yang dipinjam?")

st.subheader("Bar Plot Korelasi antara Cuaca dan Jumlah Sepeda yang Dipinjam:")
plt.figure(figsize=(8, 6))
weather_counts = data_perhari.groupby('weathersit')['cnt'].mean()
plt.bar(weather_counts.index, weather_counts.values)
plt.xlabel('Weather Situation')
plt.ylabel('Average Bike Rentals')  # String literal mulai ditutup
plt.title('Korelasi Situasi Cuaca dengan Penyewaan Sepedas')
st.pyplot(plt)


# Kesimpulan dari Pertanyaan

st.subheader("Kesimpulan")
st.write("pertanyaan 1 : Tren Jumlah Sepeda yang Dipinjam per Hari: Dapat kitaari visualisasi tren jumlah sepeda yang dipinjam per hari, terlihat bahwa terdapat fluktuasi dalam jumlah sepeda yang dipinjam seiring waktu. Puncak-puncak dan lembah-lembah dalam tren tersebut mungkin dapat dipengaruhi oleh faktor-faktor seperti musim, hari kerja, libur, dan kondisi cuaca.")
st.write("pertanyaan 2 : Korelasi antara Cuaca dan Jumlah Sepeda yang Dipinjam: Dari analisis korelasi antara situasi cuaca dan jumlah sepeda yang dipinjam, terlihat bahwa situasi cuaca memiliki pengaruh terhadap jumlah sepeda yang dipinjam. Jumlah rata-rata sepeda yang dipinjam cenderung lebih rendah saat cuaca buruk atau ekstrem dibandingkan dengan cuaca yang cerah dan menyenangkan.")
