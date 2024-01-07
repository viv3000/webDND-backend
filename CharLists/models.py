from django.db import models;

from django.contrib.auth.models import User;

class gameClass(models.Model):
    title = models.CharField(max_length=101)
    description = models.TextField()
    def __str__(self):
        return self.title;

class gameRace(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.title;

class background(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.title;

class alignment(models.Model):
    title = models.CharField(max_length=2)
    description = models.TextField()
    def __str__(self):
        return self.title;

class characteristic(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.title;

class language(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.title;

class possession(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.title;

class skill(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.title;

class spell(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.title;

class charList(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    gameClassMain = models.ForeignKey(gameClass,  on_delete=models.CASCADE)
    gameRace      = models.ForeignKey(gameRace,   on_delete=models.CASCADE)
    background    = models.ForeignKey(background, on_delete=models.CASCADE, null=True, blank=True)
    alignment     = models.ForeignKey(alignment,  on_delete=models.CASCADE, null=True, blank=True)
    user          = models.ForeignKey(User,       on_delete=models.CASCADE)

    strength     = models.IntegerField()
    dexterity    = models.IntegerField()
    constitution = models.IntegerField()
    intelegency  = models.IntegerField()
    wisdom       = models.IntegerField()
    charisma     = models.IntegerField()

    img = models.ImageField(upload_to='img/persons/', height_field=100, width_field=100, null=True, blank=True)
    def __str__(self):
        return self.name;

class gameClasses(models.Model):
    gameClass = models.ForeignKey(gameClass, on_delete=models.CASCADE)
    charList  = models.ForeignKey(charList,  on_delete=models.CASCADE)
    def __str__(self):
        return self.gameClass;

class languages(models.Model):
    language = models.ForeignKey(language, on_delete=models.CASCADE)
    charList = models.ForeignKey(charList, on_delete=models.CASCADE)
    def __str__(self):
        return self.language;

class possessions(models.Model):
    possession = models.ForeignKey(possession, on_delete=models.CASCADE)
    charList   = models.ForeignKey(charList,   on_delete=models.CASCADE)
    def __str__(self):
        return self.possession;

class skills(models.Model):
    skill    = models.ForeignKey(skill,    on_delete=models.CASCADE)
    charList = models.ForeignKey(charList, on_delete=models.CASCADE)
    def __str__(self):
        return self.skill;

class spells(models.Model):
    spell    = models.ForeignKey(spell,    on_delete=models.CASCADE)
    charList = models.ForeignKey(charList, on_delete=models.CASCADE)
    def __str__(self):
        return self.spell;

class savingThrows(models.Model):
    characteristic = models.ForeignKey(characteristic, on_delete=models.CASCADE)
    charList       = models.ForeignKey(charList,       on_delete=models.CASCADE)
    def __str__(self):
        return self.characteristic;

