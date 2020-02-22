import os
import xlrd

class exs():
    def __init__(self):
        self.data = {'subjects':[]}
        self.paths = os.listdir('./media/accounts')
        for index,files in enumerate(self.paths):
            name = ''
            for smt in os.path.splitext(files)[0]:
                if smt == '_':
                    name = name + ' '
                else:
                    name = name + smt
            f = {'index':index,'name':name,'col':[]}
            wb = xlrd.open_workbook('./media/accounts/'+files) 
            sheet = wb.sheet_by_index(0) 
            data = []
            
            for row in range(sheet.nrows):
                testlist = sheet.row_values(row)
                rowlist = []
                for val in testlist:
                    if val == '':
                        rowlist.append('-')
                    else:
                        rowlist.append(val)
                data.append(rowlist)
                #print(sheet.row_values(row))
                #data.append(sheet.row_values(row))

            f['content'] = data
            self.data['subjects'].append(f)
            

        
#excl = exs()
#
#for i in excl.data['subjects']:
#    print(i)