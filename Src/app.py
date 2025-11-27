from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello_docker():
    return '<h1> Build & Deploy Python Web App On AWS With GitHub Action</h1><br><p>When anyone talks about DevOps, CICD is the first word that comes to mind. CICD stands for Continuous Integration and Continuous Deployment (or Delivery). </p>,<p>Thank you for reading....</p> '

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
