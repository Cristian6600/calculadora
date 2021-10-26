from django.db import models

# Create your models here.
class laplace(models.Model):    
      
    var_1 = models.IntegerField(blank=True, null=True)
    var_2 = models.IntegerField(blank=True, null=True)
    var3 = models.IntegerField(blank=True, null=True)       

    var_s_1= models.IntegerField()
    var_s_2= models.IntegerField()

    numerador = models.CharField(max_length=15, blank= True, null=True)  
    denominador  = models.CharField(max_length= 15, blank= True, null=True)  
    tota = models.CharField(max_length=15, blank= True, null=True, verbose_name = "Resultado")  

    class Meta:
        verbose_name = "t^n = n!/sn^1"
        verbose_name_plural = "t^n = n!/sn^+1"

    vari = "s"
    div = "/"
    
    @property
    def total(self):
          return str(self.numerador) + self.div + str(self.denominador)
    
    @property
    def var(self):
      return self.var_1 * self.var_2 * self.var3

    @property
    def suma(self):
        return (self.var_s_1) + (self.var_s_2) 
    
    @property
    def var1(self):
      return str(self.vari) + str(self.suma)

    def save(self):
        self.numerador = self.var
        self.denominador = str(self.var1)
        self.tota = self.total
        
        super (laplace,  self).save()

class laplace_2(models.Model):
    variable_1 = models.IntegerField()
    resultado = models.CharField(max_length=30, blank=True, null=True)
    div = "/"
    vari = "s"

    class Meta:
        verbose_name = "a/s"
        verbose_name_plural = "a/s"

    @property
    def lapla_2(self):
       return str(self.variable_1) + self.div + self.vari

    def save(self):
        self.resultado = self.lapla_2
        
        super (laplace_2,  self).save()

class laplace_3(models.Model):
    var_1 = models.IntegerField()
    resultado = models.CharField(max_length=30, blank= True, null=True)

    class Meta:
        verbose_name = "1/S-a"
        verbose_name_plural = "1/S-a"

    var = 1
    vari = "s"
    div = "/"
    menos = "-"

    @property
    def lapla_3(self):
        return str(self.var) + self.div + self.vari + self.menos + str(self.var_1) 
    
    def save(self):
        self.resultado = self.lapla_3
        
        super (laplace_3,  self).save()

class laplace_4(models.Model):
    var_1 = models.IntegerField()
    var_2 = models.IntegerField()
    resultado = models.CharField(max_length=30, blank= True, null=True)
    vari = "s"
    div = "/"
    el = "s^2-"
    mas = "+"
    @property
    def var_4(self):
        return str(self.var_2 ) + self.div + self.el + str(self.var_1 * 2) + self.vari + self.mas + str(self.var_2 ** 2 + self.var_2 + 1)

    def save(self):
        self.resultado = self.var_4
        
        super (laplace_4,  self).save()

    class Meta:
        verbose_name = "e^t senb+"
        verbose_name_plural = "e^t senb+"

class laplace_5(models.Model):
    var_1 = models.IntegerField()
    var_2 = models.IntegerField()
    resultado = models.CharField(max_length=30, blank= True, null=True)

    vari = "s-"
    varis = "s+"
    div = "/"
    es = "s^2-"

    @property
    def var_5(self):
        return self.vari + str(self.var_1) + self.div + str(self.es) + str(self.var_1 * 2) + self.varis + str(self.var_1 **2 + self.var_2 **2)

    def save(self):
        self.resultado = self.var_5
        
        super (laplace_5,  self).save() 

    class Meta:
        verbose_name = "e^t cosb+"
        verbose_name_plural = "e^t cosb+"

class laplace_6(models.Model):
    var_1 = models.IntegerField()
    resultado = models.CharField(max_length=30, blank= True, null=True)
    es = "/s^2"
    class Meta:
        verbose_name = "a/s^2+a^2"
        verbose_name_plural = "a/s^2+a^2"

    @property
    def var_6(self):
        return str(self.var_1) + self.es + '+' + str(self.var_1 ** 2)

    def save(self):
        self.resultado = self.var_6
        super (laplace_6,  self).save() 
    
class laplace_7(models.Model):
    var_1 = models.IntegerField()
    resultado = models.CharField(max_length=30, blank= True, null=True)
    es = "s/s^2+"
    class Meta:
        verbose_name = "cos at = s/s^4 a^2"
        verbose_name_plural = "cos at = s/s^4 a^2"

    @property
    def var_7(self):
        return self.es + str(self.var_1 **2)

    def save(self):
        self.resultado = self.var_7
        super (laplace_7,  self).save() 

class laplace_8(models.Model):
    var_1 = models.IntegerField()
    var_2 = models.IntegerField()
    resultado = models.CharField(max_length=30, blank= True, null=True)
    es = "s/s^2+"
    class Meta:
        verbose_name = "t^ e^at = nb/(s-a)^n+1 "
        verbose_name_plural = "t^ e^at = nb/(s-a)^n+1 "

    @property
    def var_8 (self):
        return str(self.var_1 )+ '/s^'+ str(self.var_2)+ '-' + str(self.var_2 ** 2) + 's'

    def save(self):
        self.resultado = self.var_8
        super (laplace_8,  self).save() 
        

    



    







    
    
