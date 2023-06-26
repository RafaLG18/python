import pandas as pd

df= pd.read_csv('~/Downloads/teste.csv')
for i in range(len(df)):
    data_dict = {}
    data_dict['name'] = df['name'][i].replace(' ', '_')
    data_dict['description'] = df['description'][i]
    data_dict['device_type'] = df['device_type'][i]
    data_dict['ip_address'] = df['ip_address'][i]
    data_dict['ssh_port'] = df['ssh_port'][i]
print(df)
print(data_dict)

