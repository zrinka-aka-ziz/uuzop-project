labels='Age,Sex,Height,Weight,QRSduration,PRinterval,QTinterval,Tinterval,Pinterval,QRSangle,Tangle,Pangle,QRSTangle,Jangle,HeartRate,'
group1 = ['Qwidth','Rwidth','Swidth','SmallRwidth','SmallSwidth','IntDeflNum','RaggedR','DiphasicR','RaggedP','DiphasicP','RaggedT','DiphasicT']
channels = ['DI', 'DII', 'DIII', 'AVR', 'AVL', 'AVF', 'V1','V2','V3','V4','V5','V6']
group2 = ['JJamp','Qamp','Ramp','Samp','SmallRamp','SmallSamp','Pamp','Tamp','QRSA', 'QRSTA']
#num=15+len(channels)*len(group1)+len(channels)*len(group2)
#print(num) #279 OK

#dodavanje grupe 1
for channel in channels:
    for col in group1:
        new_col= channel+col+',' #new_col= channel+'_'+col+','
        labels+=new_col

#dodavanje grupe 2
for channel in channels:
    for col in group2:
        new_col= channel+col+',' #new_col= channel+'_'+col+',' ako zelimo underscore da odvaja kanale i ono sto je mjereno
        labels+=new_col

labels1 = labels[:-1] #makni zadnji zarez
labels_list=labels1.split(',')
print(len(labels_list))

#for el in labels_list:
    #print(el)
    
u_labels=",".join(labels_list)
#print(u_labels)
