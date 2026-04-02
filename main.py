import streamlit as st, pandas as pd
df = pd.read_csv('data_csv')
st.title('Phan tich gia nha tai HN')
st.subheader('DS cac ngoi nha gia > 100 trieu/n2')
gia_100 = df[df['Gia ban/n2'] > 100]
st.dataframe(gia_100)

st.subheader('Quan co gia nha cao nhat, thap nhat')
q_cao = df.groupby('Quan/Huyen')['Gia ban(tong)'].max().idxnax()
q_thap = df.groupby('Quan/Huyen')['Gia ban(tong)'].min().idxmin()
st.write(f'Quan co gia nha cao nhat: {q_cao}')
st.write(f'Quan co gia nha thap nhat: {q_thap}')

st.subheader('Loại hình nhà ở có giá cao nhất')
loai_cao = df.groupby('Loại hình nhà ở')['Giá bán (tổng)'].mean().idxmax()
st.write(f'Loại hình nhà đắt nhất, rẻ nhất')
st.subheader('ngoi nhà đắt nhất, rẻ nhất')
dat_nhat = df.loc[df['Giá bán(tổng'].idxmax()]
re_nhat = df.loc[df['Giá bán(tổng'].idxmin()]
st.write('Ngôi nhà đắt nhất:')
st.write(dat_nhat)
st.write('Ngoi nhà rẻ nhất:')
st.write(re_nhat)
