#Ascending order:(it is only for non-duplicates Elements)
l1=[56,3,2,78,6,0]
print("The original list is:",l1)
for i in range(len(l1)):
   min_value=min(l1[i:])
   min_index=l1.index(min_value)
   l1[i],l1[min_index]=l1[min_index],l1[i]
print("The list after sorted is:",l1)

#For duplicates elements:
		
l1=[5,0,2,2,6,0]
print("The original list is:",l1)
for i in range(len(l1)):
   min_value=min(l1[i:])
   min_index=l1.index(min_value,i)
   l1[i],l1[min_index]=l1[min_index],l1[i]
print("The list after sorted is:",l1)

#The below program is perfect for all because it no need to swap between if it have same value
l1=[5,0,2,2,6,0]
print("The original list is:",l1)
for i in range(len(l1)-1):
   min_value=min(l1[i:])
   min_index=l1.index(min_value,i)
   if l1[i]!=l1[min_index]:
       l1[i],l1[min_index]=l1[min_index],l1[i]
print("The list after sorted is:",l1)

#-Above value is geeting by user input.

num=int(input("Enter how many elements want:"))
list1=[int(input("Enter the index:")) for x in range(num)]
for i in range(len(list1)-1):
   m_ind=i
   for j in range(i+1,len(list1)):
       if list1[j] < list1[m_ind]:
           m_ind=j
   if list1[i]!=list1[m_ind]:
       list1[i],list1[m_ind]=list1[m_ind],list1[i]
      
print(list1)
  


