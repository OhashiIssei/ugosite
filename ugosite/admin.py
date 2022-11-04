from django.contrib import admin


from .models import Genre, Article, Problem, Term, Module, Problem ,Note,Folder

class GenreAdmin(admin.ModelAdmin):
    list_display = ('name','display_ancestors','depth','type',"videos_num","slug")#,'description'

admin.site.register(Genre,GenreAdmin)

class TermAdmin(admin.ModelAdmin):
    list_display = ('name', 'hurigana', "en_name", 'videos_num', "slug")
    prepopulated_fields = {"slug": ("en_name",)}

admin.site.register(Term, TermAdmin)


from .models import Video, Playlist

class VideosInline(admin.TabularInline):
    model = Video
class VideoAdmin(admin.ModelAdmin):
    list_display = ('name','display_problem','slug',"table","display_genre")
    # inlines = ["ProblemsInline"]
admin.site.register(Video,VideoAdmin),


class PlaylistInline(admin.TabularInline):
    model = Playlist

class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('name','title','type','display_genre','videos_num')
admin.site.register(Playlist,PlaylistAdmin)


class ProblemsInline(admin.TabularInline):
    model = Problem

class ProblemAdmin(admin.ModelAdmin):
    list_display = ('name','text', 'source',"display_genre",'slug')
    # inlines = [VideosInline]
admin.site.register(Problem,ProblemAdmin)



class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_date', 'display_module', 'slug')
    # inlines = [ProblemsInline]

admin.site.register(Article, ArticleAdmin)



class ModuleAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_description', 'articles_num', 'slug')
    # inlines = [ProblemsInline]

admin.site.register(Module, ModuleAdmin)


class NoteAdmin(admin.ModelAdmin):
    list_display = ('name', 'path' ,"id")
    # inlines = [ProblemsInline]

admin.site.register(Note,NoteAdmin)



class FolderAdmin(admin.ModelAdmin):
    list_display = ('name', 'path' ,"id")
    # inlines = [ProblemsInline]

admin.site.register(Folder, FolderAdmin)




