# coding=utf-8

import logging
import os
import time

log_path = os.path.join(os.path.dirname(__file__), './logs')


# sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
class Log(object):
    def __init__(self):
        self.logname = os.path.join(log_path, '{0}.log'.format(time.strftime('%Y-%m-%d')))

    def __str__(self):
        return self.__class__.__name__

    __repr__ = __str__

    def _printconsole(self, level, message):
        # 创建一个logger
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于写入日志文件
        fh = logging.FileHandler(self.logname, 'a', encoding='utf-8')
        fh.setLevel(logging.DEBUG)

        # 再创建一个handler，用于输出日志文件到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义handler的输出格式
        formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formater)
        ch.setFormatter(formater)

        # 给logger添加handler

        logger.addHandler(fh)
        logger.addHandler(ch)

        # 记录一条日志
        level = level.lower()

        if level == 'info':
            logger.info(message)
        elif level == 'debug':
            logger.debug(message)
        elif level == 'warning':
            logger.warning(message)
        elif level == 'error':
            logger.error(message)

        logger.removeHandler(fh)
        logger.removeHandler(ch)

        # 关闭打开的文件
        fh.close()

    def debug(self, message):
        return self._printconsole('debug', message)

    def info(self, message):
        return self._printconsole('info', message)

    def warning(self, message):
        return self._printconsole('warning', message)

    def error(self, message):
        return self._printconsole('error', message)


if __name__ == '__main__':
    log = Log()
    log.info(u'info message,打完')
    log.debug('debug message')
    log.warning('warning message')
    log.error('error message')
