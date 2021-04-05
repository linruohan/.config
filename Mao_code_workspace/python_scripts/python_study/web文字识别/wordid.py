#coding=utf-8
from aip import AipOcr,AipFace
APP_ID='10987398'
APP_KEY='GAvS7iml8fbEdMafUy8a8FXR'
SECREY_KEY='cyLzRk06RfqE0cRu3OxC0XGQSHIRYSQo '
def get_word_by_image(image,_type=None):
    client=AipOcr(APP_ID,APP_KEY,SECREY_KEY)
    options={'probability':'true'}
    options['detect_direction']='true'
    if _type:
        res=client.basicAccurate(image,options=options)
    else:
        res=client.basicGeneral(image,options=options)
    return res
def get_file_content(filepath):
    with open(filepath,'rb') as f:
        return f.read()

if __name__ == '__main__':
    image=get_file_content('001.jpg')
    path='001.jpg'
    # client = AipOcr (APP_ID, APP_KEY, SECREY_KEY)
    res=get_word_by_image(image)
    print(res)
