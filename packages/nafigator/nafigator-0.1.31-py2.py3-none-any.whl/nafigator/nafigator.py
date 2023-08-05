# coding: utf-8

"""Main module."""

from datetime import datetime
import sys
import click
import logging
import os

from .linguisticprocessor import stanzaProcessor
from .linguisticprocessor import spacyProcessor
from .preprocessprocessor import convert_pdf
from .utils import time_in_correct_format
from .nafdocument import NafDocument

from .const import Entity
from .const import WordformElement
from .const import TermElement
from .const import EntityElement
from .const import DependencyRelation
from .const import ChunkElement
from .const import udpos2nafpos_info
from .const import hidden_table
from .utils import normalize_token_orth
from .utils import remove_illegal_chars


@click.command()
@click.option('--input', default="data/example.pdf", prompt="input file", help='The input file')
@click.option('--output', default='data/example.naf', prompt="output file", help='The output file')
@click.option('--engine', default='stanza', prompt="NLP-package", help="The package to parse the text")
@click.option('--language', default='en', prompt="language", help="The language of the input file")
@click.option('--naf_version', default='v3.1', prompt="naf version", help="NAF version to convert to")
@click.option('--dtd_validation', default=False, prompt="dtd validation", help="Validate the NAF dtd")


def parse(input: str, 
          output: str, 
          engine: str, 
          language: str, 
          naf_version: str, 
          dtd_validation: bool):
    """
    """
    log_file: str = "".join(output.split(".")[0:-1])+".log"
    logging.basicConfig(filename=log_file, 
                        level=logging.INFO, 
                        filemode="w")
    tree = generate_naf(input = input, 
                        engine = engine, 
                        language = language, 
                        naf_version = naf_version, 
                        dtd_validation = dtd_validation)
    tree.write(output, "xml")


def generate_naf(input: str, 
                 engine: str, 
                 language: str, 
                 naf_version: str, 
                 dtd_validation: bool,
                 params: dict = {}):
    """
    """
    params['naf_version'] = naf_version
    params['dtd_validation'] = dtd_validation
    params['creationtime'] = datetime.now()
    params['uri'] = input
    params['language'] = language
    params['title'] = None

    if engine.lower() == 'stanza':
        params['engine'] = stanzaProcessor(language)
    elif engine.lower() == 'spacy':
        params['engine'] = spacyProcessor(language)

    params['linguistic_layers'] = ['raw', 'text', 'terms', 'entities', 'deps']
    params['cdata'] = True
    params['map_udpos2naf_pos'] = False
    params['layer_to_attributes_to_ignore'] = {'terms' : {'morphofeat', 'type'}}  # this will not add these attributes to the term element
    params['replace_hidden_characters'] = True
    params['add_mws'] = False
    params['comments'] = True

    if input[-3:].lower()=='txt':
        with open(input) as f:
            params['text'] = f.read()
    elif input[-3:].lower()=='pdf':
        params['preprocess_layers'] = ['xml']
        #params['preprocess_processor'] = preprocessprocessor.PDFMiner()
        params['xml'] = convert_pdf(input, format='xml', params=params)
        params['text'] = convert_pdf(input, format='text', params=params)
    
    text = params['text']
    if params['replace_hidden_characters']:
        text_to_use = text.translate(hidden_table)
    else:
        text_to_use = text
    assert len(text) == len(text_to_use)

    params['start_time'] = datetime.now()
    params['doc'] = params['engine'].nlp(text_to_use)
    params['end_time'] = datetime.now()
    
    process_linguistic_layers(params['doc'], params)

    # check it lengths match
    doc_text = params['engine'].document_text(params['doc'])
    raw_layer = params['tree'].raw_layer
    assert raw_layer.strip() == doc_text.strip(), f'{len(raw_layer)} - {len(doc_text)}'
    assert raw_layer.strip() == text_to_use.strip(), f'{len(raw_layer)} - {len(text_to_use)}'

    # validate naf tree
    if params['dtd_validation'] is True:
        params['tree'].validate()

    return params['tree']


def process_linguistic_layers(doc, 
                              params: dict):
    """
    """
    layers = params['linguistic_layers']
    params['tree'] = NafDocument(params)

    if params['xml']:
        add_xml_layer(params)

    if 'entities' in layers:
        add_entities_layer(params)

    if 'text' in layers:
        add_text_layer(params)

    if 'terms' in layers:
        add_terms_layer(params)

    if 'deps' in layers:
        add_deps_layer(params)

    if 'chunks' in layers:
        add_chunks_layer(params)

    if 'raw' in layers:
        add_raw_layer(params)


def entities_generator(doc, 
                       params: dict):
    """
    """
    engine = params['engine']
    for ent in engine.document_entities(doc):
        yield Entity(start=engine.entity_span_start(ent),
                     end=engine.entity_span_end(ent),
                     type=engine.entity_type(ent))


def chunks_for_doc(doc, 
                   params: dict):
    """
    """
    for chunk in params['engine'].document_noun_chunks(doc):
        if chunk.root.head.pos_ == 'ADP':
            span = doc[chunk.start-1:chunk.end]
            yield (span, 'PP')
        yield (chunk, 'NP')


def chunk_tuples_for_doc(doc, 
                         params: dict):
    """
    """
    for i, (chunk, phrase) in enumerate(chunks_for_doc(doc, params)):
        yield ChunkElement(cid='c'+str(i),
                           head='t'+str(chunk.root.i),
                           phrase=phrase,
                           text=remove_illegal_chars(chunk.orth_.replace('\n',' ')),
                           targets=['t'+str(tok.i) for tok in chunk])


def dependencies_to_add(sentence, 
                        token, 
                        total_tokens: int, 
                        params: dict):
    """
    """
    engine = params['engine']
    deps = list()
    cor = engine.offset_token_index()

    while engine.token_head_index(sentence, token) != engine.token_index(token):
        from_term = 't' + str(engine.token_head_index(sentence, token) + total_tokens + cor)
        to_term = 't' + str(engine.token_index(token) + total_tokens + cor)
        rfunc = engine.token_dependency(token)
        from_orth = engine.token_orth(token)
        to_orth = engine.token_orth(engine.token_head(sentence, token))
        dep_data = DependencyRelation(from_term = from_term,
                                      to_term = to_term,
                                      rfunc = rfunc,
                                      from_orth = from_orth,
                                      to_orth = to_orth)
        deps.append(dep_data)
        token = engine.token_head(sentence, token)
    return deps


def add_entities_layer(params: dict):
    """
    """
    tree = params['tree'].tree
    doc = params['doc']
    engine = params['engine']
    layers = params['linguistic_layers']

    current_entity = list()       # Use a list for multiword entities.
    current_entity_orth = list()  # id.

    current_token: int = 1    # Keep track of the token number.
    term_number: int = 1      # Keep track of the term number.
    entity_number: int = 1    # Keep track of the entity number.
    total_tokens: int = 0

    parsing_entity: bool = False # State change: are we working on a term or not?

    for sentence_number, sentence in enumerate(engine.document_sentences(doc), start = 1):
        
        entity_gen = entities_generator(sentence, params)
        try:
            next_entity = next(entity_gen)
        except StopIteration:
            next_entity = Entity(start=None, end=None, type=None)

        for token_number, token in enumerate(engine.sentence_tokens(sentence), start=current_token):
            # Do we need a state change?

            if token_number == next_entity.start:
                parsing_entity = True
            
            tid = 't' + str(term_number)
            if parsing_entity:
                current_entity.append(tid)
                current_entity_orth.append(normalize_token_orth(engine.token_orth(token)))

            # Move to the next term
            term_number += 1

            if parsing_entity and token_number == next_entity.end:
                # Create new entity ID.
                entity_id = 'e' + str(entity_number)
                # Create Entity data:
                entity_data = EntityElement(id=entity_id,
                                            type=next_entity.type,
                                            targets=current_entity,
                                            text=current_entity_orth,
                                            ext_refs=list())  # entity linking currently not part of spaCy

                params['tree'].add_entity_element(entity_data, params)

                entity_number += 1
                current_entity = list()
                current_entity_orth = list()
                # Move to the next entity
                parsing_entity = False
                try:
                    next_entity = next(entity_gen)
                except StopIteration:
                    # No more entities...
                    next_entity = Entity(start=None, end=None, type=None)

        # At the end of the sentence, add all the dependencies to the XML structure.
        if engine.token_reset() == False:
            current_token = token_number + 1
            total_tokens = 0
        else:
            current_token = 1
            total_tokens += token_number

    return None


def add_text_layer(params: dict):
    """
    """
    root = params['tree'].root

    pages_offset = None
    xml = params['tree']._xml_layer
    if xml is not None:
        pages_offset = [int(page.get('offset')) for page in xml]

    doc = params['doc']
    engine = params['engine']
    layers = params['linguistic_layers']

    current_token: int = 1    
    total_tokens: int = 0
    current_page: int = 0

    for sentence_number, sentence in enumerate(engine.document_sentences(doc), start=1):

        for token_number, token in enumerate(engine.sentence_tokens(sentence), start=current_token):

            if (pages_offset is not None) and (current_page < len(pages_offset)):
                if engine.token_offset(token) >= pages_offset[current_page]:
                    current_page += 1

            wid = 'w' + str(token_number + total_tokens)
            wf_data = WordformElement(page=str(current_page),
                                      sent=str(sentence_number),
                                      id=wid,
                                      length=str(len(token.text)),
                                      wordform=token.text,
                                      offset=str(engine.token_offset(token)))

            params['tree'].add_wf_element(wf_data, params)

        if engine.token_reset() is False:
            current_token = token_number + 1
            total_tokens = 0
        else:
            current_token = 1
            total_tokens += token_number

    return None


def add_terms_layer(params: dict):
    """
    """
    doc = params['doc']
    engine = params['engine']
    layers = params['linguistic_layers']

    current_term = list()       # Use a list for multiword expressions.
    current_term_orth = list()  # id.

    current_token: int = 1    # Keep track of the token number.
    term_number: int = 1      # Keep track of the term number.
    total_tokens: int = 0

    for sentence_number, sentence in enumerate(engine.document_sentences(doc), start=1):

        for token_number, token in enumerate(engine.sentence_tokens(sentence), start=current_token):

            wid = 'w' + str(token_number + total_tokens)
            tid = 't' + str(term_number)

            current_term.append(wid)
            current_term_orth.append(normalize_token_orth(engine.token_orth(token)))

            # Create TermElement data:
            spacy_pos = engine. token_pos(token)
            # :param bool map_udpos2naf_pos: if True, we use "udpos2nafpos_info"
            # to map the Universal Dependencies pos (https://universaldependencies.org/u/pos/)
            # to the NAF pos tagset
            if params['map_udpos2naf_pos']:
                if spacy_pos in udpos2nafpos_info:
                    pos = udpos2nafpos_info[spacy_pos]['naf_pos']
                    pos_type = udpos2nafpos_info[spacy_pos]['class']
                else:
                    pos = 'O'
                    pos_type = 'open'
            else:
                pos = spacy_pos
                pos_type = 'open'

            term_data = TermElement(id=tid,
                                    lemma=remove_illegal_chars(engine.token_lemma(token)),
                                    pos=pos,
                                    type=pos_type,
                                    morphofeat=engine.token_tag(token),
                                    targets=current_term,
                                    text=current_term_orth)

            params['tree'].add_term_element(term_data, params)

            # Move to the next term
            term_number += 1
            current_term = list()
            current_term_orth = list()

        # At the end of the sentence, add all the dependencies to the XML structure.
        if engine.token_reset() is False:
            current_token = token_number + 1
            total_tokens = 0
        else:
            current_token = 1
            total_tokens += token_number

    return None


def add_deps_layer(params: dict):
    """
    """
    engine = params['engine']

    current_token: int = 1
    total_tokens: int = 0

    for sent in engine.document_sentences(params['doc']):

        dependencies_for_sentence = list()

        for token_number, token in enumerate(engine.sentence_tokens(sent), start=current_token):
            for dep_data in dependencies_to_add(sent, token, total_tokens, params):
                if dep_data not in dependencies_for_sentence:
                    dependencies_for_sentence.append(dep_data)

        for dep_data in dependencies_for_sentence:
            params['tree'].add_dependency_element(dep_data, params)

        if engine.token_reset() is False:
            current_token = token_number + 1
            total_tokens = 0
        else:
            current_token = 1
            total_tokens += token_number

        if params['add_mws']:
            params['tree'].add_multi_words(params)

    return None


def add_raw_layer(params: dict):
    """
    """
    params['tree'].add_raw_text_element(params)


def add_chunks_layer(params: dict):
    """
    """
    for chunk_data in chunk_tuples_for_doc(params['doc'], params):
        params['tree'].add_chunk_element(chunk_data, params)


def add_xml_layer(params: dict):
    """
    """
    params['tree'].add_xml_element(params)


if __name__ == '__main__':
    sys.exit(parse())
