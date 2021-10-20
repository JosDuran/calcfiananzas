from flask import Flask, render_template,request,jsonify, json, session

def F_P(tasa: float, n: float ):
    return (1+tasa)**n
    
def P_F(tasa: float, n: float):
    return (1+tasa)**(-n)

def P_A( tasa: float, n: float):
    temp = ((1+tasa)**n - 1)/(tasa* (1+tasa)**n)
    return temp

def A_P(tasa: float, n: float):
    return P_A(tasa,n)**(-1)

def F_A(tasa: float, n: float):
    temp = ((1+tasa)**n - 1)/(tasa)
    return temp
def A_F(tasa: float, n: float):
    return F_A(tasa,n)**(-1)

def P_G( tasa: float, n: float):
    temp = ((1+tasa)**n - tasa*n-1)/(tasa**2* (1+tasa)**n)
    return temp

def A_G(tasa: float, n: float):
    temp = tasa**(-1)  - n/(  (1+tasa)**n -1    )
    return temp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'oh_so_secret'
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/replaceandeval', methods= ['GET','POST'])
def replaceandeval ():
    
    aexp = request.json['expr']
    aexp = aexp.replace('F/P', 'F_P')
    aexp = aexp.replace('P/F', 'P_F')
    aexp = aexp.replace('P/A', 'P_A')
    aexp = aexp.replace('A/P', 'A_P')
    aexp = aexp.replace('F/A', 'F_A')
    aexp = aexp.replace('A/F', 'A_F')
    aexp = aexp.replace('P/G', 'P_G')
    aexp = aexp.replace('A/G', 'A_G')
    ares =  str(eval(aexp))
    resnewf = aexp + '='+ ares    
    return jsonify( {'res' : ares, 'resnf' : resnewf})
 

if __name__ == "__main__" :
    app.run(debug = True, host='0.0.0.0')