"""

 Самое Важное!!!
 Всегда ДУМАТЬ! перед тем, как что-либо сделать, необходимо всё тщательно обдумать

 Радоваться Жизни  Радоваться разным мелочам

 Ценить:         Ценить то что есть и стремиться к лучшему, Ценить сегодняшний день и брать МАКСИМУМ
 Быть проще:     Ко всему относиться Проще и Спокойнее без Волнения
 Слушать Других: Прислушиваться к мнению других людей они могут быть правы  И делать выводы
 Время:          Тайм-менеджмент   Грамотное распределение времени, Контроль Времени, Правильно раставлять Приоритеты
 Уверенность:    Быть уверенным в себе НО Оценивать свои силы!
 Развития:       Развиваться, Учиться, учиться и ещё раз - учиться, Саморазвитие
 Не Надеяться:   Надеяться только на себя
 Контроль:       Быть менее Эмоциональным, Совладать с Эмоциями, Контролировать свои эмоции в любой ситуации
 Внимательность: Быть Внимательным
 Спокойствие:    Быть Спокойнее, Перестать Нервничать , Быть Расслабленным, Не Злиться на себя и на других
 Режим:          Правильный Сон, Пить Воду
 Зарядка:        Бег, Тренировки, Стойка на Голове
 Тельце в тепле: НЕ переохлаждаться

 Молчание золото:  Лучше промолчать, чем сказать и потом жалеть о том, что сказал
 Соломон:          Все пройдёт, и это тоже пройдёт
 Вообще это замечательный подход: осознать, что проблема не такая уж и проблема, и вполне решаема.
 Кто ищет-тот всегда найдет!
 Искать Другие способы
 Не спеши, а то успеешь...   Успеешь, но не туда куда хотел...
 Подумай, нужно ли тебе ЭТО и для Чего
 Надо принимать вещи такими, как они есть, и пользоваться ими с наибольшей для себя выгодой.
 Если научиться принимать вещи как они есть, страдание исчезнет.
________________________________________________________________________________________________________________________


 Django использует метаклассы для создания моделей базы данных

 Django во многом работает через метаклассы.
 Поэтому когда Django конструирует ваш класс, она делает это с помощью своего метакласса.
 Чтобы при конструировании ей знать какие-то параметры вашего класса, ну, например модель или поля в вашем случае,
 она ищет в вашем классе класс с названием Meta.

 папка migrations: предназначена для хранения миграций - скриптов,
 которые позволяют синхронизировать структуру базы данных с определением моделей

 __init__.py: указывает интерпретатору python, что текущий каталог будет рассматриваться в качестве пакета

 admin.py: предназначен для административных функций, в частности, здесь производится регистрация моделей,
  которые используются в интерфейсе администратора

 apps.py: определяет конфигурацию приложения

 models.py: хранит определение моделей, которые описывают используемые в приложении данные

 tests.py: хранит тесты приложения

 views.py: определяет функции, Классы которые получают запросы пользователей, обрабатывают их и возвращают ответ
  manage.py

  manage.py используется для создания приложений, работы с базами данных и для запуска отладочного сервера

  Все команды:    manage.py --help
  manage.py collectstatic -   Проверка статики
  manage.py makemigrations - Проверка миграции
  manage.py migrate - Применить миграции
  manage.py startproject - Создание проекта
  manage.py startapp - Создание приложения
  manage.py runserver - Запуск сервера для разработки
  manage.py createsuperuser - Создать аккаунт администратора


  asgi.py - нужен для асинхронных веб-серверов и приложений
  ASGI является духовным наследником WSGI, давнего стандарта Python для совместимости между веб-серверами, фреймворками и приложениями.

  wsgi.py - нужен для синхронных веб-серверов и приложений
  WSGI удалось предоставить гораздо больше свободы и инноваций в веб-пространстве Python,
  и цель ASGI - продолжить эту работу асинхронным Python.

  wsgi.py, который будет отвечать за обработку веб-сервером запросов к Django

  urls.py - главный файл для наших URL проектов куда мы подключаем URL наших приложений
  path('password-change/done/', PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'), name='password_change_done'),
  name - имя маршрута, для использования в html

 --- settings.py ---
  settings.py - файл со всеми настройками проекта

  BASE_DIR - построение пути к корню нашего проекта

  DEBUG - включает отключает режим отладки проекта
  DEBUG = True - Django будет отображать подробные страницы с ошибками при выбрасывании исключений приложений
  DEBUG = False - Если разворачиваем на боевом сервере устанавливаем настройку False
  никогда не публикуем проект с DEBUG = True, так как пользователю станут доступны секретные данные конфигурации приложения

  ALLOWED_HOSTS = [] - не используется при включенной отладке и запуске тестов но как только мы развернем приложение
  и установим DEBUG = False необходимо добавить домен сайта в эту настройку для того чтобы Django мог с ним работать

  INSTALLED_APPS = [] - настройка которая указывает Django какие приложения активны в нашем проекте
  по умолчанию Django подключает следующие приложения:

  INSTALLED_APPS = [
    'django.contrib.admin',         - Администрирование
    'django.contrib.auth',          - Подсистема  аутификации
    'django.contrib.contenttypes',  - Подсистема  для работы с типами обьектов
    'django.contrib.sessions',      - Подсистема  сессий
    'django.contrib.messages',      - Подсистема  сообщений
    'django.contrib.staticfiles',   - Подсистема  для управления статическим содержимым сайта
 --- End settings.py ---

 MIDDLEWARE = [] - список подлюченных промежуточных слоёв
 MIDDLEWARE - это промежуточный слой между запросом и ответом в Django
 Django Middleware - это механизм обработки запросов и ответов в Django
 Каждый компонент промежуточного программного обеспечения(СЛОЯ) отвечает за выполнение определенной функции
 Middleware может поддерживать любую комбинацию синхронных и асинхронных запросов
 Основные MIDDLEWARE:
 SessionMiddleware – поддержка сессий. Добавляет в запрос объект session
 CsrfViewMiddleware – проверяет, что POST-запросы отправлены с текущего домена
 AuthenticationMiddleware – авторизует пользователя. Добавляет в запрос поле user
 MessageMiddleware – передает пользователю короткие сообщения

 ROOT_URLCONF - указывает на Python модуль который содержит корневые шаблоны urls.py

 DATABASES - словарь содержащий настройки для всех баз данных проекта

 LANGUAGE_CODE = 'ru-ru' - Определяет код языка для Django сайта

 USE_TZ = True - указывает Django необходимость поддержки временных зон

 select_related(key) - 'ЖАДНАЯ' загрузка связанных данных по внешнему ключу key, который имеет тип ForeignKey, OneToOneField
 уменьшение количество запросов к базе данных

 'ЖАДНАЯ' загрузка - загрузка сразу всех данных
 'ЛЕНИВАЯ' загрузка - происходит в момент обращения к тому или иному атрибуту

 prefetch_related(key) - 'ЖАДНАЯ' загрузка связанных данных по внешнему ключу key, который имеет тип ManyToManyField
 уменьшение количество запросов к базе данных

 request - обьект запроса
 response - ответ
 redirect - перенаправление

 URL обозначает Uniform Resource Locator. URL это лишь адрес, который выдан уникальному ресурсу в интернете.
  В теории, каждый корректный URL ведёт на уникальный ресурс

 Каждый URL может быть напечатан напрямую в адресной строке браузера, чтобы сразу получить запрошенный ресурс

 если с Формы нужно передать ФАЙЛЫ нужно указать атрибут - enctype="multipart/form-data"

 Slug — это короткая метка, которая содержит только буквы, цифры, подчеркивания или дефисы. Обычно они используются в URL.

 --- Slug ---
 prepopulated_fields = {'slug': ('title',)} # Автозаполнение полей прописывается в Admin.py

 CSRF токен — это случайное значение, генерируемое веб-приложением и связываемое с текущей сессией пользователя
 CSRF токен - нужен для защиты межсайтовых атак
 Django требует CSRF токен при всех POST - запросах

 Django Debug Toolbar - Помогает оптимизировать проект

 Виртуальное окружение(venv) (virtual environment) - позволяет создавать изолированные среды для каждого проекта,
 в которых можно устанавливать и управлять зависимостями и пакетами, не вмешиваясь в другие проекты или системные установки Python.

 Postman – это программа, которая предоставляет вам все необходимые инструменты для тестирования API:
 возможность посылать запросы, писать документацию к API, запускать автотесты, составлять иерархию тестов,
 проводить версионирование и так далее.

 OpenAPI - это спецификация для описания API.

 Swagger использует спецификацию OpenAPI для описания и документирования API, а инструменты Swagger позволяют
 использовать эту спецификацию для создания и тестирования API, а также для генерации клиентского кода.

 Swagger простыми словами — инструмент для подготовки документации к API и проведения тестов API(Публичный интерфейс).

 ОСНОВНОЕ ОТЛИЧИЕ между Swagger и Postman заключается в том, что Swagger сконцентрирован на проектировании
 и документировании API, в то время как Postman — на тестировании и создании запросов.

 SQL-инъекция (SQLi) - это уязвимость веб-безопасности, которая позволяет злоумышленнику вмешиваться в запросы,
 которое приложение делает к своей базе данных. Как правило, это позволяет просматривать данные,
 которые он обычно не может получить

 --- HTTP ---
 HTTP сообщения - это обмен данными между сервером и клиентом
 Http запрос, Http ответ между Клиентом и Сервером

 СТАТУСЫ HTTP запросов:

 100-199: ИНФОРМАЦИОННЫЕ ответы.
 200-299: УСПЕШНАЯ обработка запроса.
 300-399: ПЕРЕНАПРАВЛЕНИЕ запроса.
 400-499: ОШИБКИ КЛИЕНТА.
 500-599: ОШИБКИ СЕРВЕРА.

 МЕТОДЫ HTTP запросов:

 Метод запроса является идемпотентным , если его можно успешно обработать несколько раз, не изменив результат.
 Метод запроса кэшируется , если соответствующий ответ может храниться для повторного использования.
 Метод запроса считается безопасным, если он не изменяет состояние ресурса

 Кэш — это память программы или устройства, которая сохраняет временные или часто используемые файлы для быстрого
 доступа к ним. Это увеличивает скорость работы приложений и операционной системы. Процесс сохранения таких файлов
 в специальном месте называется кэшированием.

 БЕЗОПАСНЫЕ (GET, HEAD, OPTIONS) — не изменяют данные, их можно выполнять в любой последовательности
 Безопасные методы - это методы, которые не изменяют состояние в базе данных (read only методы).
 Примечательно, что все безопасные методы также являются идемпотентными. Безопасными методами являются: GET, HEAD и OPTIONS.

 Отличие идемпотентных методов от безопасных заключается в том, что безопасные методы не меняют состояние базы данных,
 в то время как идемпотентные методы могут внести изменения при первом запросе,
 но последующие идентичные запросы уже не будут менять состояние в базе данных.

 Несколько следующих методов HTTP безопасные: GET, HEAD или OPTIONS.
 Все безопасные методы являются также идемпотентными, как и некоторые другие, но при этом небезопасные, такие как PUT или DELETE.

 ИДЕМПОТЕНТНЫЕ (GET, HEAD, PUT, DELETE, OPTIONS, TRACE) — при повторном выполнении результаты будут ожидаемо одинаковыми
 Идемпотентные методы - это методы, которые либо не изменяют состояние в базе данных,
 либо изменяют состояние только при первом запросе. В случае повторной отправки идентичного запроса,
 состояние в базе данных не изменяется. Идемпотентными методами являются: GET, PUT, DELETE, HEAD и OPTIONS.

 Метод HTTP является идемпотентным, если повторный идентичный запрос, сделанный один или несколько раз подряд,
 имеет один и тот же эффект, не изменяющий состояние сервера. Другими словами, идемпотентный метод не должен иметь
 никаких побочных эффектов (side-effects), кроме сбора статистики или подобных операций.

 НЕИДЕМПОТЕНТНЫЕ (POST, PATCH) — при повторном выполнении результаты будут разными, если, например,
 отправить POST-запрос на создание элемента несколько раз подряд, то он может создать несколько элементов с одинаковыми данными

 GET – получить объект или список объектов
 POST – создать объект
 PUT – обновить существующий объект
 PATCH – частично обновить существующий объект
 DELETE – удалить объект
 HEAD – получить метаданные объекта

 Метаданные — это субканальная информация об используемых данных.     информация о другой информации
 Метаданные — информация о другой информации, или данные, относящиеся к дополнительной информации о содержимом или объекте.
 субканальная информация -  (данные о данных)
 Какие бывают метаданные:
 - Структурные:
 Они содержат информацию о том, как именно хранятся какие-либо данные. Структурные метаданные можно легко обнаружить,
 просто взглянув на тот или иной файл. Так, для телефонного разговора эти данные будут содержат
 длительность и время беседы; для цифровой фотографии ─ размер и формат файла.

 - Описательные:
 Описательные. Это разнообразная дополнительная информация, которая упрощает изучение содержимого книг и файлов.
 Если речь идёт о книге, то описательные метаданные сообщат нам её название, автора, издание, краткую аннотацию и номер ISBN.

 Примеры метаданных:  Email, Телефон, Социальные сети, Веб-страницы, Цифровые медиа-библиотеки - аккаунты.


 Метод GET - используется для получения информации о ресурсе.
 Метод GET - запрашивает представление ресурса. Запросы с использованием этого метода могут только извлекать данные
 Метод HEAD - запрашивает ресурс так же, как и метод GET, но без тела ответа.
 Метод POST - предназначен для создания новых ресурсов и передачи данных
 Метод POST - используется для отправки сущностей к определённому ресурсу.
 Часто вызывает изменение состояния или какие-то побочные эффекты на сервере.
 Метод PUT - обновляет ресурс полностью
 Метод PUT - заменяет все текущие представления ресурса данными запроса.
 Метод PATCH - вносит частичные изменения в существующем ресурсе
 Метод PATCH - используется для частичного изменения ресурса
 Метод DELETE - для удаления ресурса, который указывается с помощью его URI
 Метод CONNECT - устанавливает "туннель" к серверу, определённому по ресурсу
 Метод OPTIONS - используется для описания параметров соединения с ресурсом
 Метод TRACE - выполняет вызов возвращаемого тестового сообщения с ресурса
 Метод TRACE - выполняет проверку обратной связи по пути к целевому ресурсу, предоставляя полезный механизм отладки.

 Фреймворк Django реализует АРХИТЕКТУРНЫЙ паттерн Model-View-Template или сокращенно MVT,
 который по факту является модификацией распростаненного в веб-программировании паттерна MVC (Model-View-Controller).

 Model View Template(MVT) (MVT – модель, представление и шаблон) - АРХИТЕКТУРНЫЙ ПАТТЕРН

 Основные элементы паттерна:
 URL dispatcher: при получение запроса на основании запрошенного адреса URL определяет, какой ресурс должен обрабатывать данный запрос

 View: получает запрос, обрабатывает его и отправляет в ответ пользователю некоторый ответ.
 Если для обработки запроса необходимо обращение к модели и базе данных, то View взаимодействует с ними.
 Для создания ответа может применять Template или шаблоны. В архитектуре MVC этому компоненту соответствуют контроллеры (но не представления).

 Model: описывает данные, используемые в приложении. Отдельные классы, как правило, соответствуют таблицам в базе данных.

 Template: представляет логику представления в виде сгенерированной разметки html.
 В MVC этому компоненту соответствует View, то есть представления.

 QuerySet, по сути, — список объектов заданной модели. QuerySet позволяет читать данные из базы данных,
 фильтровать и изменять их порядок

 ORM (Object-Relation Mapping) – общее название для фреймворков или библиотек,
 позволяющих автоматически связать базу данных с кодом

 Запросы в Django ORM ЛЕНИВЫЕ и они не отправляются до тех пор,
 пока их не запустят (в англоязычных текстах это называют evaluate)

 CRUD - Create(создание), Read(чтение), Update(обновление), Delete(удаление)


 __Class__ = имя класса в модели
 __Class__.objects.all()
 __Class__.objects.create(title='')
 __Class__.objects.filter(title='Best')
 __Class__.objects.filter(pk__gte=2) # __gt, __lt, __lte, __contains   <--- Lookup
 __Class__.objects.get(id=1) # получить строго одну запись
 __Class__.objects.order_by("blog__name") # сортировка по выбранному полю
 __Class__.objects.order_by("-blog__name") # обратная сортировка
 __Class__.objects.order_by("blog__name").desc()) # обратная сортировка
 __Class__.objects.filter(pk__lte=4).update('') # update - применяется к QuerySet, не работает с одной записью
 __Class__.objects.filter(cat_id=1).count() # количество записей
 __Class__.objects.get(pk=3).posts.exists() # существуют записи или нет # posts = 'название модели'_set



 ORM-команды ForeignKey   many-to-one
 RelatedManager
 <вторичная модель>_set.all() # получить всё связанное с категорией
 __Class__.women_set.all()
 cat = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='posts') # related_name
 __Class__.posts.all() # related_name='posts'
 __Class__.objects.filter(cat__slug='aktrisy') # cat = models.ForeignKey(Category, on_delete=models.PROTECT)


 Фреймворк Djnago имеет три специальных класса для организации связей:

 ForeignKey – для связей Many to One (Один ко многим) (поля отношений)
 ManyToManyField – для связей Many to Many (Многие ко многим)
 OneToOneField – для связей One to One (Один к одному)

 cat = models.ForeignKey('Category', on_delete=models.PROTECT) # функция(PROTECT) не удаляет все связанные записи с Category
 cat = models.ForeignKey('Category', on_delete=models.CASCADE) # функция(CASCADE) удаляет все связанные записи с Category

 ManyToManyField - связь с помощью промежуточной таблицы
 tag = models.ManyToManyField('TagPost', blank=True, related_name='tags')

 OneToOneField - один к одному
 husband = models.OneToOneField('Husband', on_delete=models.SET_NULL,
                                   null=True, blank=True, related_name='wuman')

 django-taggit - уже реализованный функционал,  можно без труда добавлять теги к моделям. Вывод тегов в шаблон

 QuerySet: QuerySet Method reference # Documentation

 Class Q   -  and, or, not
 Q() objects
 Приоритеты:
 1) самый низкий OR:  |
 2) средний AND: &
 3) самый высокий NOT: ~

 from django.db.models import Q
 Women.objects.filter(Q(pk__lt=5) | Q(cat_id=2)) # | == OR  # |  = Вертикальная черта
 Women.objects.filter(Q(pk__lt=5) & Q(cat_id=2)) # & == AND # & = Амперсанд
 Women.objects.filter(~Q(pk__lt=5) & Q(cat_id=2)) # ~ == NOT # ~ = Тильда
 Women.objects.filter(~Q(pk__in=[1,2,5]) | Q(cat_id=2), title__icontains='pa')


 Women.objects.order_by('pk') # сортировка
 Women.objects.order_by('-pk') # обратная сортировка

 Class F
 from django.db.models import F
 Women.objects.filter(pk__gt=F('cat_id'))
 Объект F() представляет значение поля модели, преобразованное значение поля модели или аннотированный столбец.
 Он позволяет ссылаться на значения полей модели и выполнять операции с базой данных, используя их без необходимости
 извлекать их из базы данных в память Python

 Class Value
 from django.db.models import Value
 Объект Value() представляет наименьший возможный компонент выражения: простое значение. Когда вам нужно представить
 значение целого числа, булевой или строки в выражении, вы можете обернуть это значение в объект Value()

 annotate() - метод позволяет создавать новые вычисляемые поля для нашей выборки
 lst = Husband.objects.all().annotate(is_married=Value(True))

 Агрегирующие функции: Count, Sum, Avg, Max, Min. Метод values()
 from django.db.models import Count, Sum, Avg, Max, Min

 Husband.objects.aggregate(Min('age'), Max('age'))
 Husband.objects.aggregate(res = Min('age') -  Max('age')) # если res нет TypeError: Complex aggregates require an alias
 Women.objects.filter(pk__gt=2).aggregate(res = Count('cat_id'))
 Women.objects.values('title', 'cat_id')

 Database Functions on documentations
 from django.db.models.functions import Length

 Django Debug Toolbar — это мощный инструмент для отладки Django-кода.
 Он предоставляет подробную информацию о процессе выполнения запросов, использовании базы данных,
 настройках и многих других аспектах работы Django

 --- Adminka ---
 Можно решать все типовые задачи:
 создание пользователя с разными полномочиями
 отображение всех наших приложений
 добавление/изменения/удаление записи

 @admin.register(Women)
 class WomenAdmin(admin.ModelAdmin):
 list_display = ('id', 'title', 'time_create', 'is_published')

 --- CBV  -  Class-Based Views ---
 CBV могут наследоваться от множества классов и миксинов,
 но все CBV берут начало от класса View.
 Функции/Классы пишутся в файле views.py

 Базовые виды  base.generic : View, TemplateView, RedirectView
 Общие виды отображения - generic: DetailView, ListView
 Общие представления редактирования - generic: FormView, CreateView, UpdateView, DeleteView

 --- View ---
 View - базовый класс представлений
 Базовый класс представления. Все остальные представления на основе классов наследуются от этого базового класса
 from django.views import View

 __Class__.as_view() нужно прописать в urls.py приложения
 __Class__.as_view(template_name='users/password_change_done.html') # template_name=указать шаблон html

 extra_context - только для статических данных

 get_context_data - если нужно обрабатывать еще и динамические данные

 --- TemplateView ---
 TemplateView - он служит для обработки шаблонов и отправки результата пользователю
 Отображает заданный шаблон с контекстом, содержащим параметры, зафиксированные в URL-адресе.
 from django.views.generic import TemplateView
 template_name = 'women/index.html' # служит для указания шаблона(html)
 get_context_data - возвращает контекст для использования в шаблоне
 def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    return context

 DetailView, ListView представления на основе классов предназначены для отображения данных.
 Во многих проектах они обычно являются наиболее часто используемыми представлениями.

 --- ListView ---
 ListView - Страница, представляющая список объектов
 from django.views.generic import ListView
 model = для выбора модели
 для templates формирует перменную object_list
 template_name - 'women/index.html' # служит для указания шаблона(html)
 по умолчанию шаблон ищется:
 имя приложения / имя модели _list.html
 'women/women_list.html'
 context_object_name = 'posts' # для изменения   object_list
 def get_queryset(self): - то что будет отображатся в качестве списка
    Women.objects.all().select_related('cat')
 allow_empty = False - при пустом списке будет генерироватся исключение 404

 --- DetailView ---
 from django.views.generic import DetailView
 Во время выполнения этого представления self.object будет содержать объект, над которым работает представление.
 Базовое представление для отображения одного объекта.
 Оно не предназначено для непосредственного использования, а скорее как родительский класс
 для templates формирует перменную object
 по умолчанию шаблон ищется:
 имя приложения / имя модели_detail.html
 'women/women_detail.html'
 model = для выбора модели
 slug_url_kwarg - если ищем по слагу
 pk_url_kwarg - если ищем по id  pk - primary key (первичный ключ)

 --- FormView ---
 from django.views.generic.edit import FormView # можно импортировать так
 from django.views.generic import FormView # можно импортировать так тоже

 Класс для автоматизации отображения и обработки html-форм
 Представление, отображающее форму. В случае ошибки повторно отображает форму с ошибками проверки;
  в случае успеха перенаправляется на новый URL

 Базовое представление для отображения формы. Он не предназначен для прямого использования,
 а скорее как родительский класс для того django.views.generic.edit.FormView или иного представления, отображающего форму

 form_class = AddPostForm (ссылка на сам класс без вызова () ) # ссылается на класс Формы form.py
 success_url = reverse_lazy('home') # определяет на какой URL адрес мы должны перенаправится после успешной отправки формы

 reverse_lazy - маршрут выстраивается не сразу а лишь в момент когда он необходим

 def form_valid(self, form): # для сохранения новой записи в БД
    form.save()
    return super().form_valid(form)

 в шаблон форма будет передаватся через переменую    form

 --- CreateView ---
 Служит для добавления новых записей в БД через форму

 from django.views.generic.edit import CreateView # можно импортировать так
 from django.views.generic import CreateView # можно импортировать так тоже

 Представление, отображающее форму для создания объекта,
 повторное отображение формы с ошибками проверки (если они есть) и сохранение объекта.

 При использовании CreateView у вас есть доступ к self.object создаваемому объекту.
 Если объект еще не создан, значение будет None.

 Метод уже реализован в CreateView
 def form_valid(self, form): # для сохранения новой записи в БД
    form.save()
    return super().form_valid(form)

 success_url = reverse_lazy('home')  если убрать то перенаправление будет через:
     def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

 get_absolute_url - Абсолютный путь URL

 который определен в модели, форма связана с моделью
 1) вариант
 class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'women/about.html'
    success_url = reverse_lazy('home')
    extra_context = {}

 2) вариант
 class AddPage(CreateView):
    model = Women
    fields = '__all__'
    template_name = 'women/about.html'
    extra_context = {}


 --- UpdateView ---
 Служит для изменения существующих записей в БД через форму

 from django.views.generic.edit import UpdateView # можно импортировать так
 from django.views.generic import UpdateView # можно импортировать так тоже

 При использовании UpdateView у вас есть доступ к self.object обновляемому объекту.

 Представление, отображающее форму редактирования существующего объекта,
 повторное отображение формы с ошибками проверки (если они есть) и сохранение изменений в объекте.
 При этом используется форма, автоматически сгенерированная из класса модели объекта (если класс формы не указан вручную).


 --- DeleteView ---
 Служит для удаления существующих записей в БД через форму

 from django.views.generic.edit import DeleteView # можно импортировать так
 from django.views.generic import DeleteView # можно импортировать так тоже

 Представление, отображающее страницу подтверждения и удаляющее существующий объект.
 Данный объект будет удален только в том случае, если метод запроса равен POST.
 Если это представление получено через GET, оно отобразит страницу подтверждения, которая должна содержать форму,
 которая отправляет POST на тот же URL-адрес.


 --- LoginView ---
 класс представления для авторизации пользователей
 from django.contrib.auth.views import LoginView

 --- LogoutView  ---
 класс представления для выхода пользователя из системы

 --- AuthenticationForm ---
 класс формы обработки аутентификации пользователя

 --- в settings.py можно прописать такие константы ---
 LOGIN_REDIRECT_URL - задает URL-адрес, на который следует перенаправлять пользователя после успешной авторизации

 LOGIN_URL - определяет URL-адрес, на который следует перенаправить неавторизованного пользователя при попытке посетить
 закрытую страницу сайта

 LOGOUT_REDIRECT_URL  - задает URL-адрес, на который перенапраляется пользователь после выхода

 --- Приоритеты ---
 get_user_model() - Этот метод вернет текущую активную модель пользователя - приоритет самый высокий

 <input type="hidden" name="next" value="{{ next }}" /> - средний приоритет
 в интеренет магазинах когда помещаем товар в корзину потом требуется авторизация,
  после авторизации перенаправляемся именно в корзину, не строго какая-то страница а та на которой пользователь был в последний момент

 LOGIN_REDIRECT_URL - самый низкий приоритет

 @login_required  - для функций представлений
 @login_required(login_url='/admin/') - приоритет выше чем LOGIN_URL в settings.py
 Ограничение доступа к страницам сайта с помощью декоратора
 @login_required - страница доступна только для авторизованных пользователей
 LOGIN_URL - перенаправление на выбранный адрес # в settings.py прописывается

 --- LoginRequiredMixin ---
 Миксин для проверки аутентификации пользователя, требует, чтобы пользователь был авторизован.
 from django.contrib.auth.mixins import LoginRequiredMixin
 login_url = '/admin/' - атрибут для перенаправления на выбранный URL адресс

 --- UserCreationForm ---
 Класс для регистрации пользователей
 from django.contrib.auth.forms import UserCreationForm

 --- PasswordChangeView ---
 для обработки формы изменения пароля

 --- PasswordChangeDoneView ---
 для отображения результата успешного изменения

 --- PasswordResetView ---
 Позволяет пользователю сбросить свой пароль, создав одноразовую ссылку, которую можно использовать для сброса пароля,
  и отправив эту ссылку на зарегистрированный адрес электронной почты пользователя.

 --- PasswordResetDoneView ---
 Страница, отображаемая после того, как пользователю была отправлена по электронной почте ссылка для сброса пароля

 --- PasswordResetConfirmView ---
 Представлена форма для ввода нового пароля.

 --- PasswordResetCompleteView ---
 Представляет представление, которое информирует пользователя об успешном изменении пароля

 --- PermissionRequiredMixin ---
 Этот миксин, как и permission_required декоратор, проверяет, имеет ли пользователь, обращающийся к представлению,
  все заданные разрешения. Вы должны указать разрешение (или итерацию разрешений), используя permission_required параметр

  permission_required

 --- Paginator ---
  from django.core.paginator import Paginator
 Django предоставляет высокоуровневые и низкоуровневые способы управления данными, разбитыми на страницы,
  то есть данными, разделенными на несколько страниц со ссылками «Предыдущий/Следующий

 Под капотом все методы нумерации страниц используют этот Paginator класс.
 Он выполняет всю тяжелую работу по фактическому разбиению объекта QuerySet на Page объекты

  Отправка писем в консоль(console)
  EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend" # прописываем в settings.py

 CRM-система – это сервис для автоматизации бизнес-процессов

 Flask - предоставляет простоту, гибкость и аккуратность в работе, позволяя пользователю самому выбирать,
  как реализовать те или иные вещи. Больше подойдет для создания микросервисов или приложений
 Django - предоставляет пакет «все включено»: у вас есть панель админа, интерфейсы баз данных,
  ORM, и структура каталогов для ваших приложений и проектов.
  Django хорошо подойдет для новостных сайтов, блогов и тд, благодаря тому что у него уже из коробки есть многое
   (в том числе админка), да и создавался он именно под такой тип сайтов

 фласк крут, потому что он простой, всё что надо ставишь сам, а чего не надо там и так нет, но как по мне, всё равно потом получается django.

 WebSocket (веб-сокеты) — независимый веб-протокол, который позволяет создавать
 интерактивное соединение между сервером и клиентом (браузером) и обмениваться сообщениями в реальном времени

 Сокеты являются основой для работы с сетью в Python, и они предоставляют возможность обмениваться данными между
 двумя программами через сеть.

 Для работы с сокетами в Python используется модуль socket

 Сокет — это абстракция, представляющая собой конечную точку сетевого соединения. Вам потребуется создать два сокета для
 обмена данными: один на стороне клиента и один на стороне сервера. Клиент и сервер могут обмениваться данными,
 используя эти сокеты.

 Сокет — это виртуальная конструкция из IP-адреса и номера порта. Её придумали для того, чтобы разработчикам было проще
 писать код, а программы могли передавать данные друг другу даже в пределах одного компьютера.

 --Сокеты используют для двух вещей:
 - для передачи данных по сети.
 - и для связи между приложениями.

 Существует два основных типа сокетов:
 -- TCP-сокеты (Transmission Control Protocol) — обеспечивают надежное соединение между двумя устройствами. Они обычно
 используются в веб-серверах и клиентах, почтовых серверах и других приложениях, где требуется надежность и порядок доставки данных.

 -- UDP-сокеты (User Datagram Protocol) — обеспечивают передачу данных без установления соединения. Они обычно
 используются в видео и аудио потоковых приложениях, играх и других приложениях, где скорость важнее, чем надежность.

 Лог (log) — это текстовый файл, куда автоматически записывается важная информация о работе системы или программы.
 Чаще всего говорят о логах сервера. Их записывает программное обеспечение, которое управляет внутренней частью сайта
 или онлайн-системы. Лог-файл — своеобразный журнал событий.
 Логированием называют запись логов. Оно позволяет ответить на вопросы, что происходило, когда и при каких обстоятельствах.
 Без логов сложно понять, из-за чего появляется ошибка, если она возникает периодически и только при определенных условиях.
 Лог-файл (log file) содержит в себе информацию в сокращенном формате.
 Логи хранятся в файлах с расширением .log. Их можно открыть как обычные текстовые файлы и просмотреть содержимое.
 Как правильно читать лог? 1) Вручную. 2) Cпециальной программой-анализатором.

 Для чего нужны логи:
 Устранение неполадок:
 - По логам можно понять, когда и из-за чего в работе системы возник сбой.
 Контроль работы:
 - Логи позволяют лучше отслеживать процессы, делать прогнозы на будущее и в целом контролировать работу сервера.
 Проверка стабильности:
 - Даже если с системой все хорошо, рекомендуется периодически проверять ее логи.
 Выявление злоумышленников:
 - Вирус или взлом можно обнаружить по логам.
 Маркетинг:
 - Логи — источник ценной информации для развития сайта. Они позволяют собрать статистику по посещаемости с
 «сырыми» техническими данными. Например, понять, откуда приходят пользователи, где они находятся и какими устройствами
 пользуются для визита.

 Какими бывают логи?
 - основной рассказывает о главных событиях, которые произошли непосредственно с серверным ПО;
 - журнал доступа содержит сведения о посетителях сайта;
 - лог ошибок сообщает обо всех сбоях, которые произошли во время работы ПО;
 - лог веб-сервера рассказывает об обращениях к серверу и о возможных ошибках;
 - лог баз данных записывает сведения о действиях с БД, запросах и ошибках;
 - лог почтового сервера содержит информацию об отправленных и полученных письмах и так далее.

 Наиболее важными считаются логи сервера, доступа и ошибок, но проверять советуют не только их.

 Elasticsearch (ES) – масштабируемая утилита полнотекстового поиска и аналитики, которая позволяет быстро в режиме
 реального времени хранить, искать и анализировать большие объемы данных.
 ES (Elasticsearch) - позволяет производить поиск по документам в режиме реального времени
 Elasticsearch это документоориентированная база данных
 Elasticsearch – это распределенный поисковый и аналитический движок на базе Apache Lucene.
 В Elasticsearch отправляются данные в виде документов JSON с помощью API или такого инструмента, как Logstash

 Django Channels расширяет встроенные возможности Django за пределы только HTTP,
 используя преимущества "духовного наследника"
 WSGI (Web Server Gateway Interface), ASGI (Asynchronous Server Gateway Interface).
 Если WSGI предоставлял синхронный стандарт для веб-приложений Python,
 то ASGI предоставляет как синхронные, так и асинхронные стандарты.

 Django Signals - Чтобы принять сигнал, зарегистрируйте функцию приемник с помощью метода Signal.connect().
 Функция-приемник вызывается при отправке сигнала. Все функции-приемники сигнала вызываются по очереди,
 в том порядке, в котором они были зарегистрированы
 Сигналы распространяются синхронно.

 В Django built-in signals позволяет пользовательскому коду получать уведомления об определенных действиях.

 Django-allauth — Библиотека авторизации:
 помогает реализовать функции регистрации, авторизации и управления учётными записями

 django-extensions - набор инструментов, которые помогут вам в вашей повседневной работе. manage.py shell_plus --print-sql

 django-ckeditor - Для редактирования в Админке

 pillow - Для работы с изображениями

 Crispi-forms - для работы с формами. Позволят вам управлять поведением рендеринга ваших форм

 Celery - это асинхронная очередь задач, используемая для распределенной обработки сообщений.
 Он позволяет выполнять задачи в фоновом режиме, не загружая основной поток выполнения

 Celery — это программа, которая отслеживает задачи (tasks), которые необходимо выполнить,
 и в которой есть набор обработчиков (workers), которые будут выполнять эти задачи.
 Основной смысл в том, что она (программа) может выполнять несколько задач параллельно
 и что она не блокирует поставщиков (producers) этих самых задач.

 Celery на самом деле не хранит все эти задачи в памяти, брокер сообщений хранит задачи.


 Django предназначен для создания полнофункциональных веб-приложений,
 в то время как DRF специализируется на создании RESTful API.

 --- DRF  Django REST Framework ---
 Фреймворк, работающий со стандартными моделями Django для создания гибкого и мощного API для проекта.

 DRF облегчает взаимодействие между сервером и клиентами, позволяя передавать данные в формате JSON
 и выполнять различные операции, такие как чтение, запись и удаление данных. Он также обеспечивает безопасность,
 авторизацию и управление правами доступа.

 Архитектура DRF:

 Сериализатор (Serializer): преобразует информацию, хранящуюся в базе данных и определенную с помощью моделей Django,
 в формат JSON, который легко и эффективно передаётся через API.

 Представление (View, ViewSet): определяет функции (чтение, создание, обновление, удаление), которые будут доступны через API.

 Маршрутизатор (Router): определяет URL-адреса, которые будут предоставлять доступ к каждому представлению.


 Как работает Serializer в Django REST Framework?
 Serializer преобразует информацию, хранящуюся в базе данных и определенную с помощью моделей Django, в формат,
  который легко и эффективно передается через API - JSON.

 Наиболее распространенной формой, которую принимает сериализатор DRF, является тот, который привязан непосредственно к модели Django:

 class ThingSerializer(serializers.ModelSerializer):
  class Meta:
    model = Thing
    fields = (‘name’, )

 Если взять за пример Serializer, то можно посмотреть на код джанги:

@six.add_metaclass(SerializerMetaclass)
class Serializer(BaseSerializer):
  ...
SerializerMetaclass - это тот самый метакласс, который конструирует класс ModelForm.


 -- nginx --
 Nginx – это веб сервер. Он хранит файлы сайта и направляет их по запросу на компьютер или мобильное устройство.
 То есть он нужен для быстрого отображения интернет-страничек.
 Его основная задача заключается в обработке статичного контента.
 Сервер Nginx выполняет две функции:
 - Принимает, обрабатывает и отправляет запросы клиентам
 - Играет роль прокси-сервера

 Сайты в интернете работают на веб-серверах, которые обрабатывают запросы пользователей и отвечают на них.
 Сегодня один из самых популярных веб-серверов — Nginx
 NGINX (Engine X, или «Энджин-икс») — это программное обеспечение с открытым исходным кодом для создания веб-серверов.
 Оно принимает запрос клиента, например браузера, обрабатывает его и возвращает ответ.

 --- Типа Советы ---

 -- Рефакторить и замерять скорость при помощи  @funcy.log_durations. - там на сайте еще много чего

 Ну, например, select_related на самом деле делает JOIN. А prefetch_related не делает. Не всегда синтаксис django ORM
 выдерживает реальности SQL, и появляются всякие странные вещи типа OuterRef, F, Q, и иже с ними. GROUP BY вообще замаскирован.

 Если вы хотите выполнить агрегацию, вы можете использовать функции агрегации ORM :

 from django.db.models import Count
 result = (Members.objects
     .values('designation')
     .annotate(dcount=Count('designation'))
     .order_by()
)




"""