from django.db import models

class User(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    score = models.IntegerField()

    def __str__(self):
        return self.name

class Traveler(models.Model):
    name = models.CharField(max_length=128)
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return self.name

class Item(models.Model):
    ATTACK = 'A'
    DEFENSE = 'D'
    SUPPORT = 'S'
    TYPES = [
        (ATTACK, 'Attack'),
        (DEFENSE, 'Defense'),
        (SUPPORT, 'Support'),
    ]

    name = models.CharField(max_length=128)
    type = models.CharField(
        max_length=1,
        choices=TYPES,
        default=SUPPORT,
    )

class Node(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField()
    authors = models.ManyToManyField(User)

class Choice(models.Model):
    text = models.TextField()
    parent = models.ForeignKey(
        Node,
        on_delete=models.SET_NULL,
        null=True,
        related_name='choices'
    )
    target = models.OneToOneField(
        Node,
        on_delete=models.SET_NULL,
        null=True,
        related_name='reached_by'
    )

class Reward(models.Model):
    choice = models.ForeignKey(
        Choice,
        on_delete=models.CASCADE
    )
    item = models.ForeignKey(
        Item,
        on_delete=models.SET_NULL,
        null=True
    )
    pass