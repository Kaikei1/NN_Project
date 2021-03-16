# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 14:17:47 2021

@author: Nicho
"""

import datasets
logger = datasets.logging.get_logger(__name__)
class pos_positionConfig(datasets.BuilderConfig):
    """BuilderConfig for Conll2003"""

    def __init__(self, **kwargs):
        """BuilderConfig forConll2003.

        Args:
          **kwargs: keyword arguments forwarded to super.
        """
        super(pos_positionConfig, self).__init__(**kwargs)

        
class pos_position(datasets.GeneratorBasedBuilder):
    BUILDER_CONFIGS = [
        pos_positionConfig(name="sample", version=datasets.Version("1.0.0"), description="Conll2003 dataset"),
    ]  
    def _info(self):
        return datasets.DatasetInfo(
                features=datasets.Features(
                        {
                    "position": datasets.Value("string"),
#                    "word": datasets.Value("string"),
                    "posTag": datasets.Value("string")#datasets.Sequence(
#                        datasets.features.ClassLabel(
#                            names=[
#                                '"',
#                                "''",
#                                "#",
#                                "$",
#                                "(",
#                                ")",
#                                ",",
#                                ".",
#                                ":",
#                                "``",
#                                "CC",
#                                "CD",
#                                "DT",
#                                "EX",
#                                "FW",
#                                "IN",
#                                "JJ",
#                                "JJR",
#                                "JJS",
#                                "LS",
#                                "MD",
#                                "NN",
#                                "NNP",
#                                "NNPS",
#                                "NNS",
#                                "NN|SYM",
#                                "PDT",
#                                "POS",
#                                "PRP",
#                                "PRP$",
#                                "RB",
#                                "RBR",
#                                "RBS",
#                                "RP",
#                                "SYM",
#                                "TO",
#                                "UH",
#                                "VB",
#                                "VBD",
#                                "VBG",
#                                "VBN",
#                                "VBP",
#                                "VBZ",
#                                "WDT",
#                                "WP",
#                                "WP$",
#                                "WRB",
#                            ]
#                        )
#                    ),
                }
            ),                            
                supervised_keys=None,
                homepage="https://github.com/Kaikei1/NN_Project"
                )
                
    def _split_generators(self, dl_manager: datasets.DownloadManager):
        return [
            datasets.SplitGenerator(name=datasets.Split.TRAIN, gen_kwargs={"filepath": 'sample.tsv'}),
        ]
        
    def _generate_examples(self, filepath):
        logger.info("generating examples from = %s", filepath)
        with open(filepath, encoding="utf-8") as f:
            for line in f:
                if line[0]=='*':
                    pass
                else:
                    line = line.split()
                    position = line[0]
                    word = line[1]
                    posTag = line[2]
                    yield word, {
                        "position": position,
                        "posTag": posTag
                        }





            

               

