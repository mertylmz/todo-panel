from post.models import Personel

def listItem(request):
    personels = Personel.objects.all()
    return dict(personels=personels)
