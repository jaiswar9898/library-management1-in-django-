# Generated by Django 4.0.2 on 2022-02-02 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('summary', models.TextField(help_text='Enter a brief description of the book', max_length=1000)),
                ('isbn', models.CharField(help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>', max_length=13, verbose_name='ISBN')),
                ('genre', models.CharField(help_text='Enter a book genre (e.g. Science Fiction, French Poetry etc.)', max_length=200)),
                ('quantity', models.IntegerField()),
                ('lib_author', models.CharField(default='Sara', max_length=100)),
                ('category', models.CharField(default='Featured', max_length=50)),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_no', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=10)),
                ('branch', models.CharField(max_length=3)),
                ('contact_no', models.CharField(max_length=10)),
                ('total_books_due', models.IntegerField(default=0)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(default=1234, max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(default='none', max_length=100)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lapp.book')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lapp.student')),
            ],
        ),
        migrations.CreateModel(
            name='Borrower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_date', models.DateTimeField(blank=True, null=True)),
                ('return_date', models.DateTimeField(blank=True, null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lapp.book')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lapp.student')),
            ],
        ),
    ]