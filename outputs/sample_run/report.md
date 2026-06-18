# Lab 16 Benchmark Report

## Metadata
- Dataset: hotpot_dev_distractor_v1_100_formatted.json
- Mode: qwen-flash
- Records: 200
- Agents: react, reflexion

## Summary
| Metric | ReAct | Reflexion | Delta |
|---|---:|---:|---:|
| EM | 0.78 | 0.99 | 0.21 |
| Avg attempts | 1 | 1.23 | 0.23 |
| Avg token estimate | 1858.88 | 2458.21 | 599.33 |
| Avg latency (ms) | 483.48 | 533.57 | 50.09 |

## Failure modes
```json
{
  "wrong_final_answer": 23,
  "entity_drift": 0,
  "incomplete_multi_hop": 0,
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
| 5a8b57f25542995d1e6f1371 | react | True | 1574 | Yes | yes | Were Scott Derrickson and Ed Wood of the same nationality? |
| 5a8c7595554299585d9e36b6 | react | True | 1825 | United States ambassador to Ghana and to Czechoslovakia, and Chief of Protocol of the United States. | Chief of Protocol | What government position was held by the woman who portrayed Corliss Archer in the film Kiss and Tell? |
| 5a85ea095542994775f606a8 | react | True | 1957 | The Animorphs series | Animorphs | What science fantasy young adult series, told in first person, has a set of companion books narrating the stories of enslaved worlds and alien species? |
| 5adbf0a255429947ff17385a | react | True | 1503 | No, the Laleli Mosque and Esma Sultan Mansion are not located in the same neighborhood. The Laleli Mosque is in the Laleli district of Fatih, Istanbul, while the Esma Sultan Mansion is located in Ortaköy on the Bosphorus in Istanbul. | no | Are the Laleli Mosque and Esma Sultan Mansion located in the same neighborhood? |
| 5a8e3ea95542995a26add48d | react | True | 1712 | Greenwich Village, New York City | Greenwich Village, New York City | The director of the romantic comedy "Big Stone Gap" is based in what New York city? |
| 5abd94525542992ac4f382d2 | react | True | 1748 | YG Entertainment | YG Entertainment | 2014 S/S is the debut album of a South Korean boy group that was formed by who? |
| 5a85b2d95542997b5ce40028 | react | True | 2325 | Eenasul Fateh | Eenasul Fateh | Who was known by his stage name Aladin and helped organizations improve their performance as a consultant? |
| 5a87ab905542996e4f3088c1 | react | False | 3478 | 4,000 | 3,677 seated | The arena where the Lewiston Maineiacs played their home games can seat how many people? |
| 5a7bbb64554299042af8f7cc | react | True | 1758 | Terry Richardson is older. | Terry Richardson | Who is older, Annie Morton or Terry Richardson? |
| 5a8db19d5542994ba4e3dd00 | react | True | 1740 | Yes, both Local H and For Against are from the United States. | yes | Are Local H and For Against both from the United States? |
| 5a7166395542994082a3e814 | react | True | 2108 | Kansas Song | Kansas Song | What is the name of the fight song of the university whose main campus is in Lawrence, Kansas and whose branch campuses are in the Kansas City metropolitan area? |
| 5a877e5d5542993e715abf7d | react | True | 1744 | David Weissman | David Weissman | What screenwriter with credits for "Evolution" co-wrote a film starring Nicolas Cage and Téa Leoni? |
| 5ab3b0bf5542992ade7c6e39 | react | False | 1982 | 1993 | 1999 | What year did Guns N Roses perform a promo for a movie starring Arnold Schwarzenegger as a former New York Police detective? |
| 5ab56e32554299637185c594 | react | False | 3316 | Yes, both Random House Tower and 888 7th Avenue are used for real estate. The Random House Tower is a mixed-use building housing the headquarters of Random House and a luxury apartment complex, while 888 7th Avenue is a commercial office skyscraper in Midtown Manhattan, currently serving as the corporate headquarters for Vornado Realty Trust and Pershing Square Capital Management. | no | Are Random House Tower and 888 7th Avenue both used for real estate? |
| 5ab6d09255429954757d337d | react | True | 1403 | 1986 to 2013 | from 1986 to 2013 | The football manager who recruited David Beckham managed Manchester United during what timeframe? |
| 5a75e05c55429976ec32bc5f | react | False | 2115 | 331,449,281 | 9,984 | Brown State Fishing Lake is in a country that has a population of how many inhabitants ? |
| 5ab3e45655429976abd1bcd4 | react | True | 1834 | North Atlantic Conference | the North Atlantic Conference | The Vermont Catamounts men's soccer team currently competes in a conference that was formerly known as what from 1988 to 1996? |
| 5ab29c24554299449642c932 | react | True | 1784 | Yes | yes | Are Giuseppe Verdi and Ambroise Thomas both Opera composers ? |
| 5ae0d4c9554299603e418468 | react | True | 2200 | 1969 to 1974 | 1969 until 1974 | Roger O. Egeberg was Assistant Secretary for Health and Scientific Affairs during the administration of a president that served during what years? |
| 5a8133725542995ce29dcbdb | react | True | 1380 | Robert Erskine Childers was from England. | Robert Erskine Childers DSC | Which writer was from England, Henry Roth or Robert Erskine Childers? |
| 5ae7a8175542993210983ed8 | react | True | 1866 | Pedro Rodríguez | Pedro Rodríguez | Which other Mexican Formula One race car driver has held the podium besides the Force India driver born in 1990? |
| 5ae6050f55429929b0807a5e | react | True | 1965 | Sonic the Hedgehog | Sonic | This singer of A Rather Blustery Day also voiced what hedgehog? |
| 5adddccd5542997dc7907069 | react | False | 2222 | The Apple Watch can control the program Apple Remote was originally designed to interact with—Front Row—through its integration with iOS and macOS devices. | keyboard function keys | Aside from the Apple Remote, what other device can control the program Apple Remote was originally designed to interact with? |
| 5ae2070a5542994d89d5b313 | react | True | 1671 | Badly Drawn Boy has a higher instrument to person ratio.   Explanation: Badly Drawn Boy (Damon Gough) is a solo artist who writes, produces, and plays multiple instruments on his albums, including *The Hour of Bewilderbeast* and the *About a Boy* soundtrack. In contrast, Wolf Alice is a four-piece band with one member per primary instrument (guitar, bass, drums, vocals), resulting in a lower instrument-to-person ratio. Since Badly Drawn Boy performs multiple instruments himself, his effective instrument-to-person ratio is higher than that of Wolf Alice. | Badly Drawn Boy | Which performance act has a higher instrument to person ratio, Badly Drawn Boy or Wolf Alice?  |
| 5ae22b8d554299234fd0440f | react | True | 1724 | The father of Kasper Schmeichel, Peter Schmeichel, was voted IFFHS World's Best Goalkeeper in 1992. | World's Best Goalkeeper | What was the father of Kasper Schmeichel voted to be by the IFFHS in 1992? |
| 5a722b8655429971e9dc9329 | react | True | 1588 | Lee Hazlewood was the writer of "These Boots Are Made for Walkin'" and died in 2007. | Barton Lee Hazlewood | Who was the writer of These Boots Are Made for Walkin' and who died in 2007? |
| 5adf37a95542995ec70e8f97 | react | True | 2330 | 1838 | 1838 | The 2011–12 VCU Rams men's basketball team, led by third year head coach Shaka Smart, represented Virginia Commonwealth University which was founded in what year? |
| 5abd259d55429924427fcf1a | react | True | 727 | Yes | yes | Are both Dictyosperma, and Huernia described as a genus? |
| 5a828c8355429966c78a6a50 | react | True | 1631 | Henry J. Kaiser | Henry J. Kaiser | Kaiser Ventures corporation was founded by an American industrialist who became known as the father of modern American shipbuilding? |
| 5a8a3e745542996c9b8d5e70 | react | True | 1618 | Arena of Khazan | Arena of Khazan | What is the name for the adventure in "Tunnels and Trolls", a game designed by Ken St. Andre? |
| 5ac23ff0554299636651994d | react | False | 1919 | Poison's album "Crack a Smile...and More!" was released on March 14, 2000. | 2000 | When was Poison's album "Shut Up, Make Love" released? |
| 5ae4a3265542995ad6573de5 | react | True | 1575 | Buck-Tick hails from Fujioka, Gunma, Japan. | Fujioka, Gunma | Hayden is a singer-songwriter from Canada, but where does Buck-Tick hail from? |
| 5ae0361155429925eb1afc2c | react | False | 1784 | Charles Nungesser and François Coli flew L'Oiseau Blanc. | Charles Eugène | Which  French ace pilot and adventurer fly L'Oiseau Blanc |
| 5abc0a5d5542993f40c73c64 | react | False | 2185 | Yes, Freakonomics is an American documentary, but In the Realm of the Hackers is an Australian documentary. | no | Are Freakonomics and In the Realm of the Hackers both American documentaries? |
| 5a7cc50e554299452d57ba3e | react | True | 2021 | Letters to Cleo had more members. | Letters to Cleo | Which band, Letters to Cleo or Screaming Trees, had more members? |
| 5abf63f15542997ec76fd3ea | react | False | 2458 | The Russian Civil War ended in 1923, when Red control of the newly formed Soviet Union was assured. | October 1922 | Alexander Kerensky was defeated and destroyed by the Bolsheviks in the course of a civil war that ended when ? |
| 5a8ef2a75542995a26add583 | react | True | 1693 | 2000 | 2000 | Seven Brief Lessons on Physics was written by an Italian physicist that has worked in France since what year? |
| 5a80721b554299485f5985ef | react | True | 1405 | World War II | World War II | The Livesey Hal War Memorial commemorates the fallen of which war, that had over 60 million casualties? |
| 5ab51dae5542991779162d82 | react | True | 1869 | No, only Gerald R. Ford International Airport is located in Michigan. Elko Regional Airport is in Nevada. | no | Are both Elko Regional Airport and Gerald R. Ford International Airport located in Michigan? |
| 5a7571135542992d0ec05f98 | react | True | 1710 | New York City | New York City | Ralph Hefferline was a psychology professor at a university that is located in what city? |
| 5a7a0e1e5542990783324e1a | react | True | 2150 | Scotch Collie | Scotch Collie | Which dog's ancestors include Gordon and Irish Setters: the Manchester Terrier or the Scotch Collie? |
| 5a74106b55429979e288289e | react | True | 1593 | Mumbai, Maharashtra | Mumbai | Where is the company that Sachin Warrier worked for as a software engineer headquartered?  |
| 5a79311755429970f5fffe67 | react | True | 2277 | 1962 | 1962 | A Japanese manga series based on a 16 year old high school student Ichitaka Seto, is written and illustrated by someone born in what year? |
| 5ab2d3df554299194fa9352c | react | True | 2453 | Ethiopian sovereignty and independence | sovereignty | The battle in which Giuseppe Arimondi lost his life secured what for Ethiopia? |
| 5a760ab65542994ccc918697 | react | True | 3059 | Nelson Rockefeller | Nelson Rockefeller | Alfred Balk served as the secretary of the Committee on the Employment of Minority Groups in the News Media under which United States Vice President? |
| 5a7d54165542995f4f402256 | react | False | 1552 | The Firth of Forth | Yellowcraig | A medieval fortress in Dirleton, East Lothian, Scotland borders on the south side of what coastal area? |
| 5ab859a955429934fafe6d7b | react | True | 2955 | Phil Spector | Phil Spector | Who is the writer of this song that was inspired by words on a tombstone and was the first track on the box set Back to Mono? |
| 5add61d65542995b365fab21 | react | False | 2641 | Mikhail Gorbachev initiated a forum for Nobel Peace Laureates, known as the World Summit of Nobel Peace Laureates. | Organizations could come together to address global issues | What type of forum did a former Soviet statesman initiate? |
| 5a8e068b5542995085b37384 | react | True | 1729 | Yes | yes | Are Ferocactus and Silene both types of plant? |
| 5abbf698554299114383a0b5 | react | True | 2000 | English Electric Canberra | English Electric Canberra | Which British first-generation jet-powered medium bomber was used in the South West Pacific theatre of World War II? |
| 5a8e1027554299653c1aa15f | react | True | 1876 | 2009, Big 12 Conference | 2009 Big 12 Conference | Which year and which conference was the 14th season for this conference as part of the NCAA Division that the Colorado Buffaloes played in with a record of 2-6 in conference play? |
| 5ab84bf555429916710eb01f | react | True | 1766 | 1,462 | 1,462 | In 1991 Euromarché was bought by a chain that operated how any hypermarkets at the end of 2016? |
| 5a77724455429972597f153e | react | True | 1789 | Indianapolis Motor Speedway | Indianapolis Motor Speedway | What race track in the midwest hosts a 500 mile race eavery May? |
| 5a87c13f5542996e4f30890c | react | True | 1841 | Rome | Rome | In what city did the "Prince of tenors" star in a film based on an opera by Giacomo Puccini? |
| 5ab96ab755429970cfb8eacd | react | False | 1964 | Max Martin, Savan Kotecha, Ilya Salmanzadeh, and Tove Lo. | Max Martin, Savan Kotecha and Ilya Salmanzadeh | Ellie Goulding worked with what other writers on her third studio album, Delirium? |
| 5a8a43eb5542996c9b8d5e82 | react | False | 2323 | Adelaide | Marion, South Australia | Which Australian city founded in 1838 contains a boarding school opened by a Prime Minister of Australia and named after a school in London of the same name. |
| 5ae73acb5542991e8301cc07 | react | True | 1712 | D1NZ is a series based on the drifting oversteering technique. | Drifting | D1NZ is a series based on what oversteering technique? |
| 5a7320565542991f9a20c61d | react | True | 1972 | Keith Bostic is younger. | Keith Bostic | who is younger Keith Bostic or Jerry Glanville ? |
| 5ae32e125542991a06ce9946 | react | True | 1911 | According to the 2001 census, the population of Boston, Lincolnshire — the city in which Kirton End is located — was 35,124. | 35,124 | According to the 2001 census, what was the population of the city in which Kirton End is located? |
| 5adc53f75542996e6852530a | react | False | 1447 | Yes, both Cypress and Ajuga are genera. | no | Are both Cypress and Ajuga genera? |
| 5a8b20335542996c9b8d5fb3 | react | False | 2479 | Muggsy Bogues | shortest player ever to play in the National Basketball Association | What distinction is held by the former NBA player who was a member of the Charlotte Hornets during their 1992-93 season and was head coach for the WNBA team Charlotte Sting? |
| 5a85fb085542994775f606de | react | False | 1780 | Michael Finnell | Ronald Shusett | What is the name of the executive producer of the film that has a score composed by Jerry Goldsmith? |
| 5a7be2595542997c3ec972ac | react | True | 1583 | Virginia Woolf was born earlier. She was born on 25 January 1882, while Emma Bull was born on 13 December 1954. | Adeline Virginia Woolf | Who was born earlier, Emma Bull or Virginia Woolf? |
| 5a77152355429966f1a36c2e | react | True | 1260 | The Roud Folk Song Index number of the nursery rhyme "What Are Little Boys Made Of?" is 821. | 821 | What was the Roud Folk Song Index of the nursery rhyme inspiring What Are Little Girls Made Of? |
| 5a8f4c8d554299458435d5a3 | react | False | 1554 | 70 | more than 70 countries | Scott Parkin has been a vocal critic of Exxonmobil and another corporation that has operations in how many countries ? |
| 5a80840f554299485f59863b | react | True | 1838 | Charmed | Charmed | What WB supernatrual drama series was Jawbreaker star Rose Mcgowan best known for being in? |
| 5a8361b65542992ef85e22a0 | react | True | 2463 | International Boxing Hall of Fame | International Boxing Hall of Fame | Vince Phillips held a junior welterweight title by an organization recognized by what larger Hall of Fame? |
| 5ae7ba7a5542993210983f12 | react | True | 2709 | Usher | Usher | What is the name of the singer who's song was released as the lead single from the album "Confessions", and that had popular song stuck behind for eight consecutive weeks? |
| 5ac2acff55429921a00ab02b | react | False | 1873 | The younger brother of Nick Lachey, who is a guest star in the film *The Hard Easy*, is Drew Lachey. | Bill Murray | who is the younger brother of The episode guest stars of The Hard Easy  |
| 5aba7cfe554299232ef4a2fd | react | True | 1717 | Carabao Cup | Carabao Cup | The 2017–18 Wigan Athletic F.C. season will be a year in which the team competes in the league cup known as what for sponsorship reasons? |
| 5ae5aba0554299546bf82f17 | react | False | 1874 | Tara Strong's major voice role in the animated series "Teen Titans" is Raven. | Teen Titans Go! | Which of Tara Strong major voice role in animated series is an American animated television series based on the DC Comics fictional superhero team, the "Teen Titans"? |
| 5ae1f4cb554299234fd0436d | react | True | 1685 | The inhabitant of Strasbourg, the city where the 122nd SS-Standarte was formed, in 2014 was approximately 276,170 people in the city proper, and 484,157 in the Greater Strasbourg area (Eurométropole de Strasbourg). | 276,170 inhabitants | What is the inhabitant of the city where  122nd SS-Standarte was formed in2014 |
| 5ae7e1fc55429952e35ea9cc | react | True | 1821 | People in the Netherlands wear orange clothing during Oranjegekte or to celebrate Koningsdag. | orange | What color clothing do people of the Netherlands wear during Oranjegekte or to celebrate the national holiday Koningsdag?  |
| 5ae37c765542992f92d822d4 | react | True | 1995 | Tromeo and Juliet | Tromeo and Juliet | What was the name of the 1996 loose adaptation of William Shakespeare's "Romeo & Juliet" written by James Gunn? |
| 5ae33c4d5542992f92d82262 | react | True | 1442 | Bill Clinton | William Jefferson Clinton | Robert Suettinger was the national intelligence officer under which former Governor of Arkansas? |
| 5a77cb335542997042120b3a | react | True | 1253 | John John Florence | John John Florence | What American professional Hawaiian surfer born 18 October 1992 won the Rip Curl Pro Portugal? |
| 5a8979f4554299669944a52e | react | True | 1508 | The actress who plays Bobbi Bacha in *Suburban Madness* is Sela Ward. According to the context, her full name is Sela Ann Ward. Therefore, her middle name is **Ann**. | Ann | What is the middle name of the actress who plays Bobbi Bacha in Suburban Madness? |
| 5a713ea95542994082a3e6e4 | react | False | 1956 | Alvaro Mexia had a diplomatic mission with the Ais tribe of indigenous people. | Apalachees | Alvaro Mexia had a diplomatic mission with which tribe of indigenous people? |
| 5a78bd9b554299078472774a | react | True | 1782 | Alfred Gell and Edmund Leach were both British. | British | What nationality were social anthropologists Alfred Gell and Edmund Leach? |
| 5a7625e8554299109176e66a | react | True | 1556 | 1865 | 1865 | In which year was the King who made the 1925 Birthday Honours born? |
| 5ae2dd2055429928c423950d | react | True | 1678 | Newport | Newport | What is the county seat of the county where East Lempster, New Hampshire is located? |
| 5abdf12255429976d4830a2f | react | True | 1843 | Bob Seger | Bob Seger | The Album Against the Wind was the 11th Album of a Rock singer Robert C Seger born may 6 1945. What was the Rock singers stage name ? |
| 5a88658955429938390d3f47 | react | True | 2442 | Rostker v. Goldberg held that the practice of requiring only men to register for the draft was constitutional. | Conscription | Rostker v. Goldberg held that the practice of what way of filling armed forces vacancies was consitutional? |
| 5a86ebac55429960ec39b6d6 | react | True | 1596 | Mondelez International | Mondelez International, Inc. | Handi-Snacks are a snack food product line sold by what American multinational confectionery, food, and beverage company that is based in Illinois? |
| 5aba5d2e55429901930fa799 | react | True | 2080 | Monica Lewinsky | Monica Lewinsky | What was the name of a woman from the book titled "Their Lives: The Women Targeted by the Clinton Machine " and was also a former white house intern? |
| 5ae5736e5542990ba0bbb2b3 | react | True | 2022 | April 1, 1949 | April 1, 1949 | When was the American lawyer, lobbyist and political consultant who was a senior member of the presidential campaign of Donald Trump born? |
| 5ae005b555429942ec259bec | react | True | 1508 | 1866 | 1866 | In what year was the novel that Lourenço Mutarelli based "Nina" on based first published? |
| 5a7759fc5542993569682d60 | react | True | 1600 | Teide National Park is located on the island of Tenerife in the Canary Islands, Spain. Garajonay National Park is located on the island of La Gomera, also in the Canary Islands, Spain. | Canary Islands, Spain | Where are Teide National Park and Garajonay National Park located? |
| 5a835478554299123d8c20ed | react | False | 1329 | The context does not provide information about the number of copies sold for Roald Dahl's variation on the popular anecdote, "Mrs. Bixby and the Colonel's Coat." | 250 million | How many copies of Roald Dahl's variation on a popular anecdote sold? |
| 5aba749055429901930fa7d8 | react | True | 1372 | film director | director | What occupation do Chris Menges and Aram Avakian share? |
| 5abfb3425542990832d3a1c0 | react | True | 1539 | Andrew Jaspan was the co-founder of "The Conversation", an independent not-for-profit media outlet. | The Conversation | Andrew Jaspan was the co-founder of what not-for-profit media outlet? |
| 5ac3165c5542995ef918c10a | react | True | 1221 | John Waters | John Waters | Which American film director hosted the 18th Independent Spirit Awards in 2002? |
| 5ae53b545542990ba0bbb23c | react | True | 1267 | The hotel and casino where Bill Cosby's third album, *Why Is There Air?*, was recorded is the Flamingo Las Vegas in Las Vegas, Nevada. | Las Vegas Strip in Paradise | Where does the hotel and casino located in which Bill Cosby's third album was recorded? |
| 5ae224da554299234fd043ee | react | True | 1471 | Yes, the Gibson contains gin, but the Zurracapote does not. | no | Do the drinks Gibson and Zurracapote both contain gin? |
| 5ae2b770554299495565db0f | react | True | 1496 | March and April | March and April | In what month is the annual documentary film festival, that is presented by the fortnightly published British journal of literary essays, held?  |
| 5a80b3a9554299485f5986cc | react | True | 1594 | Fairfax County | Fairfax County | Tysons Galleria is located in what county? |
| 5a8e0a005542995085b373a1 | react | True | 2080 | Bordan Tkachuk was the CEO of Viglen, which provides IT products and services, including storage systems, servers, workstations, and data/voice communications equipment and services. | IT products and services | Bordan Tkachuk was the CEO of a company that provides what sort of products? |
| 5ac1b8ee5542994d76dccedc | react | False | 2449 | Lev Yilmaz | Levni Yilmaz | Which filmmaker was known for animation, Lev Yilmaz or Pamela B. Green? |
| 5adccd795542990d50227d2c | react | True | 1582 | The ambassador of the Rabat-Salé-Kénitra administrative region to China is based in Beijing. | Beijing | In which city is the ambassador of the Rabat-Salé-Kénitra administrative region to China based? |
| 5a84c4135542994c784dda31 | react | True | 1134 | No, Yingkou and Fuding are not the same level of city. Yingkou is a prefecture-level city in Liaoning Province, while Fuding is a county-level city within Ningde Prefecture, Fujian Province. | no | Are Yingkou and Fuding the same level of city? |
| 5a8b57f25542995d1e6f1371 | reflexion | True | 1574 | Yes | yes | Were Scott Derrickson and Ed Wood of the same nationality? |
| 5a8c7595554299585d9e36b6 | reflexion | True | 1825 | United States ambassador to Ghana and to Czechoslovakia, and Chief of Protocol of the United States. | Chief of Protocol | What government position was held by the woman who portrayed Corliss Archer in the film Kiss and Tell? |
| 5a85ea095542994775f606a8 | reflexion | True | 1942 | Animorphs | Animorphs | What science fantasy young adult series, told in first person, has a set of companion books narrating the stories of enslaved worlds and alien species? |
| 5adbf0a255429947ff17385a | reflexion | True | 1503 | No, the Laleli Mosque and Esma Sultan Mansion are not located in the same neighborhood. The Laleli Mosque is in the Laleli district of Fatih, Istanbul, while the Esma Sultan Mansion is located in Ortaköy on the Bosphorus in Istanbul. | no | Are the Laleli Mosque and Esma Sultan Mansion located in the same neighborhood? |
| 5a8e3ea95542995a26add48d | reflexion | True | 1712 | Greenwich Village, New York City | Greenwich Village, New York City | The director of the romantic comedy "Big Stone Gap" is based in what New York city? |
| 5abd94525542992ac4f382d2 | reflexion | True | 1748 | YG Entertainment | YG Entertainment | 2014 S/S is the debut album of a South Korean boy group that was formed by who? |
| 5a85b2d95542997b5ce40028 | reflexion | True | 2329 | Eenasul Fateh, known by his stage name Aladin, was a former international management consultant who helped organizations improve their performance. | Eenasul Fateh | Who was known by his stage name Aladin and helped organizations improve their performance as a consultant? |
| 5a87ab905542996e4f3088c1 | reflexion | True | 7364 | 3,677 | 3,677 seated | The arena where the Lewiston Maineiacs played their home games can seat how many people? |
| 5a7bbb64554299042af8f7cc | reflexion | True | 1758 | Terry Richardson is older. | Terry Richardson | Who is older, Annie Morton or Terry Richardson? |
| 5a8db19d5542994ba4e3dd00 | reflexion | True | 1740 | Yes, both Local H and For Against are from the United States. | yes | Are Local H and For Against both from the United States? |
| 5a7166395542994082a3e814 | reflexion | True | 2108 | Kansas Song | Kansas Song | What is the name of the fight song of the university whose main campus is in Lawrence, Kansas and whose branch campuses are in the Kansas City metropolitan area? |
| 5a877e5d5542993e715abf7d | reflexion | True | 1744 | David Weissman | David Weissman | What screenwriter with credits for "Evolution" co-wrote a film starring Nicolas Cage and Téa Leoni? |
| 5ab3b0bf5542992ade7c6e39 | reflexion | True | 4508 | 1999 | 1999 | What year did Guns N Roses perform a promo for a movie starring Arnold Schwarzenegger as a former New York Police detective? |
| 5ab56e32554299637185c594 | reflexion | True | 6949 | no | no | Are Random House Tower and 888 7th Avenue both used for real estate? |
| 5ab6d09255429954757d337d | reflexion | True | 1403 | 1986 to 2013 | from 1986 to 2013 | The football manager who recruited David Beckham managed Manchester United during what timeframe? |
| 5a75e05c55429976ec32bc5f | reflexion | True | 1961 | 9,984 | 9,984 | Brown State Fishing Lake is in a country that has a population of how many inhabitants ? |
| 5ab3e45655429976abd1bcd4 | reflexion | True | 1825 | North Atlantic Conference | the North Atlantic Conference | The Vermont Catamounts men's soccer team currently competes in a conference that was formerly known as what from 1988 to 1996? |
| 5ab29c24554299449642c932 | reflexion | True | 1784 | Yes | yes | Are Giuseppe Verdi and Ambroise Thomas both Opera composers ? |
| 5ae0d4c9554299603e418468 | reflexion | True | 2200 | 1969 to 1974 | 1969 until 1974 | Roger O. Egeberg was Assistant Secretary for Health and Scientific Affairs during the administration of a president that served during what years? |
| 5a8133725542995ce29dcbdb | reflexion | True | 1387 | Robert Erskine Childers was from England. | Robert Erskine Childers DSC | Which writer was from England, Henry Roth or Robert Erskine Childers? |
| 5ae7a8175542993210983ed8 | reflexion | True | 1759 | Pedro Rodríguez | Pedro Rodríguez | Which other Mexican Formula One race car driver has held the podium besides the Force India driver born in 1990? |
| 5ae6050f55429929b0807a5e | reflexion | True | 1965 | Sonic the Hedgehog | Sonic | This singer of A Rather Blustery Day also voiced what hedgehog? |
| 5adddccd5542997dc7907069 | reflexion | True | 4927 | The keyboard function keys can control the program Apple Remote was originally designed to interact with, Front Row. | keyboard function keys | Aside from the Apple Remote, what other device can control the program Apple Remote was originally designed to interact with? |
| 5ae2070a5542994d89d5b313 | reflexion | True | 1806 | Badly Drawn Boy has a higher instrument to person ratio. | Badly Drawn Boy | Which performance act has a higher instrument to person ratio, Badly Drawn Boy or Wolf Alice?  |
| 5ae22b8d554299234fd0440f | reflexion | True | 1724 | The father of Kasper Schmeichel, Peter Schmeichel, was voted IFFHS World's Best Goalkeeper in 1992. | World's Best Goalkeeper | What was the father of Kasper Schmeichel voted to be by the IFFHS in 1992? |
| 5a722b8655429971e9dc9329 | reflexion | True | 1590 | Lee Hazlewood was the writer of "These Boots Are Made for Walkin'" and he died in 2007. | Barton Lee Hazlewood | Who was the writer of These Boots Are Made for Walkin' and who died in 2007? |
| 5adf37a95542995ec70e8f97 | reflexion | True | 2330 | 1838 | 1838 | The 2011–12 VCU Rams men's basketball team, led by third year head coach Shaka Smart, represented Virginia Commonwealth University which was founded in what year? |
| 5abd259d55429924427fcf1a | reflexion | True | 727 | Yes | yes | Are both Dictyosperma, and Huernia described as a genus? |
| 5a828c8355429966c78a6a50 | reflexion | True | 1677 | Yes, Kaiser Ventures corporation was founded by Henry J. Kaiser, an American industrialist who became known as the father of modern American shipbuilding. | Henry J. Kaiser | Kaiser Ventures corporation was founded by an American industrialist who became known as the father of modern American shipbuilding? |
| 5a8a3e745542996c9b8d5e70 | reflexion | True | 1661 | The name for the adventure in "Tunnels and Trolls" designed by Ken St. Andre is "Arena of Khazan". | Arena of Khazan | What is the name for the adventure in "Tunnels and Trolls", a game designed by Ken St. Andre? |
| 5ac23ff0554299636651994d | reflexion | True | 4359 | Poison's album "Shut Up, Make Love" was released on March 14, 2000. | 2000 | When was Poison's album "Shut Up, Make Love" released? |
| 5ae4a3265542995ad6573de5 | reflexion | True | 1581 | Japan | Fujioka, Gunma | Hayden is a singer-songwriter from Canada, but where does Buck-Tick hail from? |
| 5ae0361155429925eb1afc2c | reflexion | False | 6777 | Charles Nungesser and François Coli flew L'Oiseau Blanc. | Charles Eugène | Which  French ace pilot and adventurer fly L'Oiseau Blanc |
| 5abc0a5d5542993f40c73c64 | reflexion | True | 4939 | No | no | Are Freakonomics and In the Realm of the Hackers both American documentaries? |
| 5a7cc50e554299452d57ba3e | reflexion | True | 2021 | Letters to Cleo had more members. | Letters to Cleo | Which band, Letters to Cleo or Screaming Trees, had more members? |
| 5abf63f15542997ec76fd3ea | reflexion | True | 5368 | October 1922 | October 1922 | Alexander Kerensky was defeated and destroyed by the Bolsheviks in the course of a civil war that ended when ? |
| 5a8ef2a75542995a26add583 | reflexion | True | 1693 | 2000 | 2000 | Seven Brief Lessons on Physics was written by an Italian physicist that has worked in France since what year? |
| 5a80721b554299485f5985ef | reflexion | True | 1405 | World War II | World War II | The Livesey Hal War Memorial commemorates the fallen of which war, that had over 60 million casualties? |
| 5ab51dae5542991779162d82 | reflexion | True | 1877 | No, only Gerald R. Ford International Airport is located in Michigan. Elko Regional Airport is in Nevada. | no | Are both Elko Regional Airport and Gerald R. Ford International Airport located in Michigan? |
| 5a7571135542992d0ec05f98 | reflexion | True | 1710 | New York City | New York City | Ralph Hefferline was a psychology professor at a university that is located in what city? |
| 5a7a0e1e5542990783324e1a | reflexion | True | 2080 | Scotch Collie | Scotch Collie | Which dog's ancestors include Gordon and Irish Setters: the Manchester Terrier or the Scotch Collie? |
| 5a74106b55429979e288289e | reflexion | True | 1620 | Mumbai, Maharashtra | Mumbai | Where is the company that Sachin Warrier worked for as a software engineer headquartered?  |
| 5a79311755429970f5fffe67 | reflexion | True | 2277 | 1962 | 1962 | A Japanese manga series based on a 16 year old high school student Ichitaka Seto, is written and illustrated by someone born in what year? |
| 5ab2d3df554299194fa9352c | reflexion | True | 2433 | The battle in which Giuseppe Arimondi lost his life, the Battle of Adwa, secured Ethiopian sovereignty and independence from Italian colonization. | sovereignty | The battle in which Giuseppe Arimondi lost his life secured what for Ethiopia? |
| 5a760ab65542994ccc918697 | reflexion | True | 3059 | Nelson Rockefeller | Nelson Rockefeller | Alfred Balk served as the secretary of the Committee on the Employment of Minority Groups in the News Media under which United States Vice President? |
| 5a7d54165542995f4f402256 | reflexion | True | 3567 | Yellowcraig | Yellowcraig | A medieval fortress in Dirleton, East Lothian, Scotland borders on the south side of what coastal area? |
| 5ab859a955429934fafe6d7b | reflexion | True | 2936 | Phil Spector | Phil Spector | Who is the writer of this song that was inspired by words on a tombstone and was the first track on the box set Back to Mono? |
| 5add61d65542995b365fab21 | reflexion | True | 5835 | Mikhail Gorbachev initiated a global forum for dialogue on peace and human well-being, bringing together Nobel Peace Laureates to address pressing international issues. | Organizations could come together to address global issues | What type of forum did a former Soviet statesman initiate? |
| 5a8e068b5542995085b37384 | reflexion | True | 1729 | Yes | yes | Are Ferocactus and Silene both types of plant? |
| 5abbf698554299114383a0b5 | reflexion | True | 2000 | English Electric Canberra | English Electric Canberra | Which British first-generation jet-powered medium bomber was used in the South West Pacific theatre of World War II? |
| 5a8e1027554299653c1aa15f | reflexion | True | 1874 | 2009, Big 12 Conference | 2009 Big 12 Conference | Which year and which conference was the 14th season for this conference as part of the NCAA Division that the Colorado Buffaloes played in with a record of 2-6 in conference play? |
| 5ab84bf555429916710eb01f | reflexion | True | 1771 | 1,462 | 1,462 | In 1991 Euromarché was bought by a chain that operated how any hypermarkets at the end of 2016? |
| 5a77724455429972597f153e | reflexion | True | 1789 | Indianapolis Motor Speedway | Indianapolis Motor Speedway | What race track in the midwest hosts a 500 mile race eavery May? |
| 5a87c13f5542996e4f30890c | reflexion | True | 1812 | Rome | Rome | In what city did the "Prince of tenors" star in a film based on an opera by Giacomo Puccini? |
| 5ab96ab755429970cfb8eacd | reflexion | True | 4291 | Ellie Goulding worked with Max Martin, Savan Kotecha, and Ilya Salmanzadeh as writers on her third studio album, Delirium. | Max Martin, Savan Kotecha and Ilya Salmanzadeh | Ellie Goulding worked with what other writers on her third studio album, Delirium? |
| 5a8a43eb5542996c9b8d5e82 | reflexion | True | 5119 | Marion, South Australia | Marion, South Australia | Which Australian city founded in 1838 contains a boarding school opened by a Prime Minister of Australia and named after a school in London of the same name. |
| 5ae73acb5542991e8301cc07 | reflexion | True | 1713 | D1NZ is a series based on the drifting oversteering technique. | Drifting | D1NZ is a series based on what oversteering technique? |
| 5a7320565542991f9a20c61d | reflexion | True | 1968 | Keith Bostic is younger. | Keith Bostic | who is younger Keith Bostic or Jerry Glanville ? |
| 5ae32e125542991a06ce9946 | reflexion | True | 1911 | According to the 2001 census, the population of Boston, Lincolnshire — the city in which Kirton End is located — was 35,124. | 35,124 | According to the 2001 census, what was the population of the city in which Kirton End is located? |
| 5adc53f75542996e6852530a | reflexion | True | 5808 | Yes, Ajuga is a genus; Cypress is not a genus but a common name for trees in the genus Cupressus and related genera. | no | Are both Cypress and Ajuga genera? |
| 5a8b20335542996c9b8d5fb3 | reflexion | True | 5517 | The distinction held by the former NBA player who was a member of the Charlotte Hornets during their 1992–93 season and later served as head coach for the WNBA's Charlotte Sting is that he was the shortest player ever to play in the NBA. | shortest player ever to play in the National Basketball Association | What distinction is held by the former NBA player who was a member of the Charlotte Hornets during their 1992-93 season and was head coach for the WNBA team Charlotte Sting? |
| 5a85fb085542994775f606de | reflexion | True | 4148 | Ronald Shusett | Ronald Shusett | What is the name of the executive producer of the film that has a score composed by Jerry Goldsmith? |
| 5a7be2595542997c3ec972ac | reflexion | True | 1583 | Virginia Woolf was born earlier. She was born on 25 January 1882, while Emma Bull was born on 13 December 1954. | Adeline Virginia Woolf | Who was born earlier, Emma Bull or Virginia Woolf? |
| 5a77152355429966f1a36c2e | reflexion | True | 1253 | The Roud Folk Song Index number of the nursery rhyme "What Are Little Boys Made Of?" is 821. | 821 | What was the Roud Folk Song Index of the nursery rhyme inspiring What Are Little Girls Made Of? |
| 5a8f4c8d554299458435d5a3 | reflexion | True | 3662 | more than 70 countries | more than 70 countries | Scott Parkin has been a vocal critic of Exxonmobil and another corporation that has operations in how many countries ? |
| 5a80840f554299485f59863b | reflexion | True | 1838 | Charmed | Charmed | What WB supernatrual drama series was Jawbreaker star Rose Mcgowan best known for being in? |
| 5a8361b65542992ef85e22a0 | reflexion | True | 2463 | International Boxing Hall of Fame | International Boxing Hall of Fame | Vince Phillips held a junior welterweight title by an organization recognized by what larger Hall of Fame? |
| 5ae7ba7a5542993210983f12 | reflexion | True | 2491 | Usher | Usher | What is the name of the singer who's song was released as the lead single from the album "Confessions", and that had popular song stuck behind for eight consecutive weeks? |
| 5ac2acff55429921a00ab02b | reflexion | True | 4371 | Bill Murray | Bill Murray | who is the younger brother of The episode guest stars of The Hard Easy  |
| 5aba7cfe554299232ef4a2fd | reflexion | True | 1717 | Carabao Cup | Carabao Cup | The 2017–18 Wigan Athletic F.C. season will be a year in which the team competes in the league cup known as what for sponsorship reasons? |
| 5ae5aba0554299546bf82f17 | reflexion | True | 4369 | Tara Strong's major voice role in the animated series "Teen Titans Go!" is Raven. | Teen Titans Go! | Which of Tara Strong major voice role in animated series is an American animated television series based on the DC Comics fictional superhero team, the "Teen Titans"? |
| 5ae1f4cb554299234fd0436d | reflexion | True | 1685 | The inhabitant of Strasbourg, the city where the 122nd SS-Standarte was formed, in 2014 was approximately 276,170 people in the city proper, and 484,157 in the Greater Strasbourg area (Eurométropole de Strasbourg). | 276,170 inhabitants | What is the inhabitant of the city where  122nd SS-Standarte was formed in2014 |
| 5ae7e1fc55429952e35ea9cc | reflexion | True | 1821 | People in the Netherlands wear orange clothing during Oranjegekte or to celebrate Koningsdag. | orange | What color clothing do people of the Netherlands wear during Oranjegekte or to celebrate the national holiday Koningsdag?  |
| 5ae37c765542992f92d822d4 | reflexion | True | 1995 | Tromeo and Juliet | Tromeo and Juliet | What was the name of the 1996 loose adaptation of William Shakespeare's "Romeo & Juliet" written by James Gunn? |
| 5ae33c4d5542992f92d82262 | reflexion | True | 1479 | Bill Clinton | William Jefferson Clinton | Robert Suettinger was the national intelligence officer under which former Governor of Arkansas? |
| 5a77cb335542997042120b3a | reflexion | True | 1253 | John John Florence | John John Florence | What American professional Hawaiian surfer born 18 October 1992 won the Rip Curl Pro Portugal? |
| 5a8979f4554299669944a52e | reflexion | True | 1508 | The actress who plays Bobbi Bacha in *Suburban Madness* is Sela Ward. According to the context, her full name is Sela Ann Ward. Therefore, her middle name is **Ann**. | Ann | What is the middle name of the actress who plays Bobbi Bacha in Suburban Madness? |
| 5a713ea95542994082a3e6e4 | reflexion | True | 4377 | Apalachee | Apalachees | Alvaro Mexia had a diplomatic mission with which tribe of indigenous people? |
| 5a78bd9b554299078472774a | reflexion | True | 1782 | Alfred Gell and Edmund Leach were both British. | British | What nationality were social anthropologists Alfred Gell and Edmund Leach? |
| 5a7625e8554299109176e66a | reflexion | True | 1620 | 1865 | 1865 | In which year was the King who made the 1925 Birthday Honours born? |
| 5ae2dd2055429928c423950d | reflexion | True | 1678 | Newport | Newport | What is the county seat of the county where East Lempster, New Hampshire is located? |
| 5abdf12255429976d4830a2f | reflexion | True | 1843 | Bob Seger | Bob Seger | The Album Against the Wind was the 11th Album of a Rock singer Robert C Seger born may 6 1945. What was the Rock singers stage name ? |
| 5a88658955429938390d3f47 | reflexion | True | 2442 | Rostker v. Goldberg held that the practice of requiring only men to register for the draft was constitutional. | Conscription | Rostker v. Goldberg held that the practice of what way of filling armed forces vacancies was consitutional? |
| 5a86ebac55429960ec39b6d6 | reflexion | True | 1596 | Mondelez International | Mondelez International, Inc. | Handi-Snacks are a snack food product line sold by what American multinational confectionery, food, and beverage company that is based in Illinois? |
| 5aba5d2e55429901930fa799 | reflexion | True | 2080 | Monica Lewinsky | Monica Lewinsky | What was the name of a woman from the book titled "Their Lives: The Women Targeted by the Clinton Machine " and was also a former white house intern? |
| 5ae5736e5542990ba0bbb2b3 | reflexion | True | 2022 | April 1, 1949 | April 1, 1949 | When was the American lawyer, lobbyist and political consultant who was a senior member of the presidential campaign of Donald Trump born? |
| 5ae005b555429942ec259bec | reflexion | True | 1508 | 1866 | 1866 | In what year was the novel that Lourenço Mutarelli based "Nina" on based first published? |
| 5a7759fc5542993569682d60 | reflexion | True | 1600 | Teide National Park is located on the island of Tenerife in the Canary Islands, Spain. Garajonay National Park is located on the island of La Gomera, also in the Canary Islands, Spain. | Canary Islands, Spain | Where are Teide National Park and Garajonay National Park located? |
| 5a835478554299123d8c20ed | reflexion | True | 3072 | 250 million copies | 250 million | How many copies of Roald Dahl's variation on a popular anecdote sold? |
| 5aba749055429901930fa7d8 | reflexion | True | 1382 | film director | director | What occupation do Chris Menges and Aram Avakian share? |
| 5abfb3425542990832d3a1c0 | reflexion | True | 1539 | Andrew Jaspan was the co-founder of "The Conversation", an independent not-for-profit media outlet. | The Conversation | Andrew Jaspan was the co-founder of what not-for-profit media outlet? |
| 5ac3165c5542995ef918c10a | reflexion | True | 1221 | John Waters | John Waters | Which American film director hosted the 18th Independent Spirit Awards in 2002? |
| 5ae53b545542990ba0bbb23c | reflexion | True | 1267 | The hotel and casino where Bill Cosby's third album, *Why Is There Air?*, was recorded is the Flamingo Las Vegas in Las Vegas, Nevada. | Las Vegas Strip in Paradise | Where does the hotel and casino located in which Bill Cosby's third album was recorded? |
| 5ae224da554299234fd043ee | reflexion | True | 1471 | Yes, the Gibson contains gin, but the Zurracapote does not. | no | Do the drinks Gibson and Zurracapote both contain gin? |
| 5ae2b770554299495565db0f | reflexion | True | 1496 | March and April | March and April | In what month is the annual documentary film festival, that is presented by the fortnightly published British journal of literary essays, held?  |
| 5a80b3a9554299485f5986cc | reflexion | True | 1594 | Fairfax County | Fairfax County | Tysons Galleria is located in what county? |
| 5a8e0a005542995085b373a1 | reflexion | True | 2080 | Bordan Tkachuk was the CEO of Viglen, which provides IT products and services, including storage systems, servers, workstations, and data/voice communications equipment and services. | IT products and services | Bordan Tkachuk was the CEO of a company that provides what sort of products? |
| 5ac1b8ee5542994d76dccedc | reflexion | True | 5449 | Levni Yilmaz | Levni Yilmaz | Which filmmaker was known for animation, Lev Yilmaz or Pamela B. Green? |
| 5adccd795542990d50227d2c | reflexion | True | 1540 | Beijing | Beijing | In which city is the ambassador of the Rabat-Salé-Kénitra administrative region to China based? |
| 5a84c4135542994c784dda31 | reflexion | True | 1157 | No, Yingkou and Fuding are not the same level of city. Yingkou is a prefecture-level city in Liaoning Province, while Fuding is a county-level city in Fujian Province. | no | Are Yingkou and Fuding the same level of city? |

