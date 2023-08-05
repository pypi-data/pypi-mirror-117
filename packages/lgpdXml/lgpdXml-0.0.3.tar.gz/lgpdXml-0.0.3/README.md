# lgpdXml
## 1 - pip Install
```
pip install lgpdXml
```
## 2 - example find value of tag
```
#library
from lgpdXml import find, replace

#text
xml = '''<CNPJ>012.345.678/0001-01</CNPJ>
<NOMERAZAO>CLAUDIO TORRES ARBE</NOMERAZAO>
<CNPJ>001.001.001/0001-01</CNPJ>'''

#find using tag
nome = find(xml,'<NOMERAZAO>','</NOMERAZAO>')

#result
print(nome)

#all results of tag
cnpj = find(xml,'<CNPJ>','</CNPJ>')

#results
print(cnpj)

#specifying the index
cnpj = find(xml,'<CNPJ>','</CNPJ>')[1]

#result
print(cnpj)

#looking for tag that doesn't exist
email = find(xml,'<EMAIL>','</EMAIL>')

#result
print(email)

```

## 3 - example replace value
```
#library
from lgpdXml import find, replace

#text
xml = '''<CNPJ>012.345.678/0001-01</CNPJ>
<NOMERAZAO>CLAUDIO TORRES ARBE</NOMERAZAO>
<CNPJ>001.001.001/0001-01</CNPJ>'''

#find using tag
nome = find(xml,'<NOMERAZAO>','</NOMERAZAO>')[0]

#all results of tag
cnpj = find(xml,'<CNPJ>','</CNPJ>')[1]

#replace tag
xml = replace(xml,'****','<NOMERAZAO>',nome,'</NOMERAZAO>')

#replace tag
xml = replace(xml,'****','<CNPJ>',cnpj,'</CNPJ>')

#result
print(xml)
```