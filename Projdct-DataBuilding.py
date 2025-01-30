

#faz1 ‌BST
class Node:
    def __init__(self,title,writer,ISBN):
        self.title=title
        self.writer=writer
        self.ISBN=ISBN
        self.left=None
        self.right=None         

class BST():
     def __init__(self):       
          self.root=None
     
     #افزودن کتاب
     def Insert(self,title,writer,ISBN):
        NewNode=Node(title,writer,ISBN)
        if self.root==None:
              self.root=NewNode
              return
        root=self.root
        while True:
            if ISBN < root.ISBN:
                 if root.left ==None:
                    root.left= NewNode
                    return
                 root=root.left   

            elif ISBN > root.ISBN:
                if  root.right==None:
                    root.right=NewNode
                    return
                root=root.right
#           #از قبل وجود داره
            else:
               print(f"{ISBN:} already exists")
               return

     #نمایش کتاب‌ها
     def Inorder(self,Node):
          if Node  is not None:
             self.Inorder(Node.left)
             print(f"Title: {Node.title} writer:{Node.writer} ISBN:{Node.ISBN}")
             self.Inorder(Node.right)
              
     #حذف کتاب  
     # r ریشه درخت  
     #طبق الگوریتم جزوه
     def remove(self,r,keydelet):
         
         if r is None:
             print("Error: Tree is empty")
             return r
         if keydelet < r.ISBN:
                  r.left=self.remove(r.left,keydelet)
         elif keydelet > r.ISBN:
                  r.right=self.remove(r.right,keydelet)

         #keydelet== r.ISBN
         else:
                    
              if r.left is None:  
                   temp=r.right
                   r=None
                   return temp
              elif r.right is None:                 
                    temp=r.left
                    r=None
                    return temp
              else:
                 
                 # در صورتی که دوتا بچه داشت 
                 temp=self.DeletMin(r.right)
                 r.ISBN=temp.ISBN
                 r.title=temp.title
                 r.writer=temp.writer
##
                 r.right=self.remove(r.right, temp.ISBN)

         return r       

##
     
     def DeletMin(self,r):
          if r is None:
               print("Erorr: tree is empty")
               return r
          if r.left is not None:
               r.left=self.DeletMin(r.left)
               return r
          temp=r
          r=r.right
          del temp
          return r
                 
# faz2
class NodeUser:
      def __init__(self,name,ID) :
          self.name=name
          self.ID=ID
          self.next=None
       
     
class linklist:
    def __init__(self):
         self.first=None
         self.len=0
         

    def IsEmpty(self):
        return self.first is None
            
    #افزودن کاربر     
    def add(self,name,ID):
        AddNode=NodeUser(name,ID)
        if self.IsEmpty():
            self.first= AddNode
 #           
            self.len +=1
            return
        else:
             temp=self.first
             while temp.next !=None:
                  temp=temp.next
             temp.next=AddNode   
             self.len +=1  

     #حذف کاربر
     #حذف کاربر با شماره عضویت ID
    def remove(self,name,ID):
         if self.IsEmpty():
            print("Error:List is empty")
            return

         #گره اول باشد
         if self.first.ID==ID:
              self.first=self.first.next
              self.len-=1
              return
          #شروع از گره دوم
         temp=self.first.next
         #
         while temp is not None and temp.next is not None and temp.next.ID != ID:
              temp=temp.next

         if temp.next is not None:
            temp.next = temp.next.next  
            self.len -= 1
         else:
              print("User is not found")
    
    #نمایش کاربران
    def desplay(self):
         if self.IsEmpty():
              print("Error:List is empty")
              return
              
         ListUser=[]
         temp=self.first
         while temp  is not None:
              ListUser.append(temp.name)
              temp=temp.next
         print(ListUser)     

# faz3

class queue:
    class request:         
        def __init__(self,IdUser,ISBN):
            self.IdUser=IdUser
            self.ISBN=ISBN
            self.next=None 

    def __init__(self):
         self.rear=None
         self.front=None
         self.size=0
                

    def IsEmpty(self):
         return self.front is None

    #افزودن درخواست
    def add_request(self,IdUser,ISBN):
         
        New_Request=self.request(IdUser,ISBN)
        if self.IsEmpty():
            self.front= New_Request
            self.rear=New_Request
            return
        
        self.rear.next= New_Request
        self.rear=New_Request
        self.size +=1     

     #پردازش درخواست
    def remove(self):
         if self.IsEmpty():
              print("Erorr:list is empty")  
              return None
         else:  
            remove_request=self.front   
            self.front=self.front.next
            if self.IsEmpty():
                 self.rear=None
            self.size -=1     
         return  remove_request 
# faz4
    class history:
        def __init__(self):
             self.first=None
             self.last=None
             self.size=0  

        def IsEmpty(self):
             return self.size == 0


        #اضافه کردن به تاریخچه
        def AddHistory(self, request):
          request.next = None 
    
          if self.IsEmpty():
               self.first = request
               self.last = request
          else:
               self.last.next=request
               self.last=request               

                  
          self.size +=1


        
       # نمایش تاریخچه
        def display(self):
           if self.IsEmpty():
               print("تاریخچه خالی است.")
               return
           temp = self.first
           while temp is not None:
               print(f"User ID: {temp.IdUser}, ISBN: {temp.ISBN}")
               temp = temp.next

                
                  
             
              
              
# فاز 1: درخت کتاب‌ها
books = BST()
#افزودن کتاب
books.Insert("Math", "Maryam Mirzakhani", 123)
books.Insert("Data Structures", "Nargis Mirehai", 200)
books.Insert("Algorithms", "Zahra", 789)
books.Insert("Math", "Maryam Mirzakhani", 123)
#حذف کتاب
books.remove(books.root, 789)
#( Inorder)
print("\nList of book:")
books.Inorder(books.root)

# فاز 2: مدیریت کاربران
users = linklist()
users.add("Fatemeh", 101)
users.add("Sara", 1)
users.add("Ali", 100)
users.add("He", 102)

users.remove("He",102)

print("\nList of users:")
users.desplay()

# فاز 3: مدیریت درخواست‌های امانت 
requests = queue()
requests.add_request(101, 123)
requests.add_request(102, 200)
requests.add_request(1, 789)
print("\nLoan request processed:")
requests.remove()
# فاز 4: مدیریت تاریخچه درخواست‌ها
history_stack = queue.history()
history_stack.AddHistory(requests.remove())
print("\nRequest history :")
history_stack.display()       
        
    


