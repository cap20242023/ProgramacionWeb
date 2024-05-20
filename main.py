from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/calculocompras', methods=['GET', 'POST'])
def calculocompras():
    if request.method == 'POST':
        nombre = str(request.form['nombre'])
        edad = float(request.form['edad'])
        tarros = float(request.form['tarros'])
        sdescuento = tarros * 9000
        if edad >= 18 and edad <= 30:
          descuento = sdescuento * .15
          tpagar = sdescuento - descuento
        elif edad > 30:
            descuento = sdescuento * .25
            tpagar = sdescuento - descuento
        else:
            descuento = sdescuento
            tpagar = sdescuento - descuento

        return render_template("calculocompras.html", sdecuento=sdescuento, nombre=nombre, edad=edad,descuento=descuento,tpagar=tpagar)
    return render_template('calculocompras.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nombre = str(request.form['nombre'])
        clave = str(request.form['clave'])


        if nombre == 'juan'  and clave == 'admin':

          respuesta = 'Bienvenido Administrador  ' + nombre

        elif nombre == "pepe" and clave == 'user':
            respuesta = 'Bienvenido Usuario  ' + nombre
        else:
            respuesta = 'Usuario o Contraseña incorrecto'

        return render_template("login.html", respuesta=respuesta,nombre=nombre)
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)