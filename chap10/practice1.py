import prettytable as pt

def show_ticket(row_num):
    tb=pt.PrettyTable()
    tb.field_names=['行号','座位1','座位2','座位3','座位4','座位5']
    for i in range(1,row_num+1):
        lst=[f'第{i}行','有票','有票','有票','有票','有票']
        tb.add_row(lst)
    print(tb)

def order_ticket(row_num,row,column):
    tb=pt.PrettyTable()
    tb.field_names = ['行号', '座位1', '座位2', '座位3', '座位4', '座位5']
    for i in range(1,row_num+1):
        lst = [f'第{i}行', '有票', '有票', '有票', '有票', '有票']
        if int(row)==i:
            lst[int(column)]='已售'
        tb.add_row(lst)
    print(tb)
if __name__=='__main__':
    row_num=6
    show_ticket(row_num)
    choose_num=input('请输入您选择的座席：如4,3代表第4排第3列：')
    row,column=choose_num.split(',')
    order_ticket(row_num,row,column)



