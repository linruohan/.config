from win32com import client as wc

# 下面是office 2007支持的全部文件格式对应表：
#
# wdFormatDocument = 0
# wdFormatDocument97 = 0
# wdFormatDocumentDefault = 16
# wdFormatDOSText = 4
# wdFormatDOSTextLineBreaks = 5
# wdFormatEncodedText = 7
# wdFormatFilteredHTML = 10
# wdFormatFlatXML = 19
# wdFormatFlatXMLMacroEnabled = 20
# wdFormatFlatXMLTemplate = 21
# wdFormatFlatXMLTemplateMacroEnabled = 22
# wdFormatHTML = 8
# wdFormatPDF = 17
# wdFormatRTF = 6
# wdFormatTemplate = 1
# wdFormatTemplate97 = 1
# wdFormatText = 2
# wdFormatTextLineBreaks = 3
# wdFormatUnicodeText = 7
# wdFormatWebArchive = 9
# wdFormatXML = 11
# wdFormatXMLDocument = 12
# wdFormatXMLDocumentMacroEnabled = 13
# wdFormatXMLTemplate = 14
# wdFormatXMLTemplateMacroEnabled = 15
# wdFormatXPS = 18
word = wc.Dispatch('Word.Application')
doc = word.Documents.Open('E:\\atom\\Python\\word_handle\\001.docx')
doc.SaveAs('E:\\atom\\Python\\word_handle\\001.rtf', 6) #17对应于下表中的pdf文件
doc.Close()
word.Quit()