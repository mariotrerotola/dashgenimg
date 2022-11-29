import pandas as pd

data = pd.read_csv('data.csv', header=None)
print(data)
data.rename(columns = {0:'property', 
                       1:'sentiment'}, 
            inplace = True)
print(data.groupby(['property']).mean()) 
data['property'].to_csv('wordCloud.csv',index=False)

