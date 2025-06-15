from flask import Flask, request, render_template 

app = Flask("app")

messages = [{'title': 'Message One', 'content': 'Message One content'},{'title': 'Message 2', 'content': 'Message 2 content'} ]
passwords = {
    "saihsu" : "Pokemon10", 
    "aki" : "password",
    "parker" : "password",
    "henry" : "password",

}
@app.route("/messages")
def messages():
    return render_template('messages.html', messages=messages)



@app.route("/")
def hello_world():
    page = """
    <form action="/chat" method="get">
    <label for="username">Username:</label><br>
    <input type="text" id="username" name="username"><br>
    <label for="password">Password:</label><br>
    <input type="text" id="password" name="password"><br>
    <input type ="submit" value="Submit">
    </form> 
    """
    return page
    
@app.route("/chat", methods =["POST"])
def chat(): 
    username = request.form.get("username")
    password = request.form.get("password")
    message= request.form.get("message")
    page = """
    <form action="/chat" method="post">
    <label for="text">Enter message here:</label><br>
    <input type ="text" id="message" message="message"><br>
    <input type ="submit" value="->">
    </form>
    """
    hidden = """<input type="hidden" id="username" name = "username" value = " """ + username + """ ">"""
    if passwords.get(username) == password: 
        
        iden = "username is " + username + " password is " + password    
        return iden + "<br>" + page

    else:
        return "Incorrect username or password"

    