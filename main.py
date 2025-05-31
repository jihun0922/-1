import streamlit as st

# 앱 제목
st.title("나라별 GDP 순위 보기")

# 예시 데이터 (단위: 억 달러, 출처는 World Bank 등에서 추출 가능)
gdp_data = [
    {"국가": "미국", "GDP": 269390},
    {"국가": "중국", "GDP": 177340},
    {"국가": "일본", "GDP": 43810},
    {"국가": "독일", "GDP": 42230},
    {"국가": "한국", "GDP": 18180},
    {"국가": "인도", "GDP": 35740},
    {"국가": "영국", "GDP": 34560},
    {"국가": "프랑스", "GDP": 33180},
    {"국가": "이탈리아", "GDP": 22350},
    {"국가": "캐나다", "GDP": 22960},
]

# 정렬 방향 선택
order = st.radio("정렬 순서 선택", ("내림차순 (높은 GDP 우선)", "오름차순 (낮은 GDP 우선)"))

# 정렬 실행
reverse_sort = True if "내림차순" in order else False
sorted_data = sorted(gdp_data, key=lambda x: x["GDP"], reverse=reverse_sort)

# 출력
st.subheader("GDP 순위표")
for idx, item in enumerate(sorted_data, start=1):
    st.write(f"{idx}. {item['국가']} - ${item['GDP']:,}억")
