import streamlit as st

# Judul Aplikasi
st.title("Halo Teman-Teman Enell yang Cutiee!")

# Pertanyaan pertama
st.write("Apaa kabar?")

# Rating Hari Ini
rating = st.slider("Rating hari ini kamu gimanaa?", 1, 10)
st.write(f"Rating kamu: {rating}")

# Pertanyaan kedua
random_fact = st.radio("Gusyyy ceritain hal random kamu dong, mau yaa?", ("Yes", "No"))

if random_fact == "Yes":
    # Jika jawabannya "Yes", beri tempat untuk menulis
    answer = st.text_input("Ceritakan hal random kamu:")
    if answer:
        st.write("Terima kasih sudah berbagi!")
else:
    # Jika jawabannya "No", tampilkan emotikon sedih
    st.write("😢😢😢😢😢😢")
