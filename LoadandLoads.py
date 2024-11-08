import pickle

data = {'name': 'Alice', 'age': 30}
with open('data.pkl', 'wb') as f:
    pickle.dump(data, f)

with open('data.pkl', 'rb') as f:
    loaded_data = pickle.load(f)
    print("Loaded Data:", loaded_data)

import pickle

data = {'name': 'Alice', 'age': 30}
serialized_data = pickle.dumps(data)
print("Serialized Data:", serialized_data)

deserialized_data = pickle.loads(serialized_data)
print("Deserialized Data:", deserialized_data)
