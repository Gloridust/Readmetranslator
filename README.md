# Readmetranslator
 一键将中文 Readme 文件转译为英文版。Translate Chinese Readme files to English easily.

## 用途

- 如果您有一个包含中文内容的 Markdown 文件，并希望将其翻译成英文，这个脚本可以自动完成这个任务。

## 开始之前

在开始使用之前，请确保您已安装需要的Python依赖包。您可以使用以下命令安装所需的包：  

```
    pip3 install setuptools
    pip3 install googletrans==4.0.0-rc1
```

## 使用步骤

请按照以下步骤来使用自动翻译 Markdown 文档的脚本：

1. **准备 Markdown 文件**：将您希望翻译的 Markdown 文件准备好，并将其命名为 `README.md`（您也可以将文件命名为其他名称，但需要在后续步骤中相应地更改文件路径）。

2. **编辑脚本**：如果您需要翻译的文件不叫**README.md**,你可以在脚本中修改文件名。您可以在脚本中找到以下部分：

   ```python
   if __name__ == '__main__':
       input_file = 'README.md'  # 请替换为您的输入 Markdown 文件。
       output_file = 'README_en.md'  # 请替换为您的输出 Markdown 文件。
       translate_markdown(input_file, output_file)  # 调用 translate_markdown 函数执行翻译。
   ```

   - 将 `'README.md'` 替换为您的输入 Markdown 文件的路径。
   - 将 `'README_en.md'` 替换为您想要保存翻译后内容的文件路径。

3. **运行脚本**：在终端或命令提示符中，导航到包含脚本的目录，并运行脚本：

   ```
   python3 translate.py
   ```

4. **等待翻译**：脚本将自动读取输入的 Markdown 文件，查找其中的中文文本，并使用 Google Translate API 将其翻译成英文。此过程时间较长，请耐心等待 1～3 分钟。

5. **查看输出**：翻译完成后，翻译后的内容将保存在您指定的输出文件中（在本例中为 `'README_en.md'`）。

6. **完成**：您现在可以打开输出文件，查看翻译后的 Markdown 内容。

## 注意事项

- 请注意，这个脚本依赖于 Google Translate API，并可能对翻译的数量和速度有一些限制。确保您可以流畅的访问 GoogleTranslate。

- 请根据您的具体用例和需求，自行调整脚本中的文件路径和配置。

## 最后
如果这个脚本帮到了您，请点上右上角的star，这是对我的最佳鼓励。