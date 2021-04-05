#coding=utf-8
from email.parser import Parser
from email.header import  decode_header
from email.utils import parseaddr
import  poplib,logging



logging.basicConfig(level=logging.INFO)
def get_email():
    pop_server = 'pop.qq.com'
    email = '1214875764@qq.com'
    password = 'mjt12201214875764'



    server = poplib.POP3_SSL(pop_server, '995')
    server.set_debuglevel(1)
    print(server.getwelcome().decode('utf-8'))

    server.user(email)
    server.pass_(password)

    print('Messages: %s. Size: %s.' % server.stat())

    resp_one, mails, octets_one = server.list()
    print(mails)
    logging.info('''%s
                    resp_one: %s
                    octets_one: %s''' % (datetime.now(), resp_one, octets_one))

    #  获取最新一封邮件
    index = len(mails)
    resp_two, lines, octets_two = server.retr(index)
    logging.info('''%s
                    resp_two: %s
                    octets_two: %s''' % (datetime.now(), resp_two, octets_two))
    #  lines是一个list， 包含mail的每一行
    msg_content = b'\r\n'.join(lines).decode('utf-8')
    msg = Parser().parsestr(msg_content)
    logging.info('''%s
                    msg: %s

                    ''' % (datetime.now(), msg))

    #  可根据邮件索引号直接删除邮件
    #  server.dele(index)

    server.quit()
    print_info(msg)


def guess_charset(my_msg):
    charset = my_msg.get_charset()
    if charset is None:
        content_type = my_msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
        return charset


def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
        return value


# indent用于缩进显示
def print_info(my_msg, indent=0):
    if indent == 0:
        for header in ['Subject', 'From', 'To']:
            value = my_msg.get(header, '')
            if value:
                if header == 'Subject':
                    value = decode_str(value)
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
            print('%s%s: %s' % (' ' * indent, header, value))
    if my_msg.is_multipart():
        parts = my_msg.get_payload()
        for n, part in enumerate(parts):
            print('%spart %s' % (' ' * indent, n))
            print('%s-----------------------------------' % ' ' * indent)
            print_info(part, indent + 1)
    else:
        content_type = my_msg.get_content_type()
        if content_type == 'text/plain' or content_type == 'text/html':
            content = my_msg.get_payload(decode=True)
            charset = guess_charset(my_msg)
            if charset:
                content = content.decode(charset)
                print('%sText: %s' % (' ' * indent, content + '...'))
        else:
            print('%sAttachment: %s' % (' ' * indent, content_type))


if __name__ == '__main__':
    get_email()
