from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def Index():
    return render_template ('Index.html')

@app.route('/Index.html')
def Index1():
    return render_template ('Index.html')

@app.route('/index.html')
def inicio():
    return render_template('inicio.html')

@app.route('/')
def Quiensoy():
    return render_template ('Quiensoy.html')

@app.route('/Quiensoy.html')
def Quiensoy2():
    return render_template ('Quiensoy.html')

@app.route('/')
def Portafolio():
    return render_template ('Portafolio.html')

@app.route('/Portafolio.html')
def Portafolio3():
    return render_template ('Portafolio.html')

@app.route('/')
def Blog():
    return render_template ('Blog.html')

@app.route('/Blog.html')
def Blog4():
    return render_template ('Blog.html')

@app.route('/')
def Contactanos():
    return render_template ('Contactanos.html')

@app.route('/Contactanos.html')
def Contactanos5():
    return render_template ('Contactanos.html')

@app.route('/')
def registro():
    return render_template ('registro.html')

@app.route('/registro.html')
def registro6():
    return render_template ('registro.html')


if __name__== '__main__':
    app.run(debug=True)
    
