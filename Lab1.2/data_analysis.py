#solar activity graph

from matplotlib import pyplot
from openpyxl import load_workbook

# Загрузить таблицу Excel из файла в переменную wb
wb = load_workbook('data_analysis_lab.xlsx')
# Загрузить лист с именем "Data" в переменную sheet
sheet = wb['Data']
# Получить содержимое колонок в виде списка
x = sheet['A'][1:]
y = sheet['B'][1:]
z = sheet['C'][1:]

# Преобразовать содержимое колонок в список, содержащий только значения (без форматирования и т. п.)
def getvalue(x): return x.value

list_x = list(map(getvalue, sheet['A'][1:]))
list_y = list(map(getvalue, sheet['B'][1:]))
list_z = list(map(getvalue, sheet['C'][1:]))

# Построить график по точкам, в первом списке значения по оси X, во втором — значения по оси Y
pyplot.plot(list_x, list_y, label = "Relation")
pyplot.plot(list_x, list_z, label = "Activity")

# показать график
pyplot.show()