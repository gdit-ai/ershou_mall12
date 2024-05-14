from flask import Flask,render_template
app = Flask(__name__)
@app.route('/')
def index():
    product_list = [
         {
            "id": 2,
            "name" : "Apple 2019 MacBook Pro 16【带触控栏】九代六核i7" ,
            "price": 18799,
        },
        {
            "id": 3,
            "name": "Apple AirPods 蓝牙无线耳机 适用于iPhone7/8/X手机耳机",
            "price": 1299,
        },
        {
            "id": 4,
            "name": "小米10 双模5G 骁龙865",
            "price": 4299,
        },
        {
            "id": 5,
            "name": "Apple 2019 MacBook Pro 16【带触控栏】九代六核i7",
            "price": 18799,
        },
    ]
    return render_template("table_c1.html", product_list= product_list)
app.run(debug=True)