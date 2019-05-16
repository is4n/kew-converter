import sys
import conf

def pdf_to_text(path_in, path_out):
	if (conf.get_prop("use_pdf2txt") == '0'):
		try:
			from pdfminer.pdfdocument import PDFDocument
			from pdfminer.pdfparser import PDFParser
			from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
			from pdfminer.pdfdevice import PDFDevice, TagExtractor
			from pdfminer.pdfpage import PDFPage
			from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
			from pdfminer.cmapdb import CMapDB
			from pdfminer.layout import LAParams
			from pdfminer.image import ImageWriter	
		except:
			print ("system doesn't have PDFminer.six library installed. Try to use pdf2txt.")
			conf.set_prop("use_pdf2txt", "1")

	if (conf.get_prop("use_pdf2txt") == '0'):
		rsrcmgr = PDFResourceManager(caching=True)
		outfp = open(path_out, 'w')
		codec = 'utf-8'
		laparams = LAParams()
		imagewriter = None

		device = TextConverter(rsrcmgr, outfp, codec=codec, laparams=laparams, imagewriter=imagewriter)

		fp = open(path_in, 'rb')
		interpreter = PDFPageInterpreter(rsrcmgr, device)
		for page in PDFPage.get_pages(fp, set(), caching=True, check_extractable=True):
			interpreter.process_page(page)
		fp.close()
		device.close()
		outfp.close()
