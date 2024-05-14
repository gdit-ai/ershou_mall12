from flask import Flask, render_template, jsonify

app = Flask(__name__)

# 假设你有一些数据要显示
data_for_chart1 = {
    "categories": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "data": [820, 932, 901, 934, 1290, 1330, 1320]
}

data_for_chart2 = {
    "name": "访问来源",
    "data": [
        {"value": 335, "name": "直接访问"},
        {"value": 310, "name": "邮件营销"},
        {"value": 234, "name": "联盟广告"},
        {"value": 135, "name": "视频广告"},
        {"value": 1548, "name": "搜索引擎"}
    ]
}
@app.route('/')
def index():
    # 将数据传递给模板
    return render_template('/test/echart2.html', chart1_data=data_for_chart1, chart2_data=data_for_chart2)


if __name__ == '__main__':
    app.run(debug=True)