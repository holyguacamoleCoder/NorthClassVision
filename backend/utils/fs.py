import os
import pandas as pd

# 获取数据目录
current_file_dir = os.path.dirname(os.path.abspath(__file__)) # 获取当前文件位置
current_dir = os.path.dirname(current_file_dir)               # 获取当前文件所在目录路径/utils
parent_dir = os.path.dirname(current_dir)                     # 获取当前文件所在目录路径/utils的父目录路径/backend
data_dir = os.path.join(current_dir, '../data/')              # 数据路径

# 获取数据文件
class_dir = os.path.join(data_dir, 'Data_SubmitRecord/')
classFilename = os.path.join(class_dir, 'SubmitRecord-Class1.csv') # 提交记录表格
titleFilename = os.path.join(data_dir, 'Data_TitleInfo.csv')       # 题目信息表格
studentFilename = os.path.join(data_dir, 'Data_StudentInfo.csv')   # 学生信息表格

# 加载数据
def load_data(filename):
    try:
        df = pd.read_csv(filename)
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# 拼接文件为新df
def contact_data(classList):
    return pd.concat([load_data(os.path.join(class_dir,'SubmitRecord-' + class_i['text'] + '.csv')) for class_i in classList if class_i['checked']], axis=0)

# 合并数据题目和提交记录
# filename2: 题目信息文件
def merge_data(f1, f2):
    if isinstance(f1, str):
        f1 = load_data(f1) 
    if isinstance(f2, str):
        f2 = load_data(f2) 
    merged_data = pd.merge(f1, f2[['title_ID', 'knowledge']], on='title_ID', how='left')
    return merged_data
