import streamlit as st
import matplotlib.pyplot as plt

# تنظیمات اولیه صفحه
st.set_page_config(page_title="محاسبه سود و زیان", page_icon="💰")

st.title("💰 ماشین‌حساب سود و زیان معاملات ارز دیجیتال")

# ورودی از کاربر
buy_price = st.number_input("قیمت خرید (تومان)", min_value=0.0, format="%.2f")
sell_price = st.number_input("قیمت فروش (تومان)", min_value=0.0, format="%.2f")
amount = st.number_input("تعداد ارز (مثلاً 0.5 بیت‌کوین)", min_value=0.0, format="%.4f")
buy_fee_percent = st.number_input("کارمزد خرید (%)", min_value=0.0, value=0.4, step=0.1)
sell_fee_percent = st.number_input("کارمزد فروش (%)", min_value=0.0, value=0.4, step=0.1)

# دکمه محاسبه
if st.button("محاسبه سود یا زیان"):
    if buy_price == 0 or amount == 0:
        st.warning("لطفاً قیمت خرید و تعداد را وارد کنید.")
    else:
        buy_price_with_fee = buy_price * (1 + buy_fee_percent / 100)
        sell_price_with_fee = sell_price * (1 - sell_fee_percent / 100)
        profit = (sell_price_with_fee - buy_price_with_fee) * amount
        total = buy_price * amount
        percent = (profit / total) * 100

        if profit > 0:
            st.success(f"✅ سود: {profit:,.0f} تومان ({percent:.2f}٪ سود)")
        elif profit < 0:
            st.error(f"❌ ضرر: {abs(profit):,.0f} تومان ({abs(percent):.2f}٪ ضرر)")
        else:
            st.info("⚖️ نه سود کردید، نه ضرر.")

        # رسم نمودار سود و زیان
        fig, ax = plt.subplots()
        ax.bar(["سود/زیان"], [profit], color="green" if profit > 0 else "red")
        ax.set_ylabel("مقدار (تومان)")
        ax.set_title("نمودار سود یا زیان")
        st.pyplot(fig)
