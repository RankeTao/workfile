from PyPDF2 import PdfFileMerger
#文件路径必不能从属性中复制，必须手写输入或者从资源管理器界面复制文件夹路径
ob = open('C:\\Users\\t03492\\Desktop\\3D.PDF', 'rb')
ob3 = open('C:\\Users\\t03492\\Desktop\\25D.PDF', 'rb')
ob4 = open('C:\\Users\\t03492\\Desktop\\Chromasens相机操作手册.pdf', 'rb')
merger = PdfFileMerger()

merger.append(ob, pages = (0, 1))
merger.append(ob3, pages = (0, 1))
merger.append(ob4, pages = (0, 3))
with open('C:\\Users\\t03492\\Desktop\\result.pdf', 'wb') as fout:
    merger.write(fout)

from PyPDF2 import PdfFileReader, PdfFileWriter
readFile = 'read.pdf'
writeFile = 'write.pdf'
# 获取一个 PdfFileReader 工具
pdfReader = PdfFileReader(open(readFile, 'rb'))
# 获取 PDF 的页数
pageCount = pdfReader.getNumPages()
print(pageCount)
# 返回一个 PageObject
page = pdfReader.getPage(i)
# 获取一个 PdfFileWriter 工具
pdfWriter = PdfFileWriter()
# 将一个 PageObject 插手到 PdfFileWriter 中
pdfWriter.addPage(page)
# 输出到文件中
pdfWriter.write(open(writeFile, 'wb'))
