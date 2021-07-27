# Memes Generator

A multimedia application to dynamically generate quotes for supplied images. Accessed through CLI and a web interface (flask)

* [udacity nanodegrees](https://www.udacity.com/)
* [main program site](https://www.udacity.com/course/intermediate-python-nanodegree--nd303)


## General Overview

- The application interacts with a variety of complex filetypes. (PDF, Word Documents, CSVs, Text files). It implements a Strategy Pattern to offer flexibility of adding/editing new file types.
![link](https://upload.wikimedia.org/wikipedia/commons/3/39/Strategy_Pattern_in_UML.png)
- it loads, manipulates, and saves images.
- it integrates extracted text from the files with the images
- it accepts dynamic user input through a command-line tool and a web service. 
## Project Scaffolding

The project is structured in two main modules **`MemeEngine`** and **`QuoteEngine`** and two main invoking programs `api.py` and `meme.py` to support web & CLI interfaces, respectively.  

```
.
│   app.py                              # runs flask api
│   meme.py                             # runs modules from CMI
│   README.md                           # This file.
│
├───MemeEngine                          
│       MemeGenerator.py                # processes images and add text
│       __init__.py
│
├───QuoteEngine
│       CSVImporter.py                  # strategy: .csv reader
│       DocxImporter.py                 # strategy: .docx reader
│       Ingestor.py                     
│       IngestorInterface.py
│       PDFImporter.py                  # strategy: .pdf reader
│       QuoteModel.py
│       TXTImporter.py                  # strategy: .txt reader
│       __init__.py
│
├───templates                           # used for basic testing of web api.
│       base.html
│       meme.html
│       meme_form.html
│
└───_data                               # sample images and quotes in different file formats
    ├───DogQuotes
    │   │   DogQuotesCSV.csv
    │   │   DogQuotesDOCX.docx
    │   │   DogQuotesPDF.pdf
    │   │   DogQuotesTXT.txt
    │   │
    │   └───tmp
    ├───photos
    │   └───dog
    │           xander_1.jpg
    │           xander_2.jpg
    │           xander_3.jpg
    │           xander_4.jpg
    │
    └───SimpleLines
            SimpleLines.csv
            SimpleLines.docx
            SimpleLines.pdf
            SimpleLines.txt

```

## Dependencies
**file types support** 
- Python-docx
- pdftotext
- Pandas
- Subprocess

**Web Interface** 
- flask
- requests

**Command Line Interface**
- Argparse
- os

**OOP and others**
- ABC
- Typing
- Pillow
##  Running the program

If optional arguments are not provided, the proram uses default values under `_data` folder and a random choice of file format. 

**Command Line Interface**
run python `meme.py` with optional arguments
- `--path`  : input path the image
- `--body`  : quote you would like to add
- `--author`: author of the comment/quote

**Flask Web Interface**
- run python `api.py` from the directory where the file is located
- Simple web interface from `templates` folder is then accessed on port 5000 from localhost. http://127.0.0.1:5000