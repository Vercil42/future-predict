import streamlit as st

# GUI
st.title('🔮 Prediksi Masa Depan Anda 🔮')
st.info("Klik tombol 🔄 *Reset* di bawah atau tekan tombol *R* untuk mengulang halaman.")
st.write('Selamat datang ke Future You Predictor! Masukkan kebiasaan kamu di bawah sini:')

# Menangkap data pengguna dengan input
def data_user():
    tidur = st.slider('Masukkan berapa lama kau tidur (dalam jam):', 0.0, 12.0, 7.0)
    belajar = st.slider('Masukkan berapa lama kau biasanya belajar (dalam jam):', 0.0, 10.0, 2.0)
    olahraga = st.slider('Masukkan berapa lama kau biasanya berolahraga (dalam jam):', 0.0, 5.0, 1.0)
    screen_time = st.slider('Masukkan berapa lama kau biasanya menggunakan gadget dalam sehari (dalam jam):', 0.0, 12.0, 5.0)

    if st.button("🔍 Klik Untuk Prediksi 🔍"):
        data = {
            "tidur": tidur,
            "belajar": belajar,
            "olahraga": olahraga,
            "screen time": screen_time
        }
        skor = analisa_kebiasaan(data)
        hasil = prediksi(skor)
        st.subheader("Prediksi Masa Depan Anda:")
        st.success(hasil)

    if st.button("🔄 Reset"):
        st.rerun()

# Menentukan skor berdasarkan data kebiasaan
def analisa_kebiasaan(data):
    score = 0

    # Waktu tidur
    if 7 <= data["tidur"] <= 9:
        score += 2
    elif 6 <= data["tidur"] < 7 or 9 < data["tidur"] <= 10:
        score += 1

    # Waktu belajar
    if data["belajar"] >= 3:
        score += 2
    elif data["belajar"] >= 1:
        score += 1

    # Waktu berolahraga
    if data["olahraga"] >= 1:
        score += 2
    elif data["olahraga"] >= 0.5:
        score += 1

    # Screen time
    if data["screen time"] <= 3:
        score += 2
    elif data["screen time"] <= 5:
        score += 1

    return score

# Menentukan hasil berdasarkan skor
def prediksi(skor):
    if skor >= 7:
        return "🌟 Anda berada di jalur yang tepat untuk menjadi individu yang fokus, sehat, dan kaya!"
    elif skor >= 5:
        return "🔄 Anda baik-baik saja, tetapi masih ada ruang untuk menjadi lebih baik."
    else:
        return "⚠️ Masa depan Anda sedang khawatir.Berusahalah untuk memperbaiki kebiasaanmu!"

# Memanggil kode
data_user()