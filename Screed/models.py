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

# The item description does not change. If there is an edit, a new item description is made.
class ItemDefinition(models.Model):
    ATTACK = 'A'
    DEFENSE = 'D'
    SUPPORT = 'S'
    TYPES = [
        (ATTACK, 'Attack'),
        (DEFENSE, 'Defense'),
        (SUPPORT, 'Support'),
    ]

    # An id for the item that does not change across versions.
    tag = models.IntegerField()
    name = models.CharField(max_length=256)
    type = models.CharField(
        max_length=1,
        choices=TYPES,
        default=SUPPORT,
    )
    description = models.TextField()
    quantity = models.IntegerField(
        default=0
    )
    power = models.IntegerField()
    cost = models.IntegerField()

class Item(models.Model):
    item_definition = models.ForeignKey(
        ItemDefinition,
        on_delete=models.CASCADE
    )
    quantity = models.IntegerField(
        default=0
    )
    owner = models.ForeignKey(
        Traveler,
        on_delete=models.CASCADE
    )
    

class Node(models.Model):
    title = models.CharField(max_length=512)
    text = models.TextField()
    authors = models.ManyToManyField(User)
    score = models.IntegerField()

class edit(models.Model):
    title = models.CharField(max_length=512)
    description = models.TextField()
    text = models.TextField()
    author = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        null=True
    )
    positive = models.IntegerField()
    negative = models.IntegerField()

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
        ItemDefinition,
        on_delete=models.CASCADE
    )