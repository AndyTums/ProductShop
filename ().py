# coding: utf-8
from shop.models import Category,Subcategory,Product
c = Category.objects.all()
c
c.delete()
c
c.save()
get_ipython().run_line_magic('save', '()')
