from flask import Flask, render_template, jsonify

app = Flask(__name__)

# 假设你有一些数据要显示
data = {
    "categories": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "data": [820, 932, 901, 934, 1290, 1330, 500]
}


@app.route('/')
def index():
    # 将数据传递给模板
    return render_template('/test/echart.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)