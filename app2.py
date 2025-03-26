import streamlit as st
from PIL import Image

# Title
st.title("Data Driven Products for Business")

# Telegram Contacts
#col_tg1, col_tg2, col_tg3 = st.columns([0.8, 0.2, 2])
#with col_tg1:
#   st.markdown("**Contacts:**", unsafe_allow_html=True)
#with col_tg2:
#    tg_icon = Image.open("telegram.png")
#     st.image(tg_icon, width=20)
# with col_tg3:
#     st.markdown("[Telegram](https://t.me/anafarM9)", unsafe_allow_html=True)
#
# # Telegram Contacts
# col_tg11, col_tg21= st.columns([1.5, 1.5])
# with col_tg11:
#     st.markdown("**Contacts:**", unsafe_allow_html=True)
# with col_tg21:
#     st.markdown("[Telegram](https://t.me/anafarM9)", unsafe_allow_html=True)

# st.markdown("**Contacts:**  [Telegram](https://t.me/anafarM9)", unsafe_allow_html=True)

st.markdown(
    "<p style='text-align: center; font-size: 16px;'>"
    "<b>Contacts:</b> <a href='https://t.me/anafarM9'>Telegram</a>"
    "</p>",
    unsafe_allow_html=True
)
# Directions
#st.header("Our Directions", divider="gray")
img1 = Image.open("1.png")  # Replace with actual file path
img2 = Image.open("3.png")  # Replace with actual file path
img3 = Image.open("5.png")  # Replace with actual file path


st.subheader("Trading Support Algorithms and Front-Office Risk Systems")
col_a, col_b = st.columns([1, 2])
with col_a:
    st.image(img1, width = 200)
with col_b:
    st.write("Focused on designing and implementing advanced trading strategies and front-office applications. Our expertise spans statistical modeling, machine learning, and algorithmic trading, enabling us to build high-performance solutions for execution, market-making, and risk management. We leverage cutting-edge quantitative methods and technology to optimize trading efficiency and support real-time decision-making in dynamic market environments.")

st.subheader("Product Analytics")
col_c, col_d = st.columns([2, 1])
with col_c:
    st.write("Full end-to-end numerical analysis, A/B testing design, and pilot evaluation to ensure data-driven product improvements. We build automated reporting systems and deep-dive into data to uncover valuable insights, helping teams optimize performance and drive strategic growth.")
with col_d:
    st.image(img2, width = 200)

st.subheader("Automation of Internal Regular Company Processes")
col_e, col_f = st.columns([1, 2])
with col_e:
 #   st.image(img3, use_container_width=True)
 st.image(img3, width=200)
with col_f:
    st.write("Focused on building and maintaining Data Warehouses (DWH) and optimizing internal company processes. Our expertise includes developing scalable data architectures, automating routine tasks, and ensuring seamless data flow for analytics and decision-making. We streamline operations through robust automation solutions, enhancing efficiency and data reliability across the organization.")

