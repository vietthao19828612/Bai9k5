import streamlit as st
import pandas as pd

# Đọc dữ liệu
df = pd.read_csv('data.csv')

st.title('Phân tích giá nhà tại Hà Nội')

# 1. Danh sách nhà giá > 100 triệu/m2
st.subheader('DS các ngôi nhà giá > 100 triệu/m2')
gia_100 = df[df['Giá bán/m2'] > 100]
st.dataframe(gia_100)

# 2. Quận có giá cao nhất, thấp nhất
st.subheader('Quận có giá nhà cao nhất, thấp nhất')
q_cao = df.groupby('Quận/Huyện')['Giá bán (tổng)'].max().idxmax()
q_thap = df.groupby('Quận/Huyện')['Giá bán (tổng)'].min().idxmin()

st.write(f'Quận có giá nhà cao nhất: {q_cao}')
st.write(f'Quận có giá nhà thấp nhất: {q_thap}')

# 3. Loại hình nhà ở có giá cao nhất
st.subheader('Loại hình nhà ở có giá cao nhất')
loai_cao = df.groupby('Loaị hình nhà ở')['Giá bán (tổng)'].mean().idxmax()
st.write(f'Loại hình nhà đắt nhất: {loai_cao}')

# 4. Ngôi nhà đắt nhất và rẻ nhất
st.subheader('Ngôi nhà đắt nhất, rẻ nhất')
dat_nhat = df.loc[df['Giá bán (tổng)'].idxmax()]
re_nhat = df.loc[df['Giá bán (tổng)'].idxmin()]

st.write('Ngôi nhà đắt nhất:')
st.write(dat_nhat)

st.write('Ngôi nhà rẻ nhất:')
st.write(re_nhat)

