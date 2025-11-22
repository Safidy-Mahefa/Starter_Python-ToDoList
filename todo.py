# FONCTIONNALITES : Ajouter une tâche, Marquer une tâche comme terminée, suppr une tâche, afficher tt les tâche
# Structure : Liste [tâche,bool] / bool: pour statut d'une tâche
taskList = [["tâche1",False],["tâche2",True],["tâche3",False],["tâche4",True],["tâche5",False]]

# Fonction pour ajouter une nouvelle tâche
def addTask(task,status):
    newTask = [task,status]
    taskList.append(newTask)
    print("--/Tâche '{}' ajouté avec succès !".format(task))

# Fonction pour supprimer une tâche
def delTask(index):
    if index < 0 or index > len(taskList):
        print("--/Index invalide")
        return
    taskName = taskList[index][0]
    taskList.pop(index)
    print("--/Tâche '{}' Supprimé avec succès !".format(taskName))

# Fonction pour afficher tt les tâches
def showTasks():
    if len(taskList) == 0:
        print("--/Aucune tâche à afficher, va jouer ailleurs !--/")
    else:
        taskStatus = ""
        print("\n# Liste complète des tâches :")
        for task in taskList:
            if(task[1]):
                taskStatus = "Terminé"
            else:
                taskStatus = "En cours"
            print("{}- {} : {}".format(taskList.index(task) + 1, task[0],taskStatus))
            
# Fonction pour marquer une tâche terminé
def finishTask(index):
    if index < 0 or index > len(taskList):
        print("--/Index invalide")
        return
    if taskList[index][1]:
        print("Tâche déjà terminé !")
    else:
        taskList[index][1] = True
        print("--/Tâche '{}' Terminé avec succès !".format(taskList[index][0]))

# Fonction afficher les commandes du petit terminal
def showCommand():
    print("\n### COMMANDES: 1-> Ajouter une tâche / 2-> Supprimer une tâche / 3-> Terminer une tâche / q-> Quitter l'application  ###")
showCommand()
showTasks()

# Boucle infinie pour faire fonctionner l'app
boucle = True
while boucle:
     command = input(">")
     if command == "1":
       taskName = input("Entrez le nom de votre tâche :")
       addTask(taskName,False)
       showTasks()
       showCommand()
     elif command == "2":
        taskIndex = input("Entrez le numero de la tâche à supprimer (-1 pour tout supprimer) :")
        if taskIndex == "-1":
                taskList.clear()
                print("--/Toutes les tâches ont été supprimés !")
        else: delTask(int(taskIndex)-1)

        showTasks()
        showCommand()
     elif command == "3":
        taskIndex = input("Entrez le numero de la tâche à terminer :")
        finishTask(int(taskIndex)-1)
        showTasks()
        showCommand()
     elif command == "q":
       boucle = False
print("--/Vous avez quitté l'application !")