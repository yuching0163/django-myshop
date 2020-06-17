from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category' # 給你的模型類一個更可讀的名字
        verbose_name_plural = 'categories' # 指定模型的複數形式是什麼

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE) # use related_name to do .foods instead of restaurant.food_set on ForeignKey field裡加入related_name
    name = models.CharField('商品名稱', max_length=200)
    slug = models.SlugField(max_length=200)
    image = models.ImageField('圖片', upload_to='amazon', blank=True)
    description = models.TextField('物品描述', blank=True) # blank是針對表單的 表示填寫表單時該字段可以不填寫  null 表示資料庫該字段可以空
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField('創建時間', auto_now_add=True) # auto_now_add=True 保存的時候會保存現在時間 不管有沒有給值 之後可以在手動給值或存其他時間
    updated = models.DateTimeField('最后更改时间',auto_now=True) # auto_now=Ture 保存的時候會自動保存現在時間 之後每次存都會自動保存當前時間 不能手動給非當前時間

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),) # "id"和"slug"聯合同步查询，提高效率

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])