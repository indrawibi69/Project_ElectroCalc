import streamlit as st

st.set_page_config(
    page_title="Kalkulator Hukum Ohm",
    page_icon="⚡"
)

st.title("⚡ Kalkulator Hukum Ohm")
st.write("Menghitung Tegangan (V), Arus (I), atau Hambatan (R).")

pilihan = st.selectbox(
    "Apa yang ingin dihitung?",
    ["Tegangan (V)", "Arus (I)", "Hambatan (R)"]
)

if pilihan == "Tegangan (V)":
    I = st.number_input("Arus (I) dalam Ampere", min_value=0.0, step=0.1)
    R = st.number_input("Hambatan (R) dalam Ohm", min_value=0.0, step=1.0)

    if st.button("Hitung Tegangan"):
        V = I * R
        st.success(f"Tegangan = {V:.2f} V")

elif pilihan == "Arus (I)":
    V = st.number_input("Tegangan (V) dalam Volt", min_value=0.0, step=1.0)
    R = st.number_input("Hambatan (R) dalam Ohm", min_value=0.0, step=1.0)

    if st.button("Hitung Arus"):
        if R == 0:
            st.error("Hambatan tidak boleh 0 Ω.")
        else:
            I = V / R
            st.success(f"Arus = {I:.2f} A")

else:
    V = st.number_input("Tegangan (V) dalam Volt", min_value=0.0, step=1.0)
    I = st.number_input("Arus (I) dalam Ampere", min_value=0.0, step=0.1)

    if st.button("Hitung Hambatan"):
        if I == 0:
            st.error("Arus tidak boleh 0 A.")
        else:
            R = V / I
            st.success(f"Hambatan = {R:.2f} Ω")