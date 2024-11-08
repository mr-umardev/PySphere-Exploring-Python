import pickle

data = {'name': 'Alice', 'age': 30}
with open('data.pkl', 'wb') as f:
    pickle.dump(data, f)
print("Data dumped to file.")

import pickle

data = {'name': 'Alice', 'age': 30}
serialized_data = pickle.dumps(data)
print("Serialized Data (dumps):", serialized_data)
