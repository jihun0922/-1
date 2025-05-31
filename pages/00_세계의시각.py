import streamlit as st
from datetime import datetime, timedelta

st.title("🕒 세계 주요 도시 현재 시각 보기")

# 도시별 UTC 시차
cities = {
    "서울": 9,
    "뉴욕": -4,
    "런던": 0,
    "도쿄": 9,
    "로스앤젤레스": -7,
    "파리": 2,
    "시드니": 10,
    "두바이": 4,
    "베이징": 8,
    "모스크바": 3
}

selected_cities = st.multiselect("도시를 선택하세요", list(cities.keys()), default=list(cities.keys()))

# 현재 시간 (UTC 기준)
now_utc = datetime.utcnow()

st.subheader("도시별 현재 시각 (버튼 클릭 시 갱신)")

# 각 도시의 시간 계산
for city in selected_cities:
    offset = cities[city]
    local_time = now_utc + timedelta(hours=offset)
    st.write(f"🕓 {city}: {local_time.strftime('%Y-%m-%d %H:%M:%S')}")

# 새로고침 버튼
if st.button("⏳ 시간 갱신"):
    st.experimental_rerun()
