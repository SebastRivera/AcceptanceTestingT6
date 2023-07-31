lista = []
task = str(input("Enter the task to be added:"))

def addTask(lista, task): 
    lista.append((task, "Pending"))
    return lista

def showList(lista):
    print("Tasks:")
    for task in lista:
        print("- %s" % task)

def clearList(lista):
    lista.clear()
    return lista
    
