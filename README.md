# file_format_conversion
文件格式转换工具
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
python file_converter.py input.csv output.json --type csv2json
