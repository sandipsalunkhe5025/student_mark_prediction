
from logging import debug
from flask import Flask,render_template,request



model = pickle.load(open('stud.pkl','rb'))




app = Flask(__name__)
 

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict',methods =['POST'])
def placement():
    
        
        cgpa = float(request.form.get('cgpa'))
        iq = int(request.form.get('iq'))
        profile_score = int(request.form.get('profile_score'))
        print("CGPA",cgpa)


        result = model.predict(np.array([cgpa,iq,profile_score]).reshape(1,3))
        # print(f"{result=}")
        if result[0] == 1:
            result = "Student Placed"
        else:
            result ="Not Placed"

           


        return render_template('index.html',prediction = result)
        
        return render_template('index.html',prediction = result)

if __name__ == '__main__':
    app.run(host= '0.0.0.0',port = 8080, debug=True)