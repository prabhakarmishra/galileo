# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class AlphaAddress(models.Model):
    addressid = models.IntegerField(primary_key=True, db_column='addressId') # Field name made lowercase.
    addresstype = models.IntegerField(db_column='addressType') # Field name made lowercase.
    street1 = models.CharField(max_length=420)
    street2 = models.CharField(max_length=420)
    city = models.CharField(max_length=420)
    zipcode = models.CharField(max_length=15)
    class Meta:
        db_table = u'alpha_address'

class AlphaComment(models.Model):
    commentid = models.IntegerField(primary_key=True, db_column='commentId') # Field name made lowercase.
    itemid = models.IntegerField(db_column='itemId') # Field name made lowercase.
    userid = models.IntegerField(db_column='userId') # Field name made lowercase.
    commenttext = models.CharField(max_length=420, db_column='commentText') # Field name made lowercase.
    class Meta:
        db_table = u'alpha_comment'

class AlphaItem(models.Model):
    itemid = models.IntegerField(primary_key=True, db_column='itemId') # Field name made lowercase.
    imageref = models.CharField(max_length=300, db_column='imageRef') # Field name made lowercase.
    upc = models.CharField(max_length=135)
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=765)
    width = models.IntegerField()
    height = models.IntegerField()
    price = models.FloatField()
    categoryrank = models.IntegerField(db_column='categoryRank') # Field name made lowercase.
    tags = models.CharField(max_length=765)
    votes = models.IntegerField()
    rank = models.IntegerField()
    create_id = models.CharField(max_length=60)
    create_dt = models.DateTimeField()
    update_id = models.CharField(max_length=60)
    update_dt = models.DateTimeField()
    class Meta:
        db_table = u'alpha_item'

class AlphaOrder(models.Model):
    orderid = models.IntegerField(primary_key=True, db_column='orderId') # Field name made lowercase.
    userid = models.IntegerField(db_column='userId') # Field name made lowercase.
    comment = models.CharField(max_length=420)
    orderdate = models.DateTimeField(db_column='orderDate') # Field name made lowercase.
    status = models.CharField(max_length=3)
    fulfillmentdate = models.DateTimeField(null=True, db_column='fulfillmentDate', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'alpha_order'

class AlphaOrderitem(models.Model):
    orderitemid = models.IntegerField(primary_key=True, db_column='orderItemId') # Field name made lowercase.
    orderid = models.IntegerField(db_column='orderId') # Field name made lowercase.
    itemid = models.IntegerField(db_column='itemId') # Field name made lowercase.
    quantity = models.IntegerField()
    comment = models.CharField(max_length=420)
    class Meta:
        db_table = u'alpha_orderitem'

class AlphaOrderitemanalytics(models.Model):
    orderitemanalyticsid = models.IntegerField(primary_key=True, db_column='orderItemAnalyticsId') # Field name made lowercase.
    orderitemid = models.IntegerField(db_column='orderItemId') # Field name made lowercase.
    likesctr = models.IntegerField(db_column='likesCtr') # Field name made lowercase.
    commentsctr = models.IntegerField(db_column='commentsCtr') # Field name made lowercase.
    userid = models.IntegerField(db_column='userId') # Field name made lowercase.
    class Meta:
        db_table = u'alpha_orderitemanalytics'

class AlphaPairinganalytics(models.Model):
    pairinganalyticsid = models.IntegerField(primary_key=True, db_column='pairingAnalyticsId') # Field name made lowercase.
    pairingsid = models.IntegerField(db_column='pairingsId') # Field name made lowercase.
    likectr = models.IntegerField(db_column='likeCtr') # Field name made lowercase.
    commentctr = models.IntegerField(db_column='commentCtr') # Field name made lowercase.
    class Meta:
        db_table = u'alpha_pairinganalytics'

class AlphaPairings(models.Model):
    pairingsid = models.IntegerField(primary_key=True, db_column='pairingsId') # Field name made lowercase.
    name = models.CharField(max_length=420)
    tagline = models.CharField(max_length=420)
    servingsize = models.IntegerField(db_column='servingSize') # Field name made lowercase.
    class Meta:
        db_table = u'alpha_pairings'

class AlphaPairingsitem(models.Model):
    pairingsitemid = models.IntegerField(primary_key=True, db_column='PairingsItemId') # Field name made lowercase.
    pairingsid = models.IntegerField(db_column='pairingsId') # Field name made lowercase.
    itemid = models.IntegerField(db_column='itemId') # Field name made lowercase.
    class Meta:
        db_table = u'alpha_pairingsitem'

class AlphaStore(models.Model):
    storeid = models.IntegerField(primary_key=True, db_column='storeId') # Field name made lowercase.
    storetype = models.IntegerField(db_column='storeType') # Field name made lowercase.
    name = models.CharField(max_length=420)
    url = models.CharField(max_length=420)
    tagline = models.CharField(max_length=420)
    contactname = models.CharField(max_length=420, db_column='contactName') # Field name made lowercase.
    contactphone = models.CharField(max_length=420, db_column='contactPhone') # Field name made lowercase.
    phone = models.CharField(max_length=420)
    fax = models.CharField(max_length=420)
    latitude = models.CharField(max_length=60)
    longitude = models.CharField(max_length=60)
    street1 = models.CharField(max_length=420)
    street2 = models.CharField(max_length=420)
    city = models.CharField(max_length=420)
    zipcode = models.CharField(max_length=15)
    class Meta:
        db_table = u'alpha_store'

class AlphaUser(models.Model):
    userid = models.IntegerField(primary_key=True, db_column='userId') # Field name made lowercase.
    fname = models.CharField(max_length=90, db_column='fName') # Field name made lowercase.
    lname = models.CharField(max_length=90, db_column='lName') # Field name made lowercase.
    dob = models.DateField()
    emailid = models.CharField(unique=True, max_length=90, db_column='emailId') # Field name made lowercase.
    password = models.CharField(max_length=30)
    gender = models.CharField(max_length=18)
    tagline = models.CharField(max_length=420)
    class Meta:
        db_table = u'alpha_user'

class AlphaUseraddress(models.Model):
    useraddressid = models.IntegerField(primary_key=True, db_column='userAddressId') # Field name made lowercase.
    addressid = models.IntegerField(db_column='addressId') # Field name made lowercase.
    userid = models.IntegerField(db_column='userId') # Field name made lowercase.
    class Meta:
        db_table = u'alpha_useraddress'

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=240)
    class Meta:
        db_table = u'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        db_table = u'auth_group_permissions'

class AuthMessage(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    message = models.TextField()
    class Meta:
        db_table = u'auth_message'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    content_type = models.ForeignKey(DjangoContentType)
    codename = models.CharField(unique=True, max_length=300)
    class Meta:
        db_table = u'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(unique=True, max_length=90)
    first_name = models.CharField(max_length=90)
    last_name = models.CharField(max_length=90)
    email = models.CharField(max_length=225)
    password = models.CharField(max_length=384)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    is_superuser = models.IntegerField()
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    class Meta:
        db_table = u'auth_user'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)
    class Meta:
        db_table = u'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        db_table = u'auth_user_user_permissions'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300)
    app_label = models.CharField(unique=True, max_length=300)
    model = models.CharField(unique=True, max_length=300)
    class Meta:
        db_table = u'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(max_length=120, primary_key=True)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        db_table = u'django_session'

class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)
    domain = models.CharField(max_length=300)
    name = models.CharField(max_length=150)
    class Meta:
        db_table = u'django_site'

class PistonConsumer(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765)
    description = models.TextField()
    key = models.CharField(max_length=54)
    secret = models.CharField(max_length=96)
    status = models.CharField(max_length=48)
    user = models.ForeignKey(AuthUser, null=True, blank=True)
    class Meta:
        db_table = u'piston_consumer'

class PistonNonce(models.Model):
    id = models.IntegerField(primary_key=True)
    token_key = models.CharField(max_length=54)
    consumer_key = models.CharField(max_length=54)
    key = models.CharField(max_length=765)
    class Meta:
        db_table = u'piston_nonce'

class PistonResource(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765)
    url = models.TextField()
    is_readonly = models.IntegerField()
    class Meta:
        db_table = u'piston_resource'

class PistonToken(models.Model):
    id = models.IntegerField(primary_key=True)
    key = models.CharField(max_length=54)
    secret = models.CharField(max_length=96)
    token_type = models.IntegerField()
    timestamp = models.IntegerField()
    is_approved = models.IntegerField()
    user = models.ForeignKey(AuthUser, null=True, blank=True)
    consumer = models.ForeignKey(PistonConsumer)
    class Meta:
        db_table = u'piston_token'

