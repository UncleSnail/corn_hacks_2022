# from django.db import models

# class User(models.Model):
#     name = models.CharField()
#     email = models.EmailField()
#     score = models.IntegerField()

#     def __str__(self):
#         return self.name

# class Traveler(models.Model):
#     name = models.CharField()
#     user = models.ForeignKey(User)

#     def __str__(self):
#         return self.name

# class Item(models.Model):
#     ATTACK = 'A'
#     DEFENSE = 'D'
#     SUPPORT = 'S'
#     TYPES = [
#         (ATTACK, 'Attack'),
#         (DEFENSE, 'Defense'),
#         (SUPPORT, 'Support'),
#     ]

#     name = models.CharField()
#     type = models.CharField(
#         max_length=1,
#         choices=TYPES,
#         default=SUPPORT
#     )

# class Node(models.Model):
#     title = models.CharField()
#     text = models.TextField()
#     authors = models.ManyToManyField(User)

# class Choice(models.Model):
#     text = models.TextField()
#     parent = models.ForeignKey(Node)
#     target = models.ForeignKey(Node)

# class Reward(models.Model):
#     choice = models.ForeignKey(Choice)
#     item = models.ForeignKey(Item)
#     pass