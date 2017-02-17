import collections, pickle, os

class GlobalParam (collections.UserDict):
    # Save global parameters
    def SaveParam(self, filename = 'config.cfg'):
        path = os.path.abspath(os.curdir)  #Get current directory
        path = path.rstrip("\n")+"\\"+filename
        fhandle = open(path, 'wb')
        pickle.dump(self, fhandle)
        fhandle.close

    # Load global parameters
    def LoadParam(self, filename = 'config.cfg'):
        try:
            path=os.path.abspath(os.curdir)  #Get current directory
            path=path.rstrip("\n")+"\\"+filename 
            fhandle=open(path,'rb')
            #  fhandle.seek(0)
            self.clear
            self.update(pickle.load(fhandle))
            fhandle.close
            return "Config loaded"
        except(EnvironmentError, pickle.UnpicklingError) as err:
            print("{0}: import error: {1}".format(
            os.path.basename(sys.argv[0]), err))
            return "Config IO Error"
        finally:
            if fhandle is not None:
                fhandle.close()

    

class Global(object):
    """description of class"""
    globalparam=GlobalParm() #[('datapath','c:\MyFiles\Development\Complex2016workdir\TestData\\n')]