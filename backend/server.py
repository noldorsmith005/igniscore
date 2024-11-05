from flask import Flask, request, jsonify
from flask_cors import CORS
import random
import json
import base64
import os


app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})

CHARMAP = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "~", "!", "@", "#", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", ",", ".", "<", ">", "/", "?"]

AUTHENICATION = "#VERIFIED#"
ERROR = "#ERROR#"
DB = "database.json"

APPTOKEN = "ZQM.FS(^f!|WeKA&paZ5].*+u[>efN#s~Z~du98)0:OnVX@),cdRJG1(x|zVn3tC*/EC,)Rj,q,G)<A=U-P[[<i]tY3fTnvxdCC5~J0e#hOlafCG" #111
ADMINTOKEN = "i&if*M>4?ua3PSD3v9S&m6~:vGt|BxXEb>zX1x+wML>+CFr:d_7IH0m=j<gq<=fhAa6Ch<cS[F.QE5Ur_s!#DOXO=hA;h6DI!7xT{#{IEogK}_A,ri8a/6X*h+B^)=2qhH,Un-oZCLAF.7{_RI}5:&?ZQTG1l&Je&s-~eqtoTlDgB!Y#XZ07+Quht1tuZ/DuZ[jrA75t90#w|k8Ub_4#U.,0sOGiTD#h7fOML/~V{aMsnR~VA9~eBn48501U-xmFPTRJ6;.h1IDt4uikcv<ntQk(oxD|!k!.?FjrjjoSxw})B5SE+4_Anw[zkW~l8ygO,TW)/_iWMiF<n2MZ5&SjG*m&VQY1mH5vmeW-39-(AIe<6?z}OGN}G>m3/(me.W?rt;Gy31aZJcYrrrZsx8a+PB}L0-3[CBx@BMEW{1Gx!DScJ]&LIXlfOY*Lu!FkPTA1*PiKaS~c5bxxcD:H;y*[}weB|{)rn}cW;381Kb*~&d{,|hcG+6N0n+6kY3?=9t^y;4>MxC,mc+?~-X4LJ*+3O{3xh1Vv!UtsPt*gw)MI>*K{~YUus^|jM=B>hg_3n?y(y@+R07EtJ[9pjX<=jJ9hDFb^b~*(=Z;!N<bXrMZyB00C),RUtTO7QFy[)^Pd3W#bZJX:=~tyRp.aI=-q(1?z=PduU5.@/NpJAbR]H,ebEk9Mi/5_d.6qp4&DbHy+Y6>JTGKvhv^mwm^i4uD:;hT7<Z]~}RgNepIjwggdSG,nS#GLn>o(LlIn9<=OQg(tN:ThTr2zK/f]N1lc2_hw*TrFzexnCKjsrPS4R=}2Rx4z0iv02TeLVPxp~Zf[M78F8OcBw6@5NAyS[;^,T=RrqwD6Dd=?fwhfw7/CAbQB-9!va}koMrkY4i,7xG]b#NlUEZTq9x9Of<yrfLU)aM>PLb>*cuy#/_vybS7}&(^^1nU^&<C9M1/??rhS:=.c_fdXV+6g^6Ma9nL2uqa9<BIeHHDE*i+tk9Zo}w=iWEnU}o!_" #999

Admin = ["172.66.2.214"]


#--------------------------------------### Server Functions ###--------------------------------------#

def newToken():
    i = 0
    token = ""
    while i <= 100:
        idx = random.randint(0, 87)
        token = token + CHARMAP[idx]

        i += 1

    return token
    
def searchString(base, filter):
    base = list(base.lower())
    filter = list(filter.lower())
    matched = []
    char = 0
    subchar = 0
    while char < len(base) and subchar < len(filter):
        if base[char] == filter[subchar]:
            matched.append(filter[subchar])
            char += 1
            subchar += 1
        else :
            if len(matched) > 0:
                matched = []
            char += 1
        if matched == filter:
            return True

    return False
   
#----------------------------------------------------------------------------#
#--------------------------------------### Routing Protocols ###--------------------------------------#
#----------------------------------------------------------------------------#

#----------------------------### Home Route (Browser Display) (Admin Access Only) ###----------------------------#
@app.route("/", methods=["GET"])
def home():
    ip_addr = request.remote_addr
    if ip_addr in Admin:
        db = open(DB)
        data = json.load(db)
        db.close()

        return data, 200
    else :
        messsage = f"Unauthorized request to admin-token server functionality from {ip_addr}"
        print(messsage)
        return jsonify(messsage), 200

#--------------------------------------### Fetch Compositions ###--------------------------------------#
@app.route("/works/<category>/all", methods=["GET"]) 
def fetchCompositions(category):
    ip_addr = request.remote_addr
    apptoken = request.headers.get("App-Token")
    usertoken = request.headers.get("User-Token")

    compositions = []

    if apptoken == APPTOKEN:
        with open(DB, 'r') as file:
            data = json.load(file)
            users = data["Users"]
            Sessions = data["Sessions"]
            for session in Sessions:
                if session["token"] == usertoken:
                    for user in users:
                        if user["username"] == category:
                            contacts = user["contacts"]
                            for contact in contacts:
                                compositions.append(contact)

                            response = jsonify(compositions)
                            return response, 200
            
            print(f"Invalid user token from {ip_addr}")
            return jsonify(ERROR), 200
    
    else :
        print(f"Unauthorized server request detected from {ip_addr}. Invalid app token")
        return jsonify(ERROR), 200
    
#--------------------------------------### Add Composition (Admin Access) ###--------------------------------------#
@app.route("/works/all", methods=["POST"]) 
def addComposition():
    ip_addr = request.remote_addr
    data = request.get_json()
    name = data["username"]
    category = data["category"]
    runtime = data["runtime"]
    thumbnail = data["thumbnail"]
    file = data["file"]
    apptoken = request.headers.get("App-Token")
    usertoken = request.headers.get("User-Token")

    if apptoken == APPTOKEN:
        with open(DB, 'r') as file:
            data = json.load(file)
            users = data["Users"]
            Sessions = data["Sessions"]
            for session in Sessions:
                if session["token"] == usertoken:
                    with open(DB, 'w') as file:
                        file.seek(0)
                        json.dump(data, file, indent = 4, ensure_ascii=False)
                    
                    return jsonify(AUTHENICATION), 200
            
            print(f"Invalid user token from {ip_addr}")
            return jsonify(ERROR), 200
    
    else :
        print(f"Unauthorized server request detected from {ip_addr}. Invalid app token")
        return jsonify(ERROR), 200

#--------------------------------------### Remove Contact ###--------------------------------------#
@app.route("/users/<username>/contacts/<contactuser>", methods=["DELETE"]) 
def deleteContact(username, contactuser):
    ip_addr = request.remote_addr
    apptoken = request.headers.get("App-Token")
    usertoken = request.headers.get("User-Token")

    if apptoken == APPTOKEN:
        with open(DB, 'r') as file:
            data = json.load(file)
            users = data["Users"]
            Sessions = data["Sessions"]
            for session in Sessions:
                if session["token"] == usertoken:
                    for user in users:
                        if user["username"] == username:
                            for contact in user["contacts"]:
                                if contact == contactuser:
                                    user["contacts"].remove(contact)

                                    with open(DB, 'w') as file:
                                        file.seek(0)
                                        json.dump(data, file, indent = 4)
                                    
                                    return jsonify(AUTHENICATION), 200
                        
                            return jsonify(ERROR), 200    
                    return jsonify(ERROR), 200
            
            print(f"Invalid user token from {ip_addr}")
            return jsonify(ERROR), 200
    
    else :
        print(f"Unauthorized server request detected from {ip_addr}. Invalid app token")
        return jsonify(ERROR), 200

#--------------------------------------### Modify Chat ###--------------------------------------#
@app.route("/chatstreams/groups/<id>/settings", methods=["PATCH"]) 
def modifyChat(id):
    ip_addr = request.remote_addr
    chat_data = request.get_json()
    new_pic = chat_data["newpic"]
    new_name = chat_data["newname"]
    new_admins = chat_data["newadmins"]
    new_users = chat_data["newusers"]
    self_destructing = chat_data["selfdestruct"]
    apptoken = request.headers.get("App-Token")
    usertoken = request.headers.get("User-Token")

    if apptoken == APPTOKEN:
        with open(DB, 'r') as file:
            data = json.load(file)
            chats = data["ChatStreams"]
            Sessions = data["Sessions"]
            for session in Sessions:
                if session["token"] == usertoken:
                    id = int(id)
                    for chat in chats:
                        if chat["id"] == id:
                            chat["name"] = new_name
                            chat["admins"] = new_admins
                            chat["selfdestructing"] = self_destructing
                            if new_pic != "":
                                path = chat["picture"]
                                with open(path, 'wb') as image_file:
                                    image_file.seek(0)
                                    image_data = base64.b64decode(new_pic)
                                    image_file.write(image_data)

                            chat["users"] = []
                            for user in new_users:
                                if (validate(user)):
                                    chat["users"].append(user)

                                else :
                                    return jsonify(ERROR), 200
                            for admin in chat["admins"]:
                                if not admin in chat["users"]:
                                    chat["admins"].remove(admin)

                
                            with open(DB, 'w') as file:
                                file.seek(0)
                                json.dump(data, file, indent = 4)

                            response = jsonify(AUTHENICATION)
                            return response, 200
                    
                    response = jsonify(ERROR)
                    return response, 200
                    
            print(f"Invalid user token from {ip_addr}")
            return jsonify(ERROR), 200
        
    else :
        print(f"Unauthorized server request detected from {ip_addr}")


#----------------------------------------------------------------------------#
#--------------------------------------### Entry-Point ###--------------------------------------#
#----------------------------------------------------------------------------#
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9000, debug=True)

