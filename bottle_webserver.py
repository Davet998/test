from bottle import route, run, template

# http://127.0.0.1:8080/hello/dave

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

run(host='localhost', port=8080)
