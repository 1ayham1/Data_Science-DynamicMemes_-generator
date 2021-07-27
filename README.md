# Data_Science-DynamicMemes_-generator

A multimedia application to dynamically generate images with quotes.

* [main project site]
* [udacity nanodegrees](https://www.udacity.com/)


## General Overview

- The application interacts with a variety of complex filetypes. (PDF, Word Documents, CSVs, Text files).
- it loads, manipulates, and saves images.
- it accepts dynamic user input through a command-line tool and a web service. 

![link](https://upload.wikimedia.org/wikipedia/commons/3/39/Strategy_Pattern_in_UML.png)

## Project Scaffolding

```
.
│   app.py
│   meme.py
│   README.md      # This file.
│
├───MemeEngine
│       MemeGenerator.py
│       __init__.py
│
├───QuoteEngine
│       CSVImporter.py
│       DocxImporter.py
│       Ingestor.py
│       IngestorInterface.py
│       PDFImporter.py
│       QuoteModel.py
│       TXTImporter.py
│       __init__.py
│
├───templates
│       base.html
│       meme.html
│       meme_form.html
│
├───tmp
└───_data
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

## requirements and running the program
-docx
-pandas
-[xpdf reader](https://www.xpdfreader.com/download.html) 
-flask
-pdftotext
-requests

## Usage
