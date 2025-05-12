import streamlit as st

# تنظیمات اولیه صفحه
st.set_page_config(page_title="محاسبه سود و زیان", page_icon="💰")

st.title("💰 ماشین‌حساب سود و زیان معاملات ارز دیجیتال")

# ورودی از کاربر
buy_price = st.number_input("قیمت خرید (تومان)", min_value=0.0, format="%.2f")
sell_price = st.number_input("قیمت فروش (تومان)", min_value=0.0, format="%.2f")
amount = st.number_input("تعداد ارز (مثلاً 0.5 بیت‌کوین)", min_value=0.0, format="%.4f")
buy_fee_percent = st.number_input("کارمزد خرید (%)", min_value=0.0, value=0.4, step=0.1)
sell_fee_percent = st.number_input("کارمزد فروش (%)", min_value=0.0, value=0.4, step=0.1)

# وقتی دکمه "محاسبه" زده شد
if st.button("محاسبه سود یا زیان"):
    if buy_price == 0 or amount == 0:
        st.warning("لطفاً قیمت خرید و تعداد را وارد کنید.")
    else:
        # اعمال کارمزد روی قیمت‌ها
        buy_price_with_fee = buy_price * (1 + buy_fee_percent / 100)
        sell_price_with_fee = sell_price * (1 - sell_fee_percent / 100)

        # محاسبه سود و زیان
        profit = (sell_price_with_fee - buy_price_with_fee) * amount
        total = buy_price_with_fee * amount
        percent = (profit / total) * 100

        # نمایش نتیجه
        if profit > 0:
            st.success(f"✅ سود: {profit:,.0f} تومان ({percent:.2f}٪ سود)")
        elif profit < 0:
            st.error(f"❌ ضرر: {abs(profit):,.0f} تومان ({abs(percent):.2f}٪ ضرر)")
        else:
            st.info("⚖️ نه سود کردید، نه ضرر.")
