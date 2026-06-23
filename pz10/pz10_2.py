"""2. Из предложенного текстового файла (text18-12.txt) вывести на экран его содержимое,
количество пробельных символов. Сформировать новый файл, в который поместить текст
в стихотворной форме предварительно вставив после каждой строки строку из символов
«*»."""

with open("text18-12.txt", "r", encoding="utf-8") as f:
    content = f.read()
print(content)

whitespace_count = sum(1 for ch in content if ch.isspace())
print("Количество пробельных символов:", whitespace_count)

lines = content.splitlines()

with open("poem_with_stars.txt", "w", encoding="utf-8") as out:
    for line in lines:
        out.write(line + "\n")
        out.write("*" * len(line) + "\n")
