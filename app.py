from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open('test.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Fuel_Type=request.form['fuel']
        if(Fuel_Type=='Petrol'):
            Fuel_Type_Petrol=1
            Fuel_Type_Diesel=0
            Fuel_Type_LPG=0
            Fuel_Type_Electric=0
            Fuel_Type_CNG__CNG=0
            Fuel_Type_Hybrid=0
            Fuel_Type_Petrol__CNG=0
            Fuel_Type_Petrol__LPG=0
        elif(Fuel_Type=='Diesel'):
            Fuel_Type_Petrol=0
            Fuel_Type_Diesel=1
            Fuel_Type_LPG=0
            Fuel_Type_Electric=0
            Fuel_Type_CNG__CNG=0
            Fuel_Type_Hybrid=0
            Fuel_Type_Petrol__CNG=0
            Fuel_Type_Petrol__LPG=0
        elif(Fuel_Type=='Petrol + LPG'):
            Fuel_Type_Petrol=0
            Fuel_Type_Diesel=0
            Fuel_Type_LPG=0
            Fuel_Type_Electric=0
            Fuel_Type_CNG__CNG=0
            Fuel_Type_Hybrid=0
            Fuel_Type_Petrol__CNG=0
            Fuel_Type_Petrol__LPG=1
        elif(Fuel_Type=='LPG'):
            Fuel_Type_Petrol=0
            Fuel_Type_Diesel=0
            Fuel_Type_LPG=1
            Fuel_Type_Electric=0
            Fuel_Type_CNG__CNG=0
            Fuel_Type_Hybrid=0
            Fuel_Type_Petrol__CNG=0
            Fuel_Type_Petrol__LPG=0
        elif(Fuel_Type=='Electric'):
            Fuel_Type_Petrol=0
            Fuel_Type_Diesel=0
            Fuel_Type_LPG=0
            Fuel_Type_Electric=1
            Fuel_Type_CNG__CNG=0
            Fuel_Type_Hybrid=0
            Fuel_Type_Petrol__CNG=0
            Fuel_Type_Petrol__LPG=0
        elif(Fuel_Type=='CNG + CNG'):
            Fuel_Type_Petrol=0
            Fuel_Type_Diesel=0
            Fuel_Type_LPG=0
            Fuel_Type_Electric=0
            Fuel_Type_CNG__CNG=1
            Fuel_Type_Hybrid=0
            Fuel_Type_Petrol__CNG=0
            Fuel_Type_Petrol__LPG=0
        elif(Fuel_Type=='Hybrid'):
            Fuel_Type_Petrol=0
            Fuel_Type_Diesel=0
            Fuel_Type_LPG=0
            Fuel_Type_Electric=0
            Fuel_Type_CNG__CNG=0
            Fuel_Type_Hybrid=1
            Fuel_Type_Petrol__CNG=0
            Fuel_Type_Petrol__LPG=0
        elif(Fuel_Type=='Petrol + CNG'):
            Fuel_Type_Petrol=0
            Fuel_Type_Diesel=0
            Fuel_Type_LPG=0
            Fuel_Type_Electric=0
            Fuel_Type_CNG__CNG=0
            Fuel_Type_Hybrid=0
            Fuel_Type_Petrol__CNG=1
            Fuel_Type_Petrol__LPG=0
        else:
            Fuel_Type_Petrol=0
            Fuel_Type_Diesel=0
            Fuel_Type_LPG=0
            Fuel_Type_Electric=0
            Fuel_Type_CNG__CNG=0
            Fuel_Type_Hybrid=0
            Fuel_Type_Petrol__CNG=0
            Fuel_Type_Petrol__LPG=0
        
        Year = int(request.form['Year'])
        
        Transmission=request.form['Transmission']
        if(Transmission=='Manual'):
            Transmission_Manual=1
        else:
            Transmission_Manual=0
        
        Owner=int(request.form['Owner'])
        
        Seller_Type=request.form['Seller type']
        if(Seller_Type=='Individual'):
            Seller_Type_Individual=1
            Seller_Type_Corporate=0
        elif(Seller_Type=='Corporate'):
            Seller_Type_Individual=0
            Seller_Type_Corporate=1
        else:
            Seller_Type_Individual=0
            Seller_Type_Corporate=0
        
        Engine =int(request.form['Engine'])
        
        Max_Power =float(request.form['Max Power'])
        
        Fuel_Tank_Capacity =float(request.form['Fuel Tank Capacity'])
        
        prediction=model.predict([[Year,Owner,Engine,Max_Power,Fuel_Tank_Capacity,Fuel_Type_CNG__CNG,Fuel_Type_Diesel,Fuel_Type_Electric,Fuel_Type_Hybrid,Fuel_Type_LPG,Fuel_Type_Petrol,Fuel_Type_Petrol__CNG,Fuel_Type_Petrol__LPG
                                   ,Transmission_Manual,Seller_Type_Corporate,Seller_Type_Individual]])
        output=round(prediction[0],2)
        return render_template('result.html', prediction=output)

if __name__=="__main__":
    app.run(debug=True)