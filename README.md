# 文件格式转换工具

## 介绍
一个简单的 Python 工具，用于在 CSV 和 JSON 文件格式之间进行转换。

## 功能
- 将 CSV 文件转换为 JSON 格式
- 将 JSON 文件转换为 CSV 格式
- 支持命令行参数指定输入和输出文件
- 基本的数据类型转换
- 错误处理（文件不存在、格式错误等）

## 使用方法

### 安装
确保你已经安装了 Python 3.x。该项目使用 Python 标准库，无需额外安装依赖。

### 运行

#### CSV 转 JSON
```bash
python main.py input.csv output.json --type csv2json
```

#### JSON 转 CSV
```bash
python main.py input.json output.csv --type json2csv
```

### 参数说明
- `input`: 输入文件路径
- `output`: 输出文件路径
- `--type`: 转换类型，可选值为 `csv2json` 或 `json2csv`

## 代码结构

### 主要模块
- `csv_to_json(input_file, output_file)`: 处理 CSV 到 JSON 的转换
- `json_to_csv(input_file, output_file)`: 处理 JSON 到 CSV 的转换
- `main()`: 主函数，解析命令行参数并调用相应的转换函数

### 错误处理
代码中添加了基本的错误处理，包括：
- 文件不存在错误
- JSON 格式错误
- CSV 格式错误
- 其他常见错误

### 日志记录
使用 Python 的 logging 模块记录日志信息，方便调试和追踪程序运行状态。


## 编码过程

### 项目初始化
1. 创建项目文件夹，命名为 `file_format_conversion`。
2. 在项目文件夹内创建 `file_converter.py` 文件，用于编写转换工具的代码。
3. 创建 `README.md` 文件，用于记录项目的使用说明和文档。

### 代码实现

#### 导入必要的模块
```python
import argparse
import csv
import json
import os
import logging
```

#### 配置日志记录
```python
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
```

#### 实现 CSV 转 JSON 的功能
```python
def csv_to_json(input_file, output_file):
    """
    将 CSV 文件转换为 JSON 格式。
    
    :param input_file: 输入的 CSV 文件路径
    :param output_file: 输出的 JSON 文件路径
    """
    try:
        # 检查输入文件是否存在
        if not os.path.exists(input_file):
            logger.error(f"输入文件 {input_file} 不存在")
            return
        
        # 读取 CSV 文件
        with open(input_file, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            data = [row for row in reader]
        
        # 写入 JSON 文件
        with open(output_file, 'w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, indent=4, ensure_ascii=False)
        
        logger.info(f"成功将 {input_file} 转换为 {output_file}")
    
    except FileNotFoundError:
        logger.error(f"文件 {input_file} 不存在")
    except Exception as e:
        logger.error(f"转换过程中发生错误：{e}")
```

#### 实现 JSON 转 CSV 的功能
```python
def json_to_csv(input_file, output_file):
    """
    将 JSON 文件转换为 CSV 格式。
    
    :param input_file: 输入的 JSON 文件路径
    :param output_file: 输出的 CSV 文件路径
    """
    try:
        # 检查输入文件是否存在
        if not os.path.exists(input_file):
            logger.error(f"输入文件 {input_file} 不存在")
            return
        
        # 读取 JSON 文件
        with open(input_file, 'r', encoding='utf-8') as jsonfile:
            data = json.load(jsonfile)
        
        # 检查数据是否为列表
        if not isinstance(data, list):
            logger.error("JSON 文件内容不是数组")
            return
        
        # 如果数据为空，直接返回
        if len(data) == 0:
            logger.warning("JSON 文件内容为空数组")
            return
        
        # 获取表头
        headers = data[0].keys()
        
        # 写入 CSV 文件
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)
        
        logger.info(f"成功将 {input_file} 转换为 {output_file}")
    
    except FileNotFoundError:
        logger.error(f"文件 {input_file} 不存在")
    except json.JSONDecodeError:
        logger.error(f"文件 {input_file} 不是有效的 JSON 格式")
    except Exception as e:
        logger.error(f"转换过程中发生错误：{e}")
```

#### 实现主函数，解析命令行参数
```python
def main():
    """
    主函数，解析命令行参数并调用相应的转换函数。
    """
    parser = argparse.ArgumentParser(description="文件格式转换工具")
    parser.add_argument("input", help="输入文件路径")
    parser.add_argument("output", help="输出文件路径")
    parser.add_argument("--type", choices=["csv2json", "json2csv"], required=True,
                        help="转换类型：csv2json 或 json2csv")
    
    args = parser.parse_args()
    
    input_file = args.input
    output_file = args.output
    convert_type = args.type
    
    # 检查输入文件是否存在
    if not os.path.exists(input_file):
        logger.error(f"输入文件 {input_file} 不存在")
        return
    
    # 根据转换类型调用相应的函数
    if convert_type == "csv2json":
        csv_to_json(input_file, output_file)
    elif convert_type == "json2csv":
        json_to_csv(input_file, output_file)
    else:
        logger.error("不支持的转换类型")

if __name__ == "__main__":
    main()
```



## 示例数据

### CSV 示例数据
```csv
id,name,age,salary,department,join_date
1,John Doe,30,5000.5,HR,2020-01-15
2,Jane Smith,28,5500.75,Engineering,2019-06-22
3,Bob Johnson,35,6000.0,Marketing,2021-03-10
4,Alice Brown,27,5200.25,Finance,2022-07-18
5,Michael Davis,32,5800.0,IT,2020-11-30
```

### JSON 示例数据
```json
[
    {
        "id": 1,
        "name": "John Doe",
        "age": 30,
        "salary": 5000.5,
        "department": "HR",
        "join_date": "2020-01-15"
    },
    {
        "id": 2,
        "name": "Jane Smith",
        "age": 28,
        "salary": 5500.75,
        "department": "Engineering",
        "join_date": "2019-06-22"
    },
    {
        "id": 3,
        "name": "Bob Johnson",
        "age": 35,
        "salary": 6000.0,
        "department": "Marketing",
        "join_date": "2021-03-10"
    },
    {
        "id": 4,
        "name": "Alice Brown",
        "age": 27,
        "salary": 5200.25,
        "department": "Finance",
        "join_date": "2022-07-18"
    },
    {
        "id": 5,
        "name": "Michael Davis",
        "age": 32,
        "salary": 5800.0,
        "department": "IT",
        "join_date": "2020-11-30"
    }
]
```
