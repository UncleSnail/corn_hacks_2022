from django.db import models
# from django.contrib.auth.models import User

class User(models.Model):
    name = models.CharField(max_length=127)
    email = models.EmailField()
    score = models.IntegerField(default=1)

    def __str__(self):
        return self.name

class StatDefinition(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    authors = models.ManyToManyField(User)

    def __str__(self):
        return self.name

# The item description does not change. If there is an edit, a new item description is made.
class ItemDefinition(models.Model):
    ATTACK = 'A'
    DEFENSE = 'D'
    SUPPORT = 'S'
    BURDEN = 'B'
    TYPES = [
        (ATTACK, 'Attack'),
        (DEFENSE, 'Defense'),
        (SUPPORT, 'Support'),
        (BURDEN, 'Burden'),
    ]

    # An id for the item that does not change across versions.
    tag = models.IntegerField(null=True)
    name = models.CharField(max_length=255)
    type = models.CharField(
        max_length=1,
        choices=TYPES,
        default=SUPPORT,
    )
    description = models.TextField()
    authors = models.ManyToManyField(User)
    quantity = models.IntegerField(
        default=0
    )
    power_type = models.ForeignKey(
        StatDefinition,
        on_delete=models.SET_NULL,
        null=True,
        related_name='power_item'
    )
    power = models.IntegerField(default=0)
    cost_type = models.ForeignKey(
        StatDefinition,
        on_delete=models.SET_NULL,
        null=True,
        related_name='cost_item'
    )
    cost = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    

class Node(models.Model):
    title = models.CharField(max_length=511)
    text = models.TextField()
    authors = models.ManyToManyField(User)
    positive = models.IntegerField(default=1)
    negative = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Traveler(models.Model):
    name = models.CharField(max_length=127)
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True
    )
    node = models.ForeignKey(
        Node,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

class Stat(models.Model):
    definition = models.ForeignKey(
        StatDefinition,
        on_delete=models.CASCADE,
        null=True
    )
    owner = models.ForeignKey(
        Traveler,
        on_delete=models.CASCADE,
        null=True
    )
    score = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.definition} - {self.owner}'

class Item(models.Model):
    definition = models.ForeignKey(
        ItemDefinition,
        on_delete=models.CASCADE,
        null=True
    )
    quantity = models.IntegerField(
        default=0
    )
    owner = models.ForeignKey(
        Traveler,
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return f'{self.definition} - {self.owner}'

class Edit(models.Model):
    title = models.CharField(max_length=511)
    description = models.TextField()
    text = models.TextField()
    author = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    positive = models.IntegerField(default=1)
    negative = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Reward(models.Model):
    node = models.ForeignKey(
        Node,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    item = models.ForeignKey(
        ItemDefinition,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{self.item} <- {self.node}'

class Check(models.Model):
    title = models.CharField(max_length=511)
    success_message = models.TextField()
    success_target = models.ForeignKey(
        Node,
        on_delete=models.SET_NULL,
        null=True,
        related_name='from_success'
    )
    failure_message = models.TextField()
    failure_target = models.ForeignKey(
        Node,
        on_delete=models.SET_NULL,
        null=True,
        related_name='from_failure'
    )
    stat_type = models.ForeignKey(
        StatDefinition,
        on_delete=models.SET_NULL,
        null=True
    )
    value = models.IntegerField(default=1)
    item_requirement = models.ForeignKey(
        ItemDefinition,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title

class Choice(models.Model):
    text = models.TextField()
    parent = models.ForeignKey(
        Node,
        on_delete=models.SET_NULL,
        null=True
    )
    target = models.ForeignKey(
        Node,
        on_delete=models.SET_NULL,
        null=True,
        related_name='reached_by'
    )
    choice_check = models.ForeignKey(
        Check,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='parent'
    )

    def __str__(self):
        return self.text