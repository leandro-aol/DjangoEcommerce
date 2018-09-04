from django.template import Library

register = Library()

@register.inclusion_tag('catalog/pagination.html')
def pagination(request, paginator, page_obj):
    
    context = {
        'request' : request,
        'paginator' : paginator,
        'page_obj' : page_obj,
    }

    getvars = request.GET.copy()
    
    if 'page' in getvars:
        del getvars['page']

    if len(getvars) > 0:
        context['getvars'] = '&{}'.format(getvars.urlencode())
    else:
        context['getvars'] = ''

    return context