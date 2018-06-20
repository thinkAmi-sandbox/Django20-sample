from django.db import models


class NullBlank(models.Model):
    charNull = models.CharField(max_length=10, null=True)
    charBlank = models.CharField(max_length=10, blank=True)
    charNullBlank = models.CharField(max_length=10, null=True, blank=True)
    charBlankUnique = models.CharField(
        max_length=10, blank=True, unique=True,
    )
    charNullBlankUnique = models.CharField(
        max_length=10, null=True, blank=True, unique=True,
    )

    intNull = models.IntegerField(null=True)
    intBlank = models.IntegerField(blank=True)
    intNullBlank = models.IntegerField(null=True, blank=True)

    dateNull = models.DateTimeField(null=True)
    dateBlank = models.DateTimeField(blank=True)
    dateNullBlank = models.DateTimeField(null=True, blank=True)

    # BooleanFieldでは、 null=True にはできない
    # マイグレーション作成時に、以下のエラーが出る
    # nullblank.NullBlank.boolNull: (fields.E110) BooleanFields do not accept null values.
    #   HINT: Use a NullBooleanField instead.
    # nullblank.NullBlank.boolNullBlank: (fields.E110) BooleanFields do not accept null values.
    #   HINT: Use a NullBooleanField instead.
    # boolNull = models.BooleanField(null=True)
    # boolNullBlank = models.BooleanField(null=True, blank=True)
    boolBlank = models.BooleanField(blank=True)

    # null=Trueにする場合は、こちら
    nullboolNull = models.NullBooleanField(null=True)
    nullboolBlank = models.NullBooleanField(blank=True)
    nullboolNullBlank = models.NullBooleanField(null=True, blank=True)
