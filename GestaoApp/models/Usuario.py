from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.hashers import *
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, Permission, Group, BaseUserManager)

class MyUserManager(BaseUserManager):
  def create_user(self, usuario, nome, email, password):
    if not usuario:
      raise ValueError('Nome de usuario obrigatorio')
    if not nome:
      raise ValueError('Nome obrigatorio')
    if not email:
      raise ValueError('Email obrigatorio')
    if not password:
      raise ValueError('Senha obrigatoria')

    user = self.model(
      usuario=usuario,
      nome=nome,
      email=self.normalize_email(email),
    )

    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_superuser(self, usuario, nome, email, password):
    if not usuario:
      raise ValueError('Nome de usuario obrigatorio')
    if not nome:
      raise ValueError('Nome obrigatorio')
    if not email:
      raise ValueError('Email obrigatorio')
    if not password:
      raise ValueError('Senha obrigatoria')

    user = self.model(
      usuario=usuario,
      email=self.normalize_email(email),
      nome=nome,
    )

    user.is_admin = True
    user.set_password(password)
    user.save(using=self._db)
    return user

class Usuario(AbstractBaseUser, PermissionsMixin):
  nome = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  usuario = models.CharField(unique=True, max_length=60)

  USERNAME_FIELD = 'usuario'
  EMAIL_FIELD = 'email'
  REQUIRED_FIELDS = ['nome', 'email']

  objects = MyUserManager()

  def get_full_name(self):
    return self.nome

  def get_short_name(self):
    return self.usuario

  def __str__(self):
    return self.nome

  class Meta:
    managed = True
    db_table = 'Usuario'