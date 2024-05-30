import joblib
# Load the model
model = joblib.load('model/model.pkl')

example = [[1, 30.83, 0.000, 1, 1, 1.25, 1, 1, 1, 0, 202, 0	]]
y_real = 1

y = model.predict(example)

print('Predicted: ', y[0])
