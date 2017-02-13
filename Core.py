# Ядро комплекса
# Классы Workspace, WorkspaceObject
import numpy as np

#============================================================
class Workspace(object):
    """description of class"""
    a=[] #LIST of workspaceObject
    def addObject(self, newObject):
        a.append(newObject)

#============================================================
class WorkspaceObject(object):
    """description of class"""
    pass

#============================================================
class Signal_1D(WorkspaceObject):
    # Класс одномерного сигнала
    def __init__(self):
        self.SigProp = {"SigName": "Какой-то сигнал", "fs": 1, "fsUnit": 1}  # Словарь с параметрами сигнала
        self.Waveform = np.array([1, 2, 3])

    def __str__(self):
        msg=self.SigProp["SigName"]
        return msg

    def loadSignal(self, param, SourceType = 1):
        # Тут сделать загрузку из разных источников
        if SourceType == 1:
            filename = param
            # fhandle = None
            flag = False
            try:
                fhandle = open(filename)
                line = fhandle.readline
                while line:
                    line = fhandle.readline()

                    if flag == False:
                        if line == "#DATA#\n":
                            flag = True
                    elif line != "":
                        line = line.rstrip("\n")
                        try:
                            self.Waveform.append(float(line))
                        except:
                            print("Error1")
                            print(line)
                self.Waveform = np.array(self.Waveform)
            except:
                print("Error2")


#============================================================
class Signal_nD(WorkspaceObject):
    # Класс многомерного сигнала
    Signals = []  # LIST of workspaceObject

    def addSignal(self, newObject):
        self.Signals.append(newObject)


