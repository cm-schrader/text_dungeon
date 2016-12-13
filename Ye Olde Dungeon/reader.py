# Custom Reader for interpreting commands
# Syntax: Verb + Descriptor/Noun
# Define dictionaries for verbs and nouns and a list for verb exceptions(bypasses "Too many verbs" error).
#from main import ran

def interpret(command, verb_dict, noun_dict, exceptions, overide):
    """
    Interprets a sentence
    :param command: The sentence
    :param verb_dict: Dictionary of allowed verb commands
    :param noun_dict: Dictionary of available nouns
    :param exceptions: List of nouns to which 'Too many verbs' error does not apply
    :return: Tuple of verb, noun, and descriptor
    """
    line = str(command).split()
    print(str(line))
    verb = None
    subject = None
    object = None
    descriptor = None
    post_verb = []
    modifiers = {
        "with": "with",
        "using": "with",
        "via": "via",
        "through": "via",
        "at": "at"
    }
    #if overide is not None:
    #    ran = overide
    for i, item in enumerate(line):
        word = item.lower()
        if word in verb_dict and verb is None:
            verb = word
        elif verb is not None and verb not in exceptions and word in verb_dict:
            raise SyntaxError("Too many verbs.")
        elif word in noun_dict and subject is None:
            subject = word
        elif subject is not None and word in noun_dict:
            post_verb.append(word)
            object = word
        elif word in modifiers:
            if descriptor is None:
                descriptor = (modifiers[word])
                if verb is not None:
                    post_verb.append(word)
            elif verb in exceptions:
                post_verb.append(word)
            else:
                raise SyntaxError("That does not make sense.")
        else:
            post_verb.append(word)
        i += 1
    if verb is None:
        raise SyntaxError("No verb")
    delete_chars = dict.fromkeys(map(ord, "[]',"), None)
    post_verb = str(post_verb).translate(delete_chars)
    del delete_chars
    result = (verb, subject, descriptor, post_verb, object, verb_dict, overide)
    del modifiers
    return result


def execute(action_tuple):
    """
    Executes commands from the interpret function
    :param action_tuple: Tuple of the verb, noun, and descriptor
    :return: Preforms a function from a dictionary
    """
    verb = action_tuple[0]
    verb_dict = action_tuple[5]
    verb_dict[verb](action_tuple)


def exe(command, verb_dict, noun_dict, exceptions, override):
    """
    Interprets a command and executes it
    :param override: Overrides RNG attributes, ex. damage
    :param command: String to be interpreted
    :param verb_dict: Dictionary of allowed verb commands
    :param noun_dict: Dictionary of available nouns
    :param exceptions: List of nouns to which 'Too many verbs' error does not apply
    :return: Executes a command from a dictionary
    """
    execute(interpret(command, verb_dict, noun_dict, exceptions, override))