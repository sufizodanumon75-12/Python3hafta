import datetime
class Task:
    def __init__(self,id,title,description,deadline):
        self.id = id
        self.title = title
        self.description = description
        self.deadline = deadline
        self.is_complited = False
        self.created_at = datetime.datetime.now()
        
    def __str__(self):
        return f'{self.title} -- {self.deadline} -- {self.is_complited} -- {self.created_at}'
    
class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1
        
    def create_task(self,title,description,deadline):
        task = Task(self.next_id,title,description,deadline)
        self.tasks.append(task)
        self.next_id += 1
        
    def show_all(self):
        for task in self.tasks:
            print(task)
            
    def show_uncomplited_tasks(self):
        for task in self.tasks:
            if not task.is_complited:
                print(task)

    def expired(self):
        expired_tasks=[]
        now=datetime.datetime.now()
        for task in self.tasks:
            res=datetime.datetime.strptime(task.deadline,'%d-%m-%Y').date()
            if res<now:
                expired_tasks.append(task)
                print(expired_tasks)

    def sort_by_desc(self):
        urgent_tasks=[]
        bahazur_tasks=[]
        for task in self.tasks:
            if task.description == 'urgent':
                urgent_tasks.append(task)
                print('urgent tasks: ',urgent_tasks)
            if task.description == "bahazur":
                bahazur_tasks.append(task)
                print("bahazur task: ",bahazur_tasks)
    
    def quantity_of_task(self):
        print(len(self.tasks))
        
    def get_by_id(self,id):
        for task in self.tasks:
            if id == task.id:
                return task
    
    def update_task(self,id,new_title,new_description,new_deadline):
        for task in self.tasks:
            if task.id == id:
                self.title =new_title
                self.description = new_description
                self.deadline = new_description   
                
    def change_status(self,id):
        for task in self.tasks:
            if id == task.id:
                self.tasks.remove(task)
                
    def delete(self,id):
            for task in self.tasks:
                task.is_comlited = True
                print(task)
                
    def cleaning(self):
        self.tasks.clear()
        

tm=TaskManager()

while True:
    print(
        '''
        1.Create a task 
        2.Show all task 
        3.Show uncomplited task 
        4.Show expired task
        5.Sort by description
        6.Quantity of task
        7.Get by id
        8.Update task
        9. Change status of task
        10.Delete one task
        11.Clear all
        12. Logout''' )

    rakam=int(input("Make your choose: "))

    if rakam == 1:
        title=input('Enter title of task: ')
        description=input('Enter description of task, description must be urgent or bahazur: ')
        deadline=input('Enter your deadline: ')
        tm. create_task(title, description, deadline)

    if rakam == 2:
        tm. show_all()

    if rakam == 3:
        tm.show_uncomplited_tasks()
        
    if rakam == 4:
        tm.expired()
        
    if rakam == 5:
        tm.sort_by_desc()
        
    if rakam == 6:
        tm.quantity_of_task()
        
    if rakam == 7:
        id=int(input('Enter id of task: '))
        print(tm.get_by_id(id))

    if rakam == 8:
        id=int(input('Enter id of task: '))
        new_title=input('Enterd new title of task: ')
        new_description=input('Enter new description of task: ')
        new_deadline=input('Enter your new deadline: ')
        tm.update_task(id,new_title,new_description, new_deadline)

    if rakam == 9:
        id=int(input('Enter id of task: '))
        tm. change_status(id)

    if rakam == 10:
        id=int(input('Enter id of task: '))
        tm.delete(id)

    if rakam == 11:
        tm.cleaning()

    if rakam == 12:
        print('Logout')
        break

