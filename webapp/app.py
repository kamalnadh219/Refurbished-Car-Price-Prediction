#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[2]:


from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np


# In[3]:


from flask import Flask, request, render_template
import numpy as np
import pickle

app = Flask(__name__)

# Load the model pipeline
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('home.html', prediction=None)  # Pass None initially for prediction

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form.to_dict()

    # Prepare input data
    input_data = [
        str(data['feature1']).strip(),  # Clean input for ordinal feature
        int(data['feature2']),
        str(data['feature3']).strip(),  # Clean input for one-hot feature
        int(data['feature4']),
        str(data['feature5']).strip(),  # Clean input for ordinal feature
        int(data['feature6']),
        float(data['feature7']),
        float(data['feature8'])
    ]

    input_array = np.array(input_data).reshape(1, -1)

    # Make prediction
    try:
        prediction = model.predict(input_array)
        result = prediction[0]  # Get the predicted value

        return render_template('home.html', prediction=result)  # Render with prediction
    except ValueError as e:
        return render_template('home.html', prediction="Error: " + str(e))  # Handle error

if __name__ == "__main__":
    app.run(debug=True)


# In[ ]:




