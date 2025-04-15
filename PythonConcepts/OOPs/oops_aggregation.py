"""
Aggregation is Known as (HAS-A) relationship in OOPs. 
It is used to create a relationship between two objects.
"""

class UserProfile:
    """
    This class is used to create a user profile.
    """
    def __init__(self, name, age, college):
        self.name = name
        self.age = age
        self.college = college
    
    def __str__(self):
        return f"{self.name} is of age {self.age} and in college {self.college.name}"
    
    def update_college(self, name, location):
        self.college.update_college_details(name, location)
        return f"{self.name} is of age {self.age} and in college {self.college.name}"

        

class College:
    """
    This class is used to create a college.
    """
    def __init__(self, name, location):
        self.name = name
        self.location = location
    
    def update_college_details(self, name, location):
        self.name = name
        self.location = location



college_ = College(name="UIET CSJM", location="Kanpur") # Create a college object
user = UserProfile(name="RamGopal", age=25, college=college_) # Create a user profile object
print(user)
user.update_college(name="Updated Name", location="Updated Location") # Update the college details
print(user)