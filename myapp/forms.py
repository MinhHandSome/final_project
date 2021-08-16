from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm, fields, widgets, Form
from .models import Director, Film,Genres
from django.contrib.auth.models import User
from myapp import models

class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = "__all__"
        widgets={
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'image_url' : forms.TextInput(attrs={'class':'form-control'}),
            'director' : forms.Select(attrs={'class':'form-control'}),
            'genres' : forms.Select(attrs={'class':'form-control'}),
            'runtime' : forms.TextInput(attrs={'class':'form-control'}),
            'rated' : forms.TextInput(attrs={'class':'form-control'}),
            'actor' : forms.TextInput(attrs={'class':'form-control'}),
            'content' : forms.Textarea(attrs={'class':'form-control'}),
            'video_url':forms.TextInput(attrs={'class':'form-control'}),
            
        }
        #Thuộc tính  'fields' quan trọng,mình muốn cái property/ thuộc tính của class được hiển thị HTML
        #Lấy tất cả thuộc tính : fields="__all__"
    #Validation client/brower: Kiểm tra đưuọc bắt buộc phải nhập tên, họ và email. email phải đúng format
    
    # #Mình muốn validate ở phía server thì viết form vvaf muốn validate field nào thì tạo hàm tên ' clean_<field>'
#     def clean_email(self): #Validation cho thuộc tính email của Reporter 
#         input_email = self.cleaned_data['email']
        # try:    
        #     Reporter.objects.get(email=input_email) # lấy Report theo email
        # except Reporter.DoesNotExist:
        #     #Report lấy không được 
        #     #Chứng tỏ input_email này chưa có trong database
        #     return input_email
        # #input_email đã tồn tại trong database 
        # #raise error cho client biết 
        # raise ValidationError(f"{input_email} đã tồn tại vui lòng chọn email khác")

class DirectorForm(ModelForm):
    class Meta:
        model = Director
        fields = "__all__"
        widgets={
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'age' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
        }
    def clean_email(self):
        input_email= self.cleaned_data['email']
        try:
            Director.objects.get(email=input_email)
        except Director.DoesNotExist :
            return input_email
        raise ValidationError(f"{input_email} đã tồn tại vui lòng chọn email khác")
class GenresForm(ModelForm):
    class Meta:
        model = Genres
        fields = "__all__"
        widgets={
            'name' : forms.TextInput(attrs={'class':'form-control'}),
        }   
    def clean_name(self):
        input_name= self.cleaned_data['name']
        try:
            Director.objects.get(name=input_name)
        except Director.DoesNotExist :
            return input_name
        raise ValidationError(f"{input_name} đã tồn tại vui lòng chọn tên khác")    


class RegisterForm(Form):
    username = forms.CharField(
        label="Tên Đăng Nhập",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'id':'username'
            }
        )
    )
    password = forms.CharField(
        label="Mật Khẩu",
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'id':'password'
            }
        )
    )
    confirm_password = forms.CharField(
        label="Nhập Lại Mật Khẩu",
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'id':'confirm_password'
            }
        )
    )
    first_name=forms.CharField(
        label="Tên",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'id':'first_name'
            }
        )
    )
    last_name = forms.CharField(
        label="Họ",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'id':'last_name'
            }
        )
        )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'id':'email'
            }
        )
    
    )

    def clean_username(self):
        inputed_username=self.cleaned_data['username']
        try:
            User.objects.get(username=inputed_username)
            raise ValidationError(f"Tên đăng nhập '{inputed_username}' đã tồn tại vui lòng chọn tên đăng nhập khác ")
        except User.DoesNotExist:
            return inputed_username

    def clean_email(self):
        inputed_email=self.cleaned_data['email']
        try:
            User.objects.get(email=inputed_email)
            raise ValidationError(f"Email '{inputed_email}' đã tồn tại vui lòng chọn Email khác ")
        except User.DoesNotExist:
            return inputed_email

    def clean_confirm_password(self):
        inputed_password= self.cleaned_data["password"]
        inputed_confirm_password= self.cleaned_data["confirm_password"]
        if inputed_password!=inputed_confirm_password:
            raise ValidationError(f"Mật khẩu không khớp nhau")
        return inputed_confirm_password

    def save_user(self):
        User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            email=self.cleaned_data['email'],
        )
class LoginForm(Form):
    username = forms.CharField(
        label="Tên Đăng Nhập",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'id':'username'
            }
        )
    )
    password = forms.CharField(
        label="Mật Khẩu",
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'id':'password'
            }
        )
    )
    # remember = forms.CheckboxInput()