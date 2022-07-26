'''
import smtplib
import config
from main import *


mail = rass()
'''
'''
from csv import excel
import pandas

excel_data_df = pandas.read_excel('rass.xlsx', sheet_name='ЗФО бакалавры')

# print whole sheet data
print(excel_data_df)

print(excel_data_df.iloc[0]['ФИО'])

excel_data_df.at[0,'Отправлено']='Да'
print(excel_data_df)

#df_marks = pandas.DataFrame({'name': ['Somu', 'Kiku', 'Amol', 'Lini'], 'physics': [68, 74, 77, 78], 'chemistry': [84, 56, 73, 69], 'algebra': [78, 88, 82, 87]})

writer = pandas.ExcelWriter('output.xlsx')
excel_data_df.to_excel('zfo.xlsx', sheet_name='zfo') # save the excel file writer.save()
'''
from csv import excel
import pandas

from main import rass
import time
excel_data_df = pandas.read_excel('Рассылка (7).xlsx', sheet_name='Маги Программирование')

# print whole sheet data    
print(excel_data_df)

mail = rass()
for i, row in excel_data_df.iterrows():
    pass
    if row['Почта'] != None:
        mail.sendMail(row['Почта'])
        pass



mail.sendMail('laa@urtisi.ru')


