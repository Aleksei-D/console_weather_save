
import peewee

database_proxy = peewee.DatabaseProxy()


class WeatherBase(peewee.Model):
    date = peewee.DateTimeField()
    weather = peewee.CharField()
    temp = peewee.IntegerField()

    class Meta:
        database = database_proxy

