#%%
import matplotlib.pyplot as plt


#%%
am = [1,2,3,4,5,6,7,8,9,10,11,0]
pm = [13,14,15,16,17,18,19,20,21,22,23,12]
ampm = [[am[i],pm[i]] for i in range(len(am))]
count = [1,2,3,4,5,6,7,8,9,10,11,12]

#ax = plt.subplot(111)
#ax.spines['right'].set_visible(False)
#ax.spines['top'].set_visible(False)
plt.xlabel('number shown')
plt.ylabel('hours passed since new day')
#ax.figure(figsize=(5,2))
plt.xticks(count)
plt.yticks([(i)*2 for i in range(12)])
plt.grid(c='#dddddd')
#ax.legend(am)
#ax.remove_axes((1,1,1,1))
plt.title('Why AM and PM is confusing',size=14, pad=24)
plt.plot(count,am,marker='o',label='am')
plt.plot(count,pm,marker='o',label='pm')
plt.legend()
plt.savefig('ploooot.png')
# %%

hours_passed = [i+1 for i in range(24)]

am = [1,2,3,4,5,6,7,8,9,10,11,None,None,None,None,None,None,None,None,None,None,None,None,12]
pm = [None,None,None,None,None,None,None,None,None,None,None,12,1,2,3,4,5,6,7,8,9,10,11,None]

plt.xlabel('hours passed since new day')
plt.ylabel('number shown')
plt.xticks(hours_passed[1::2])
plt.yticks([i+1 for i in range(12)])
plt.grid(c='#dddddd')

plt.scatter(hours_passed,am,marker='o',label='am',zorder=2)
plt.scatter(hours_passed,pm,marker='o',label='pm',zorder=2)

plt.title('Why AM and PM is confusing (inversed)',size=14, pad=24)
#plt.plot(count,am,marker='o',label='am')
#plt.plot(count,pm,marker='o',label='pm')
plt.legend()
plt.savefig('plooootInverse.png')


# %%
