from flask import Flask
#from werkzeug.routing import BaseConverter

# class IntListConverter(BaseConverter):
#     regex = r'\d+(?:,\d+)*,?'

#     def to_python(self, value):
#         return [int(x) for x in value.split(',')]

#     def to_url(self, value):
#         return ','.join(str(x) for x in value)

app = Flask(__name__)
#app.url_map.converters['int_list'] = BaseConverter
    
@app.route('/', methods=["GET"])
def index():
    return "Hello World"

@app.route('/add/<n1>/<n2>', methods=["GET"])
def add(n1, n2):
    return str(float(n1)+float(n2))

@app.route('/divide/<n1>/<n2>', methods=["GET"])
def divide(n1, n2):
    quotient = 0
    try:
        quotient = str(float(n1)/float(n2))
    except ZeroDivisionError as e:
        quotient = str(e)
    return quotient

@app.route('/arr/<values>/', methods=["GET"])
@app.route('/arr/<values>/<option>', methods=["GET"])
def getArr(values, option=None):
    print("values: ", values)
    vArr = values.split(",")

    if option == "reverse":
        return str(vArr[::-1])

    return str(vArr)

if __name__ == "__main__":
    app.run(debug=True)



    
