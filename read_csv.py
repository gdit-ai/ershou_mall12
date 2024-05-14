import pandas as pd

# 读取CSV文件
# df = pd.read_csv('./csv/data.csv')
df = pd.read_csv('./csv/data3.csv',encoding = "GB2312")

# print(df)
# 显示前几行数据，检查数据是否正确读取
print(df.head())

print(df['industry_type'])
industry_type_list = df['industry_type']
industry_type_value_list = df['industry_type_value']

# 访问特定的行（例如，第3行，注意索引通常从0开始）
print(df.iloc[1])


# 访问特定行和列的数据（例如，第3行'Column1'列的数据）
# print(df.at[2, 'Column1'])  # 使用.at[]访问单个值

df.to_csv('processed_file.csv', index=False)  # index=False表示不保存行索引
