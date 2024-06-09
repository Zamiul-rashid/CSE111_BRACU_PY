class User:
    activities = ["Post", "Like", "Comment"]
    def __init__(self, name,email):
        self.name = name
        self.email = email
    def UserActivity(self, activityType):
        if activityType in User.activities:
            return True
        else:
            return False
    def userDetail(self):
        return f"User Detail:\nName:{self.name}\
        \nEmail: {self.email}"
        
class BracbookUser(User):
    def __init__(self, name, email, phone_num=None):
        super().__init__(name, email)
        self.num = phone_num
        self.activities  = []
    def UserActivity(self, meh):
        self.meh = meh
        
        if self.meh in User.activities:
            print(f"{self.name} has {self.meh}(d/ed) successfully.")
            self.activities.append(self.meh)
        else:
            print(f"No activities found like {self.meh}")
    def userDetail(self):
        print(
            super().userDetail()
        )
        if self.num != None :
            print(F"Phone: {self.num}")
        return(
            f"Activity log: {','.join(self.activities)}" if len(self.activities) == 0 else F"Activity log: No recent activity"
        )
            
            
        
        
#Write your code here
user1 = BracbookUser("Rakait","xyz@gmail.com")
print("1===========================")
print(user1.userDetail())
print("2===========================")
user2 = BracbookUser("Sazzad","abc@gmail.com","01727xxxxxx")
print("3===========================")
print(user2.userDetail())
print("4===========================")
user1.UserActivity("Like")
print("5===========================")
user1.UserActivity("Comment")
print("6===========================")
print(user1.userDetail())
print("7===========================")
user2.UserActivity("Share")
print("8===========================")
user2.UserActivity("Comment")
print("9===========================") 
print(user2.userDetail())