import streamlit as st

# تنظیمات صفحه
st.set_page_config(page_title="محاسبه سود و زیان", page_icon="💰")

st.title("💰 ماشین‌حساب سود و زیان معاملات ارز دیجیتال")

# انتخاب حالت
mode = st.radio("انتخاب حالت:", ["📈 محاسبه سود و زیان", "🧠 تحلیل معکوس (محاسبه قیمت فروش هدف)"])

# نرخ تبدیل دلاری (قابل تنظیم توسط کاربر)
usd_rate = st.number_input("نرخ دلار (تومان)", min_value=1.0, value=60000.0, step=100.0)

# ورودی‌های مشترک
buy_price = st.number_input("قیمت خرید (تومان)", min_value=0.0, format="%.2f")
amount = st.number_input("تعداد ارز", min_value=0.0, format="%.4f")
buy_fee_percent = st.number_input("کارمزد خرید (%)", min_value=0.0, value=0.4, step=0.1)
sell_fee_percent = st.number_input("کارمزد فروش (%)", min_value=0.0, value=0.4, step=0.1)

# حالت ۱: محاسبه سود و زیان
if mode == "📈 محاسبه سود و زیان":
    sell_price = st.number_input("قیمت فروش (تومان)", min_value=0.0, format="%.2f")

    if st.button("محاسبه سود یا زیان"):
        if buy_price == 0 or amount == 0:
            st.warning("لطفاً قیمت خرید و تعداد را وارد کنید.")
        else:
            buy_price_with_fee = buy_price * (1 + buy_fee_percent / 100)
            sell_price_with_fee = sell_price * (1 - sell_fee_percent / 100)

            profit = (sell_price_with_fee - buy_price_with_fee) * amount
            total = buy_price * amount
            percent = (profit / total) * 100 if total else 0
            profit_usd = profit / usd_rate

            if profit > 0:
                st.success(f"✅ سود: {profit:,.0f} تومان ({percent:.2f}٪)")
                st.success(f"💵 معادل سود به دلار: ${profit_usd:,.2f}")
            elif profit < 0:
                st.error(f"❌ ضرر: {abs(profit):,.0f} تومان ({abs(percent):.2f}٪)")
                st.error(f"💵 معادل ضرر به دلار: ${abs(profit_usd):,.2f}")
            else:
                st.info("⚖️ نه سود کردید، نه ضرر.")

# حالت ۲: تحلیل معکوس
elif mode == "🧠 تحلیل معکوس (محاسبه قیمت فروش هدف)":
    desired_profit = st.number_input("مقدار سود مورد انتظار (تومان)", min_value=0.0, format="%.0f")

    if st.button("محاسبه قیمت فروش موردنیاز"):
        if buy_price == 0 or amount == 0:
            st.warning("لطفاً قیمت خرید و تعداد را وارد کنید.")
        else:
            buy_price_with_fee = buy_price * (1 + buy_fee_percent / 100)

            # فرمول برعکس برای پیدا کردن قیمت فروش نهایی
            sell_price_with_fee = (desired_profit / amount) + buy_price_with_fee
            sell_price = sell_price_with_fee / (1 - sell_fee_percent / 100)
            profit_usd = desired_profit / usd_rate

            st.info(f"برای {desired_profit:,.0f} تومان سود، باید در قیمت حدود {sell_price:,.0f} تومان بفروشید.")
            st.info(f"💵 معادل این سود به دلار: ${profit_usd:,.2f}")
