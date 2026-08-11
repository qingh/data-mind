import chainlit as cl
import pandas as pd
import plotly.express as px

from mysql_db import fetch_all

rows = fetch_all("SELECT * FROM user_table")
print("###", rows)


@cl.step(type="tool")
async def tool():
    # Fake tool
    await cl.sleep(2)
    return "Response from the tool!"


@cl.on_message
async def main(message: cl.Message):
    # 假设这是你的分析结果
    df = pd.DataFrame(
        {
            "月份": ["1月", "2月", "3月", "4月"],
            "销售额": [12000, 15000, 9000, 21000],
            "利润率": [0.12, 0.15, 0.08, 0.18],
        }
    )

    # 1. 展示数据表格
    table_element = cl.Dataframe(data=df, display="inline", name="分析结果表")

    # 2. 展示趋势图
    fig = px.line(df, x="月份", y="销售额", markers=True, title="月度销售额趋势")
    chart_element = cl.Plotly(name="销售趋势", figure=fig, display="inline")

    await cl.Message(
        content="这是本季度的数据分析结果：", elements=[table_element, chart_element]
    ).send()
