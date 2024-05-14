from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def user():
    return render_template('/test/ajax.html')
    # return render_template('/test/ajax_get.html')

@app.route('/addUser', methods=['POST'])
def login():
    json = request.json
    print('recv:', json)
    dea = {'status': "开始学习"}
    return jsonify(dea)
    # return json

@app.route('/get_test', methods=['GET'])
def get_test():
    json = request.json
    print('recv:', json)
    dea = {'status': "开始学习"}
    return jsonify(dea)


if __name__ == '__main__':
    app.run(debug=True)
