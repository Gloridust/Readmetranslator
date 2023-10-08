# Readmetranslator
 The Chinese Readme file is translated into an English version with one click.Translate Chinese Readme Files to English Easily.
For English?
## use

-If you have a Markdown file containing Chinese content and want to translate it into English, this script can automatically complete this task.

## before the start

Before starting use, make sure you have the Python dependency package you have installed.You can use the following command to install the required package:

```
    pip3 install setuptools
    pip3 install googletrans==4.0.0-rc1
```

## Steps for usage

Please follow the steps below to use the script of the automatic translation Markdown document:

1. ** Prepare the Markdown file **: Prepare the Markdown file you want to translate and name it `Readme.md` (you can also name the file as other names, but you need to change it in the subsequent steps accordinglyfile path).

2. ** Prepare files to be translated **: If the file you need to translate is not called ** Readme.md **, you need to modify the file name ** Readme.md **.

3. ** Running script **: In the terminal or command prompt, navigate to the directory containing the script, and run the script:

```
   python3 translate.py
   ```

4. ** Waiting for translation **: The script will automatically read the input Markdown file, find the Chinese text in it, and translate it into English with Google Translate API.This process is longer, please wait patiently for 1 to 3 minutes.

5. ** View output **: After the translation is completed, the content of the translation will be stored in the output file you specified (in this example, `'readme_en.md'`).

6. ** Complete **: You can now open the output file and check the translated Markdown content.

## Precautions

-Please note that this script depends on the Google Translate API and may have some restrictions on the number and speed of the translation.Make sure you can smoothly access Googletranslate.

-Promite the file path and configuration of the script according to your specific use cases and needs.

## at last
If this script helps you, please click the Star in the upper right corner, which is the best encouragement for me.