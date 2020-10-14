from django.forms import ModelForm
from .models import Comment


class FormComment(ModelForm):
    def clean(self):
        data = self.cleaned_data
        name = data.get('comment_name')
        email = data.get('comment_email')
        content = data.get('comment_content')

        if len(name) < 5:
            self.add_error(
                'comment_name',
                'Nome precisa ter mais que 5 Caracteres'
            )
        if not content:
            self.add_error(
                'comment_content',
                'Comentário não pode ser vazio.'
            )

    class Meta:
        model = Comment
        fields = ('comment_name', 'comment_email', 'comment_content')
