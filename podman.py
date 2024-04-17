import matplotlib.pyplot as plt
import pandas as pd
podman=pd.read_csv('podman.csv')
print(podman)
#year_month = str(podman['created_year']) + str(podman['created_month'])
podman['yearmonth'] = podman.created_year.map(str) + podman.created_month.map(str)

print (podman)
rhel7 = podman[podman['rhel_major'] ==7]
rhel8 = podman[podman['rhel_major'] ==8]
rhel9 = podman[podman['rhel_major'] ==9]
    


fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(rhel7['yearmonth'], rhel7['syscount'],c='red', label='RHEL7',linestyle='-')
ax.plot(rhel8['yearmonth'], rhel8['syscount'],c='green', label='RHEL8',linestyle='-')
ax.plot(rhel9['yearmonth'],\
rhel9['syscount'],c='blue',label='RHEL9',linestyle='--')
ax.legend()
plt.show() 
