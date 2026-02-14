import streamlit as st

# Səhifə nizamlamaları
st.set_page_config(page_title="Sənin üçün sürpriz 💖", page_icon="💌")

# Arxa fon və dizayn üçün CSS
st.markdown("""
    <style>
    .stApp {
        background-color: #ffb6c1;
    }
    .big-font {
        font-size:35px !important;
        font-weight: bold;
        color: #d00000;
        text-align: center;
        font-family: 'Comic Sans MS', cursive;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<p class="big-font">Mənimlə bir ömür boyu olmağa razısan? 🌹</p>', unsafe_allow_html=True)

# Düymələr üçün sütunlar
col1, col2 = st.columns(2)

with col1:
    if st.button("BƏLİ! ❤️"):
        st.balloons()
        st.success("Səni çox sevirəm! Hər günümüz belə gözəl keçsin! 🥂✨")
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHJleXozbmZ3Znd4Zzh3bmZ3Znd4Zzh3bmZ3Znd4Zzh3bmZ3Znd4Zzh3JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCBhbmxpY2smaz0x/l4pTdcifPKUYMDRLO/giphy.gif")

with col2:
    if st.button("Xeyr... 🥺"):
        st.warning("Ehhh, bir daha düşün bəlkə? 😜")
        st.info("Məncə sol tərəfdəki düymə daha qəşəngdir!")
