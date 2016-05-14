def bubblesort(items):
	for i in range(0,len(items)):
	   for j in range(0,len(items)-i-1):
		  if items[j]>items[j+1]:
			 items[j],items[j+1]=items[j+1],items[j]

def insertionsort(items):
	for i in range(1,len(items)):
	   j=i
	   while j>0 and items[j]<items[j-1] :
		  items[j],items[j-1]=items[j-1],items[j] 	          
		  j -=1

def quicksort(items):
	if len(items) > 1:
	   pivot_index=len(items) //2
	   smaller=[]
	   larger=[]
	   for i,val in enumerate(items) :
		  if i != pivot_index:
			 if val < items[pivot_index]:
				smaller.append(val)
			 else :
				larger.append(val)

	   quicksort(smaller)
	   quicksort(larger)
	   items[:]=smaller + [items[pivot_index]] + larger               

def main():
	items=[4,2,7,8,1,20,3,5]
	bubblesort(items)
	print items
	items=[4,2,7,8,1,20,3,5]
	insertionsort(items)
	print items 
	items=[4,2,7,8,1,20,3,5]
	quicksort(items)
	print items 

if __name__ == '__main__':
	main()	