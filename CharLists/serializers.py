from rest_framework import serializers

from .models import gameClass, gameClasses, gameRace, background, alignment, characteristic, language, languages, possession, possessions, skill, skills, charList, savingThrows, spell, spells

class gameClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = gameClass;
        fields = ['id', 'title', 'description'];

class gameRaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = gameRace;
        fields = ['id', 'title', 'description'];

class backgroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = background;
        fields = ['id', 'title', 'description'];

class alignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = alignment;
        fields = ['title', 'description'];

class characteristicSerializer(serializers.ModelSerializer):
    class Meta:
        model = characteristic;
        fields = ['title', 'description'];

class languageSerializer(serializers.ModelSerializer):
    class Meta:
        model = language;
        fields = ['title', 'description'];

class possessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = possession;
        fields = ['title', 'description'];

class skillSerializer(serializers.ModelSerializer):
    class Meta:
        model = skill;
        fields = ['title', 'description'];

class spellSerializer(serializers.ModelSerializer):
    class Meta:
        model = spell;
        fields = ['title', 'description'];

class charListSerializer(serializers.ModelSerializer):
    gameClassMain = serializers.SlugRelatedField(
        read_only=True,
        slug_field='title'
    )
    gameRace = serializers.SlugRelatedField(
        read_only=True,
        slug_field='title'
    )
    background = serializers.SlugRelatedField(
        read_only=True,
        slug_field='title'
    )
    alignment = serializers.SlugRelatedField(
        read_only=True,
        slug_field='title'
    )
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = charList;
        fields = ['name', 
                  'gameClassMain',
                  'gameRace',
                  'background',
                  'alignment',
                  'user',
                  'strength', 'dexterity', 'constitution', 'intelegency', 'wisdom', 'charisma', 
                  'description'];

class charListImgSerializer(serializers.ModelSerializer):
    gameClassMain = serializers.SlugRelatedField(
        read_only=True,
        slug_field='title'
    )
    gameRace = serializers.SlugRelatedField(
        read_only=True,
        slug_field='title'
    )
    background = serializers.SlugRelatedField(
        read_only=True,
        slug_field='title'
    )
    alignment = serializers.SlugRelatedField(
        read_only=True,
        slug_field='title'
    )
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = charList;
        fields = ['name', 
                  'gameClassMain', 
                  'gameRace', 
                  'background', 
                  'alignment', 
                  'user',
                  'img',
                  'strength', 'dexterity', 'constitution', 'intelegency', 'wisdom', 'charisma', 'description'];

class gameClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = gameClasses;
        fields = ['gameClass', 'charList'];

class languagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = languages;
        fields = ['language', 'charList'];
        
class possessionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = possessions;
        fields = ['possession', 'charList'];
        
class skillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = skills;
        fields = ['skill', 'charList'];
        
class spellsSerializer(serializers.ModelSerializer):
    class Meta:
        model = spells;
        fields = ['spell', 'charList'];
        
class savingThrowsSerializer(serializers.ModelSerializer):
    class Meta:
        model = savingThrows;
        fields = ['savingThrow', 'charList'];
        
