import os
import json
import openpyxl
import pandas as pd

def json_to_excel(json_folder, excel_file):
    # 创建一个Excel writer对象
    with pd.ExcelWriter(excel_file, engine='openpyxl') as writer:
        # 遍历json文件夹中的所有文件
        for json_file in os.listdir(json_folder):
            if json_file.endswith('.json'):
                file_path = os.path.join(json_folder, json_file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                # 将键值对提取出来
                items = []
                for key, value in data.items():
                    items.append({'Key': key, 'Value': value})
                
                # 将键值对转换为DataFrame
                df = pd.DataFrame(items)
                
                # 将DataFrame写入Excel中的不同工作表
                sheet_name = os.path.splitext(json_file)[0]
                df.to_excel(writer, sheet_name=sheet_name, index=False)

    print(f"All JSON files have been written to {excel_file}")

# 调用函数，将json文件夹路径和目标excel文件路径传入
json_folder = ''
excel_file = 'a.xlsx'
json_to_excel(json_folder, excel_file)
