import win32com.client
import winsound
speak = win32com.client.Dispatch('SAPI.SPVOICE')
winsound.Beep(2015, 3000)
speak.Speak('程序运行完毕!')