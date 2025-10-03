dict_ticket={
    'G1569':['beijingnan-tianjinnan','18:06','18:39','00:33'],
    'G1567':['beijingnan-tianjinnan','18:15','18:49','00:34'],
    'G8917':['beijingnan-tianjinxi','18:20','19:19','00:59'],
    'G203':['beijingnan-tianjinnan','18:35','19:09','00:34']
}
print('train\t\tdepart-arrive\t\t\t\tdepart time\t\tarrive time\t\ttime cost')
for key in dict_ticket.keys():
    print(key, end='\t\t')
    for item in dict_ticket.get(key):
        print(item, end='\t\t')
    print()

train_no=input('please input train no:')
info=dict_ticket.get(train_no,'train not exists')
if info!='train not exists':
    person=input('please input person:')
    s=info[0]+' '+info[1]+' depart'
    print('you have purchased '+train_no+' '+s+',please '+person+' get the ticket ASAP.')
else:
    print('sorry.',info)