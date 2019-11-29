"""Contains function to create triples from user input."""

from app.types.triple import Triple
import spacy

def create_triples(user_input):
    """
    Create triples from user input.

    :type user_input: str
    :rtype: list of app.types.triple.Triple
    """
    language = spacy.load('en_core_web_sm')
    document = language(user_input)
    entities = document.ents
    entities_count = len(entities)
    if entities_count < 2:
        return []
    else:
        triples = []
        for entity_current_index in range(0, entities_count, 2):
            entity_current = entities[entity_current_index]
            entity_next = entities[entity_current_index + 1]
            predicate = _get_predicate(user_input, entities, entities_count, entity_current_index)
            triple = Triple(predicate, entity_current.text, entity_next.text)
            triples.append(str(triple))
        return triples

def _get_predicate(user_input, entities, entities_count, entity_current_index):
    if entity_current_index == 0:
        start = 0
    else:
        start = entities[entity_current_index - 1].end_char + 1
    if entities_count - entity_current_index < 3:
        stop = len(user_input)
    else:
        stop = entities[entity_current_index + 2].start_char
    predicate = user_input[start:stop].strip()
    return predicate
