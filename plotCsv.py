import pandas as pd
import matplotlib.pyplot as plt

import pandas as pd
import matplotlib.pyplot as plt

# 读取CSV文件
data = pd.read_csv('E:/UnityProject/CrowdSimDemo/Assets/DynamicCoordinates_20230817132515.csv')
data1 = pd.read_csv('E:/UnityProject/CrowdSimDemo/Assets/DynamicCoordinates_20230817174253.csv')
data2 = pd.read_csv('E:/UnityProject/CrowdSimDemo/Assets/DynamicCoordinates_20230817174721.csv')
data3 = pd.read_csv('E:/UnityProject/CrowdSimDemo/Assets/DynamicCoordinates_20230817175756.csv')
data4 = pd.read_csv('E:/UnityProject/CrowdSimDemo/Assets/DynamicCoordinates_20230817180252.csv')
data5 = pd.read_csv('E:/UnityProject/CrowdSimDemo/Assets/DynamicCoordinates_20230817182156.csv')
data6 = pd.read_csv('E:/UnityProject/CrowdSimDemo/Assets/DynamicCoordinates_20230817182417.csv')
data7 = pd.read_csv('E:/UnityProject/CrowdSimDemo/Assets/DynamicCoordinates_20230817182609.csv')
data8 = pd.read_csv('E:/UnityProject/CrowdSimDemo/Assets/DynamicCoordinates_20230817182803.csv')
data9 = pd.read_csv('E:/UnityProject/CrowdSimDemo/Assets/DynamicCoordinates_20230817183018.csv')
data10 = pd.read_csv('E:/UnityProject/CrowdSimDemo/Assets/DynamicCoordinates_20230817183212.csv')
data11 = pd.read_csv('E:/UnityProject/CrowdSimDemo/Assets/DynamicCoordinates_20230817183810.csv')
data12 = pd.read_csv('E:/UnityProject/CrowdSimDemo/Assets/DynamicCoordinates_20230817184205.csv')
data13 = pd.read_csv('E:/UnityProject/CrowdSimDemo/Assets/DynamicCoordinates_20230817184358.csv')
data14 = pd.read_csv('E:/UnityProject/CrowdSimDemo/Assets/DynamicCoordinates_20230817184602.csv')
data15 = pd.read_csv('E:/UnityProject/CrowdSimDemo/Assets/DynamicCoordinates_20230817184852.csv')
data16 = pd.read_csv('E:/UnityProject/CrowdSimDemo/Assets/DynamicCoordinates_20230817185152.csv')
data17 = pd.read_csv('E:/UnityProject/CrowdSimDemo/Assets/DynamicCoordinates_20230817185353.csv')
data18 = pd.read_csv('E:/UnityProject/CrowdSimDemo/Assets/DynamicCoordinates_20230817185542.csv')
data19 = pd.read_csv('E:/UnityProject/CrowdSimDemo/Assets/DynamicCoordinates_20230817185730.csv')
data = (data+data1+data2+data3+data4+data5+data6+data7+data8+data9+data10+data11+data12+data13+data14+data15+data16+data17+data18+data19)/20
alldata = [data,data1,data2,data3,data4,data5,data6,data7,data8,data9,data10,data11,data12,data13,data14,data15,data16,data17,data18,data19]
# fig, axes = plt.subplots(nrows=4, ncols=5, figsize=(10, 5))

# exp1adata1 = pd.read_csv('E:/UnityProject/CrowdSimDemo/Assets/DynamicCoordinates_20230818004329.csv')
# exp1adata2 = pd.read_csv('E:/UnityProject/CrowdSimDemo/Assets/DynamicCoordinates_20230818004651.csv')
# exp1adata3 = pd.read_csv('E:/UnityProject/CrowdSimDemo/Assets/DynamicCoordinates_20230818004939.csv')
# exp1adata4 = pd.read_csv('E:/UnityProject/CrowdSimDemo/Assets/DynamicCoordinates_20230818005228.csv')
# exp1adata5 = pd.read_csv('E:/UnityProject/CrowdSimDemo/Assets/DynamicCoordinates_20230818005507.csv')
# exp1adata = (exp1adata1+exp1adata2+exp1adata3+exp1adata4+exp1adata5)/5

# e1adays = exp1adata['days']
# e1auninfectedCount = exp1adata['uninfectedCount']/19
# e1aincubationCount = exp1adata['incubationCount']/19
# e1aasymptomaticCount = exp1adata['asymptomaticCount']/19
# e1asymptomaticCount = exp1adata['symptomaticCount']/19
# e1aimmuneCount = exp1adata['immuneCount']/19

# exp1bdata1 = pd.read_csv('E:/UnityProject/CrowdSimDemo/Assets/DynamicCoordinates_20230818010712.csv')
# exp1bdata2 = pd.read_csv('E:/UnityProject/CrowdSimDemo/Assets/DynamicCoordinates_20230818010949.csv')
# exp1bdata3 = pd.read_csv('E:/UnityProject/CrowdSimDemo/Assets/DynamicCoordinates_20230818011206.csv')
# exp1bdata4 = pd.read_csv('E:/UnityProject/CrowdSimDemo/Assets/DynamicCoordinates_20230818011530.csv')
# exp1bdata5 = pd.read_csv('E:/UnityProject/CrowdSimDemo/Assets/DynamicCoordinates_20230818011756.csv')
# exp1bdata = (exp1bdata1+exp1bdata2+exp1bdata3+exp1bdata4+exp1bdata5)/5

# e1bdays = exp1bdata['days']
# e1buninfectedCount = exp1bdata['uninfectedCount']/19
# e1bincubationCount = exp1bdata['incubationCount']/19
# e1basymptomaticCount = exp1bdata['asymptomaticCount']/19
# e1bsymptomaticCount = exp1bdata['symptomaticCount']/19
# e1bimmuneCount = exp1bdata['immuneCount']/19

# exp1cdata1 = pd.read_csv('E:/UnityProject/CrowdSimDemo/Assets/DynamicCoordinates_20230818012633.csv')
# exp1cdata2 = pd.read_csv('E:/UnityProject/CrowdSimDemo/Assets/DynamicCoordinates_20230818012849.csv')
# exp1cdata3 = pd.read_csv('E:/UnityProject/CrowdSimDemo/Assets/DynamicCoordinates_20230818013115.csv')
# exp1cdata4 = pd.read_csv('E:/UnityProject/CrowdSimDemo/Assets/DynamicCoordinates_20230818013359.csv')
# exp1cdata5 = pd.read_csv('E:/UnityProject/CrowdSimDemo/Assets/DynamicCoordinates_20230818013633.csv')
# exp1cdata = (exp1cdata1+exp1cdata2+exp1cdata3+exp1cdata4+exp1cdata5)/5

# e1cdays = exp1cdata['days']
# e1cuninfectedCount = exp1cdata['uninfectedCount']/19
# e1cincubationCount = exp1cdata['incubationCount']/19
# e1casymptomaticCount = exp1cdata['asymptomaticCount']/19
# e1csymptomaticCount = exp1cdata['symptomaticCount']/19
# e1cimmuneCount = exp1cdata['immuneCount']/19

# exp2adata1 = pd.read_csv('E:/UnityProject/CrowdSimDemo/Assets/DynamicCoordinates_20230818023043.csv')
# exp2adata2 = pd.read_csv('E:/UnityProject/CrowdSimDemo/Assets/DynamicCoordinates_20230818023043.csv')
# exp2adata3 = pd.read_csv('E:/UnityProject/CrowdSimDemo/Assets/DynamicCoordinates_20230818023043.csv')
# exp2adata4 = pd.read_csv('E:/UnityProject/CrowdSimDemo/Assets/DynamicCoordinates_20230818023043.csv')
# exp2adata5 = pd.read_csv('E:/UnityProject/CrowdSimDemo/Assets/DynamicCoordinates_20230818023043.csv')
# exp2adata = (exp2adata1+exp2adata2+exp2adata3+exp2adata4+exp2adata5)/5

# e2adays = exp2adata['days']
# e2auninfectedCount = exp2adata['uninfectedCount']/19
# e2aincubationCount = exp2adata['incubationCount']/19
# e2aasymptomaticCount = exp2adata['asymptomaticCount']/19
# e2asymptomaticCount = exp2adata['symptomaticCount']/19
# e2aimmuneCount = exp2adata['immuneCount']/19

# exp2bdata1 = pd.read_csv('E:/UnityProject/CrowdSimDemo/Assets/DynamicCoordinates_20230818023908.csv')
# exp2bdata2 = pd.read_csv('E:/UnityProject/CrowdSimDemo/Assets/DynamicCoordinates_20230818024125.csv')
# exp2bdata3 = pd.read_csv('E:/UnityProject/CrowdSimDemo/Assets/DynamicCoordinates_20230818024432.csv')
# exp2bdata4 = pd.read_csv('E:/UnityProject/CrowdSimDemo/Assets/DynamicCoordinates_20230818024650.csv')
# exp2bdata5 = pd.read_csv('E:/UnityProject/CrowdSimDemo/Assets/DynamicCoordinates_20230818025007.csv')
# exp2bdata = (exp2bdata1+exp2bdata2+exp2bdata3+exp2bdata4+exp2bdata5)/5

# e2bdays = exp2bdata['days']
# e2buninfectedCount = exp2bdata['uninfectedCount']/19
# e2bincubationCount = exp2bdata['incubationCount']/19
# e2basymptomaticCount = exp2bdata['asymptomaticCount']/19
# e2bsymptomaticCount = exp2bdata['symptomaticCount']/19
# e2bimmuneCount = exp2bdata['immuneCount']/19

# exp2cdata1 = pd.read_csv('E:/UnityProject/CrowdSimDemo/Assets/DynamicCoordinates_20230818025320.csv')
# exp2cdata2 = pd.read_csv('E:/UnityProject/CrowdSimDemo/Assets/DynamicCoordinates_20230818025607.csv')
# exp2cdata3 = pd.read_csv('E:/UnityProject/CrowdSimDemo/Assets/DynamicCoordinates_20230818025816.csv')
# exp2cdata4 = pd.read_csv('E:/UnityProject/CrowdSimDemo/Assets/DynamicCoordinates_20230818030025.csv')
# exp2cdata5 = pd.read_csv('E:/UnityProject/CrowdSimDemo/Assets/DynamicCoordinates_20230818030241.csv')
# exp2cdata = (exp2cdata1+exp2cdata2+exp2cdata3+exp2cdata4+exp2cdata5)/5

# e2cdays = exp2cdata['days']
# e2cuninfectedCount = exp2cdata['uninfectedCount']/19
# e2cincubationCount = exp2cdata['incubationCount']/19
# e2casymptomaticCount = exp2cdata['asymptomaticCount']/19
# e2csymptomaticCount = exp2cdata['symptomaticCount']/19
# e2cimmuneCount = exp2cdata['immuneCount']/19

exp3adata1 = pd.read_csv('E:/UnityProject/CrowdSimDemo/Assets/DynamicCoordinates_20230818051353.csv')
exp3adata2 = pd.read_csv('E:/UnityProject/CrowdSimDemo/Assets/DynamicCoordinates_20230818051740.csv')
exp3adata3 = pd.read_csv('E:/UnityProject/CrowdSimDemo/Assets/DynamicCoordinates_20230818052013.csv')
exp3adata4 = pd.read_csv('E:/UnityProject/CrowdSimDemo/Assets/DynamicCoordinates_20230818052219.csv')
exp3adata5 = pd.read_csv('E:/UnityProject/CrowdSimDemo/Assets/DynamicCoordinates_20230818052519.csv')
exp3adata = (exp3adata1+exp3adata2+exp3adata3+exp3adata4+exp3adata5)/5

e3adays = exp3adata['days']
e3auninfectedCount = exp3adata['uninfectedCount']/19
e3aincubationCount = exp3adata['incubationCount']/19
e3aasymptomaticCount = exp3adata['asymptomaticCount']/19
e3asymptomaticCount = exp3adata['symptomaticCount']/19
e3aimmuneCount = exp3adata['immuneCount']/19

exp3bdata1 = pd.read_csv('E:/UnityProject/CrowdSimDemo/Assets/DynamicCoordinates_20230818052748.csv')
exp3bdata2 = pd.read_csv('E:/UnityProject/CrowdSimDemo/Assets/DynamicCoordinates_20230818052842.csv')
exp3bdata3 = pd.read_csv('E:/UnityProject/CrowdSimDemo/Assets/DynamicCoordinates_20230818052923.csv')
exp3bdata4 = pd.read_csv('E:/UnityProject/CrowdSimDemo/Assets/DynamicCoordinates_20230818053016.csv')
exp3bdata5 = pd.read_csv('E:/UnityProject/CrowdSimDemo/Assets/DynamicCoordinates_20230818053123.csv')
exp3bdata = (exp3bdata1+exp3bdata2+exp3bdata3+exp3bdata4+exp3bdata5)/5

e3bdays = exp3bdata['days']
e3buninfectedCount = exp3bdata['uninfectedCount']/19
e3bincubationCount = exp3bdata['incubationCount']/19
e3basymptomaticCount = exp3bdata['asymptomaticCount']/19
e3bsymptomaticCount = exp3bdata['symptomaticCount']/19
e3bimmuneCount = exp3bdata['immuneCount']/19

days = data['days']
uninfectedCount = data['uninfectedCount']/19
incubationCount = data['incubationCount']/19
asymptomaticCount = data['asymptomaticCount']/19
symptomaticCount = data['symptomaticCount']/19
immuneCount = data['immuneCount']/19
# 提取其他需要的列数据，如第2个折线所需的incubationCount

# # 未感染
# plt.plot(days, uninfectedCount, label='Uninfected Count')
# plt.xlabel('Days')
# plt.ylabel('Agents')
# plt.title('Numbers of Uninfected Agents Over Days')
# plt.legend()
# plt.show()

# # 潜伏期
# plt.plot(days, incubationCount, label='Incubation Count')
# plt.xlabel('Days')
# plt.ylabel('Agents')
# plt.title('Numbers of Incubation Agents Over Days')
# plt.legend()
# plt.show()

# # 有症状
# plt.plot(days, asymptomaticCount, label='Asymptomatic Count')
# plt.xlabel('Days')
# plt.ylabel('Agents')
# plt.title('Numbers of Asymptomatic Agents Over Days')
# plt.legend()
# plt.show()

# # 无症状
# plt.plot(days, symptomaticCount, label='Symptomatic Count')
# plt.xlabel('Days')
# plt.ylabel('Agents')
# plt.title('Numbers of Symptomatic Agents Over Days')
# plt.legend()
# plt.show()

# # 免疫
# plt.plot(days, immuneCount, label='Immune Count')
# plt.xlabel('Days')
# plt.ylabel('Agents')
# plt.title('Numbers of Immuned Agents Over Days')
# plt.legend()
# plt.show()


plt.plot(days, uninfectedCount, label='Uninfected Agents')
plt.plot(days, incubationCount, label='Incubation Agents')
plt.plot(days, asymptomaticCount, label='Asymptomatic Agents')
plt.plot(days, symptomaticCount, label='Symptomatic Agents')
plt.plot(days, immuneCount, label='Immune Agents')
plt.xlabel('Days')
plt.ylabel('Agents')
plt.title('Overview of Experiment 3 Control Group')
plt.legend()
plt.show()

# plt.plot(days, asymptomaticCount+symptomaticCount, label='Infected Agents')
# plt.xlabel('Days')
# plt.ylabel('Agents')
# plt.title('Infection Rates Over Days')
# plt.legend()
# plt.show()

# plt.plot(e1adays, e1auninfectedCount, label='Uninfected Agents')
# plt.plot(e1adays, e1aincubationCount, label='Incubation Agents')
# plt.plot(e1adays, e1aasymptomaticCount, label='Asymptomatic Agents')
# plt.plot(e1adays, e1asymptomaticCount, label='Symptomatic Agents')
# plt.plot(e1adays, e1aimmuneCount, label='Immune Agents')
# plt.xlabel('Days')
# plt.ylabel('Agents')
# plt.title('Overview of Experiment 1 Group A')
# plt.legend()
# plt.show()

# plt.plot(e1bdays, e1buninfectedCount, label='Uninfected Agents')
# plt.plot(e1bdays, e1bincubationCount, label='Incubation Agents')
# plt.plot(e1bdays, e1basymptomaticCount, label='Asymptomatic Agents')
# plt.plot(e1bdays, e1bsymptomaticCount, label='Symptomatic Agents')
# plt.plot(e1bdays, e1bimmuneCount, label='Immune Agents')
# plt.xlabel('Days')
# plt.ylabel('Agents')
# plt.title('Overview of Experiment 1 Group B')
# plt.legend()
# plt.show()

# plt.plot(e2adays, e2auninfectedCount, label='Uninfected Agents')
# plt.plot(e2adays, e2aincubationCount, label='Incubation Agents')
# plt.plot(e2adays, e2aasymptomaticCount, label='Asymptomatic Agents')
# plt.plot(e2adays, e2asymptomaticCount, label='Symptomatic Agents')
# plt.plot(e2adays, e2aimmuneCount, label='Immune Agents')
# plt.xlabel('Days')
# plt.ylabel('Agents')
# plt.title('Overview of Experiment 2 Group A')
# plt.legend()
# plt.show()

# plt.plot(e2bdays, e2buninfectedCount, label='Uninfected Agents')
# plt.plot(e2bdays, e2bincubationCount, label='Incubation Agents')
# plt.plot(e2bdays, e2basymptomaticCount, label='Asymptomatic Agents')
# plt.plot(e2bdays, e2bsymptomaticCount, label='Symptomatic Agents')
# plt.plot(e2bdays, e2bimmuneCount, label='Immune Agents')
# plt.xlabel('Days')
# plt.ylabel('Agents')
# plt.title('Overview of Experiment 2 Group B')
# plt.legend()
# plt.show()

# plt.plot(e2cdays, e2cuninfectedCount, label='Uninfected Agents')
# plt.plot(e2cdays, e2cincubationCount, label='Incubation Agents')
# plt.plot(e2cdays, e2casymptomaticCount, label='Asymptomatic Agents')
# plt.plot(e2cdays, e2csymptomaticCount, label='Symptomatic Agents')
# plt.plot(e2cdays, e2cimmuneCount, label='Immune Agents')
# plt.xlabel('Days')
# plt.ylabel('Agents')
# plt.title('Overview of Experiment 2 Group C')
# plt.legend()
# plt.show()

plt.plot(e3adays, e3auninfectedCount, label='Uninfected Agents')
plt.plot(e3adays, e3aincubationCount, label='Incubation Agents')
plt.plot(e3adays, e3aasymptomaticCount, label='Asymptomatic Agents')
plt.plot(e3adays, e3asymptomaticCount, label='Symptomatic Agents')
plt.plot(e3adays, e3aimmuneCount, label='Immune Agents')
plt.xlabel('Days')
plt.ylabel('Agents')
plt.title('Overview of Experiment 3 Group A')
plt.legend()
plt.show()

plt.plot(e3bdays, e3buninfectedCount, label='Uninfected Agents')
plt.plot(e3bdays, e3bincubationCount, label='Incubation Agents')
plt.plot(e3bdays, e3basymptomaticCount, label='Asymptomatic Agents')
plt.plot(e3bdays, e3bsymptomaticCount, label='Symptomatic Agents')
plt.plot(e3bdays, e3bimmuneCount, label='Immune Agents')
plt.xlabel('Days')
plt.ylabel('Agents')
plt.title('Overview of Experiment 3 Group B')
plt.legend()
plt.show()

plt.plot(days, asymptomaticCount+symptomaticCount, label='Control Group')
plt.plot(e3adays, e3aasymptomaticCount+e3asymptomaticCount, label='Experimental Group A')
plt.plot(e3bdays, e3basymptomaticCount+e3bsymptomaticCount, label='Experimental Group B')
plt.xlabel('Days')
plt.ylabel('Agents')
plt.title('Infection Rates Over Days')
plt.legend()
plt.show()
# 以相似的方式绘制其他折线图