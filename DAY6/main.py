'''
    This day's project is a console-based recipe manager.
    It uses directories as a database, so there is not a directory called 'recipes', it will make one.
    The user can see the categories, and see which recipes are in as same as create new or delete the existing ones.
    It also can create and delete categories (delete a category will totally delete all recipes in).
'''


from pathlib import Path
from os import system
from getpass import getpass
import os
from shutil import rmtree

CURRENT_PATH = Path().absolute()
MENU_OPTIONS_NUMBER = 6
CUSTOM_PRINTS = {
    "welcome": "Welcome user!\n",
    "recipes-path": "Recipes are located here: '{arg}'\n",
    "show-recipe-name": "\nThe recipe name is '{arg}'",
    "show-recipe-text": "The file contains the following text: '{arg}'\n",
    "recipe-created": "Recipe '{arg}.txt' created successfully!",
    "recipe-deleted": "Recipe deleted successfully!",
    "category-created": "Category '{arg}' created successfully!",
    "category-deleted": "Category deleted successfully!",
    "empty-file": "'{arg}' is empty",
    "input-menu": "Select an option (number): ",
    "input-category": "Select a category option (number, -1 to quit): ",
    "input-recipe": "Select a recipe option (number, -1 to quit): ",
    "pause-prompt": "\nPress ENTER to continue\n",
    "recipe-title-prompt": "Type the title of the new recipe (ENTER to cancel): ",
    "recipe-content-prompt": "Type the content of the new recipe: ",
    "category-creation-prompt": "Type the new category (ENTER to cancel): ",
    "error-input": "ERROR: Should be a number between 1 and 6!",
    "error-recipe-creation": "ERROR: File could not be created!",
    "error-category-creation": "ERROR: Category could not be created!",
    "error-recipe-exists": "ERROR: Recipe already exists!",
    "error-category-exists": "ERROR: Category already exists!",
    "error-empty-dir": "ERROR: Empty directory",
    "menu-1": "1. Show recipe",
    "menu-2": "2. Create recipe",
    "menu-3": "3. Create category",
    "menu-4": "4. Delete recipe",
    "menu-5": "5. Delete category",
    "menu-6": "6. Close program",
    "title-category": "---- CATEGORIES ----",
    "title-recipe": "---- RECIPES ----",
    "title-create-category": "---- CREATE CATEGORY ----",
    "title-delete-category": "---- DELETE CATEGORY ----",
    "title-create-recipe": "---- CREATE RECIPE ----",
    "title-delete-recipe": "---- DELETE RECIPE ----",
}


def main():
    menu_selection = 0
    init()
    pause_execution()
    while menu_selection != 6:
        print_main_menu()
        try:
            menu_selection = int(input(CUSTOM_PRINTS["input-menu"]))
            if menu_selection < 1 or menu_selection > 6:
                raise Exception
        except:
            print(CUSTOM_PRINTS["error-input"])
            pause_execution()
            continue
        execute_selected(menu_selection)
        pause_execution()
        system("cls")


def init():
    print(CUSTOM_PRINTS["welcome"])
    if not Path(CURRENT_PATH, "recipes").exists():
        os.mkdir(Path(CURRENT_PATH, "recipes"))
    print(CUSTOM_PRINTS["recipes-path"].format(arg=CURRENT_PATH))


def print_main_menu():
    system("cls")
    [print(CUSTOM_PRINTS[f"menu-{i}"]) for i in range(1, MENU_OPTIONS_NUMBER + 1)]


def pause_execution():
    getpass(CUSTOM_PRINTS["pause-prompt"])


def execute_selected(selected: int):
    categories_list = list(Path(CURRENT_PATH, "recipes").iterdir())
    categories_enum = enumerate(Path(CURRENT_PATH, "recipes").iterdir())
    system("cls")
    match selected:
        case 1:
            if check_empty_dir(categories_list):
                return
            category_selected = select_from_list(categories_enum, categories_list, "category")
            if category_selected == -1:
                return
            show_recipe(categories_list[category_selected])
        case 2:
            if check_empty_dir(categories_list):
                return
            category_selected = select_from_list(categories_enum, categories_list, "category")
            if category_selected == -1:
                return
            create_recipe(categories_list[category_selected])
        case 3:
            create_category()
        case 4:
            if check_empty_dir(categories_list):
                return
            category_selected = select_from_list(categories_enum, categories_list, "category")
            if category_selected == -1:
                return
            delete_recipe(categories_list[category_selected])
        case 5:
            if check_empty_dir(categories_list):
                return
            category_selected = select_from_list(categories_enum, categories_list, "category")
            if category_selected == -1:
                return
            delete_category(categories_list[category_selected])
        case 6:
            exit()


def check_empty_dir(arr: []):
    if len(arr) != 0:
        return False
    else:
        print(CUSTOM_PRINTS["error-empty-dir"])
        return True


def select_from_list(_enum, _list, item_to_select: str):
    selected = 0
    done = False
    print(CUSTOM_PRINTS[f"title-{item_to_select}"])
    [print(f"{index + 1}: {item.stem}") for index, item in _enum]
    while not done:
        try:
            selected = int(input(CUSTOM_PRINTS[f"input-{item_to_select}"]))
            if selected == -1:
                return -1
            if selected < 1 or selected > len(_list):
                raise Exception
            selected -= 1
            done = True
        except:
            continue
    return selected


def show_recipe(recipe_path: Path):
    system("cls")
    recipes_list = list(recipe_path.iterdir())
    recipes_enum = enumerate(recipe_path.iterdir())
    if check_empty_dir(recipes_list):
        return
    recipe_selected = select_from_list(recipes_enum, recipes_list, "recipe")
    if recipe_selected == -1:
        return
    file = recipes_list[recipe_selected]
    file_content = file.open().read()
    print(CUSTOM_PRINTS["show-recipe-name"].format(arg=file.stem))
    if len(file_content) == 0:
        print(CUSTOM_PRINTS["empty-file"].format(arg=file.stem))
    else:
        print(CUSTOM_PRINTS["show-recipe-text"].format(arg=file_content))


def create_recipe(recipe_path: Path):
    system("cls")
    print(CUSTOM_PRINTS["title-create-recipe"])
    recipe_title = input(CUSTOM_PRINTS["recipe-title-prompt"])
    if len(recipe_title) != 0:
        file = Path(recipe_path, f"{recipe_title}.txt")
        if not file.exists():
            recipe_text = input(CUSTOM_PRINTS["recipe-content-prompt"])
            file.write_text(recipe_text)
            print(CUSTOM_PRINTS["recipe-created"].format(arg=recipe_title))
        else:
            print(CUSTOM_PRINTS["error-recipe-exists"])
    else:
        print(CUSTOM_PRINTS["error-recipe-creation"])


def create_category():
    system("cls")
    print(CUSTOM_PRINTS["title-create-category"])
    category = input(CUSTOM_PRINTS["category-creation-prompt"])
    if len(category) != 0:
        path = Path(CURRENT_PATH, "recipes", category)
        if not path.exists():
            os.mkdir(Path(CURRENT_PATH, "recipes", category))
            print(CUSTOM_PRINTS["category-created"].format(arg=category))
        else:
            print(CUSTOM_PRINTS["error-category-exists"])
    else:
        print(CUSTOM_PRINTS["error-category-creation"])


def delete_recipe(recipe_path: Path):
    system("cls")
    print(CUSTOM_PRINTS["title-delete-recipe"])
    recipes_list = list(recipe_path.iterdir())
    recipes_enum = enumerate(recipe_path.iterdir())
    if check_empty_dir(recipes_list):
        return
    recipe_selected = select_from_list(recipes_enum, recipes_list, "recipe")
    if recipe_selected == -1:
        return
    os.remove(Path(recipes_list[recipe_selected]))
    print(CUSTOM_PRINTS["recipe-deleted"])


def delete_category(category_path: Path):
    system("cls")
    print(CUSTOM_PRINTS["title-delete-category"])
    rmtree(category_path)
    print(CUSTOM_PRINTS["category-deleted"])


main()
