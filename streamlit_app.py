
import streamlit as st
import pandas as pd

st.title("🧮 테더 거래금액 계산기")
uploaded_file = st.file_uploader("엑셀 파일을 업로드하세요 (.xlsx)", type="xlsx")

if uploaded_file:
    try:
        df = pd.read_excel(uploaded_file, skiprows=2)
        df = df[df["자산"] == "테더"]
        df["거래금액(숫자)"] = (
            df["거래금액"]
            .astype(str)
            .str.replace(",", "")
            .str.replace(" KRW", "")
            .astype(float)
        )
        total = df["거래금액(숫자)"].sum()
        point = total * 0.0001
        maker_reward = total * 0.00035
        total_point = point + maker_reward

        st.success(f"✅ 총 테더 거래금액: {int(total):,} 원")
        st.info(f"📌 거래 포인트 (0.01%): {point:,.2f} P")
        st.info(f"📌 메이커 리워드 (0.035%): {maker_reward:,.2f} P")
        st.info(f"🏁 총 포인트: {total_point:,.2f} P")
    except Exception as e:
        st.error(f"❌ 오류 발생: {e}")
