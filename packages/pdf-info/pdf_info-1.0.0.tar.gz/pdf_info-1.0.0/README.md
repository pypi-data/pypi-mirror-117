This is a very easy to use package.

1 - Installation
    pip install pdf_info
2 - Import package
    import pdf_info
3 - Create python object for the package
    ob = pdf_info.pdf_info_class()
4 - function calling
    result = ob.pdf_info(file_path,page_num,tag)
    ......
    file_path = path to the pdf  .... eg.- "c:/users/hp/.../<file_name>.pdf
    page_num = page number of the pdf which information has to be extracted
    tag = the tag whose information has to be extracted eg.-"headers","paragraphs","keywords"


Example - 
import pdf_info
ob = pdf_info.pdf_info_class()
file_path = "C:/Users/hp/....../<file_name>.pdf"
res = ob.pdf_info(file_path,1,"headers")  // return all the headers of the given pdf on page 1