"""Latin language corpora available for download or loading locally.
All remote corpora hosted by github on the cltk organization account, eg:
'http://github.com/cltk' + name
"""

LATIN_CORPORA = [
    {'encoding': 'utf-8',
     'markup': 'tei_xml',
     'location': 'remote',
     'type': 'text',
     'name': 'latin_text_perseus',
     'origin': 'https://github.com/cltk/latin_text_perseus.git'},
    {'encoding': 'utf-8',
     'markup': 'xml',
     'name': 'latin_treebank_perseus',
     'origin': 'https://github.com/cltk/latin_treebank_perseus.git',
     'location': 'remote',
     'type': 'treebank'},
    {'encoding': 'utf-8',
     'markup': 'plaintext',
     'name': 'latin_text_latin_library',
     'origin': 'https://github.com/cltk/latin_text_latin_library.git',
     'location': 'remote',
     'type': 'text'},
    {'encoding': 'latin-1',
     'markup': 'beta_code',
     'location': 'local',
     'name': 'phi5',
     'origin': None,
     'type': 'text'},
    {'encoding': 'latin-1',
     'markup': 'beta_code',
     'origin': None,
     'name': 'phi7',
     'location': 'local',
     'type': 'text'},
    {'encoding': 'utf-8',
     'markup': 'plaintext',
     'name': 'latin_proper_names_cltk',
     'origin': 'https://github.com/cltk/latin_proper_names_cltk.git',
     'location': 'remote',
     'type': 'lexicon'},
    {'origin': 'https://github.com/cltk/latin_models_cltk.git',
     'name': 'latin_models_cltk',
     'location': 'remote',
     'type': 'model'},
    {'encoding': 'utf-8',
     'markup': 'python',
     'name': 'latin_pos_lemmata_cltk',
     'origin': 'https://github.com/cltk/latin_pos_lemmata_cltk.git',
     'location': 'remote',
     'type': 'lemma'},
    {'encoding': 'utf-8',
     'markup': 'xml',
     'name': 'latin_treebank_index_thomisticus',
     'origin': 'https://github.com/cltk/latin_treebank_index_thomisticus.git',
     'location': 'remote',
     'type': 'treebank'},
    {'encoding': 'xml',
     'markup': 'plaintext',
     'name': 'latin_lexica_perseus',
     'origin': 'https://github.com/cltk/latin_lexica_perseus.git',
     'location': 'remote',
     'type': 'lexicon'},
    {'encoding': 'utf-8',
     'markup': 'plaintext',
     'name': 'latin_training_set_sentence_cltk',
     'origin': 'https://github.com/cltk/latin_training_set_sentence_cltk.git',
     'location': 'remote',
     'type': 'training_set'},
    {'origin': 'https://github.com/cltk/latin_word2vec_cltk.git',
     'name': 'latin_word2vec_cltk',
     'location': 'remote',
     'type': 'model'},
    {'encoding': 'utf-8',
     'markup': 'tei_xml',
     'location': 'remote',
     'type': 'text',
     'name': 'latin_text_antique_digiliblt',
     'origin': 'https://github.com/cltk/latin_text_antique_digiliblt.git'},
     {'location': 'remote',
     'type': 'text',
     'name': 'latin_text_corpus_grammaticorum_latinorum',
     'origin': 'https://github.com/cltk/latin_text_corpus_grammaticorum_latinorum.git'},
    {'location': 'remote',
     'type': 'text',
     'name': 'latin_text_poeti_ditalia',
     'origin': 'https://github.com/cltk/latin_text_poeti_ditalia.git'}
]
