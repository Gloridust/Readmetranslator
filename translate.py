from googletrans import Translator

print("程序已开始运行，请您耐心等待；文件处理时长一般在 1～3 分钟，请确保您能连接到 GoogleTranslate 服务。")

def translate_text(text):
    translator = Translator()
    translated_lines = []

    # 分割文本为段落
    paragraphs = text.split('\n\n')

    for paragraph in paragraphs:
        # 使用 Google 翻译将段落文本翻译为英语。
        english_paragraph = translator.translate(paragraph, src='auto', dest='en').text

        # 修复段落首字母大写问题
        english_paragraph = english_paragraph[0].upper() + english_paragraph[1:]

        translated_lines.append(english_paragraph)

    # 连接翻译后的段落为一个字符串
    translated_text = '\n\n'.join(translated_lines)

    return translated_text

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

input("翻译完毕，请按下 ENTER 来结束程序...")