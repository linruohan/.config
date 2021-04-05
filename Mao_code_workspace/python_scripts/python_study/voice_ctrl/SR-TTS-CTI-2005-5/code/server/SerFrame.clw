; CLW file contains information for the MFC ClassWizard

[General Info]
Version=1
LastClass=CSerFrameDlg
LastTemplate=CDialog
NewFileInclude1=#include "stdafx.h"
NewFileInclude2=#include "SerFrame.h"
ODLFile=SerFrame.odl

ClassCount=10
Class1=CSerFrameApp
Class2=CSerFrameDlg
Class3=CAboutDlg
Class4=CSerFrameDlgAutoProxy

ResourceCount=9
Resource1=IDD_ABOUTBOX
Resource2=IDR_MAINFRAME
Resource3=IDD_TELOPT
Resource4=IDD_CHANNELTYPE
Class5=CNameList
Resource5=IDD_FAXOPT
Class6=CTelOptDlg
Resource6=IDD_NETOPT
Class7=CNetOptDlg
Resource7=IDD_NAMELIST
Class8=CShowAllChanTypeDlg
Resource8=IDD_SERFRAME_DIALOG
Class9=CFaxOptDlg
Class10=CSendFaxDlg
Resource9=IDR_MENU1

[CLS:CSerFrameApp]
Type=0
HeaderFile=SerFrame.h
ImplementationFile=SerFrame.cpp
Filter=N
LastObject=CSerFrameApp
BaseClass=CWinApp
VirtualFilter=AC

[CLS:CSerFrameDlg]
Type=0
HeaderFile=SerFrameDlg.h
ImplementationFile=SerFrameDlg.cpp
Filter=D
LastObject=IDC_BUTTON1
BaseClass=CDialog
VirtualFilter=dWC

[CLS:CAboutDlg]
Type=0
HeaderFile=SerFrameDlg.h
ImplementationFile=SerFrameDlg.cpp
Filter=D

[DLG:IDD_ABOUTBOX]
Type=1
Class=CAboutDlg
ControlCount=4
Control1=IDC_STATIC,static,1342177283
Control2=IDC_STATIC,static,1342308480
Control3=IDC_STATIC,static,1342308352
Control4=IDOK,button,1342373889

[CLS:CSerFrameDlgAutoProxy]
Type=0
HeaderFile=DlgProxy.h
ImplementationFile=DlgProxy.cpp
BaseClass=CCmdTarget
Filter=N

[DLG:IDD_SERFRAME_DIALOG]
Type=1
Class=CSerFrameDlg
ControlCount=15
Control1=IDB_CLOSE,button,1342242816
Control2=IDB_MANAGENAME,button,1342242816
Control3=IDB_START,button,1342242816
Control4=IDB_STOP,button,1476460544
Control5=IDC_STATIC,static,1342308352
Control6=IDB_NETOPT,button,1342242816
Control7=IDB_TELOPT,button,1342242816
Control8=IDB_FAXOPT,button,1342242816
Control9=ID_REPORT,SysListView32,1350631425
Control10=IDL_FAXREPORT,SysListView32,1350631425
Control11=IDC_STATIC,static,1342308352
Control12=IDB_SENDFAX_SERFRAME,button,1476460544
Control13=IDE_FAX_DIAL_NO,edit,1350631552
Control14=IDC_STATIC,static,1342308352
Control15=IDC_BUTTON1,button,1073807360

[MNU:IDR_MENU1]
Type=1
Class=?
Command1=IDC_NEW
CommandCount=1

[DLG:IDD_NAMELIST]
Type=1
Class=CNameList
ControlCount=15
Control1=IDC_NAMELIST,SysListView32,1350631425
Control2=IDC_STATIC,static,1342308352
Control3=IDE_HOSTNAME,edit,1350631552
Control4=IDC_STATIC,static,1342308352
Control5=IDE_PERSONNAME,edit,1350631552
Control6=IDC_STATIC,static,1342308352
Control7=IDE_DTMFNO,edit,1350631552
Control8=IDC_STATIC,static,1342308352
Control9=IDE_INLINENO,edit,1350631552
Control10=IDB_SHOWALL,button,1342242816
Control11=IDB_PERSONNEW,button,1342242816
Control12=IDB_PERSONEDIT,button,1342242816
Control13=IDB_PERSONDEL,button,1342242816
Control14=IDB_PERSONSEARCH,button,1342242816
Control15=IDB_CLOSE,button,1342242816

[CLS:CNameList]
Type=0
HeaderFile=namelist.h
ImplementationFile=namelist.cpp
BaseClass=CDialog
LastObject=CNameList
Filter=D
VirtualFilter=dWC

[DLG:IDD_TELOPT]
Type=1
Class=CTelOptDlg
ControlCount=20
Control1=IDC_STATIC,static,1342308352
Control2=IDE_OUTLINENO,edit,1350631552
Control3=IDC_STATIC,static,1342308352
Control4=IDE_INLINENUM,edit,1350631552
Control5=IDC_STATIC,button,1342177287
Control6=IDC_STATIC,static,1342308352
Control7=IDE_INLINE1,edit,1350631552
Control8=IDC_STATIC,static,1342308352
Control9=IDE_INLINE2,edit,1350631552
Control10=IDC_STATIC,static,1342308352
Control11=IDE_INLINE3,edit,1350631552
Control12=IDC_STATIC,static,1342308352
Control13=IDE_INLINE4,edit,1350631552
Control14=IDC_STATIC,static,1342308352
Control15=IDE_INLINE5,edit,1350631552
Control16=IDC_STATIC,static,1342308352
Control17=IDE_INLINE6,edit,1350631552
Control18=IDB_OK,button,1342242816
Control19=IDB_CANCEL,button,1342242816
Control20=IDC_SHOW_ALL_CHAN,button,1342242817

[DLG:IDD_NETOPT]
Type=1
Class=CNetOptDlg
ControlCount=6
Control1=IDC_STATIC,static,1342308352
Control2=IDE_SERVER_IP,edit,1350631552
Control3=IDC_STATIC,static,1342308352
Control4=IDE_SERVER_PORT,edit,1350631552
Control5=IDB_OK,button,1342242817
Control6=IDB_CANCEL,button,1342242816

[CLS:CTelOptDlg]
Type=0
HeaderFile=teloptdlg.h
ImplementationFile=teloptdlg.cpp
BaseClass=CDialog
LastObject=CTelOptDlg
Filter=D
VirtualFilter=dWC

[CLS:CNetOptDlg]
Type=0
HeaderFile=NetOptDlg.h
ImplementationFile=NetOptDlg.cpp
BaseClass=CDialog
Filter=D
LastObject=CNetOptDlg
VirtualFilter=dWC

[DLG:IDD_CHANNELTYPE]
Type=1
Class=CShowAllChanTypeDlg
ControlCount=2
Control1=IDOK,button,1342242817
Control2=IDL_ALLCHENNELTYPE,SysListView32,1350631425

[CLS:CShowAllChanTypeDlg]
Type=0
HeaderFile=ShowAllChanTypeDlg.h
ImplementationFile=ShowAllChanTypeDlg.cpp
BaseClass=CDialog
Filter=D
LastObject=CShowAllChanTypeDlg
VirtualFilter=dWC

[DLG:IDD_FAXOPT]
Type=1
Class=CFaxOptDlg
ControlCount=4
Control1=IDC_STATIC,static,1342308352
Control2=IDE_OUTLINEWITHFAX,edit,1350631552
Control3=IDB_OK,button,1342242817
Control4=IDB_CANCEL,button,1342242816

[CLS:CFaxOptDlg]
Type=0
HeaderFile=FaxOptDlg.h
ImplementationFile=FaxOptDlg.cpp
BaseClass=CDialog
Filter=D
LastObject=CFaxOptDlg
VirtualFilter=dWC

[CLS:CSendFaxDlg]
Type=0
HeaderFile=SendFaxDlg.h
ImplementationFile=SendFaxDlg.cpp
BaseClass=CDialog
Filter=D
LastObject=IDB_CANCEL
VirtualFilter=dWC

