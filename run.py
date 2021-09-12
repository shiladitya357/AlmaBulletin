from bulletin import app
from bulletin import db

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5001)
