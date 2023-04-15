from django import forms
from django.forms.models import inlineformset_factory
from .models import Course, Module

#creatimng formset to manage courses
'''
    formset_factory()/inlineformset_factory is an abstraction that simplifies 
    working with related objects
'''

ModuleFormSet = inlineformset_factory(Course,
                                        Module,
                                        fields= ['title', 'description'],
                                        extra= 2,
                                        can_delete=True)