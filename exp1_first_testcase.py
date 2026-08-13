import pandas as pd
data = {
    'Sky': ['Sunny', 'Sunny', 'Rainy', 'Sunny', 'Rainy', 'Sunny'],
    'AirTemp': ['Warm', 'Warm', 'Cold', 'Warm', 'Warm', 'Warm'],
    'Humidity': ['Normal', 'High', 'High', 'High', 'Normal', 'Normal'],
    'Wind': ['Strong', 'Strong', 'Strong', 'Strong', 'Weak', 'Weak'],
    'Water': ['Warm', 'Warm', 'Warm', 'Cool', 'Warm', 'Warm'],
    'Forecast': ['Same', 'Same', 'Change', 'Same', 'Same', 'Same'],
    'PlayTennis': ['Yes', 'Yes', 'No', 'Yes', 'No', 'Yes']
}

df=pd.DataFrame(data)

cn=df.iloc[:, :-1].values
t=df.iloc[:,-1].values
h=["@"]*len(cn[0])

for i in range(len(cn)):
   if t[i]=="Yes":
      for j in range(len(h)):
           if h[j]=='@':
              h[j]=cn[i][j]
           elif h[j]!=cn[i][j]:
               h[j]='?'


print("final hypothesis")
print(h)
   
   
   
    
   
   
