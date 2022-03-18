import pretty_yarrrml2rml as yarrrml2rml
from fnmatch import translate

def translate(input):
    print("------------------------START TRANSLATING YARRRML TO RML-------------------------------")

    print("yarrrm: ", input)

    list_initial_sources = yarrrml2rml.source_mod.get_initial_sources(input)
    rml_mapping = [yarrrml2rml.mapping_mod.add_prefix(input)]
    try:
        for mapping in input.get(yarrrml2rml.constants.YARRRML_MAPPINGS):
            #print('mapping: ', mapping )
            subject_list = yarrrml2rml.subject_mod.add_subject(input, mapping)
            source_list = yarrrml2rml.source_mod.add_source(input, mapping, list_initial_sources)
            pred = yarrrml2rml.predicate_object_mod.add_predicate_object_maps(input, mapping)
            it = 0
            for source in source_list:
                for subject in subject_list:
                    map_aux = yarrrml2rml.mapping_mod.add_mapping(mapping, it)
                    if type(source) is list:
                        rml_mapping.append(map_aux + source[0] + subject + pred + source[1])
                    else:
                        rml_mapping.append(map_aux + source + subject + pred)
                    rml_mapping[len(rml_mapping) - 1] = rml_mapping[len(rml_mapping) - 1][:-2]
                    rml_mapping.append(".\n\n\n")
                    it = it + 1

        #print("RML content successfully created!\n Starting the validation with RDFLib....")
        #print(rml_mapping)
        rml_mapping_string = "".join(rml_mapping)
        
    except Exception as e:
        #print("------------------------ERROR-------------------------------")
        #print("RML content not generated: " + str(e))
        return "Error Occured!", 500

    print("------------------------END TRANSLATION-------------------------------")

    return rml_mapping_string
