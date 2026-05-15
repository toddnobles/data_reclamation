# NER Preliminary results

## Flair
--- RapidFuzz NER Evaluation: flair_test ---
Ground Truth: ner_tests/undergrad_ground_truths/eden_gts
Distance Threshold: 2
-------------------------------------------------------------------------------------------------------------------------------------------------
FILE                                                                        | MATCH (TP)   | MISS (FN)    | ERROR (FP)   | RECALL   | PRECISION
-------------------------------------------------------------------------------------------------------------------------------------------------
NARA_1324_v1_p184-185_1_0                                                   | 17           | 40           | 90           |    29.8% |    15.9%
NARA_1327_b032_f1516                                                        | 2            | 1            | 3            |    66.7% |    40.0%
NARA_1327_b059_f2943                                                        | 2            | 1            | 1            |    66.7% |    66.7%
NARA_1329_b011_c00_0052                                                     | 2            | 0            | 0            |   100.0% |   100.0%
NARA_1329_b011_c00_0087                                                     | 2            | 0            | 0            |   100.0% |   100.0%
NARA_1329_b011_c00_0088                                                     | 2            | 0            | 0            |   100.0% |   100.0%
NARA_1329_b011_c00_0585                                                     | 2            | 0            | 0            |   100.0% |   100.0%
NARA_1329_b011_c00_0633                                                     | 1            | 0            | 1            |   100.0% |    50.0%
NARA_1329_b014_c00_0440                                                     | 1            | 0            | 0            |   100.0% |   100.0%
WA_Cush_NARA_2645385_Agapith_Johnnie_Redacted_shrunk_pdf                    | 15           | 9            | 24           |    62.5% |    38.5%
WA_Cush_NARA_2645385_Allen_Fray_Redacted_shrunk_pdf                         | 6            | 2            | 8            |    75.0% |    42.9%
WA_Cush_NARA_2645385_Atkins_Joseph_Redacted_shrunk_pdf                      | 9            | 8            | 20           |    52.9% |    31.0%
WA_Cush_NARA_2645385_Bernard_Mary_shrunk_pdf                                | 0            | 2            | 4            |     0.0% |     0.0%
WA_Cush_NARA_2645385_Boyd_Hazel_Redacted_shrunk_pdf                         | 6            | 6            | 16           |    50.0% |    27.3%
WA_Cush_NARA_2645385_Boyd_Samuel_Redacted_shrunk_pdf                        | 13           | 10           | 15           |    56.5% |    46.4%
WA_Cush_NARA_2645385_Brooks_Dick_Simon_Redacted_shrunk_pdf                  | 8            | 7            | 5            |    53.3% |    61.5%
WA_Cush_NARA_2645385_Chamberlain_Wallace_shrunk_pdf                         | 0            | 1            | 2            |     0.0% |     0.0%
WA_Cush_NARA_2645385_Charley_Benjamin_Redacted_shrunk_pdf                   | 12           | 5            | 14           |    70.6% |    46.2%
WA_Cush_NARA_2645385_Charley_Grace_Redacted_shrunk_pdf                      | 5            | 3            | 4            |    62.5% |    55.6%
WA_Cush_NARA_2645385_Chenois_Rose_Redacted_shrunk_pdf                       | 3            | 12           | 4            |    20.0% |    42.9%
WA_Cush_NARA_2645385_Clark_Emma_shrunk_pdf                                  | 5            | 3            | 3            |    62.5% |    62.5%
WA_Cush_NARA_2645385_Clark_Faustine                                         | 2            | 1            | 0            |    66.7% |   100.0%
WA_Cush_NARA_2645385_Crofoot_Earl_Redacted_shrunk_pdf                       | 23           | 15           | 17           |    60.5% |    57.5%
WA_Cush_NARA_2645385_Dave_Willie_Redacted_shrunk_pdf                        | 14           | 17           | 24           |    45.2% |    36.8%
WA_Cush_NARA_2645385_Dupuis_Bert_shrunk_pdf                                 | 0            | 0            | 2            |     0.0% |     0.0%
WA_Cush_NARA_2645385_Frank_Margaret_Redacted_shrunk_pdf                     | 4            | 8            | 13           |    33.3% |    23.5%
WA_Cush_NARA_2645385_Goodman_Alfred_Redacted_shrunk_pdf                     | 7            | 6            | 10           |    53.8% |    41.2%
WA_Cush_NARA_2645385_Gunnier_Bessie_shrunk_pdf                              | 1            | 0            | 1            |   100.0% |    50.0%
WA_Cush_NARA_2645385_Hammer_Leo_Paul_Redacted_shrunk_pdf                    | 19           | 11           | 25           |    63.3% |    43.2%
WA_Cush_NARA_2645385_Henry_Ethel_E_Redacted_shrunk_pdf                      | 12           | 12           | 19           |    50.0% |    38.7%
WA_Cush_NARA_2645385_Henry_John_Redacted_shrunk_pdf                         | 9            | 2            | 2            |    81.8% |    81.8%
WA_Cush_NARA_2645385_Horn_Adeline_Redacted_shrunk_pdf                       | 1            | 1            | 1            |    50.0% |    50.0%
WA_Cush_NARA_2645385_Hunt_William_Redacted_shrunk_pdf                       | 15           | 27           | 36           |    35.7% |    29.4%
WA_Cush_NARA_2645385_James_Nancy_Redacted_shrunk_pdf                        | 7            | 6            | 12           |    53.8% |    36.8%
WA_Cush_NARA_2645385_Joseph_Joseph_Redacted_shrunk_pdf                      | 7            | 14           | 27           |    33.3% |    20.6%
WA_Cush_NARA_2645385_KingGeorge_Anita_Redacted_shrunk_pdf                   | 6            | 2            | 7            |    75.0% |    46.2%
WA_Cush_NARA_2645385_Legard_Edwin_Joseph_Redacted_shrunk_pdf                | 4            | 4            | 5            |    50.0% |    44.4%
WA_Cush_NARA_2645385_Lewis_Nina_Redacted_shrunk_pdf                         | 10           | 11           | 21           |    47.6% |    32.3%
WA_Cush_NARA_2645385_Martin_Eva_shrunk_pdf                                  | 0            | 1            | 1            |     0.0% |     0.0%
WA_Cush_NARA_2645385_Martin_Narcisse_Redacted_shrunk_pdf                    | 8            | 18           | 22           |    30.8% |    26.7%
WA_Cush_NARA_2645385_Martin_William_G_Redacted_shrunk_pdf                   | 13           | 9            | 25           |    59.1% |    34.2%
WA_Cush_NARA_2645385_McDonald_Harry_Redacted_shrunk_pdf                     | 8            | 12           | 13           |    40.0% |    38.1%
WA_Cush_NARA_2645385_McDonald_Margaret_Redacted_shrunk_pdf                  | 9            | 8            | 14           |    52.9% |    39.1%
WA_Cush_NARA_2645385_Michel_Henry_Redacted_shrunk_pdf                       | 19           | 18           | 19           |    51.4% |    50.0%
WA_Cush_NARA_2645385_Moses_Patsy_Redacted_shrunk_pdf                        | 30           | 23           | 37           |    56.6% |    44.8%
WA_Cush_NARA_2645385_Napolean_Edna_shrunk_pdf                               | 0            | 1            | 2            |     0.0% |     0.0%
WA_Cush_NARA_2645385_Nostrum_Fred_Redacted_shrunk_pdf                       | 13           | 11           | 28           |    54.2% |    31.7%
WA_Cush_NARA_2645385_Parriseau_Antoine_Redacted_shrunk_pdf                  | 16           | 15           | 19           |    51.6% |    45.7%
WA_Cush_NARA_2645385_Parriseau_Patrick_Redacted_shrunk_pdf                  | 30           | 24           | 35           |    55.6% |    46.2%
james_arquette                                                              | 2            | 0            | 0            |   100.0% |   100.0%
-------------------------------------------------------------------------------------------------------------------------------------------------
OVERALL CORPUS TOTALS                                                       | 402          | 387          | 651          |    51.0% |    38.2%
AVERAGE DOCUMENT SCORES                                                     | -            | -            | -            |    55.6% |    46.3%
-------------------------------------------------------------------------------------------------------------------------------------------------
Overall F1-Score (Corpus): 43.65%
Average F1-Score (Doc):    50.55%




## Gemma using olmocr OCR text
--- RapidFuzz NER Evaluation: gemma_test ---
Ground Truth: ner_tests/undergrad_ground_truths/eden_gts
Distance Threshold: 2
-------------------------------------------------------------------------------------------------------------------------------------------------
FILE                                                                        | MATCH (TP)   | MISS (FN)    | ERROR (FP)   | RECALL   | PRECISION
-------------------------------------------------------------------------------------------------------------------------------------------------
NARA_1324_v1_p184-185_1_0                                                   | 18           | 39           | 84           |    31.6% |    17.6%
NARA_1327_b032_f1516                                                        | 2            | 1            | 2            |    66.7% |    50.0%
NARA_1327_b059_f2943                                                        | 2            | 1            | 1            |    66.7% |    66.7%
NARA_1329_b011_c00_0052                                                     | 2            | 0            | 0            |   100.0% |   100.0%
NARA_1329_b011_c00_0087                                                     | 2            | 0            | 0            |   100.0% |   100.0%
NARA_1329_b011_c00_0088                                                     | 2            | 0            | 0            |   100.0% |   100.0%
NARA_1329_b011_c00_0585                                                     | 2            | 0            | 0            |   100.0% |   100.0%
NARA_1329_b011_c00_0633                                                     | 1            | 0            | 1            |   100.0% |    50.0%
NARA_1329_b014_c00_0440                                                     | 1            | 0            | 0            |   100.0% |   100.0%
WA_Cush_NARA_2645385_Agapith_Johnnie_Redacted_shrunk_pdf                    | 8            | 16           | 10           |    33.3% |    44.4%
WA_Cush_NARA_2645385_Allen_Fray_Redacted_shrunk_pdf                         | 5            | 3            | 4            |    62.5% |    55.6%
WA_Cush_NARA_2645385_Atkins_Joseph_Redacted_shrunk_pdf                      | 8            | 9            | 6            |    47.1% |    57.1%
WA_Cush_NARA_2645385_Bernard_Mary_shrunk_pdf                                | 1            | 1            | 3            |    50.0% |    25.0%
WA_Cush_NARA_2645385_Boyd_Hazel_Redacted_shrunk_pdf                         | 5            | 7            | 8            |    41.7% |    38.5%
WA_Cush_NARA_2645385_Boyd_Samuel_Redacted_shrunk_pdf                        | 9            | 14           | 4            |    39.1% |    69.2%
WA_Cush_NARA_2645385_Brooks_Dick_Simon_Redacted_shrunk_pdf                  | 7            | 8            | 1            |    46.7% |    87.5%
WA_Cush_NARA_2645385_Chamberlain_Wallace_shrunk_pdf                         | 0            | 1            | 1            |     0.0% |     0.0%
WA_Cush_NARA_2645385_Charley_Benjamin_Redacted_shrunk_pdf                   | 10           | 7            | 6            |    58.8% |    62.5%
WA_Cush_NARA_2645385_Charley_Grace_Redacted_shrunk_pdf                      | 3            | 5            | 2            |    37.5% |    60.0%
WA_Cush_NARA_2645385_Chenois_Rose_Redacted_shrunk_pdf                       | 3            | 12           | 3            |    20.0% |    50.0%
WA_Cush_NARA_2645385_Clark_Emma_shrunk_pdf                                  | 4            | 4            | 1            |    50.0% |    80.0%
WA_Cush_NARA_2645385_Clark_Faustine                                         | 2            | 1            | 0            |    66.7% |   100.0%
WA_Cush_NARA_2645385_Crofoot_Earl_Redacted_shrunk_pdf                       | 21           | 17           | 10           |    55.3% |    67.7%
WA_Cush_NARA_2645385_Dave_Willie_Redacted_shrunk_pdf                        | 13           | 18           | 18           |    41.9% |    41.9%
WA_Cush_NARA_2645385_Dupuis_Bert_shrunk_pdf                                 | 0            | 0            | 2            |     0.0% |     0.0%
WA_Cush_NARA_2645385_Frank_Margaret_Redacted_shrunk_pdf                     | 4            | 8            | 9            |    33.3% |    30.8%
WA_Cush_NARA_2645385_Goodman_Alfred_Redacted_shrunk_pdf                     | 5            | 8            | 2            |    38.5% |    71.4%
WA_Cush_NARA_2645385_Gunnier_Bessie_shrunk_pdf                              | 1            | 0            | 1            |   100.0% |    50.0%
WA_Cush_NARA_2645385_Hammer_Leo_Paul_Redacted_shrunk_pdf                    | 9            | 21           | 4            |    30.0% |    69.2%
WA_Cush_NARA_2645385_Henry_Ethel_E_Redacted_shrunk_pdf                      | 11           | 13           | 9            |    45.8% |    55.0%
WA_Cush_NARA_2645385_Henry_John_Redacted_shrunk_pdf                         | 11           | 0            | 0            |   100.0% |   100.0%
WA_Cush_NARA_2645385_Horn_Adeline_Redacted_shrunk_pdf                       | 1            | 1            | 1            |    50.0% |    50.0%
WA_Cush_NARA_2645385_Hunt_William_Redacted_shrunk_pdf                       | 13           | 29           | 23           |    31.0% |    36.1%
WA_Cush_NARA_2645385_James_Nancy_Redacted_shrunk_pdf                        | 7            | 6            | 7            |    53.8% |    50.0%
WA_Cush_NARA_2645385_Joseph_Joseph_Redacted_shrunk_pdf                      | 4            | 17           | 8            |    19.0% |    33.3%
WA_Cush_NARA_2645385_KingGeorge_Anita_Redacted_shrunk_pdf                   | 6            | 2            | 4            |    75.0% |    60.0%
WA_Cush_NARA_2645385_Legard_Edwin_Joseph_Redacted_shrunk_pdf                | 4            | 4            | 3            |    50.0% |    57.1%
WA_Cush_NARA_2645385_Lewis_Nina_Redacted_shrunk_pdf                         | 9            | 12           | 10           |    42.9% |    47.4%
WA_Cush_NARA_2645385_Martin_Eva_shrunk_pdf                                  | 0            | 1            | 1            |     0.0% |     0.0%
WA_Cush_NARA_2645385_Martin_Narcisse_Redacted_shrunk_pdf                    | 5            | 21           | 17           |    19.2% |    22.7%
WA_Cush_NARA_2645385_Martin_William_G_Redacted_shrunk_pdf                   | 11           | 11           | 10           |    50.0% |    52.4%
WA_Cush_NARA_2645385_McDonald_Harry_Redacted_shrunk_pdf                     | 6            | 14           | 6            |    30.0% |    50.0%
WA_Cush_NARA_2645385_McDonald_Margaret_Redacted_shrunk_pdf                  | 8            | 9            | 8            |    47.1% |    50.0%
WA_Cush_NARA_2645385_Michel_Henry_Redacted_shrunk_pdf                       | 16           | 21           | 6            |    43.2% |    72.7%
WA_Cush_NARA_2645385_Moses_Patsy_Redacted_shrunk_pdf                        | 26           | 27           | 15           |    49.1% |    63.4%
WA_Cush_NARA_2645385_Napolean_Edna_shrunk_pdf                               | 1            | 0            | 0            |   100.0% |   100.0%
WA_Cush_NARA_2645385_Nostrum_Fred_Redacted_shrunk_pdf                       | 15           | 9            | 18           |    62.5% |    45.5%
WA_Cush_NARA_2645385_Parriseau_Antoine_Redacted_shrunk_pdf                  | 14           | 17           | 7            |    45.2% |    66.7%
WA_Cush_NARA_2645385_Parriseau_Patrick_Redacted_shrunk_pdf                  | 27           | 27           | 17           |    50.0% |    61.4%
james_arquette                                                              | 2            | 0            | 0            |   100.0% |   100.0%
-------------------------------------------------------------------------------------------------------------------------------------------------
OVERALL CORPUS TOTALS                                                       | 347          | 442          | 353          |    44.0% |    49.6%
AVERAGE DOCUMENT SCORES                                                     | -            | -            | -            |    53.6% |    58.4%
-------------------------------------------------------------------------------------------------------------------------------------------------
Overall F1-Score (Corpus): 46.61%
Average F1-Score (Doc):    55.90%


## NER STacked BERT
--- RapidFuzz NER Evaluation: ner_stacked_bert_test ---
Ground Truth: ner_tests/undergrad_ground_truths/eden_gts
Distance Threshold: 2
-------------------------------------------------------------------------------------------------------------------------------------------------
FILE                                                                        | MATCH (TP)   | MISS (FN)    | ERROR (FP)   | RECALL   | PRECISION
-------------------------------------------------------------------------------------------------------------------------------------------------
NARA_1324_v1_p184-185_1_0                                                   | 12           | 45           | 59           |    21.1% |    16.9%
NARA_1327_b032_f1516                                                        | 2            | 1            | 10           |    66.7% |    16.7%
NARA_1327_b059_f2943                                                        | 2            | 1            | 7            |    66.7% |    22.2%
NARA_1329_b011_c00_0052                                                     | 2            | 0            | 2            |   100.0% |    50.0%
NARA_1329_b011_c00_0087                                                     | 2            | 0            | 3            |   100.0% |    40.0%
NARA_1329_b011_c00_0088                                                     | 2            | 0            | 1            |   100.0% |    66.7%
NARA_1329_b011_c00_0585                                                     | 2            | 0            | 1            |   100.0% |    66.7%
NARA_1329_b011_c00_0633                                                     | 1            | 0            | 3            |   100.0% |    25.0%
NARA_1329_b014_c00_0440                                                     | 1            | 0            | 2            |   100.0% |    33.3%
WA_Cush_NARA_2645385_Agapith_Johnnie_Redacted_shrunk_pdf                    | 11           | 13           | 45           |    45.8% |    19.6%
WA_Cush_NARA_2645385_Allen_Fray_Redacted_shrunk_pdf                         | 4            | 4            | 28           |    50.0% |    12.5%
WA_Cush_NARA_2645385_Atkins_Joseph_Redacted_shrunk_pdf                      | 8            | 9            | 44           |    47.1% |    15.4%
WA_Cush_NARA_2645385_Bernard_Mary_shrunk_pdf                                | 1            | 1            | 3            |    50.0% |    25.0%
WA_Cush_NARA_2645385_Boyd_Hazel_Redacted_shrunk_pdf                         | 6            | 6            | 29           |    50.0% |    17.1%
WA_Cush_NARA_2645385_Boyd_Samuel_Redacted_shrunk_pdf                        | 15           | 8            | 23           |    65.2% |    39.5%
WA_Cush_NARA_2645385_Brooks_Dick_Simon_Redacted_shrunk_pdf                  | 6            | 9            | 23           |    40.0% |    20.7%
WA_Cush_NARA_2645385_Chamberlain_Wallace_shrunk_pdf                         | 0            | 1            | 2            |     0.0% |     0.0%
WA_Cush_NARA_2645385_Charley_Benjamin_Redacted_shrunk_pdf                   | 10           | 7            | 45           |    58.8% |    18.2%
WA_Cush_NARA_2645385_Charley_Grace_Redacted_shrunk_pdf                      | 5            | 3            | 10           |    62.5% |    33.3%
WA_Cush_NARA_2645385_Chenois_Rose_Redacted_shrunk_pdf                       | 2            | 13           | 11           |    13.3% |    15.4%
WA_Cush_NARA_2645385_Clark_Emma_shrunk_pdf                                  | 5            | 3            | 6            |    62.5% |    45.5%
WA_Cush_NARA_2645385_Clark_Faustine                                         | 2            | 1            | 6            |    66.7% |    25.0%
WA_Cush_NARA_2645385_Crofoot_Earl_Redacted_shrunk_pdf                       | 23           | 15           | 31           |    60.5% |    42.6%
WA_Cush_NARA_2645385_Dave_Willie_Redacted_shrunk_pdf                        | 14           | 17           | 36           |    45.2% |    28.0%
WA_Cush_NARA_2645385_Dupuis_Bert_shrunk_pdf                                 | 0            | 0            | 3            |     0.0% |     0.0%
WA_Cush_NARA_2645385_Frank_Margaret_Redacted_shrunk_pdf                     | 5            | 7            | 21           |    41.7% |    19.2%
WA_Cush_NARA_2645385_Goodman_Alfred_Redacted_shrunk_pdf                     | 4            | 9            | 25           |    30.8% |    13.8%
WA_Cush_NARA_2645385_Gunnier_Bessie_shrunk_pdf                              | 1            | 0            | 1            |   100.0% |    50.0%
WA_Cush_NARA_2645385_Hammer_Leo_Paul_Redacted_shrunk_pdf                    | 15           | 15           | 48           |    50.0% |    23.8%
WA_Cush_NARA_2645385_Henry_Ethel_E_Redacted_shrunk_pdf                      | 9            | 15           | 45           |    37.5% |    16.7%
WA_Cush_NARA_2645385_Henry_John_Redacted_shrunk_pdf                         | 5            | 6            | 17           |    45.5% |    22.7%
WA_Cush_NARA_2645385_Horn_Adeline_Redacted_shrunk_pdf                       | 0            | 2            | 4            |     0.0% |     0.0%
WA_Cush_NARA_2645385_Hunt_William_Redacted_shrunk_pdf                       | 19           | 23           | 62           |    45.2% |    23.5%
WA_Cush_NARA_2645385_James_Nancy_Redacted_shrunk_pdf                        | 3            | 10           | 20           |    23.1% |    13.0%
WA_Cush_NARA_2645385_Joseph_Joseph_Redacted_shrunk_pdf                      | 8            | 13           | 48           |    38.1% |    14.3%
WA_Cush_NARA_2645385_KingGeorge_Anita_Redacted_shrunk_pdf                   | 4            | 4            | 26           |    50.0% |    13.3%
WA_Cush_NARA_2645385_Legard_Edwin_Joseph_Redacted_shrunk_pdf                | 3            | 5            | 14           |    37.5% |    17.6%
WA_Cush_NARA_2645385_Lewis_Nina_Redacted_shrunk_pdf                         | 8            | 13           | 41           |    38.1% |    16.3%
WA_Cush_NARA_2645385_Martin_Eva_shrunk_pdf                                  | 0            | 1            | 1            |     0.0% |     0.0%
WA_Cush_NARA_2645385_Martin_Narcisse_Redacted_shrunk_pdf                    | 8            | 18           | 51           |    30.8% |    13.6%
WA_Cush_NARA_2645385_Martin_William_G_Redacted_shrunk_pdf                   | 13           | 9            | 42           |    59.1% |    23.6%
WA_Cush_NARA_2645385_McDonald_Harry_Redacted_shrunk_pdf                     | 9            | 11           | 26           |    45.0% |    25.7%
WA_Cush_NARA_2645385_McDonald_Margaret_Redacted_shrunk_pdf                  | 9            | 8            | 24           |    52.9% |    27.3%
WA_Cush_NARA_2645385_Michel_Henry_Redacted_shrunk_pdf                       | 16           | 21           | 36           |    43.2% |    30.8%
WA_Cush_NARA_2645385_Moses_Patsy_Redacted_shrunk_pdf                        | 33           | 20           | 84           |    62.3% |    28.2%
WA_Cush_NARA_2645385_Napolean_Edna_shrunk_pdf                               | 0            | 1            | 2            |     0.0% |     0.0%
WA_Cush_NARA_2645385_Nostrum_Fred_Redacted_shrunk_pdf                       | 12           | 12           | 41           |    50.0% |    22.6%
WA_Cush_NARA_2645385_Parriseau_Antoine_Redacted_shrunk_pdf                  | 15           | 16           | 27           |    48.4% |    35.7%
WA_Cush_NARA_2645385_Parriseau_Patrick_Redacted_shrunk_pdf                  | 28           | 26           | 66           |    51.9% |    29.8%
james_arquette                                                              | 1            | 1            | 2            |    50.0% |    33.3%
-------------------------------------------------------------------------------------------------------------------------------------------------
OVERALL CORPUS TOTALS                                                       | 366          | 423          | 1207         |    46.4% |    23.3%
AVERAGE DOCUMENT SCORES                                                     | -            | -            | -            |    50.1% |    24.2%
-------------------------------------------------------------------------------------------------------------------------------------------------
Overall F1-Score (Corpus): 30.99%
Average F1-Score (Doc):    32.63%




## On much smaller set of docs
--- RapidFuzz NER Evaluation: gemma_test ---
Ground Truth: ner_tests/ground_truth
Distance Threshold: 2
-------------------------------------------------------------------------------------------------------------------------------------------------
FILE                                                                        | MATCH (TP)   | MISS (FN)    | ERROR (FP)   | RECALL   | PRECISION
-------------------------------------------------------------------------------------------------------------------------------------------------
NARA_1327_b001_f005                                                         | 7            | 0            | 0            |   100.0% |   100.0%
NARA_RG75_91_b1117_33364                                                    | 23           | 1            | 1            |    95.8% |    95.8%
NARA_RG75_91_b1756_09452                                                    | 5            | 3            | 1            |    62.5% |    83.3%
annie_harris                                                                | 2            | 0            | 0            |   100.0% |   100.0%
daniel_varner                                                               | 1            | 0            | 1            |   100.0% |    50.0%
edward_spott                                                                | 2            | 1            | 0            |    66.7% |   100.0%
flora_ross                                                                  | 3            | 0            | 0            |   100.0% |   100.0%
-------------------------------------------------------------------------------------------------------------------------------------------------
OVERALL CORPUS TOTALS                                                       | 43           | 5            | 3            |    89.6% |    93.5%
AVERAGE DOCUMENT SCORES                                                     | -            | -            | -            |    89.3% |    89.9%
-------------------------------------------------------------------------------------------------------------------------------------------------
Overall F1-Score (Corpus): 91.49%
Average F1-Score (Doc):    89.58%

--- RapidFuzz NER Evaluation: flair_test ---
Ground Truth: ner_tests/ground_truth
Distance Threshold: 2
-------------------------------------------------------------------------------------------------------------------------------------------------
FILE                                                                        | MATCH (TP)   | MISS (FN)    | ERROR (FP)   | RECALL   | PRECISION
-------------------------------------------------------------------------------------------------------------------------------------------------
NARA_1327_b001_f005                                                         | 7            | 0            | 2            |   100.0% |    77.8%
NARA_RG75_91_b1117_33364                                                    | 22           | 2            | 9            |    91.7% |    71.0%
NARA_RG75_91_b1756_09452                                                    | 4            | 4            | 6            |    50.0% |    40.0%
annie_harris                                                                | 2            | 0            | 0            |   100.0% |   100.0%
daniel_varner                                                               | 1            | 0            | 0            |   100.0% |   100.0%
edward_spott                                                                | 2            | 1            | 0            |    66.7% |   100.0%
flora_ross                                                                  | 3            | 0            | 0            |   100.0% |   100.0%
-------------------------------------------------------------------------------------------------------------------------------------------------
OVERALL CORPUS TOTALS                                                       | 41           | 7            | 17           |    85.4% |    70.7%
AVERAGE DOCUMENT SCORES                                                     | -            | -            | -            |    86.9% |    84.1%
-------------------------------------------------------------------------------------------------------------------------------------------------
Overall F1-Score (Corpus): 77.36%
Average F1-Score (Doc):    85.48%


# Using Gemma as ground truth versus flair 
--- RapidFuzz NER Evaluation: flair_test ---
Ground Truth: ner_tests/outputs/gemma_test
Distance Threshold: 2
-------------------------------------------------------------------------------------------------------------------------------------------------
FILE                                                                        | MATCH (TP)   | MISS (FN)    | ERROR (FP)   | RECALL   | PRECISION
-------------------------------------------------------------------------------------------------------------------------------------------------
NARA_1324_v1_p184-185_1_0                                                   | 84           | 18           | 23           |    82.4% |    78.5%
NARA_1327_b001_f005                                                         | 7            | 0            | 2            |   100.0% |    77.8%
NARA_1327_b002_f0048_0                                                      | 13           | 3            | 18           |    81.2% |    41.9%
NARA_1327_b013_f0597_0                                                      | 2            | 4            | 5            |    33.3% |    28.6%
NARA_1327_b031_f1511_0                                                      | 11           | 5            | 6            |    68.8% |    64.7%
NARA_1327_b032_f1512                                                        | 3            | 0            | 0            |   100.0% |   100.0%
NARA_1327_b032_f1513                                                        | 5            | 0            | 1            |   100.0% |    83.3%
NARA_1327_b032_f1514                                                        | 2            | 0            | 0            |   100.0% |   100.0%
NARA_1327_b032_f1515                                                        | 3            | 1            | 2            |    75.0% |    60.0%
NARA_1327_b032_f1516                                                        | 3            | 1            | 2            |    75.0% |    60.0%
NARA_1327_b059_f2943                                                        | 3            | 0            | 0            |   100.0% |   100.0%
NARA_1327_b059_f2944                                                        | 3            | 0            | 0            |   100.0% |   100.0%
NARA_1327_b135_f5308                                                        | 2            | 2            | 1            |    50.0% |    66.7%
NARA_1327_b136_f5360                                                        | 9            | 1            | 1            |    90.0% |    90.0%
NARA_1327_b137_f5385_0                                                      | 1            | 1            | 3            |    50.0% |    25.0%
NARA_1327_b138_f5450                                                        | 11           | 3            | 8            |    78.6% |    57.9%
NARA_1327_b139_f5487                                                        | 11           | 4            | 12           |    73.3% |    47.8%
NARA_1328_b001_c00b_0019                                                    | 4            | 1            | 0            |    80.0% |   100.0%
NARA_1328_b003_c00s_0145                                                    | 3            | 0            | 0            |   100.0% |   100.0%
NARA_1328_b005_c00h_0009                                                    | 2            | 0            | 0            |   100.0% |   100.0%
NARA_1328_b006_c00n_0008                                                    | 1            | 0            | 1            |   100.0% |    50.0%
NARA_1328_b006_c00o_0001                                                    | 3            | 2            | 4            |    60.0% |    42.9%
NARA_1329_b001_c00b_0017                                                    | 2            | 0            | 0            |   100.0% |   100.0%
NARA_1329_b001_c00l_0032                                                    | 2            | 0            | 0            |   100.0% |   100.0%
NARA_1329_b002_c00w_0080_0                                                  | 2            | 0            | 0            |   100.0% |   100.0%
NARA_1329_b003_c00o_0001_0                                                  | 2            | 0            | 0            |   100.0% |   100.0%
NARA_1329_b003_c00s_0007                                                    | 2            | 0            | 0            |   100.0% |   100.0%
NARA_1329_b004_c00h_0013                                                    | 2            | 0            | 0            |   100.0% |   100.0%
NARA_1329_b004_c00n_0005                                                    | 1            | 1            | 0            |    50.0% |   100.0%
NARA_1329_b006_c00a_0073                                                    | 2            | 0            | 0            |   100.0% |   100.0%
NARA_1329_b008_c00r_0093                                                    | 3            | 0            | 0            |   100.0% |   100.0%
NARA_1329_b009_c00_0029                                                     | 0            | 1            | 1            |     0.0% |     0.0%
NARA_1329_b011_c00_0052                                                     | 2            | 0            | 0            |   100.0% |   100.0%
NARA_1329_b011_c00_0087                                                     | 2            | 0            | 0            |   100.0% |   100.0%
NARA_1329_b011_c00_0088                                                     | 2            | 0            | 0            |   100.0% |   100.0%
NARA_1329_b011_c00_0585                                                     | 2            | 0            | 0            |   100.0% |   100.0%
NARA_1329_b011_c00_0633                                                     | 2            | 0            | 0            |   100.0% |   100.0%
NARA_1329_b014_c00_0440                                                     | 1            | 0            | 0            |   100.0% |   100.0%
NARA_1329_b014_c00_0608                                                     | 3            | 0            | 0            |   100.0% |   100.0%
NARA_1344B_graduatelist                                                     | 640          | 27           | 119          |    96.0% |    84.3%
NARA_RG75_91_b1117_33364                                                    | 21           | 3            | 10           |    87.5% |    67.7%
NARA_RG75_91_b1756_09452                                                    | 2            | 4            | 8            |    33.3% |    20.0%
NARA_RG75_91_b1996_59565                                                    | 3            | 2            | 6            |    60.0% |    33.3%
WA_Cush_NARA_2645372_Attendance_1920_PG_JT_Redacted_shrunk_pdf              | 6            | 23           | 36           |    20.7% |    14.3%
WA_Cush_NARA_2645372_Pupil_Lists_1917_1918_shrunk_pdf                       | 0            | 68           | 114          |     0.0% |     0.0%
WA_Cush_NARA_2645385_Abbott_John_1919_Redacted_shrunk_pdf                   | 15           | 5            | 17           |    75.0% |    46.9%
WA_Cush_NARA_2645385_Adams_Caleb_1919_Redacted_shrunk_pdf                   | 10           | 1            | 8            |    90.9% |    55.6%
WA_Cush_NARA_2645385_Agapith_Johnnie_Redacted_shrunk_pdf                    | 16           | 2            | 23           |    88.9% |    41.0%
WA_Cush_NARA_2645385_Allen_Abraham_1919_Redacted_shrunk_pdf                 | 7            | 0            | 2            |   100.0% |    77.8%
WA_Cush_NARA_2645385_Allen_Alice_1917_Redacted_shrunk_pdf                   | 6            | 0            | 5            |   100.0% |    54.5%
WA_Cush_NARA_2645385_Allen_Fray_Redacted_shrunk_pdf                         | 8            | 1            | 6            |    88.9% |    57.1%
WA_Cush_NARA_2645385_Anderson_James_1919                                    | 1            | 0            | 0            |   100.0% |   100.0%
WA_Cush_NARA_2645385_Anderson_James_1919_shrunk_pdf                         | 1            | 0            | 0            |   100.0% |   100.0%
WA_Cush_NARA_2645385_Andrews_Christine_Redacted_shrunk_pdf                  | 1            | 0            | 0            |   100.0% |   100.0%
WA_Cush_NARA_2645385_Andy_Amos_Redacted_shrunk_pdf                          | 6            | 0            | 7            |   100.0% |    46.2%
WA_Cush_NARA_2645385_Atkins_Joseph_Redacted_shrunk_pdf                      | 12           | 2            | 17           |    85.7% |    41.4%
WA_Cush_NARA_2645385_Ayaganak_Bessie_shrunk_pdf (1)                         | 2            | 2            | 2            |    50.0% |    50.0%
WA_Cush_NARA_2645385_Ayaganak_Bessie_shrunk_pdf                             | 2            | 2            | 2            |    50.0% |    50.0%
WA_Cush_NARA_2645385_Beauvais_Alex_Redacted_shrunk_pdf                      | 12           | 5            | 48           |    70.6% |    20.0%
WA_Cush_NARA_2645385_Bennett_Barton_shrunk_pdf                              | 1            | 0            | 0            |   100.0% |   100.0%
WA_Cush_NARA_2645385_Bennett_Clara_Redacted_shrunk_pdf                      | 8            | 3            | 9            |    72.7% |    47.1%
WA_Cush_NARA_2645385_Benson_Elsie_Redacted_shrunk_pdf                       | 12           | 3            | 30           |    80.0% |    28.6%
WA_Cush_NARA_2645385_Benson_Horsley_Redacted_shrunk_pdf                     | 8            | 3            | 15           |    72.7% |    34.8%
WA_Cush_NARA_2645385_Benson_Kelly_Redacted_shrunk_pdf                       | 9            | 2            | 6            |    81.8% |    60.0%
WA_Cush_NARA_2645385_Bercie_Isabel_Redacted_shrunk_pdf                      | 12           | 1            | 2            |    92.3% |    85.7%
WA_Cush_NARA_2645385_Bercie_Vera_Redacted_shrunk_pdf                        | 9            | 0            | 0            |   100.0% |   100.0%
WA_Cush_NARA_2645385_Bernard_Alfred_shrunk_pdf                              | 0            | 1            | 2            |     0.0% |     0.0%
WA_Cush_NARA_2645385_Bernard_Isabel_shrunk_pdf                              | 0            | 2            | 2            |     0.0% |     0.0%
WA_Cush_NARA_2645385_Bernard_Mary_shrunk_pdf                                | 3            | 1            | 1            |    75.0% |    75.0%
WA_Cush_NARA_2645385_Bernard_Theodolina                                     | 0            | 2            | 4            |     0.0% |     0.0%
WA_Cush_NARA_2645385_Bernard_Theodolina_shrunk_pdf                          | 1            | 2            | 2            |    33.3% |    33.3%
WA_Cush_NARA_2645385_Bernard_Theresa_Redacted_shrunk_pdf                    | 16           | 5            | 20           |    76.2% |    44.4%
WA_Cush_NARA_2645385_Bill_Raymond_Redacted_shrunk_pdf                       | 6            | 0            | 12           |   100.0% |    33.3%
WA_Cush_NARA_2645385_Blair_George_Redacted_shrunk_pdf                       | 5            | 0            | 0            |   100.0% |   100.0%
WA_Cush_NARA_2645385_Blair_Lily_Redacted_shrunk_pdf                         | 16           | 3            | 15           |    84.2% |    51.6%
WA_Cush_NARA_2645385_Boyd_Hazel_Redacted_shrunk_pdf                         | 10           | 3            | 12           |    76.9% |    45.5%
WA_Cush_NARA_2645385_Boyd_Samuel_Redacted_shrunk_pdf                        | 12           | 1            | 16           |    92.3% |    42.9%
WA_Cush_NARA_2645385_Brooks_Dick_Simon_Redacted_shrunk_pdf                  | 8            | 0            | 5            |   100.0% |    61.5%
WA_Cush_NARA_2645385_Brown_Lizzie_Redacted_shrunk_pdf                       | 17           | 5            | 16           |    77.3% |    51.5%
WA_Cush_NARA_2645385_Burnard_Alex_Redacted_shrunk_pdf                       | 9            | 0            | 2            |   100.0% |    81.8%
WA_Cush_NARA_2645385_Caisse_Byron_Redacted_shrunk_pdf                       | 16           | 3            | 19           |    84.2% |    45.7%
WA_Cush_NARA_2645385_Caisse_Constance_shrunk_pdf                            | 0            | 1            | 0            |     0.0% |     0.0%
WA_Cush_NARA_2645385_Caisse_Gertrude_shrunk_pdf                             | 0            | 1            | 2            |     0.0% |     0.0%
WA_Cush_NARA_2645385_Chamberlain_Carmen_shrunk_pdf                          | 0            | 2            | 2            |     0.0% |     0.0%
WA_Cush_NARA_2645385_Chamberlain_Wallace                                    | 0            | 1            | 2            |     0.0% |     0.0%
WA_Cush_NARA_2645385_Chamberlain_Wallace_shrunk_pdf                         | 0            | 1            | 2            |     0.0% |     0.0%
WA_Cush_NARA_2645385_Chamberlain__Percy_shrunk_pdf                          | 0            | 1            | 3            |     0.0% |     0.0%
WA_Cush_NARA_2645385_Charley_Benjamin_Redacted_shrunk_pdf                   | 16           | 0            | 10           |   100.0% |    61.5%
WA_Cush_NARA_2645385_Charley_Edith_Redacted_shrunk_pdf                      | 6            | 0            | 0            |   100.0% |   100.0%
WA_Cush_NARA_2645385_Charley_Grace_Redacted_shrunk_pdf                      | 4            | 1            | 5            |    80.0% |    44.4%
WA_Cush_NARA_2645385_Charley_Josephine_Redacted_shrunk_pdf                  | 17           | 2            | 16           |    89.5% |    51.5%
WA_Cush_NARA_2645385_Chenois_Rose_Redacted_shrunk_pdf                       | 6            | 0            | 1            |   100.0% |    85.7%
WA_Cush_NARA_2645385_Clark_Andrew                                           | 4            | 0            | 2            |   100.0% |    66.7%
WA_Cush_NARA_2645385_Clark_Andrew_shrunk_pdf                                | 4            | 0            | 2            |   100.0% |    66.7%
WA_Cush_NARA_2645385_Clark_Emma_shrunk_pdf                                  | 5            | 0            | 3            |   100.0% |    62.5%
WA_Cush_NARA_2645385_Clark_Faustine                                         | 2            | 0            | 0            |   100.0% |   100.0%
WA_Cush_NARA_2645385_Cornoyer_DeLorme_Redacted_shrunk_pdf                   | 18           | 1            | 27           |    94.7% |    40.0%
WA_Cush_NARA_2645385_Crofoot_Earl_Redacted_shrunk_pdf                       | 25           | 6            | 15           |    80.6% |    62.5%
WA_Cush_NARA_2645385_Crow_David_Redacted_shrunk_pdf                         | 17           | 1            | 19           |    94.4% |    47.2%
WA_Cush_NARA_2645385_Dave_Willie_Redacted_shrunk_pdf                        | 29           | 2            | 9            |    93.5% |    76.3%
WA_Cush_NARA_2645385_Desauntel_Mabel_shrunk_pdf                             | 0            | 2            | 0            |     0.0% |     0.0%
WA_Cush_NARA_2645385_Dick_Ernest_Redacted_shrunk_pdf                        | 10           | 3            | 18           |    76.9% |    35.7%
WA_Cush_NARA_2645385_Dupuis_Bert                                            | 2            | 0            | 0            |   100.0% |   100.0%
WA_Cush_NARA_2645385_Dupuis_Bert_shrunk_pdf                                 | 2            | 0            | 0            |   100.0% |   100.0%
WA_Cush_NARA_2645385_Frank_Annie_Redacted_shrunk_pdf                        | 19           | 5            | 15           |    79.2% |    55.9%
WA_Cush_NARA_2645385_Frank_Margaret_Redacted_shrunk_pdf                     | 10           | 3            | 7            |    76.9% |    58.8%
WA_Cush_NARA_2645385_Freidlauder_Josie_Redacted_shrunk_pdf                  | 10           | 0            | 6            |   100.0% |    62.5%
WA_Cush_NARA_2645385_Garrison_Raymond_Redacted_shrunk_pdf                   | 9            | 1            | 8            |    90.0% |    52.9%
WA_Cush_NARA_2645385_George_Jennie_Redacted_shrunk_pdf                      | 16           | 1            | 16           |    94.1% |    50.0%
WA_Cush_NARA_2645385_Goodman_Alfred_Redacted_shrunk_pdf                     | 7            | 0            | 10           |   100.0% |    41.2%
WA_Cush_NARA_2645385_Gunnier_Bessie_shrunk_pdf                              | 2            | 0            | 0            |   100.0% |   100.0%
WA_Cush_NARA_2645385_Hall_Thomas_Edward                                     | 0            | 1            | 2            |     0.0% |     0.0%
WA_Cush_NARA_2645385_Hammer_Leo_Paul_Redacted_shrunk_pdf                    | 13           | 0            | 31           |   100.0% |    29.5%
WA_Cush_NARA_2645385_Hawk_Catherine_Redacted_shrunk_pdf                     | 13           | 0            | 18           |   100.0% |    41.9%
WA_Cush_NARA_2645385_Henry_Ethel_E_Redacted_shrunk_pdf                      | 16           | 4            | 15           |    80.0% |    51.6%
WA_Cush_NARA_2645385_Henry_John_Redacted_shrunk_pdf                         | 9            | 2            | 2            |    81.8% |    81.8%
WA_Cush_NARA_2645385_Horn_Adeline_Redacted_shrunk_pdf                       | 2            | 0            | 0            |   100.0% |   100.0%
WA_Cush_NARA_2645385_Hunt_William_Redacted_shrunk_pdf                       | 34           | 2            | 17           |    94.4% |    66.7%
WA_Cush_NARA_2645385_James_Nancy_Redacted_shrunk_pdf                        | 11           | 3            | 8            |    78.6% |    57.9%
WA_Cush_NARA_2645385_Joseph_Joseph_Redacted_shrunk_pdf                      | 9            | 3            | 25           |    75.0% |    26.5%
WA_Cush_NARA_2645385_KingGeorge_Anita_Redacted_shrunk_pdf                   | 10           | 0            | 3            |   100.0% |    76.9%
WA_Cush_NARA_2645385_Klinger_Eddie_shrunk_pdf                               | 0            | 1            | 2            |     0.0% |     0.0%
WA_Cush_NARA_2645385_Legard_Edwin_Joseph_Redacted_shrunk_pdf                | 6            | 1            | 3            |    85.7% |    66.7%
WA_Cush_NARA_2645385_Lewis_Nina_Redacted_shrunk_pdf                         | 16           | 3            | 15           |    84.2% |    51.6%
WA_Cush_NARA_2645385_Martin_Eva_shrunk_pdf                                  | 1            | 0            | 0            |   100.0% |   100.0%
WA_Cush_NARA_2645385_Martin_Narcisse_Redacted_shrunk_pdf                    | 19           | 3            | 11           |    86.4% |    63.3%
WA_Cush_NARA_2645385_Martin_William_G_Redacted_shrunk_pdf                   | 14           | 7            | 24           |    66.7% |    36.8%
WA_Cush_NARA_2645385_McCoy_Leonard_Redacted_shrunk_pdf                      | 12           | 2            | 18           |    85.7% |    40.0%
WA_Cush_NARA_2645385_McDonald_Harry_Redacted_shrunk_pdf                     | 12           | 0            | 9            |   100.0% |    57.1%
WA_Cush_NARA_2645385_McDonald_Margaret_Redacted_shrunk_pdf                  | 14           | 2            | 9            |    87.5% |    60.9%
WA_Cush_NARA_2645385_Michel_Henry_Redacted_shrunk_pdf                       | 21           | 1            | 17           |    95.5% |    55.3%
WA_Cush_NARA_2645385_Moses_Patsy_Redacted_shrunk_pdf                        | 34           | 7            | 33           |    82.9% |    50.7%
WA_Cush_NARA_2645385_Moses_Peter_Redacted_shrunk_pdf                        | 33           | 7            | 45           |    82.5% |    42.3%
WA_Cush_NARA_2645385_Napolean_Edna_shrunk_pdf                               | 0            | 1            | 2            |     0.0% |     0.0%
WA_Cush_NARA_2645385_Nostrum_Fred_Redacted_shrunk_pdf                       | 27           | 6            | 14           |    81.8% |    65.9%
WA_Cush_NARA_2645385_Parriseau_Antoine_Redacted_shrunk_pdf                  | 17           | 4            | 18           |    81.0% |    48.6%
WA_Cush_NARA_2645385_Parriseau_Patrick_Redacted_shrunk_pdf                  | 37           | 7            | 28           |    84.1% |    56.9%
WA_Cush_NARA_2645385_Pechette_Joe_shrunk_pdf                                | 1            | 1            | 0            |    50.0% |   100.0%
annie_harris                                                                | 2            | 0            | 0            |   100.0% |   100.0%
daniel_varner                                                               | 1            | 1            | 0            |    50.0% |   100.0%
edward_spott                                                                | 2            | 0            | 0            |   100.0% |   100.0%
flora_ross                                                                  | 3            | 0            | 0            |   100.0% |   100.0%
james_arquette                                                              | 2            | 0            | 0            |   100.0% |   100.0%
-------------------------------------------------------------------------------------------------------------------------------------------------
OVERALL CORPUS TOTALS                                                       | 1798         | 339          | 1279         |    84.1% |    58.4%
AVERAGE DOCUMENT SCORES                                                     | -            | -            | -            |    77.7% |    61.6%
-------------------------------------------------------------------------------------------------------------------------------------------------
Overall F1-Score (Corpus): 68.97%
Average F1-Score (Doc):    68.71%