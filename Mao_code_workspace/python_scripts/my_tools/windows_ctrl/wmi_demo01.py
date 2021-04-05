import wmi
import pprint  # not really necessary. Only used to pretty print results. :D


class RegistryApplications:
    """Provides WMI based accessors to the computer/remote computers list of Applications installed. The data is taken
    from the registry where uninstall paths are kept.

    Keyword arguments:
    real -- the real part (default 0.0)
    imag -- the imaginary part (default 0.0)
    """

    HKEY_CLASSES_ROOT = 2147483648
    HKEY_CURRENT_USER = 2147483649
    HKEY_LOCAL_MACHINE = 2147483650
    HKEY_USERS = 2147483651
    HKEY_CURRENT_CONFIG = 2147483653

    REG_SZ = 1
    REG_EXPAND_SZ = (2)
    REG_BINARY = (3)
    REG_DWORD = (4)
    REG_MULTI_SZ = (7)
    REG_QWORD = (11)

    strComputer = r"myremotepcname"
    strUsername = r"myusername"
    strPassword = r"mypassword"

    intTotalNumberOfInstalledApps = 0

    strApplications = []
    __singleApplicationData = []

    def __init__(self, computerName=r".", userName=r"myusername", password=r"mypassword"):
        """
        Keyword arguments:
        computerName -- name of the computer to access. (default=".")
        userName -- username of the computer preferably Admin member. (default="myusername")
        password -- password string of the username for that particular computer. (default="mypassword")
        """
        assert isinstance(userName, str)
        assert isinstance(password, str)
        assert isinstance(computerName, str)
        self.strComputer = computerName
        self.strUsername = userName
        self.strPassword = password

    def setSecurity(self, userName, password):
        """
        Keyword arguments:
        userName -- username of the computer preferably Admin member. (default="myusername")
        password -- password string of the username for that particular computer. (default="mypassword")
        """
        assert isinstance(userName, str)
        assert isinstance(password, str)
        self.strUsername = userName
        self.strPassword = password

    def setComputerName(self, computerName):
        """
        Keyword arguments:
        computerName -- name of the computer to access. (default=".")
        """
        assert isinstance(computerName, str)
        self.strComputer = computerName

    @property
    def getResult(self):
        """Description: Initiates the collection of data from the remote or local computer. The result is returned.
        Immediately by this function.
        """
        oReg = wmi.WMI(
            moniker=r"winmgmts:{impersonationLevel=impersonate}!\\" + self.strComputer + r"\root\default:StdRegProv",
            user=self.strUsername,
            password=self.strPassword,
            computer=self.strComputer,
        )
        sSubKeyName = r"Software\Microsoft\Windows\CurrentVersion\Uninstall"

        result, keys = oReg.EnumKey(
            hDefKey=self.HKEY_LOCAL_MACHINE,
            sSubKeyName=sSubKeyName,
        )

        sPossibleValues = []
        listResult = []

        if result == 0:

            self.intTotalNumberOfInstalledApps = len(keys)

            # Each key is a single application.
            for key in keys:
                self.__singleApplicationData = []

                # print key
                path = sSubKeyName + '\\' + key
                subResult, sNames, sIntType = oReg.EnumValues(
                    hDefKey=self.HKEY_LOCAL_MACHINE,
                    sSubKeyName=path,
                )

                if "DisplayName" not in sNames:
                    self.__singleApplicationData.append(["DisplayName", key])
                for x in xrange(0, len(sNames)):
                    if sIntType[x] == self.REG_SZ or sIntType[x] == self.REG_EXPAND_SZ or sIntType[
                        x] == self.REG_MULTI_SZ:
                        if [sNames[x], sIntType[x]] not in sPossibleValues:
                            sPossibleValues.append([sNames[x], sIntType[x]])

                        subResult, strValueName = oReg.GetStringValue(
                            hDefKey=self.HKEY_LOCAL_MACHINE,
                            sSubKeyName=sSubKeyName + '\\' + key,
                            sValueName=sNames[x],
                        )

                        # Only insert to result if the value & name is of len > 0
                        if subResult == 0 and (
                                (len(sNames[x]) > 0 and len(strValueName) > 0) or (sNames[x] == "DisplayName")):
                            self.__singleApplicationData.append([sNames[x], strValueName])

                if (len(self.__singleApplicationData) > 0):
                    listResult.append(self.__singleApplicationData)

        return listResult


# Example usage
x = RegistryApplications(
    computerName='myremotepcname',  # computerName='.', # use this (".") for localhost
    userName='myusername',
    password='mypassword'
)

result = x.getResult
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(result)
pp.pprint("Total Number of Installed Applications via Result: " + str(len(result)))
pp.pprint("Total Number of Installed Applications via Keys: " + str(x.intTotalNumberOfInstalledApps))
