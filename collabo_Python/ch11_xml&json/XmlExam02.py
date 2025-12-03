from xml.etree.ElementTree import Element, ElementTree, SubElement

# xml 파일에 추가할 사전 정보
humanDic = {'kim':('김철수', 30, '남자', '마포구 공덕동'), 'park':('박영희', 20, '여자', '동대문구 휘경동')}

# xml 파일의 속성에 추가할 사전 정보
anotherDic = {'kim':('01011112222','hello@naver.com'), 'park':('01033334444','world@daum.net')}

# root element "human"을 생성하면서 속성 gender을 추가합니다.
xmldata = Element('members') # 여러명이므로 복수로 작성

for key, myTuple in humanDic.items():
    mem = SubElement(xmldata, 'member')
    mem.attrib['id'] = key

    # 하위 엘리먼트 추가하기
    SubElement(mem, 'name'). text = str(myTuple[0])
    SubElement(mem, 'age'). text = str(myTuple[1])
    SubElement(mem, 'gender'). text = str(myTuple[2])
    SubElement(mem, 'adress'). text = str(myTuple[3])

    # tuple의 전화번호와 이메일 정보를 속성에 추가합니다.
    anotherInfo = anotherDic[key]
    mem.attrib['phone'] = anotherInfo[0]
    mem.attrib['email'] = anotherInfo[1]
# end for

# 기존 element에 속성(attribute) 추가하기
# xmldata.attrib['birth'] = '19951223'
#
# SubElement(xmldata, 'name'). text = '홍길동'
# SubElement(xmldata, 'age'). text = '30'
# SubElement(xmldata, 'address'). text = '마포구 공덕동'

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

xmlFile = 'XmlExam02.xml'
ElementTree(xmldata).write(xmlFile, encoding='utf-8')
print(xmlFile + '파일 생성')