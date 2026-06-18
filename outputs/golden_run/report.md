# Lab 16 Benchmark Report

## Metadata
- Dataset: hotpot_golden.json
- Mode: qwen-flash
- Records: 40
- Agents: react, reflexion

## Summary
| Metric | ReAct | Reflexion | Delta |
|---|---:|---:|---:|
| EM | 1.0 | 1.0 | 0.0 |
| Avg attempts | 1 | 1 | 0 |
| Avg token estimate | 425.7 | 425.9 | 0.2 |
| Avg latency (ms) | 321.25 | 288.15 | -33.1 |

## Failure modes
```json
{
  "entity_drift": 0,
  "incomplete_multi_hop": 0,
  "wrong_final_answer": 0,
  "looping": 0,
  "reflection_overfit": 0
}
```

## Extensions implemented
- structured_evaluator
- reflection_memory
- benchmark_report_json
- mock_mode_for_autograding

## Discussion
Reflexion helps when the first attempt stops after the first hop or drifts to a wrong second-hop entity. The tradeoff is higher attempts, token cost, and latency. In a real report, students should explain when the reflection memory was useful, which failure modes remained, and whether evaluator quality limited gains.


## Detailed Results
| QID | Agent | Correct | Tokens | Predicted Answer | Gold Answer | Question |
|---|---|---|---|---|---|---|
| gold1 | react | True | 380 | Beijing | Beijing | What is the capital of the country where the Great Wall was built? |
| gold2 | react | True | 412 | Classical | classical | What genre of music is the composer of Swan Lake most known for? |
| gold3 | react | True | 399 | The Peruvian sol | Peruvian sol | What currency is used in the country where Machu Picchu is located? |
| gold4 | react | True | 377 | Mediterranean Sea | Mediterranean Sea | In which body of water does the longest river in Africa empty? |
| gold5 | react | True | 403 | The Linux operating system was originally written in the C programming language. | C | What programming language was used to originally write the operating system created by Linus Torvalds? |
| gold6 | react | True | 456 | The official languages of Belgium are Dutch, French, and German. | Dutch, French, and German | What is the official language of the country that borders France to the northeast and has Brussels as its capital? |
| gold7 | react | True | 557 | The director of The Shawshank Redemption, Frank Darabont, did not receive an Academy Award, as the film was nominated for seven Oscars but did not win any. | no Academy Award win | What award did the director of the 1994 film that is set in Shawshank State Penitentiary receive from the Academy? |
| gold8 | react | True | 378 | Mars | Mars | What planet is the NASA rover Curiosity currently exploring? |
| gold9 | react | True | 468 | The highest mountain in Italy, the country where the Colosseum is located, is Mont Blanc at 4,808 metres. | Mont Blanc | What is the highest mountain in the country where the Colosseum is located? |
| gold10 | react | True | 441 | Uranium | uranium | Which element did the scientist who developed the theory of general relativity help theorize could be released from atoms for enormous energy? |
| gold11 | react | True | 380 | The Amazon River flows into the Atlantic Ocean. | Atlantic Ocean | What ocean does the Amazon River flow into? |
| gold12 | react | True | 427 | India has a federal parliamentary democratic republic government. | federal parliamentary democratic republic | What type of government does the country where the Taj Mahal is located have? |
| gold13 | react | True | 440 | 66,000 | approximately 66000 | What is the population of the city where the headquarters of the company that created the iPhone is located? |
| gold14 | react | True | 440 | The Bab-el-Mandeb Strait | Bab-el-Mandeb | What strait separates the continent where Mount Kilimanjaro is located from the Arabian Peninsula? |
| gold15 | react | True | 412 | Neil Armstrong | Neil Armstrong | Who was the first person to set foot on the celestial body that causes tides on Earth? |
| gold16 | react | True | 373 | Football | football | What sport is the club that plays at Camp Nou known for? |
| gold17 | react | True | 484 | The deepest point in the ocean that borders Japan to the east is the Challenger Deep in the Mariana Trench, at approximately 10,935 metres. | Challenger Deep | What is the deepest point in the ocean that borders Japan to the east? |
| gold18 | react | True | 429 | Canadian-American | Canadian-American | What nationality was the architect who designed the museum in Bilbao that is part of the Guggenheim network? |
| gold19 | react | True | 389 | Africa | Africa | What continent is the country where the pyramids of Giza are located on? |
| gold20 | react | True | 469 | 1951 | 1951 | In what year was the treaty signed that ended the war in which the atomic bomb was first used in combat? |
| gold1 | reflexion | True | 380 | Beijing | Beijing | What is the capital of the country where the Great Wall was built? |
| gold2 | reflexion | True | 412 | Classical | classical | What genre of music is the composer of Swan Lake most known for? |
| gold3 | reflexion | True | 399 | The Peruvian sol | Peruvian sol | What currency is used in the country where Machu Picchu is located? |
| gold4 | reflexion | True | 377 | Mediterranean Sea | Mediterranean Sea | In which body of water does the longest river in Africa empty? |
| gold5 | reflexion | True | 406 | The Linux operating system was originally written in the C programming language. | C | What programming language was used to originally write the operating system created by Linus Torvalds? |
| gold6 | reflexion | True | 449 | Dutch, French, and German | Dutch, French, and German | What is the official language of the country that borders France to the northeast and has Brussels as its capital? |
| gold7 | reflexion | True | 557 | The director of The Shawshank Redemption, Frank Darabont, did not receive an Academy Award, as the film was nominated for seven Oscars but did not win any. | no Academy Award win | What award did the director of the 1994 film that is set in Shawshank State Penitentiary receive from the Academy? |
| gold8 | reflexion | True | 387 | Mars | Mars | What planet is the NASA rover Curiosity currently exploring? |
| gold9 | reflexion | True | 468 | The highest mountain in Italy, the country where the Colosseum is located, is Mont Blanc at 4,808 metres. | Mont Blanc | What is the highest mountain in the country where the Colosseum is located? |
| gold10 | reflexion | True | 441 | Uranium | uranium | Which element did the scientist who developed the theory of general relativity help theorize could be released from atoms for enormous energy? |
| gold11 | reflexion | True | 380 | The Amazon River flows into the Atlantic Ocean. | Atlantic Ocean | What ocean does the Amazon River flow into? |
| gold12 | reflexion | True | 427 | India has a federal parliamentary democratic republic government. | federal parliamentary democratic republic | What type of government does the country where the Taj Mahal is located have? |
| gold13 | reflexion | True | 440 | 66,000 | approximately 66000 | What is the population of the city where the headquarters of the company that created the iPhone is located? |
| gold14 | reflexion | True | 440 | The Bab-el-Mandeb Strait | Bab-el-Mandeb | What strait separates the continent where Mount Kilimanjaro is located from the Arabian Peninsula? |
| gold15 | reflexion | True | 412 | Neil Armstrong | Neil Armstrong | Who was the first person to set foot on the celestial body that causes tides on Earth? |
| gold16 | reflexion | True | 373 | Football | football | What sport is the club that plays at Camp Nou known for? |
| gold17 | reflexion | True | 480 | The deepest point in the ocean that borders Japan to the east is the Challenger Deep in the Mariana Trench, at approximately 10,935 metres. | Challenger Deep | What is the deepest point in the ocean that borders Japan to the east? |
| gold18 | reflexion | True | 429 | Canadian-American | Canadian-American | What nationality was the architect who designed the museum in Bilbao that is part of the Guggenheim network? |
| gold19 | reflexion | True | 393 | Africa | Africa | What continent is the country where the pyramids of Giza are located on? |
| gold20 | reflexion | True | 468 | 1951 | 1951 | In what year was the treaty signed that ended the war in which the atomic bomb was first used in combat? |

