from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.qgsyonz.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

##여기는 서버공간

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/bucket", methods=["POST"])
def bucket_post():
    bucket_receive = request.form['bucket_give'] ##서버에서는 bucket_give 데이터를 bucket_recieve라고 받는다
    #그리고 그 bucket_recieve를 몽고 디비로 보낸다.
    
    doc = {
        'bucket':bucket_receive,
       
        }
    db.buckets.insert_one(doc)

    return jsonify({'result': '저장완료!'})
    
@app.route("/bucket", methods=["GET"])
def bucket_get():
    all_buckets = list(db.buckets.find({},{'_id':False}))

    return jsonify({'result': all_buckets})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)