class User:
    def __init__(self,name):
        self.name = name
        self.is_log_in = False
    def log_in(self):
        self.is_log_in = True
def is_log_in_decorator(function):
    def wrapped_function(user):
        if user.is_log_in == True:
            function(user)
        else:
            print("please log in before create post.")
    return wrapped_function
@is_log_in_decorator
def create_post(user):
    print("Successfully created post")

new_user = User("Dear")
new_user.log_in()
create_post(new_user)

