import os
import pandas
import xlsxwriter
allj=pandas.DataFrame()
for i in range(1,41):
	df=pandas.read_excel('結果'+str(i)+'.xlsx')
	allj=pandas.concat([allj,df])
writer = pandas.ExcelWriter('結果.xlsx',engine="xlsxwriter")
allj.to_excel(writer,index=False)