import pandas as pd
import matplotlib.pyplot as plt
#***********************************************************************#
#Code for visualizing first query
cv= pd.read_csv("C:\\Users\\Hany\\Desktop\\1.csv")
plt.barh(cv['Name'], cv['total_Purchase'], color = "purple")
plt.title("The Total Purchases For Every Genre")
plt.xlabel('Total Purchases', labelpad= 10)
plt.ylabel('Genre Name', labelpad= 10)
ax= plt.gca()
for tick in ax.yaxis.get_major_ticks():
    tick.label.set_fontsize(7)
    for tick in ax.xaxis.get_major_ticks():
        tick.label.set_fontsize(8)
plt.show()
#***********************************************************************#
#Code for visualizing second query
cv= pd.read_csv("C:\\Users\\Hany\\Desktop\\2.csv")
plt.barh(cv['Name'], cv['Total_Purchase_Rock'], color = "red")
plt.title(" The Names For Most Popular Artists For Rock Genre")
plt.xlabel('Total Purchase Rock genre', labelpad= 10)
plt.ylabel('Artist Name', labelpad= 10)
ax= plt.gca()
for tick in ax.yaxis.get_major_ticks():
    tick.label.set_fontsize(9)
    for tick in ax.xaxis.get_major_ticks():
        tick.label.set_fontsize(9)
plt.show()
#***********************************************************************#
#Code for visualizing third query
cv= pd.read_csv("C:\\Users\\Hany\\Desktop\\3.csv")
plt.barh(cv['Name'], cv['NumberOf_Tracks'], color = "blue")
plt.title("Number of Tracks for every genre")
plt.xlabel('Number of Track', labelpad= 10)
plt.ylabel('Genre Name', labelpad= 10)
ax= plt.gca()
for tick in ax.yaxis.get_major_ticks():
    tick.label.set_fontsize(7)
    for tick in ax.xaxis.get_major_ticks():
        tick.label.set_fontsize(8)
plt.show()
;
#***********************************************************************#
#Code for visualizing fourth query
cv= pd.read_csv("C:\\Users\\Hany\\Desktop\\4.csv")
plt.barh(cv['Title'], cv['NumberTrack_forEachAlbum'], color = "orange")
plt.title("Names of Top made albums based on Number Albums in each Track")
plt.xlabel('NumberTrack_forEachAlbum', labelpad= 10)
plt.ylabel('Album Title', labelpad= 10)
ax= plt.gca()
for tick in ax.yaxis.get_major_ticks():
    tick.label.set_fontsize(9)
    for tick in ax.xaxis.get_major_ticks():
        tick.label.set_fontsize(9)
plt.show()