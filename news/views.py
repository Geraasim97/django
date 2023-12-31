from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from news.forms import ArticleForm
from news.models import Article
from pytils.translit import slugify

from django.core.mail import send_mail
from django.conf import settings


class ArticleCreateView(CreateView):
    """Контроллер создания статьи"""
    model = Article
    form_class = ArticleForm
    success_url = reverse_lazy('news:list')

    def form_valid(self, form):  # динамическое формирование slug name для заголовка при создании статьи
        if form.is_valid():
            new_article = form.save()
            new_article.slug = slugify(new_article.title)[:20]
            new_article.save()

        return super().form_valid(form)


class ArticleListView(ListView):
    """Контроллер просмотра списка статей"""
    model = Article
    paginate_by = 3  # количество элементов на одну страницу

    def get_queryset(self, *args, **kwargs):  # ограничение на вывод статей (только опубликованные)
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class ArticleDetailView(DetailView):
    """Контроллер просмотра отдельной статьи"""
    model = Article

    def get_object(self, queryset=None):  # добавление счетчика просмотров
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        if self.object.views_count == 100:  # отправка email при 100 просмотрах
            send_mail(
                subject="Django: новое достижение",
                message=f'Поздравляем! Ваша статья "{self.object.title}" набрала 100 просмотров',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=settings.EMAIL_RECEPIENT_LIST
            )
        return self.object


class ArticleUpdateView(UpdateView):
    """Контроллер редактирования статьи"""
    model = Article
    form_class = ArticleForm

    def form_valid(self, form):  # динамическое изменение slug name для заголовка при редактировании статьи
        if form.is_valid():
            new_article = form.save()
            new_article.slug = slugify(new_article.title)[:20]
            new_article.save()

        return super().form_valid(form)

    def get_success_url(self):  # после редактирования перенаправление на просмотр статьи
        return reverse("news:view", kwargs={"slug": self.object.slug})


class ArticleDeleteView(DeleteView):
    """Контроллер удаления статьи"""
    model = Article
    success_url = reverse_lazy('news:list')