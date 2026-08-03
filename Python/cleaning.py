import pandas as pd
import matplotlib.pyplot as plt

# Baca data
df = pd.read_excel("Loan_data.xlsm")

# Lihat semua nama kolom
print(df.columns)

# Baca 5 data teratas
print(df.head())

# Baca 5 data terbawah
print(df.tail())

#hapus kolom tidak diperlukan
columns_to_drop = [
    'LoanID',
    'Education',
    'EmploymentType',
    'MaritalStatus',
    'LoanPurpose',
    'HasCoSigner',
    'HasMortgage'
]

df_clean = df.drop(columns=columns_to_drop)

df_clean.to_csv('loan_clean.csv', index=False)

#Proses Cleaning Data. Apakah ada missing value, outlier, duplikat data?
# ===== 1. Missing Value =====
#Cek Missing value
print("missing value each column")
print(df_clean.isnull().sum())

#memperbaiki missing value (jika ada)
numeric_cols = df_clean.select_dtypes(include='number').columns #memilih kolom angka seperti int dan float
categorical_cols = df_clean.select_dtypes(include=['object','category']).columns #Lebih spesifik: tidak ikut kolom tanggal/datetime, jadi tidak error.

#kolom 'HasDependents' diganti jadi numerik
df_clean['HasDependents'] = df_clean['HasDependents'].fillna('No').map({
    'Yes': 1,
    'No': 0
})

# ===== 2. Outlier (IQR Method) =====
# Buat boxplot untuk semua kolom numerik
plt.figure(figsize=(10,6))
df[numeric_cols].boxplot()
plt.title("Boxplot Sebelum Menghapus Outlier")
plt.xlabel("Kolom")
plt.ylabel("Nilai")
plt.show()

for col in numeric_cols:
    Q1=df_clean[col].quantile(.25) #dari 100%
    Q3=df_clean[col].quantile(.75)
    IQR=Q3-Q1
    #Batas atas dan batas bawah
    lower_bound = Q1-1.5*IQR
    upper_bound = Q3+1.5*IQR
    #hapus baris yang berada diluar batas
    df_clean=df_clean[(df_clean[col] >= lower_bound) & (df_clean[col] <= upper_bound)]

print("outlier dihapus untuk semua kolom numerik")

# Buat boxplot untuk semua kolom numerik
plt.figure(figsize=(10,6))
df_clean[numeric_cols].boxplot()
plt.title("Boxplot Sesudah Menghapus Outlier")
plt.xlabel("Kolom")
plt.ylabel("Nilai")
plt.show()

# ===== 3. Duplikat Value =====
duplicate_all=df_clean[df_clean.duplicated(keep=False)]
print("Duplikat berdasarkan seluruh kolom =")
print(duplicate_all)

# ===== SIMPAN DATA SETELAH CLEANING =====
print(df_clean.head())
print(df_clean.info())

df_clean.to_csv('loan_clean_final.csv', index=False)

print("Data berhasil disimpan!")