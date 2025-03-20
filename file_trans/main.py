import argparse
import csv
import json
import os


def csv_to_json(input_file, output_file):
	"""
    将 CSV 文件转换为 JSON 格式
    """
	try:
		with open(input_file, 'r', encoding='utf-8') as csvfile:
			reader = csv.DictReader(csvfile)
			data = [row for row in reader]

		with open(output_file, 'w', encoding='utf-8') as jsonfile:
			json.dump(data, jsonfile, indent=4, ensure_ascii=False)

		print(f"成功将 {input_file} 转换为 {output_file}")

	except FileNotFoundError:
		print(f"错误：文件 {input_file} 不存在")
	except Exception as e:
		print(f"转换过程中发生错误：{e}")


def json_to_csv(input_file, output_file):
	"""
    将 JSON 文件转换为 CSV 格式
    """
	try:
		with open(input_file, 'r', encoding='utf-8') as jsonfile:
			data = json.load(jsonfile)

		if not isinstance(data, list):
			print("错误：JSON 文件内容不是数组")
			return

		if len(data) == 0:
			print("警告：JSON 文件内容为空数组")
			return

		headers = data[0].keys()

		with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
			writer = csv.DictWriter(csvfile, fieldnames=headers)
			writer.writeheader()
			writer.writerows(data)

		print(f"成功将 {input_file} 转换为 {output_file}")

	except FileNotFoundError:
		print(f"错误：文件 {input_file} 不存在")
	except json.JSONDecodeError:
		print(f"错误：文件 {input_file} 不是有效的 JSON 格式")
	except Exception as e:
		print(f"转换过程中发生错误：{e}")


def main():
	parser = argparse.ArgumentParser(description="文件格式转换工具")
	parser.add_argument("input", help="输入文件路径")
	parser.add_argument("output", help="输出文件路径")
	parser.add_argument("--type", choices=["csv2json", "json2csv"], required=True,
						help="转换类型：csv2json 或 json2csv")

	args = parser.parse_args()

	input_file = args.input
	output_file = args.output
	convert_type = args.type

	if not os.path.exists(input_file):
		print(f"错误：输入文件 {input_file} 不存在")
		return

	if convert_type == "csv2json":
		csv_to_json(input_file, output_file)
	elif convert_type == "json2csv":
		json_to_csv(input_file, output_file)
	else:
		print("错误：不支持的转换类型")


if __name__ == "__main__":
	main()