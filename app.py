from flask import Flask, render_template,request

def F_P(tasa: float, n: int ):
    return (1+tasa)**n
    
def P_F(tasa: float, n: int):
    return (1+tasa)**(-n)

def F_A(tasa: float, n: int):
    temp = ((1+tasa)**n - 1)/(tasa)
    return temp
def A_F(tasa: float, n: int):
    return F_A(tasa,n)**(-1)

def P_G( tasa: float, n: int):
    temp = ((1+tasa)**n - tasa*n-1)/(tasa**2* (1+tasa)**n)
    return temp

def A_G(tasa: float, n: int):
    temp = tasa**(-1)  - n/(  (1+tasa)**n -1    )
    return temp

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/replaceandeval', methods= ['POST'])
def replaceandeval ():
    aexp = request.form['expression']
    anew = aexp.replace('/', '_')
    ares = str(eval(anew))
    return(ares)

if __name__ == "__main__" :
    app.run(debug = True, host='0.0.0.0')