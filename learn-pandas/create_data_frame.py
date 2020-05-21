import pandas as pd

#Gera uma colecao imutavel
collection = pd.DataFrame()

collection['name'] = ['teste','felipe','mary']
collection['age'] = ['12','14','15']
collection['driver'] = [True,False,False]



print(collection)

new_person = pd.Series( ['nani','13',False], index=['name','age','driver'])

collection = collection.append(new_person, ignore_index=True)
collection = collection.append(new_person, ignore_index=True)
collection = collection.append(new_person, ignore_index=True)

print(collection)


