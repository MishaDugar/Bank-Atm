class Person:
    def __init__(self,age,name,height,weight):
        self.age=age      
        self.name=name 
        self.height=height 
        self.weight=weight 

    def display(self):
        print("Name: "+self.name)  
        print("Age: "+str(self.age))   
        print("Height: "+str(self.height))
        print("Weight: "+str(self.weight))

p1= Person(33,"Jhon",5.8,50)
p1.display()