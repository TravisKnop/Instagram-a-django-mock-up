from django.db import models
from django.core.validators import RegexValidator


# Should I import User?


class Name(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    username = models.CharField(max_length=20)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'."
                                         " Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], blank=True)
    sex = models.CharField(max_length=10)
    bio = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Gram(models.Model):
    author = models.ForeignKey(Name)
    entry = models.FileField()
    caption = models.CharField(max_length=500)
    gram_datetime = models.DateTimeField(auto_now_add=True)
    number_of_likes = Like.liked_gram.count()


class Like(models.Model):
    liked_gram = models.ForeignKey(Gram)
    liker = models.ForeignKey(Name)
    like_datetime = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    commented_post = models.ForeignKey(Gram)
    commenter = models.ForeignKey(Name)
    comment = models.CharField(max_length=500)
    comment_datetime = models.DateTimeField(auto_now_add=True)


class Follower(models.Model):
    follower = models.ForeignKey(Name)

    def __str__(self):
        return self.follower

    @property
    def number_followers(self):
        return self.followers.count()


class Following(models.Model):
    following = models.ForeignKey(Name)

    def __str__(self):
        return self.following

    @property
    def number_following(self):
        return self.following.count()


class Test(models.Model):
    def testname(self):
        print("hi?")





