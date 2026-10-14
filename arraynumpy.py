import numpy as np
row=int(input("Enter the no of rows"))
col=int(input("Enter the no of cols"))
data=[]
for i in range(row):
    rows=[]
    for j in range(col):
        rows.append(int(input(f"i{i}j{j}")))
    data.append(rows)
arr=np.array(data)
#print(arr)
while True:
    print("\n1.Display \n2.insert row \n3.delete row \n4.update row \n5.search \n6.sort \n7.transpose \n8.sum \n9.min and max \n10.mean \n11.exit")
    choice=int(input("Enter the option"))
    if choice==1:
        print(arr)
    elif choice==2:
        new_row=[]
        print(f"Enter {arr.shape[1]} no of element in row")
        for j in range(arr.shape[1]):
            new_row.append(int(input(f"Enter the elements {j}")))
        arr=np.vstack((arr,new_row))
        print(arr)
    elif choice==3:
        index=int(input("Enter the row index to delete"))
        if index>=0 and index<arr.shape[0]:
            arr=np.delete(arr,index,axis=0)
            print("row deleted successfully")
        else:
            print("row not found")
    elif choice==4:
        r=int(input("Enter the row index"))
        c=int(input("Enter the col index"))
        new_val=int(input("Enter the new val"))
        if arr.shape[0]>r and arr.shape[1]>c:
            arr[r][c]=new_val
            print("value updated")
        else:
            print("Element not found")
    elif choice==5:
        search=int(input("enter the value to search"))
        result=np.where(arr==search)
        if(len(result[0])>0):
            for i in range(len(result[0])):
                print(f"row{result[0][i]} col{result[1][i]}")
        else:
            print("Invalid option")
    elif choice==6:
        ch=int(input("Enter the no to choice"))
        if ch==1:
            arr=np.sort(arr,axis=1)
            print(arr)
        elif ch==2:
            arr=np.sort(arr,axis=0)
            print(arr)
    elif choice==7:
        arr=arr.T
        print("Transpose of a matrix")
        print(arr)
    elif choice==8:
        print("sum of the values:",np.sum(arr))
        print("sum of the row wise:",np.sum(arr,axis=1))
        print("sum of the col wise:",np.sum(arr,axis=0))
    elif choice==9:
        print("min and max",np.min(arr),np.max(arr))
    elif choice==10:
        print("mean of the value:",np.mean(arr))
    elif choice==12:
        break
