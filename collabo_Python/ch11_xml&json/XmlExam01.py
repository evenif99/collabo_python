from xml.etree.ElementTree import Element, ElementTree

# root element "human"을 생성하면서 속성 gender을 추가합니다.
xmldata = Element('human', gender = '남자')

# 기존 element에 속성(attribute) 추가하기
xmldata.attrib['birth'] = '19951223'

xmlFile = 'XmlExam01.xml'
ElementTree(xmldata).write(xmlFile, encoding='utf-8')
print(xmlFile + '파일 생성')