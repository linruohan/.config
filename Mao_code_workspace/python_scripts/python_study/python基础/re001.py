#coding=utf-8
import  re

list=['15865548338cong' ,'abcd18701687236ef','gafei18511371536' ,'wb15865737271dad13244556677']

print(list)

for items in list:

    # start
    l=re.match( r'\d{11}',items )

    print('match:',l )

    if l!=None:

        print('match.group(0)',l.group(0))

    # start-end
    m = re.search( '[0-9]{11}',items )

    print('search:',m.group( 0))

    print('search,.start:',m.start())

    print('search,.end:',m.end())

    print('search,.span:',m.span())

    # replace
    n=re.sub( r'\d','*' ,items)

    print('sub:',n )

    # return list
    o=re.findall(r'\d{11}',items )

    print('findall:',o )

    # str2list
    p=re.split( r'\d+',items )

    print('split:',p )

    # iterator
    q=re.finditer(r'\d+',items )

    for i in q:

        print('finditer:' ,i.group())

    pattern=re.compile(r'\d{11}')

    print pattern.findall(items)


    print('***********************************************' )
