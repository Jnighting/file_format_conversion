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
