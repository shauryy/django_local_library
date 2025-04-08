from ninja import NinjaAPI, Schema
from typing import List
from django.shortcuts import get_object_or_404
from .models import Author, Genre, Language

# Initialize API
api = NinjaAPI()

class AuthorSchema(Schema):
    id: int
    first_name: str
    last_name: str
    date_of_birth: str = None
    date_of_death: str = None

class AuthorCreateSchema(Schema):
    first_name: str
    last_name: str
    date_of_birth: str = None
    date_of_death: str = None

class GenreSchema(Schema):
    id: int
    name: str

class GenreCreateSchema(Schema):
    name: str

class LanguageSchema(Schema):
    id: int
    name: str

class LanguageCreateSchema(Schema):
    name: str

@api.get("/authors", response=List[AuthorSchema])
def list_authors(request):
    return Author.objects.all()

@api.get("/authors/{author_id}", response=AuthorSchema)
def get_author(request, author_id: int):
    author = get_object_or_404(Author, id=author_id)
    return author

@api.post("/authors", response=AuthorSchema)
def create_author(request, data: AuthorCreateSchema):
    author = Author.objects.create(**data.dict())
    return author

@api.put("/authors/{author_id}", response=AuthorSchema)
def update_author(request, author_id: int, data: AuthorCreateSchema):
    author = get_object_or_404(Author, id=author_id)
    for attr, value in data.dict().items():
        setattr(author, attr, value)
    author.save()
    return author

@api.delete("/authors/{author_id}")
def delete_author(request, author_id: int):
    author = get_object_or_404(Author, id=author_id)
    author.delete()
    return {"success": True}

@api.get("/genres", response=List[GenreSchema])
def list_genres(request):
    return Genre.objects.all()

@api.get("/genres/{genre_id}", response=GenreSchema)
def get_genre(request, genre_id: int):
    genre = get_object_or_404(Genre, id=genre_id)
    return genre

@api.post("/genres", response=GenreSchema)
def create_genre(request, data: GenreCreateSchema):
    genre = Genre.objects.create(**data.dict())
    return genre

@api.put("/genres/{genre_id}", response=GenreSchema)
def update_genre(request, genre_id: int, data: GenreCreateSchema):
    genre = get_object_or_404(Genre, id=genre_id)
    genre.name = data.name
    genre.save()
    return genre

@api.delete("/genres/{genre_id}")
def delete_genre(request, genre_id: int):
    genre = get_object_or_404(Genre, id=genre_id)
    genre.delete()
    return {"success": True}

@api.get("/languages", response=List[LanguageSchema])
def list_languages(request):
    return Language.objects.all()

@api.get("/languages/{language_id}", response=LanguageSchema)
def get_language(request, language_id: int):
    language = get_object_or_404(Language, id=language_id)
    return language

@api.post("/languages", response=LanguageSchema)
def create_language(request, data: LanguageCreateSchema):
    language = Language.objects.create(**data.dict())
    return language

@api.put("/languages/{language_id}", response=LanguageSchema)
def update_language(request, language_id: int, data: LanguageCreateSchema):
    language = get_object_or_404(Language, id=language_id)
    language.name = data.name
    language.save()
    return language

@api.delete("/languages/{language_id}")
def delete_language(request, language_id: int):
    language = get_object_or_404(Language, id=language_id)
    language.delete()
    return {"success": True}
