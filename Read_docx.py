# 아래 코드는 docx 라이브러리를 사용하여 word 파일을 읽어오는 코드입니다.
# word 파일을 읽어오기 위해서는 python-docx 라이브러리를 설치해야 합니다.
# pip install python-docx
# read_word 함수에 파일의 경로와 이름, 확장자를 문자열로 넣으면 read_text로 반환됩니다.
# 이 라이브러리는 word 파일 안의 text만 읽고 표는 읽지 못합니다.
# 표 까지 읽고 싶다면 아래와 같이 pdf로 변환하여 사용하면 됩니다.
import docx
def read_word(file_path):
    read_text = []
    doc = docx.Document(file_path)
    for para in doc.paragraphs:
        read_text.append(para.text)
    # for i in range (len(read_text)):
    #     if "Specifications" in read_text[i]: # 특정 문자열을 찾는법
    #         print("YES")
    read_text = ("".join(read_text))
    return read_text
# read_text = read_word("C:\\Users\\theo.yoon\\Downloads\\20019964-001(Specification).docx")
# print(read_text)

# 아래 코드는 docx2pdf 라이브러리를 사용하여 word 파일을 pdf 파일로 변환하는 코드입니다.
# word 파일을 pdf 파일로 변환하기 위해서는 docx2pdf 라이브러리를 설치해야 합니다.
# docx2pdf를 설치하고 변환 전 파일 위치와 변환 후 파일 위치를 문자열로 넣으면 변환됩니다.
import docx2pdf
input_file = "C:\\Users\\theo.yoon\\Downloads\\20019964-001(Specification).docx"
output_file = "C:\\Users\\theo.yoon\\Downloads\\20019964-001(Specification).pdf"
def docx_to_pdf(input_file, output_file):
    docx2pdf.convert(input_file, output_file)
# docx_to_pdf(input_file, output_file)

# 아래 함수는 pdf 파일을 읽어오는 함수입니다.
# pdf 파일을 읽어오기 위해서는 PyMuPDF 라이브러리를 설치해야 합니다.
# 아래 pdf는 표도 읽어 오기 때문에 좋습니다.
import fitz
def read_pdf(file_path):
    read_text = []
    doc = fitz.open(file_path)
    for page in doc:
        read_text.append(page.get_text())
    read_text = ("".join(read_text))
    return read_text
# read_text = read_pdf(input_file)
# print(read_text)