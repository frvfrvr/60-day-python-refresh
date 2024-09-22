contents = ['quick brown fox jump over lazy dog', 
            'lorem ipsum si vous plait', 
            'yoroshiku onegaishimasu']

filenames = ["doc.txt", 
             "report.txt", 
             "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"./files/{filename}")
    file.write(content)
    
