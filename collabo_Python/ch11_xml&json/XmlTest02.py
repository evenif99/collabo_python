from xml.etree.ElementTree import Element, ElementTree, SubElement

mydict = {'hong': ('홍길동', 60, 80, 70), 'park': ('박영희', 50, 70, 95)}

anotherDic = {'hong':('210', '70.000'), 'park':('215', '71.667')}

xmldata = Element('members')

for key, myTuple in mydict.items():
    mem = SubElement(xmldata, 'member')
    mem.attrib['id'] = key

    kor = myTuple[1]
    eng = myTuple[2]
    math = myTuple[3]

    total = kor + eng + math
    average = total / 3.0

    # 하위 엘리먼트 추가하기
    SubElement(mem, 'name'). text = str(myTuple[0])
    SubElement(mem, 'kor'). text = str(kor)
    SubElement(mem, 'eng'). text = str(eng)
    SubElement(mem, 'math'). text = str(math)

    # tuple의 전화번호와 이메일 정보를 속성에 추가합니다.
    anotherInfo = anotherDic[key]
    mem.attrib['total'] = str(total)
    mem.attrib['average'] = '%.3f' % average
# end for

def indent(elem, level=0):
    mytab = '\t'
    i = '\n' + level * mytab

    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + mytab

        if not elem.tail or not elem.tail.strip():
            elem.tail = i

        for elem in elem:
            indent(elem, level + 1)

        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i
# end def

indent(xmldata)

xmlFile = 'XmlTest02.xml'
ElementTree(xmldata).write(xmlFile, encoding='utf-8')
print(xmlFile + '파일 생성')