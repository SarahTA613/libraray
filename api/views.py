from django.shortcuts import render,HttpResponse,redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Books,Category
from . forms import BooksForm
# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render (request,'home.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        



    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('showBooks')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')



def ShowAllBooks(request):
    
    category = request.GET.get('category')

    if category == None:
        books = Books.objects.order_by('-title')
        page_num = request.GET.get("page")
        paginator = Paginator(books, 2)
        try:
            books = paginator.page(page_num)
        except PageNotAnInteger:
            books = paginator.page(1)
        except EmptyPage:
            books = paginator.page(paginator.num_pages)             
    else:
        books = Books.objects.filter(category__name=category)
       
    
    categories = Category.objects.all()
    
    context = {
        'books': books,
        'categories': categories
    }

    return render(request, 'showBooks.html', context)



def bookDetail(request, pk):
    eachBook = Books.objects.get(id=pk)

    

    context = {
        'eachBook': eachBook,
        
    }

    return render(request, 'bookDetail.html', context)


def addBook(request):
    form = BooksForm()

    if request.method == 'POST':
        form = BooksForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('showBooks')
    else:
        form = BooksForm()

    context = {
        "form":form
    }

    return render(request, 'addBook.html', context)

def updateBook(request,pk):
    book = Books.objects.get(id=pk)

    form = BooksForm(instance=book)

    if request.method == 'POST':
        form = BooksForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('showBooks')

    context = {
        "form":form
    }

    return render(request, 'updateBook.html', context)

def deleteBook(request, pk):
    book = Books.objects.get(id=pk)
    book.delete()
    return redirect('showBooks')    

def searchBar(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            books = Books.objects.filter(title__icontains=query) 
            return render(request, 'searchbar.html', {'books':books})
        else:
            print("No information to show")
            return render(request, 'searchbar.html', {})

