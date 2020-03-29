from flask import (
    Blueprint, redirect, render_template, request, url_for
)
import json

from foundry.ffxiv.data import (
    WORLDS, search_character, get_character_api, get_data, set_data
)
from foundry.ffxiv.models import Character, Job, Item

bp = Blueprint('ffxiv', __name__, url_prefix='/ffxiv')

@bp.route('/')
def index():
    return render_template('ffxiv/index.html')

@bp.route('/characters/', methods=('GET', 'POST'))
def characters():
    characters = None

    if request.method == 'POST':
        name = request.form['name']
        server = request.form['server']

        characters = search_character(name, server)

    return render_template('ffxiv/characters.html', worlds=WORLDS, characters=characters)

@bp.route('/characters/<int:lodestone_id>')
def character(lodestone_id):

    character = get_character_api(lodestone_id)

    return render_template('ffxiv/character.html', character=character)

@bp.route('/actions/')
def actions():
    actions = get_data('actions')

    #! this should go somewhere else
    types = ["Ability", "Spell"]

    return render_template('ffxiv/actions.html', actions=actions, types=types)

@bp.route('/items/', methods=('GET', 'POST'))
def items():
    items = get_data('items')

    if request.method == 'POST':
        name = request.form.get('name')
        Type = request.form.get('type')
        level = request.form.get('level')
        value = request.form.get('value')
        description = request.form.get('description')

        new_item = Item.from_dict({'name':name, 'type':Type, 'description':description})
        items[new_item.name] = new_item

        set_data('items', items)

    return render_template('ffxiv/items.html', items=items, types=Item.TYPES)

@bp.route('/recipes/', methods=('GET', 'POST'))
def recipes():
    from foundry.ffxiv.models import Recipe
    from foundry.ffxiv.data import CRYSTALS, get_db

    db = get_db()
    recipe_components = db.execute(
        "SELECT recipes.name, recipes.level, recipes.type, recipes.yield, recipes.difficulty, recipes.durability, recipes.max_quality, recipes.crystalA, recipes.num_crystalA, recipes.crystalB, recipes.num_crystalB, components.name AS component, map.num " \
            "FROM map_recipe_component AS map " \
            "LEFT JOIN recipes ON recipes.pk = map.recipe_fk " \
            "LEFT JOIN components ON components.pk = map.component_fk"
    ).fetchall()

    recipes = {}
    for row in recipe_components:
        name = row['name']
        if not name in recipes:
            new_recipe = Recipe.from_row(row)
            recipes[name] = new_recipe
        recipes.get(name).add_material(row['component'], row['num'])


    if request.method == 'POST':
        pass

    
    items = get_data('items')

    return render_template('ffxiv/recipes.html', jobs=Job.JOBS, types=Recipe.TYPES, items=items, crystals=CRYSTALS)

@bp.route('/logs/', methods=('GET', 'POST'))
def logs():
    return render_template('ffxiv/logs.html')

@bp.route('/quests/', methods=('GET', 'POST'))
def quests():
    quests = get_data('quests')
    locations = get_data('locations')

    # TODO: this should go somewhere else
    quest_lines = ["Seventh Umbral Era", "Seventh Astral Era", "Heavensward", "Dragonsong War", "Stormblood", "The Legend Returns", "Shadowbringers", "Post-Shadowbringers"]

    return render_template('ffxiv/quests.html', quests=quests, locations=locations, quest_lines=quest_lines)

@bp.route('/locations/', methods=('GET', 'POST'))
def locations():
    from models import Location

    locations = get_data('locations')

    #! User can add an region/zone/area without filling out landmass/region/zone
    if request.method == 'POST':
        name = request.form['name']
        loc_type = request.form['type']
        within = {loc_type: request.form[loc_type.lower()] for loc_type in Location.TYPES[:-1]}

        new_location = Location(name, loc_type, within)

        if loc_type == 'landmass':
            locations[new_location.name] = new_location
            return redirect(url_for('ffxiv.locations'))

        landmass = locations.get(within['Landmass'])
        region = landmass.get_subregion(within['Region'])
        zone = region.get_subregion(within['Zone'])
        if zone:
            zone.add_subregion(new_location)
        elif region:
            region.add_subregion(new_location)
        elif landmass:
            landmass.add_subregion(new_location)
        else:
            locations[new_location.name] = new_location

        set_data('locations', locations)

    return render_template('ffxiv/locations.html', locations=locations, types=Location.TYPES)

# @bp.route('/locations/delete/<landmass>/')
# @bp.route('/locations/delete/<landmass>/<region>')
# @bp.route('/locations/delete/<landmass>/<region>/<zone>')
# @bp.route('/locations/delete/<landmass>/<region>/<zone>/<area>')
# def alter_location(landmass=None, region=None, zone=None, area=None):
#     locations = get_data('locations')

#     landmass = locations.get(landmass)
#     region = landmass.get_subregion(region)
#     zone = region.get_subregion(zone)
#     area = region.get_subregion(area)

#     if area: zone.del_subregion(area)
#     elif zone: region.del_subregion(zone)
#     elif region: landmass.del_subregion(region)
#     elif landmass: del locations[landmass]
#     else:
#         return KeyError

#     set_data('locations', locations)


#? This only applies to the current blueprint but maybe I should make it more global
# adds a custom jinja filter called `json_dumps` to enable recursive JSON serialization
@bp.app_template_filter("json_dumps")
def json_dumps(obj):
    from json import dumps
    return dumps(obj, default=lambda obj:obj.json())