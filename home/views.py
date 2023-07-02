from django.shortcuts import render

def home_index(request):
    bio = """
    I’m a postdoctoral researcher at Colorado State University applying machine learning techniques to large datasets in high-energy neutrino physics. I develop software and infrastructure that allows complex machine learning algorithms to run at scale using GPU resources. I have experience in utilizing various machine learning frameworks in both Python and C++.\n

    I’ve also demonstrated strong communication skills through presentations at various conferences. I won a flash talk award at the XIX International Workshop on Neutrino Telescopes and received first prize in the poster contest at the 53rd annual Fermilab Users Meeting. The challenge of distilling complex information into clear, understandable language is one that I always welcome.
    """
    projects_url = "/projects/"
    publications_url = "/publications/"

    context = {
        'bio': bio,
        'projects_url': projects_url,
        'publications_url': publications_url
    }

    return render(request, "home_index.html", context)
