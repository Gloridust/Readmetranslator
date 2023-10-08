from googletrans import Translator

def translate_text(text):
    translator = Translator()
    english_text = translator.translate(text, src='auto', dest='en').text
    # 修复首字母大写问题
    english_text = english_text[0].upper() + english_text[1:]
    return english_text

def translate_markdown(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        markdown_text = f.read()

    # 直接翻译全部内容
    translated_text = translate_text(markdown_text)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(translated_text)

if __name__ == '__main__':
    input_file = 'README.md'  # 请替换为您的输入 Markdown 文件。
    output_file = 'README_en.md'  # 请替换为您的输出 Markdown 文件。
    translate_markdown(input_file, output_file)
