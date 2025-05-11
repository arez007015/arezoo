import streamlit as st

st.set_page_config(page_title="محاسبه سود و زیان", page_icon="💰")
st.title("💰 ماشین‌حساب سود و زیان معاملات ارز دیجیتال")

buy_price = st.number_input("قیمت خرید (تومان)", min_value=0.0, format="%.2f")
sell_price = st.number_input("قیمت فروش (تومان)", min_value=0.0, format="%.2f")
amount = st.number_input("تعداد ارز (مثلاً 0.5 بیت‌کوین)", min_value=0.0, format="%.4f")

if st.button("محاسبه سود یا زیان"):
    if buy_price == 0 or amount == 0:
        st.warning("لطفاً قیمت خرید و تعداد را وارد کنید.")
    else:
        profit = (sell_price - buy_price) * amount
        total = buy_price * amount
        percent = (profit / total) * 100

        if profit > 0:
            st.success(f"✅ سود: {profit:,.0f} تومان ({percent:.2f}٪ سود)")
        elif profit < 0:
            st.error(f"❌ ضرر: {abs(profit):,.0f} تومان ({abs(percent):.2f}٪ ضرر)")
        else:
            st.info("⚖️ نه سود کردید، نه ضرر.")
