# http://127.0.0.1:5000/symbol/[20MICRONS]

from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# users_path1 = 'https://archives.nseindia.com/content/equities/EQUITY_L.csv'
users_path = 'C:\\Users\\Hello\\Downloads\\combine_data.csv'


@app.route('/symbol/<string:n>')
def get(n):
    dic = {}
    data = pd.read_csv(users_path)
    data = data.to_dict()
    smbl = data["symbol"]
    for i in smbl:
        if smbl[i] == n:
            for j in data:
                dic[j] = data[j][i]
            return dic


if __name__ == '__main__':
    app.run(debug=True)