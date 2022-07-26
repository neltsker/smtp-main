from csv import excel
import pandas

from gosuslugi import rass
import time
excel_data_df = pandas.read_excel('рассылка (8).xlsx', sheet_name='Лист1')

# print whole sheet data    
print(excel_data_df)

mail = rass()
old_mail=None
for i, row in excel_data_df.iterrows():
    #print(row['Почта'])
    if row['Почта'] != old_mail:
        mail.sendMail(row['Почта'])
        old_mail = row['Почта']
        pass
    else:
        pass
    
    #print(f"Index: {i}")
	#print(f"{row['ФИО']}\n")
    
    #print()
    #print(row['ФИО'])

mail.sendMail('laa@urtisi.ru')
