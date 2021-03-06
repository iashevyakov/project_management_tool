# Generated by Django 2.2.14 on 2020-12-15 18:36

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('name', models.CharField(max_length=50, verbose_name='ФИО')),
                ('role', models.CharField(choices=[('pm', 'Project Manager'), ('dev', 'Developer'), ('qa', 'QA engineer'), ('analyst', 'Analyst'), ('area_dev', 'Dev Area Lead'), ('area_qa', 'QA Area Lead'), ('area_analyst', 'Analyst Area Lead'), ('lead_dev', 'Dev Lead'), ('lead_qa', 'QA Lead'), ('lead_analyst', 'Analyst Lead')], default='pm', max_length=20, verbose_name='Роль')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('chief', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subordinates', to=settings.AUTH_USER_MODEL, verbose_name='Начальник')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Dates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название даты')),
                ('date', models.DateField(verbose_name='Дата')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('date_start', models.DateField(verbose_name='Дата начала')),
                ('date_end', models.DateField(verbose_name='Дата завершения')),
                ('status', models.CharField(choices=[('open', 'Открыт'), ('in_progress', 'В работе'), ('delay', 'Идёт с задержкой'), ('closed', 'Завершён')], max_length=20, verbose_name='Статус')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='Последнее изменение')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_projects', to=settings.AUTH_USER_MODEL, verbose_name='Кем создан')),
                ('employees', models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL, verbose_name='Сотрудники')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
            },
        ),
        migrations.CreateModel(
            name='Sprint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('date_start', models.DateField(verbose_name='Дата начала')),
                ('date_end', models.DateField(verbose_name='Дата завершения')),
                ('status', models.CharField(choices=[('open', 'Открыт'), ('in_progress', 'В работе'), ('delay', 'Идёт с задержкой'), ('closed', 'Завершён')], max_length=20, verbose_name='Статус')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='Последнее изменение')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_sprints', to=settings.AUTH_USER_MODEL, verbose_name='Кем создан')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_sprints', to='tasks.Project')),
            ],
            options={
                'verbose_name': 'Спринт',
                'verbose_name_plural': 'Спринты',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('description', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Описание')),
                ('accept_criterion', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Критерий приёмки')),
                ('deadline', models.DateTimeField(blank=True, null=True, verbose_name='Дата завершения')),
                ('redline', models.DateTimeField(blank=True, null=True, verbose_name='Запасная дата завершения')),
                ('state', models.CharField(choices=[('to-do', 'Поставлена'), ('in_progress', 'В работе'), ('postponed', 'Отложена'), ('done', 'Завершена'), ('delay', 'Идёт с задержкой'), ('late', 'Опоздание')], default='to-do', max_length=20, verbose_name='Статус')),
                ('priority', models.CharField(choices=[('low', 'Low'), ('normal', 'Normal'), ('high', 'High'), ('critical', 'Critical')], default='low', max_length=20, verbose_name='Приоритет')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='Последнее изменение')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_tasks', to=settings.AUTH_USER_MODEL, verbose_name='Кем создана')),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tasks_assigned', to=settings.AUTH_USER_MODEL, verbose_name='Ответственный')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_tasks', to='tasks.Project', verbose_name='Проект')),
                ('sprint', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sprint_tasks', to='tasks.Sprint', verbose_name='Спринт')),
                ('sub_tasks', models.ManyToManyField(blank=True, related_name='parent_task', to='tasks.Task', verbose_name='Подзадачи')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_description', models.CharField(max_length=200, verbose_name='Описание')),
                ('is_done', models.BooleanField(default=False, verbose_name='Done')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.Task')),
            ],
            options={
                'verbose_name': 'Чек лист',
                'verbose_name_plural': 'Чек листы',
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='dates',
            field=models.ManyToManyField(blank=True, null=True, to='tasks.Dates'),
        ),
        migrations.AddField(
            model_name='employee',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='employee',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
