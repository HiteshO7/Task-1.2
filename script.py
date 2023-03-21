from flask import *
from twilio.rest import Client
import random

app = Flask(__name__,template_folder='template')
app.secret_key="otp"

@app.route('/')
def home():
    return render_template("loggin.html")

@app.route('/getOTP',methods=['POST'])
def getOTP():

    number = request.form['number']
    val=getOTPApi(number)
    if val:
        return render_template('otp.html')

@app.route('/validateOTP',methods=['POST'])
def validateOTP():
    otp = request.form['otp']
    if 'response' in session:
        s = session['response']
        session.pop('response',None)
        if s == otp:
            return render_template('home.html')
        else:
            return'You are not Authorized, sorry'


def generateOTP():
    return random.randrange(100000,999999)

def getOTPApi(number):
    account_sid ='ACeb3038036a03aed4783c1ae8c514a6d8'
    auth_token ='6cc5d4a3af48021664b38b90d2ecc768'
    client = Client(account_sid, auth_token)
    otp = generateOTP()
    body ='Your OTP is' + str(otp)
    session['response'] = str(otp)
    message = client.messages.create(
                              from_='+19144543174',
                              body=body,
                              to=number

                        )

    if message.sid:
        return True
    else:
        False




if __name__=='__main__':
    app.run(debug=True)
