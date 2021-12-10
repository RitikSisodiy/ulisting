from allauth import socialaccount
from listing.models import listingCat
from allauth.socialaccount.models import SocialAccount
def allTimeFunc(request):
    res = {}
    if request.user.is_authenticated and request.user.is_superuser != True:
        res['socialdata'] = SocialAccount.objects.get(user=request.user)
    res['listingCat'] = listingCat.objects.all().order_by('name')
    return res