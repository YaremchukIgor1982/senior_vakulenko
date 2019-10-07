import docx
def test_Text():

    doc = docx.Document('Web Copy.docx')
    for i in doc.paragraphs:
        print(i.text)