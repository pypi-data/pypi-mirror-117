
#  Data extractor for PDF documents - pdf-info

  
  
  

A command line tool and Python library to support your analysis of pdf documents.

  

Extracts important fetures from a document like headers, paragraphs, important keywords and subscripts.

  

Returns a vector of relevant details!!

  

##  Installation

  
  
  

### Install `pdf-info` using pip

`pip install pdf-info`

  
  
  

###  Use as Python Library

  

You can easily add `pdf-info` to your own Python scripts as library.

  

`from pdf_info import pdf_info_class`
`ob = pdf_info_class()`
`result = ob.pdf_info('path/to/my/file.pdf',page_number,tag)`

  

####  List of tags supported are - "headers", "paragraphs", "keywords", "subscripts".

  
  

##  Maintainers

  

-  [Satyam Prakash](https://github.com/satprak)
