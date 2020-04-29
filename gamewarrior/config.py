from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def pagination(request, data, num=10):
    paginator = Paginator(data, num)
    pages = request.GET.get('page')
    try:
        blogs = paginator.page(pages)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)

    index = blogs.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 9 if index >=9 else 0
    end_index = index + 9 if index <= max_index - 9 else max_index
    page_range = paginator.page_range[start_index:end_index]

    return blogs, page_range