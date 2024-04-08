from django.contrib.sitemaps import Sitemap
from .models import TempUser, Car

class TempUserSitemap(Sitemap):
    changefrq = 'daily'
    priority = 0.6
    protocol = 'http'

    def items(self):
        return TempUser.objects.all()

    def lastmod(self, obj):
        return obj.added_date
    
    def location(self, obj):
        return '/base/%s' % (obj.user_agent)
    
class CarSitemap(Sitemap):
    changefrq = 'daily'
    priority = 0.6
    protocol = 'http'

    def items(self):
        return Car.objects.all()
    
    def location(self, obj):
        return '/base/%s' % (obj.price)
