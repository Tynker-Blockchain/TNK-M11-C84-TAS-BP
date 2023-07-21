from flask import Flask, render_template, request
import os
from encrypt import encrypt, generateKeys
# Import generateHash from hash.py


STATIC_DIR = os.path.abspath('static')

app = Flask(__name__, static_folder=STATIC_DIR)
app.use_static_for_root = True

blockData={}
encryptedData ={}

@app.route("/", methods= ["GET", "POST"])
def home():
    print("running")
    print(request.args.get("form"))
    global blockData, encryptedData
    validation = None
    if request.method == "GET":
        return render_template('index.html')
    else: 
        sender = request.form.get("sender")
        receiver = request.form.get("receiver")
        amount = request.form.get("amount")
       
        blockData = { 
                "sender": sender, 
                "receiver": receiver, 
                "amount": amount
            }
        
        # Remove generation of keys
        publicKey, privateKey = generateKeys()

        # Instead of encrypting, use the generateHas() to generate hash for sender, receiver
        sender = encrypt(sender, publicKey)
        receiver = encrypt(receiver, publicKey)  
        

        # Concatinate sender, receiver and amount and generateHash and store the result in blockHash variable
        

        # Add a key "hash" in the encryptedData and store blockHash in it 
        encryptedData = { 
                "sender": sender, 
                "receiver": receiver, 
                "amount": amount
            }

    return render_template('index.html', blockData = blockData, encryptedData = encryptedData)
    
if __name__ == '__main__':
    app.run(debug = True, port=4000)