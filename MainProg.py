
import Core
import Global
import matplotlib.pyplot as plt

# Загружаем глобальные параметры
Config = Global.GlobalParam()
#  Config.NewConfigFile()
Config.LoadParam()

# Создаем сигнал
Sig1 = Core.Signal_1D()

filename = Config['datapath'].rstrip("\\n") + "\\Radon1.txt"
Sig1.loadSignal(filename)
Sig1.SigProp["SigName"]="Radon"
fig=plt.figure()

plt.plot(Sig1.Waveform)
plt.show()





