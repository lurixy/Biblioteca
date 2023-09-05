from django.db import models
from django.db import models

class Cidade(models.Model):
    nome = models.CharField(max_length=50)
    uf = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome
    

class Autor(models.Model):
    nome = models.CharField(max_length=50)
    site = models.CharField(max_length=50)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    
class Editora(models.Model):
    nome = models.CharField(max_length=50)
    site = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
        
    def __str__(self):
        return self.nome 

class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome 
    
class Livro(models.Model):
    nome = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    preco = models.PositiveBigIntegerField()
    datapubli = models.BooleanField()

    def __str__(self):
        return f'{self.categoria} {self.editora} {self.nome} {self.autor} {self.preco}{self.datapubli}'
    
class Leitores(models.Model):
    nome= models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    cpf = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome
    
class Emprestimo(models.Model):
    dataemp = models.DateField()
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    leitor = models.ForeignKey(Leitores, on_delete=models.CASCADE)
    datadev = models.DateTimeField()
    

    def __str__(self):
        return self.nome 