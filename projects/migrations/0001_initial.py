# Generated by Django 2.1.7 on 2019-03-21 18:14

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
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
                ('display_name', models.CharField(default='', max_length=20)),
                ('display_picture', models.CharField(default='https://via.placeholder.com/150x150?text=user_display_picture', max_length=200)),
                ('is_sutd', models.BooleanField(default='False')),
                ('graduation_year', models.IntegerField()),
                ('pillar', models.CharField(choices=[('FRSH', 'Freshmore'), ('EPD', 'Engineering Product and Design'), ('ESD', 'Engineering Systems Design'), ('ASD', 'Architecture and Sustainable Design'), ('ISTD', 'Information Systems Technology and Design'), ('PSTG', 'Post-graduate')], default='', max_length=4)),
                ('admin_groups', models.CharField(choices=[('UROP', 'Undergraduate Research Opportunities Project'), ('UTOP', 'Undergraduate Teaching Opportunities Project'), ('ACAD', 'Academic Project (1D, 2D etc.)'), ('SELF', 'Student-initiated project'), ('NONE', "Unknown, or doesn't fall into any category")], default='', max_length=4)),
                ('contact_email', models.CharField(default='none@example.com', max_length=200)),
                ('personal_links', models.CharField(default='', max_length=200)),
                ('bio', models.CharField(default='', max_length=300)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('title', models.CharField(default='', max_length=200)),
                ('project_uid', models.CharField(default='', max_length=20, primary_key=True, serialize=False)),
                ('featured_image', models.CharField(default='https://via.placeholder.com/500x250?text=project_featured_image', max_length=200)),
                ('caption', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('UROP', 'Undergraduate Research Opportunities Project'), ('UTOP', 'Undergraduate Teaching Opportunities Project'), ('ACAD', 'Academic Project (1D, 2D etc.)'), ('SELF', 'Student-initiated project'), ('NONE', "Unknown, or doesn't fall into any category")], default='NONE', max_length=4)),
                ('url', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('ACCEPT', 'Accepted Project, will display'), ('REJECT', 'Rejected Project, will not display'), ('PENDING', 'Pending Project, will not display')], default='PENDING', max_length=10)),
                ('published_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='tags',
            field=models.ManyToManyField(to='projects.Tag'),
        ),
        migrations.AddField(
            model_name='project',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
