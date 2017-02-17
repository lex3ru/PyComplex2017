# Ядро комплекса
# Классы Workspace, WorkspaceObject
import numpy as np
import matplotlib.pyplot as plt
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
        self.SigProp = {"SigName": "Какой-то сигнал",
                             "fs": 1,
                         "fsUnit": 1,
                        "TStart" : 0}  # Словарь с параметрами сигнала

        self.Waveform = np.array([1, 2, 3]) #   Временная форма (отсчеты) сигнала
        self.timeline = np.array([0, 1, 2]) #   Отсчеты времени TODO Сделать генератор ???

    def __str__(self):
        msg=self.SigProp["SigName"]
        return msg
    # Загрузка сигнала из внешнего источника
    def loadSignal(self, param, SourceType = 1):
        # TODO Тут сделать загрузку из разных источников
        WF=[]
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
                            WF.append(float(line))
                        except:
                            print("Core.loadsignal.Error1")
                            print(line)
                self.Waveform = np.array(WF)
            except:
                print("Core.loadsignal.Error2")

    def NormCenter(self):
        #  Центрируем
        self.Waveform = self.Waveform - self.Waveform.mean()
        #  Нормируем
        self.Waveform = self.Waveform / self.Waveform.std()


#============================================================
class Signal_nD(WorkspaceObject):
    # Класс многомерного сигнала
    Signals = []  # LIST of workspaceObject
    Timeline = [] # Ось времени
#  TODO Варианты синхронизации сигналов по времени (добавление пропусков, децимация, интерполяция)
#  TODO Преобразование оси времени совместно со всеми сигналами
    def __init__(self, param = {"TStart":0,"Length": 100, "fs": 1, "fsUnit": 1}):
        #  Создаем общую для всех сигналов ось времени.
        self.Timeline = np.linspace(param["TStart"], param["TStart"]+param["Length"]/param["fs"], param["Length"])
        self.NDSignalParam = param

    def addSignal(self, newObject):
#  TODO Добавить проверку "влезает ли сигнал в ось времени
        self.Signals.append(newObject)

    def createSignal(self, n = 2):
        # создаем N одномерных пустых сигналов и добавляем его к многомерному
        for i in range(n):
            self.Signals.append(Signal_1D())

    def plot(self):

        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)

        for i in range(len(self.Signals)):
            ax.plot(self.Signals[i].Waveform)
        plt.show()
