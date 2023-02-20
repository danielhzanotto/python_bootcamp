class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticated_decorator(function):
    def wrapper(*args):

        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper


@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post")


user_daniel = User('daniel')
create_blog_post(user_daniel)

user_maria = User('maria')
user_maria.is_logged_in = True
create_blog_post(user_maria)
