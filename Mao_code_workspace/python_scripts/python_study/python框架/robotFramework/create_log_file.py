import os
import sys

class main:
    def create_log_path(self, case=None, outputdir=None):
        '''Create Case log Directory
        Usage: | Create Log Path | caseName | outputDir |
        '''
        G_TEST_PATH = str(outputdir)
        g_log = os.getenv('G_LOG')
        print('=' * 100)
        print(G_TEST_PATH)
        print('=' * 100)
        # Window code
        base = 'f:\\robotframework\\'
        os.system('rd -Q ' + '"' + os.path.join(base, 'logs', 'current') + '"')
        os.system('mklink /D ' + '"' + os.path.join(base, 'logs', 'current') + '"' + ' ' + '"' + G_TEST_PATH + '"')
        #
        if case:
            # 处理特殊字符
            case_name = case
            special_chars = [' ', '(', ')', '<', '>', '@', '$', '#']
            for i in special_chars:
                case_name = str (case_name).replace (i, '_')
            print('case_name:' + case_name)
            G_CASE_LOG_PATH = os.path.join(G_TEST_PATH, case_name)
            print('G_CASE_LOG_PATH:' + G_CASE_LOG_PATH)
            if not os.path.exists(G_CASE_LOG_PATH):
                os.mkdir(G_CASE_LOG_PATH)
                os.environ['G_CURRENTLOG'] = str(G_CASE_LOG_PATH)
                print('G_CURRENTLOG:' + os.getenv('G_CURRENTLOG'))
            else:
                print('AT_ERROR : Create Log File FAIL!')
                print('AT_ERROR : ' + G_CASE_LOG_PATH + ' has exist!')
        else:
            print('AT_ERROR : Create Log File FAIL!')
            print('AT_ERROR : ' + case + ' NOT Exist!')