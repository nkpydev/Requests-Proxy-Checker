from requests import exceptions

class ProxyCheckerDirHandlingError(OSError):
    """Directory Handling Error"""
    #print('Hello!')
    print('Error with Files and DIRs!!')

class ProxyCheckerRequestException(Exception):
    """ Any exception related to Requests """
    pass