# Generated by Django 4.2.7 on 2023-11-15 16:07

from django.db import migrations, models
import django.db.models.fields.reverse_related


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0003_alter_book_author_alter_book_library'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.fields.reverse_related.ManyToManyRel, to='test_app.author'),
        ),
        migrations.AlterField(
            model_name='librarybook',
            name='library',
            field=models.ForeignKey(on_delete=django.db.models.fields.reverse_related.ManyToOneRel, to='test_app.library'),
        ),
    ]
