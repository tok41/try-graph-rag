"""
spaCyを使ううえでのhelper関数
"""

import itertools
from typing import Dict, List


HEAD_DEPS = {"nsubj", "nsubjpass", "dobj", "pobj", "attr"}
NOUN_POS = {"NOUN", "PROPN"}
MODIFIER_DEPS = {"compound", "amod"}
VERB_POS = {"VERB", "AUX"}
VERB_DEP = {"ROOT", "conj", "acl"}
SUBJ_DEPS = {"nsubj", "nsubjpass"}
OBJ_DEPS = {"dobj", "attr"}


def get_noun_phrase_map(doc) -> dict:
    """文章中の名詞句を抽出する
    """
    noun_map = {}
    for token in doc:
        if (token.dep_ in HEAD_DEPS) and (token.pos_ in NOUN_POS):
            modifiers = [child for child in token.lefts if child.dep_ in MODIFIER_DEPS]
            noun_parts = sorted(modifiers + [token], key=lambda t: t.i)
            phrase = " ".join(tok.lemma_ for tok in noun_parts)
            noun_map[token] = phrase
    return noun_map


def get_svo_from_sentence(sentence, noun_map: Dict) -> List[dict]:
    """
    １文から SVO の3つ組（トリプル）を抽出する

    - Main SVO:
        subject: nsubj/nsubjpass (acl verbの場合は head 名詞を補助で採用)
        verb: verb lemma
        object: dobj/attr

    - 前置詞 triples:
        subject: same as above
        verb: verb_lemma + "_" + prep.text  (e.g., use_for)
        object: pobj of prep
    """
    svos: List[dict] = []

    for verb in sentence:  # 文中の動詞をキーにしてSVO構造を抽出する
        if not (verb.dep_ in VERB_DEP and verb.pos_ in VERB_POS):
            continue

        # --- subjects ---
        subjects = [c for c in verb.children if c.dep_ in SUBJ_DEPS]

        # acl動詞(名詞を修飾する動詞)で主語が見つからない場合、修飾先名詞(verb.head)を主語にする
        if not subjects and verb.dep_ == "acl":
            head = verb.head
            if head.pos_ in NOUN_POS:
                subjects = [head]

        subject_phrases = [noun_map.get(s, s.lemma_) for s in subjects]
        if not subject_phrases:
            # 主語がない動詞はスキップ
            # ここでは knowledge graph を作りたいので、トリプルを抽出したいので
            continue

        # --- direct objects / attributes ---
        objects = [c for c in verb.children if c.dep_ in OBJ_DEPS]
        object_phrases = [noun_map.get(o, o.lemma_) for o in objects]

        # 主語×目的語のメイントリプル
        svos.extend(
            {
                "subject": s,
                "verb": verb.lemma_,
                "object": o
            }
            for s, o in itertools.product(subject_phrases, object_phrases)
        )

        # --- 前置詞 objects ---
        preps = [c for c in verb.children if c.dep_ == "prep"]
        for prep in preps:
            pobj_tokens = [c for c in prep.children if c.dep_ == "pobj"]
            pp_objects = [noun_map.get(p, p.lemma_) for p in pobj_tokens]
            if not pp_objects:
                continue
            verb_prep = f"{verb.lemma_}_{prep.text}"  # 前置詞の場合は、Vをこの形にする
            svos.extend(
                {
                    "subject": s,
                    "verb": verb_prep,
                    "object": o
                }
                for s, o in itertools.product(subject_phrases, pp_objects)
            )

    return svos
