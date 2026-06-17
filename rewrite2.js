const fs = require('fs');
const base = 'C:/Users/elieu/OneDrive/Desktop/biofinaltest/';

// unit4 #5 [4.1] - "correct publication detail" → required properties of genetic material (4.1 p5)
const u4 = JSON.parse(fs.readFileSync(base+'unit4_questions.json','utf8'));
u4[5] = {
  section:'4.1', title:'DNA Advances Through the 20th Century', t:'mc',
  q:'Before the structure of DNA was determined, scientists already understood what properties genetic material must have to perform its function. According to Unit 4.1, which option correctly lists these required properties?',
  a:1,
  opts:[
    'It must be a large protein molecule capable of folding into a complex 3-D structure that enzymes can recognize.',
    'It must be able to store information for structure, development, and metabolism; replicate with high accuracy; and be capable of undergoing rare mutations.',
    'It must dissolve easily in water, leave the nucleus freely during cell division, and degrade rapidly after use.',
    'It must bond directly to ribosomes, be present only in the cytoplasm, and lack the ability to change over generations.'
  ],
  explanation:'According to the Unit 4.1 notes, by the mid-20th century scientists understood that genetic material needed to: (1) store information for structure, development, and metabolism; (2) be stable enough to replicate with high accuracy; and (3) be capable of undergoing rare mutations to allow heritable variation. These three criteria were the functional requirements that DNA needed to satisfy to serve as hereditary material. Option A describes protein, not DNA. Options C and D describe properties that would make DNA non-functional as genetic material.'
};

// unit4 #62 [4.8] - "Mendel's life and experimental approach" → Particulate Theory vs Blending Inheritance (4.8 p3-4)
u4[62] = {
  section:'4.8', title:'Mendelian Inheritance P1 - Mendelian Genetics', t:'mc',
  q:"Gregor Mendel's results directly contradicted the dominant theory of inheritance accepted during his time. What was that theory, and what did Mendel's Particulate Theory propose instead?",
  a:2,
  opts:[
    "The prevailing theory held that offspring always resemble only one parent; Mendel's Particulate Theory proposed that traits blend equally from both parents in every generation.",
    "Spontaneous generation of new traits was the accepted view; Mendel's Particulate Theory proposed that all traits are inherited exclusively from the father.",
    "Blending inheritance proposed that contrasting parental traits merged into intermediate forms in offspring; Mendel's Particulate Theory proposed that discrete hereditary factors (alleles) are reshuffled between generations without blending.",
    "Inheritance of acquired characteristics was the dominant view; Mendel's Particulate Theory proposed that traits acquired during a parent's lifetime are passed to offspring in modified form."
  ],
  explanation:"The notes state that blending inheritance — the idea that parents of contrasting appearance produce offspring of intermediate appearance — was the popular concept during Mendel's time. Mendel's findings contradicted this, leading him to formulate the Particulate Theory of Inheritance, which holds that inheritance involves the reshuffling of discrete hereditary factors (alleles) from generation to generation rather than a permanent blending of parental traits. Option A reverses the relationship. Option B describes spontaneous generation, which applies to cells, not trait inheritance. Option D describes Lamarckian inheritance of acquired characteristics, a separate and unrelated theory."
};
fs.writeFileSync(base+'unit4_questions.json', JSON.stringify(u4,null,2));
console.log('unit4 #5 and #62 done');

// unit5 #2 [5.1] - "which vegetables Darwin used" → dogs descended from gray wolf / artificial selection mechanism (5.1 p14)
const u5 = JSON.parse(fs.readFileSync(base+'unit5_questions.json','utf8'));
u5[2] = {
  section:'5.1', title:'Darwin & Evidence for Evolution', t:'mc',
  q:'According to Unit 5.1, all domestic dog breeds are descended from the gray wolf, which began to be domesticated approximately 14,000 years ago. What does this example best demonstrate about artificial selection?',
  a:0,
  opts:[
    'A single ancestral species can produce extremely diverse phenotypes when humans selectively choose which individuals reproduce — demonstrating that heritable variation and selective pressure are sufficient to drive major phenotypic change.',
    'Artificial selection requires geographic isolation between populations for new phenotypes to develop, as seen in dog breeds developed in different regions.',
    'Dog breeds represent distinct new species created through artificial selection, proving that selection alone can produce reproductive isolation within a short timeframe.',
    'Domestic dogs acquired new traits through the inheritance of characteristics developed during the wolves’ lifetimes, such as tameness from repeated human contact.'
  ],
  explanation:"Unit 5.1 states that Darwin used the example of artificial selection to demonstrate his ideas on natural selection. All domestic dog breeds descend from the gray wolf; breeders chose which traits to perpetuate by selecting which individuals would reproduce, and the process of diversification led to extreme phenotypic differences. This shows that heritable variation combined with consistent selective pressure is sufficient to drive enormous phenotypic change. Option B is incorrect because geographic isolation is not required — artificial selection operates within a single breeding population. Option C is incorrect because dog breeds are not separate species; they can still interbreed. Option D describes Lamarckian inheritance of acquired characteristics, which is incorrect."
};
fs.writeFileSync(base+'unit5_questions.json', JSON.stringify(u5,null,2));
console.log('unit5 #2 done');

// unit8 #9 [8.2] - "which years population milestones" → two types of overpopulation (8.2 p19)
const u8 = JSON.parse(fs.readFileSync(base+'unit8_questions.json','utf8'));
u8[9] = {
  section:'8.2', title:'Population Ecology', t:'mc',
  q:'According to Unit 8.2, what are the two distinct types of overpopulation that can threaten an environment?',
  a:3,
  opts:[
    'Overpopulation caused by immigration from less-developed countries, and overpopulation caused by high birth rates in developed nations.',
    'Overpopulation due to lack of predators, and overpopulation due to disease resistance spreading through the population.',
    'Overpopulation caused by the exponential growth phase exceeding the deceleration phase, and overpopulation caused by an insufficient carrying capacity.',
    'Overpopulation due to population growth (too many individuals), and overpopulation due to increased resource consumption per capita (fewer individuals consuming at unsustainably high rates).'
  ],
  explanation:'Unit 8.2 notes that environmental impact is measured in terms of population size, resource consumption per capita, and resultant pollution. Correspondingly, two types of overpopulation are defined: (1) overpopulation due to population growth — there are simply too many individuals for the environment to support; and (2) overpopulation due to increased resource consumption — a smaller population consuming at an extremely high per-capita rate can still exceed the carrying capacity. This distinction is important because addressing overpopulation requires targeting the correct factor. Options A and B describe drivers of population change, not the two defined types of overpopulation. Option C conflates population growth models with the concept of overpopulation.'
};
fs.writeFileSync(base+'unit8_questions.json', JSON.stringify(u8,null,2));
console.log('unit8 #9 done');
console.log('All 4 additional questions rewritten.');
