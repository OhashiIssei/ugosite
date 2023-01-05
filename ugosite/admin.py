from django.contrib import admin


from .models import Category, Article, Problem, Term

class TermAdmin(admin.ModelAdmin):
    list_display = ('name','hurigana')

admin.site.register(Term, TermAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent','created_date', 'type')
    # inlines = [ProblemsInline]

admin.site.register(Article, ArticleAdmin)



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name' ,'parent','created_date','type')
    # inlines = [ProblemsInline]

admin.site.register(Category, CategoryAdmin)



from youtube.models import VideoOnApp,VideoType,VideoSearch

class VideoOnAppAdmin(admin.ModelAdmin):
    list_display = ('title','source','video_type','video_genre','problem','point')
    # inlines = [ProblemsInline]

admin.site.register(VideoOnApp, VideoOnAppAdmin)

class VideoTypeAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    # inlines = [ProblemsInline]

admin.site.register(VideoType,VideoTypeAdmin)

class VideoSearchAdmin(admin.ModelAdmin):
    list_display = ('id','keyword','display_video_types')
    # inlines = [ProblemsInline]

admin.site.register(VideoSearch, VideoSearchAdmin)

