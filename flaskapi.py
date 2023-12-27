from dotenv import load_dotenv
from flask import Flask, request, jsonify
from services.single_url import IITD
from services.prompt import prompt_response
from flask_cors import CORS, cross_origin

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)



@app.route('/home', methods=["GET","POST"])
@cross_origin()
def embeddings():
        try:
                if request.method == "POST":
                        o=IITD()
                        o.runall()
                        return jsonify({"Message":"Embedding are created successfully"})
        except Exception as e:
                return jsonify({"Error message in main method":e})


@app.route('/qna', methods=["GET","POST"])
@cross_origin()
def output():
        try:
                if request.method == "POST":
                        data = request.get_json()
                        user_question = data['Question']
                        obj=prompt_response()
                        result=obj.ask_question(user_question)
                        # result={"Answer":result['answer'], 
                        #         "Source":result['sources']}
                        
                        # # return result
                        return jsonify(result)
                

        except Exception as e:
                return jsonify({"Error message in main method":e})

if __name__ == '__main__':
    app.run(debug=True)