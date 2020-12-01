from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class SignUpForm(UserCreationForm):
    form_class = UserCreationForm

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(SignUpForm, self).form_valid(form)
