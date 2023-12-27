from flask import Flask,render_template,request

app = Flask(__name__)


from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://waralkarshayu:shayu123@cluster0.3tchlbf.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client["Registration"]

collection = db["Data"]

@app.route("/")
def home():
     return render_template("index.html")

@app.route("/main",methods=["GET","POST"])
def Registration_Page():
        if request.method == "GET":
             return render_template("form.html")
        else:
            name = request.form.get("name")
            age = request.form.get("age")
            city = request.form.get("city")

            data ={
                 "name":name,
                 "age":age,
                 "city":city
            }
            collection.insert_one(data)
            return render_template("result.html")


if __name__ == "__main__":
    app.run(debug=True)        
