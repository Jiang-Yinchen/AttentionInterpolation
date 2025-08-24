# Attention Interpolation
这是一个简单的插值工具，目前支持多项式插值。
## 使用方法
按照输入你想要的数列即可。
### 参数设置
```python
LANGUAGE = "Chinese"
OUTPUT_TO_FILE = True
FILE_NAME = "output.md"
LATEX_MARK = "\\[", "\\]", "\\(", "\\)"
WAIT_AT_THE_END = True
```
你需要设置这五个参数，它们分别位于 `main.py` 文件的第 3~7 行。

| 参数名               | 类型  | 允许值                      | 说明                     |
|-------------------|-----|--------------------------|------------------------|
| `LANGUAGE`        | 字符串 | `"Chinese"`, `"English"` | 设置输出语言，目前只支持中文和英文。     |
| `OUTPUT_TO_FILE`  | 布尔值 | `True`, `False`          | 设置是否将输出写入 Markdown 文件。 |
| `FILE_NAME`       | 字符串 | 任意字符串                    | 设置输出文件名。               |
| `LATEX_MARK`      | 元组  | 任意字符串                    | 设置 LaTeX 标记            |
| `WAIT_AT_THE_END` | 布尔值 | `True`, `False`          | 设置是否在输出结束后等待。          |