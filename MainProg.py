
import Core
import Global
import matplotlib.pyplot as plt
import copy

# Загружаем глобальные параметры
Config = Global.GlobalParam()
#  Config.NewConfigFile()
Config.LoadParam()

# Создаем сигнал
Sig1 = Core.Signal_1D()
Sig1.loadSignal(Config['datapath'].rstrip("\\n") + "\\Radon1.txt")
Sig1.SigProp["SigName"]="Radon"
Sig1.NormCenter()

Sig2 = Core.Signal_1D()
Sig2.loadSignal(Config['datapath'].rstrip("\\n") + "\\Debet.txt")
Sig2.SigProp["SigName"]="Debet"
Sig2.NormCenter()

Glob=Core.Signal_nD()
Glob.addSignal(Sig1)
Glob.addSignal(Sig2)
fig = Glob.plot()


"""
plt.plot(Sig2.Waveform)  #  Рисуем сигнал
plt.show()               #  Показываем окно с графиком


#  ТЕСТ ГЕЙНДЖЕРА
#  from scipy import stats
import statsmodels.api as sm
#  from statsmodels.graphics.api import qqplot

ar_mod20 = sm.tsa.ARMA(Sig1.Waveform, (2,0)).fit(disp=False)
print(ar_mod20.params)

arx_mod20 = sm.tsa.ARMA(Sig1.Waveform, (2,0), Sig2.Waveform).fit(disp=False)
print(ar_mod20.params)
print(arx_mod20.params)
"""




