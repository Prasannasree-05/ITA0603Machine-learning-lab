import pandas as pd

data = {
    'Color': ['Red', 'Red', 'Yellow', 'Red', 'Yellow', 'Red'],
    'Size': ['Big', 'Big', 'Small', 'Big', 'Big', 'Big'],
    'Shape': ['Round', 'Oval', 'Round', 'Round', 'Oval', 'Round'],
    'Taste': ['Sweet', 'Sweet', 'Sour', 'Sweet', 'Sour', 'Sweet'],
    'Fruit': ['Apple', 'Apple', 'Lemon', 'Apple', 'Lemon', 'Apple'],
    'Season': ['Winter', 'Winter', 'Summer', 'Winter', 'Summer', 'Winter'],
    'Accept': ['Yes', 'Yes', 'No', 'Yes', 'No', 'Yes']
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
