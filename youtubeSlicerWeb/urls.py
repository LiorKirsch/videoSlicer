from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('views',
    # Examples:
    # url(r'^$', 'youtubeSlicerWeb.views.home', name='home'),
    # url(r'^youtubeSlicerWeb/', include('youtubeSlicerWeb.foo.urls')),
    url(r'^getVideo$', 'getVideo', name='getVideo'),
    url(r'^getVideoDetails$', 'getVideoDetails', name='getVideoDetails'),
    url(r'^sliceVideo$', 'sliceVideo', name='sliceVideo'),
    url(r'^downloadVideo$', 'downloadVideo', name='downloadVideo'),
            
    url(r'^$', 'getBasic', name='getBasic'),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
