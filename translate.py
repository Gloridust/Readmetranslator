import re  # 导入正则表达式模块 're'。
from googletrans import Translator  # 导入 'googletrans' 模块中的 Translator 类。

def translate_markdown(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        markdown_text = f.read()  # 读取输入的 Markdown 文件内容。

    translator = Translator()  # 创建一个 Translator 对象以进行翻译。

    # 使用正则表达式查找Markdown文档中的中文部分。
    chinese_pattern = re.compile(r'[\u4e00-\u9fa5]+')  # 定义一个匹配中文字符的正则表达式模式。
    chinese_matches = chinese_pattern.findall(markdown_text)  # 找到所有中文文本的匹配项。

    for chinese_text in chinese_matches:
        # 使用Google翻译将中文文本翻译为英语。
        english_text = translator.translate(chinese_text, src='zh-cn', dest='en').text

        # 将原始Markdown文档中的中文文本替换为英文翻译。
        markdown_text = markdown_text.replace(chinese_text, english_text)

    # 将翻译后的Markdown文本保存到输出文件。
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(markdown_text)

if __name__ == '__main__':
    input_file = 'README.md'  # 请替换为您的输入Markdown文件。
    output_file = 'README_en.md'  # 请替换为您的输出Markdown文件。
    translate_markdown(input_file, output_file)  # 调用 translate_markdown 函数进行翻译。
