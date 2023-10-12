#Personal Budget Tracker
#Allow users to enter their income and the expenses along with 
#the respective categories, and display the categories, remaining budget
#and spending trends
#The transactions are stored in a file
import pandas as pd
import matplotlib.pyplot as plt

income=0
expenses=[]
rem=0
food=0
home=0
work=0
fun=0
misc=0


#Allow user to add income
def add_inc():

  global income  #global variable

  amt=int(input("\nEnter income: "))
  income+=amt  #increment amount


#Allow user to input expense and category
def add_exp():

  global food,work,fun,misc,home

  cat=input("\nEnter category name: ")       #Category name
  
  print("\nEnter category:\n")
  print("1.Food\n2.Home\n3.Work\n4.Fun\n5.Misc\n")   #Choose category it comes under
 
  catno=int(input("\nEnter category(1-5):"))
 
  exp=int(input("\nEnter expense amount: "))
 
  if catno==1:
    food+=exp
  elif catno==2:
    home+=exp
  elif catno==3:
    work+=exp
  elif catno==4:
    fun+=exp
  elif catno==5:
    misc+=exp                 #Appropriately append amount to respective expense category

  expenses.append((cat,exp))  #Store data in list 'expenses'


#Display expenses and respective category
def disp_exp():

  for cat,exp in expenses:
    print("\nCategory: ",cat," Expenses: ",exp)
  

#Calculate remaining budget by deducting expense amount from income
def calc_budget():

  global rem
  tot=0  #tot variable stores total expense amount

  for cat,exp in expenses:
    tot+=exp

  rem=income-tot  #rem variable gives remaining budget

  print("\nAmount spent in each category:\n")
  print("1.Food: ",food,"\n2.Home: ",home,"\n3.Work: ",work,"\n4.Fun: ",fun,"\n5.Misc: ",misc)
  print("\nTotal money spent: ",tot)
  print("\nTotal remaining budget: ",rem)
  

#Store results of the transactions in a file 'tran.txt'
def store():

  with open("tran.txt",'w') as file:
    file.write(f"{income}")    #Income is entered into file

    for cat,exp in expenses:
      file.write(f"\n{cat},{exp}")    
      #Category and expense is written into file
  
  with open("cate.txt",'w') as file:
    file.write(f"{food}\n{home}\n{work}\n{fun}\n{misc}")


#Load data that is stored in a file 'tran.txt'
def load():
  global income
  global rem

  try:
    with open("tran.txt",'r') as file:
      income=int(file.readline().strip())  #Use split to remove trailing and 
                                           #leading white spaces
      for line in file:
        cat,exp=line.strip().split(',')
        expenses.append((cat,int(exp)))
    
    with open("cate.txt", 'r') as file:
        lines = file.read().splitlines()
        if len(lines) == 5:
            food, home, work, fun, misc = map(int, lines)

  except FileNotFoundError:       #If no file exists, create an empty one
    pass
  

#Display graph of expenses
def display_graph1(categories, expenses):

    # Create a DataFrame from the categories and expenses
    df = pd.DataFrame({'Category': categories, 'Expense': expenses})

    # Create a bar chart
    df.plot(kind='bar', x='Category', y='Expense', legend=False)
    plt.xlabel('Category Name')
    plt.ylabel('Expense')
    plt.title('Category Name vs. Expense')
    plt.xticks(rotation=45)  # Rotate x-axis labels for readability

    plt.show()  # Display the graph

def display_graph2():
    #Create a DataFrame from the expenses list
    df = pd.DataFrame(expenses, columns=['Category', 'Expense'])

    #Group by category and sum the expenses
    grouped = df.groupby('Category')['Expense'].sum()

    #Create a bar chart
    grouped.plot(kind='bar')
    plt.xlabel('Category')
    plt.ylabel('Expense')
    plt.title('Category vs. Expense')
    plt.xticks(rotation=45)  #Rotate x-axis labels for readability

    plt.show()  #Display the graph
  

#Main function
def main():
  
  print("Welcome to your Personal Budget Tracker!")
  print("Here you can keep track of your expenses.")

  while(1):    #Infinite loop
    print("\n\nMenu \n1.Add income \n2.Add expense \n3.Display expenses \n4.Display budget \n5.Save and display graph")
    
    ch=int(input("\nEnter choice: "))

    if ch==1:
      add_inc()               #Add income
    elif ch==2:
      add_exp()               #Add expenses 
    elif ch==3:
      disp_exp()              #Display expenses
    elif ch==4:
      calc_budget()           #Calculate budget
    elif ch==5:
      store()  
      print("\n")
      display_graph1(['Food', 'Home', 'Work', 'Fun', 'Misc'], [food, home, work, fun, misc])
      print("\n\n")
      display_graph2()  # Display the graph           
      break
    else:
      print("Invalid input")  #Any other input


#Call main function
if __name__=="__main__":
  main()








