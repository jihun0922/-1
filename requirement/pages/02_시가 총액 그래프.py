import plotly.graph_objects as go
import pandas as pd
import plotly.graph_objects as go
import pandas as pd
import plotly.io as pio
pio.renderers.default = 'browser'  # 브라우저에서 그래프 열기


# 시가총액 데이터 (단위: 조 달러)
data = {
    '기업명': ['Apple', 'Microsoft', 'Alphabet', 'Amazon', 'NVIDIA', 'Meta Platforms', 'Tesla', 'Berkshire Hathaway', 'TSMC', 'Saudi Aramco'],
    '2022': [2.07, 1.79, 1.15, 0.86, 0.68, 0.36, 0.38, 0.68, 0.54, 1.86],
    '2023': [2.87, 2.53, 1.92, 1.87, 1.66, 0.59, 0.39, 0.70, 0.45, 2.11],
    '2024': [3.78, 3.13, 2.32, 2.30, 3.28, 1.47, 1.29, 1.02, 1.02, 1.80]
}

df = pd.DataFrame(data)

# 연도별 시가총액 변화를 선 그래프로 표시
fig = go.Figure()

years = ['2022', '2023', '2024']
for i in range(len(df)):
    fig.add_trace(go.Scatter(
        x=years,
        y=[df.loc[i, year] for year in years],
        mode='lines+markers',
        name=df.loc[i, '기업명']
    ))

fig.update_layout(
    title='2022~2024년 시가총액 상위 10개 기업의 시가총액 변화',
    xaxis_title='연도',
    yaxis_title='시가총액 (조 달러)',
    hovermode='x unified'
)

fig.show()
