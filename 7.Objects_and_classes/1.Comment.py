class Comment :
    def __init__(self, username, content, likes=0):
        self.username = username
        self.content = content
        self.likes = likes

comment = Comment('user_one', 'I dont like this book', '2')
comment.username = 'Dreadlordow'
comment.content = 'I like this nickname'

print(comment.username)
print(comment.content)
print(comment.likes)