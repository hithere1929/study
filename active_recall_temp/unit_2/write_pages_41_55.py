import json
import os

dest_dir = r"C:\Users\elieu\OneDrive\Desktop\biofinaltest\active_recall_temp\unit_2"
os.makedirs(dest_dir, exist_ok=True)

pages_data = {
    41: {
        "unit": 2,
        "page": 41,
        "filename": "Unit_2_2.txt",
        "section_title": "Chemistry of Organic Molecules",
        "page_num_in_file": 5,
        "slide_title": "Covalent Bonds",
        "original_text": "Covalent Bonds\u00a8Types of covalent bonds:\u00a4Single bondnDenoted with a single, solid line representing 2 elements sharing 1 pair of electrons\u00a4Double bondnDenoted with a pair of solid, parallel lines representing 2 elementssharing 2 pairs of electrons\u00a4Triple bondnDenoted with 3 solid, parallel lines representing 2 elements sharing 3 pairs of electrons",
        "explanation": "Covalent bonds can be categorized based on the number of electron pairs shared between two atoms. A single bond is represented by a single solid line and involves two atoms sharing one pair of electrons. A double bond is shown as a pair of parallel solid lines, representing the sharing of two pairs of electrons. A triple bond is denoted by three parallel solid lines, representing two elements sharing three pairs of electrons.",
        "questions": [
            {
                "q": "What does a double covalent bond represent?",
                "opts": [
                    "Two atoms sharing one pair of electrons.",
                    "Two atoms sharing two pairs of electrons.",
                    "Two atoms sharing three pairs of electrons.",
                    "An ionic attraction between two charged atoms."
                ],
                "a": 1,
                "exp": "A double bond represents two elements sharing two pairs (four total) of electrons, shown as two parallel lines."
            },
            {
                "q": "How is a triple covalent bond denoted in a structural chemical formula?",
                "opts": [
                    "A single solid line",
                    "A dashed line",
                    "Two parallel solid lines",
                    "Three parallel solid lines"
                ],
                "a": 3,
                "exp": "A triple bond is denoted using three solid, parallel lines to represent the sharing of three electron pairs."
            }
        ]
    },
    42: {
        "unit": 2,
        "page": 42,
        "filename": "Unit_2_2.txt",
        "section_title": "Chemistry of Organic Molecules",
        "page_num_in_file": 6,
        "slide_title": "Functional Groups",
        "original_text": "Functional Groups\u00a8Functional group: a cluster of atoms attached to an organic compound\u00a4Influences the characteristics of the molecule\u00a4Influences the chemical reactions the molecule undergoes\u00a8Ex: -OH = hydroxylgroup\u00a4Makes the molecule polar\u00a4Makes the molecule hydrophilic(water-loving); soluble in water\u00a4Organic compounds with hydroxyl groups attached known as alcohols\u00a8Other functional groups:\u00a4Carboxyl \u00a4Amino\u00a4Phosphate",
        "explanation": "A functional group is a specific cluster of atoms attached to an organic compound. These groups are critical because they influence the physical and chemical characteristics of the molecule as well as the types of chemical reactions it can undergo. An example is the hydroxyl group (-OH), which confers polarity onto the molecule, making it hydrophilic (water-loving) and soluble in water. Organic compounds containing one or more hydroxyl groups are known as alcohols. Other key functional groups in biological molecules include carboxyl, amino, and phosphate groups.",
        "questions": [
            {
                "q": "What is a functional group?",
                "opts": [
                    "A bond between metal and non-metal atoms.",
                    "A cluster of atoms attached to an organic compound that influences its characteristics and chemical reactions.",
                    "The central carbon chain of a carbohydrate.",
                    "An inactive part of a molecule that does not dissolve in water."
                ],
                "a": 1,
                "exp": "A functional group is a cluster of atoms attached to an organic compound that determines its properties and chemical reactivity."
            },
            {
                "q": "What properties does a hydroxyl group (-OH) impart to an organic molecule?",
                "opts": [
                    "It makes the molecule non-polar and hydrophobic.",
                    "It makes the molecule polar, hydrophilic, and soluble in water.",
                    "It turns the molecule into an inorganic salt.",
                    "It causes the molecule to form double bonds with carbon."
                ],
                "a": 1,
                "exp": "A hydroxyl group makes the molecule polar and hydrophilic (water-loving), which increases its solubility in water. Molecules with -OH groups are called alcohols."
            }
        ]
    },
    43: {
        "unit": 2,
        "page": 43,
        "filename": "Unit_2_2.txt",
        "section_title": "Chemistry of Organic Molecules",
        "page_num_in_file": 7,
        "slide_title": "Large C -Molecules",
        "original_text": "Large C -Molecules\u00a8Many organic compounds built from smaller, simpler molecules called monomers\u00a4Can bond to each other to form polymers –a molecule that consists of repeated, linked units\u00a8Macromolecule –a large polymer consisting of identical or structurally similar monomers\u00a4Carbohydrates\u00a4Proteins\u00a4Lipids\u00a4Nucleic Acids",
        "explanation": "Many large organic compounds are constructed from smaller, simpler molecular building blocks called monomers. Monomers can chemically bond to one another to form polymers, which are molecules consisting of repeated, linked monomer units. A macromolecule is defined as a large polymer made of identical or structurally similar monomers. The four primary classes of biological macromolecules are carbohydrates, proteins, lipids, and nucleic acids.",
        "questions": [
            {
                "q": "What is a polymer?",
                "opts": [
                    "A single, unbonded sub-atomic particle.",
                    "A molecule that consists of repeated, linked monomer units.",
                    "An inorganic compound that does not contain carbon.",
                    "An electron orbital furthest from the nucleus."
                ],
                "a": 1,
                "exp": "A polymer is a larger molecule composed of multiple repeated, linked units called monomers."
            },
            {
                "q": "Which of the following is NOT one of the four classes of macromolecules mentioned on the slide?",
                "opts": ["Carbohydrates", "Proteins", "Lipids", "Amino acids"],
                "a": 3,
                "exp": "The four classes of macromolecules listed are Carbohydrates, Proteins, Lipids, and Nucleic Acids. Amino acids are the monomers of proteins, not a class of macromolecules itself."
            }
        ]
    },
    44: {
        "unit": 2,
        "page": 44,
        "filename": "Unit_2_2.txt",
        "section_title": "Chemistry of Organic Molecules",
        "page_num_in_file": 8,
        "slide_title": "Polymer Formation/Degradation",
        "original_text": "Polymer Formation/Degradation\u00a8Monomerscombine to form polymersthrough a condensation reaction\u00a4Each time a monomer unit is added, a watermolecule is released\u00a4AKA dehydration synthesis\u00a8Polymers are broken down into their component monomers through a hydrolysis reaction\u00a4A watermolecule breaks the bond linking the monomers",
        "explanation": "Monomers combine to form larger polymer molecules via a condensation reaction, which is also commonly referred to as dehydration synthesis. During this reaction, each time a new monomer unit is linked to the chain, a water molecule is released. Conversely, polymers are degraded back into their individual monomer components through a hydrolysis reaction. In hydrolysis, a water molecule is consumed to break the chemical bond that links the monomers together.",
        "questions": [
            {
                "q": "What type of reaction links monomers together to form a polymer while releasing a water molecule?",
                "opts": ["Hydrolysis reaction", "Condensation reaction (dehydration synthesis)", "Ionization reaction", "Neutralization reaction"],
                "a": 1,
                "exp": "A condensation reaction (or dehydration synthesis) links monomers together and releases a water molecule as a byproduct."
            },
            {
                "q": "How does a hydrolysis reaction break down polymers?",
                "opts": [
                    "By releasing a water molecule to form a double bond.",
                    "By using a water molecule to break the bond linking the monomers.",
                    "By adding thermal energy to melt the covalent bonds.",
                    "By converting organic compounds into inorganic salts."
                ],
                "a": 1,
                "exp": "Hydrolysis uses a water molecule to chemically split the bond between monomers in a polymer chain."
            }
        ]
    },
    45: {
        "unit": 2,
        "page": 45,
        "filename": "Unit_2_2.txt",
        "section_title": "Chemistry of Organic Molecules",
        "page_num_in_file": 9,
        "slide_title": "Energy Currency",
        "original_text": "Energy Currency\u00a8Processes of life require constant supply of energy\u00a4Available to cells in the form of molecules that can store large amounts of energy in their chemical bonds\u00a4Most commonly adenosine triphosphate, ATP\nnComposed of 5-carbon sugar (ribose), nitrogen-containing double ring (adenine), 3 covalently linked phosphategroups\u00a8Covalent bonds between phosphates relatively unstable because of their net negative charge and close proximityto each other\u00a4Hydrolysis of ATP molecules releases energy that can be used by the cell to drive necessary chemical reactions",
        "explanation": "The processes of life require a continuous supply of energy, which is made available to cells through molecules capable of storing significant amounts of energy in their chemical bonds. The primary energy currency molecule used by cells is adenosine triphosphate (ATP). ATP is composed of three parts: a 5-carbon sugar (ribose), a nitrogen-containing double ring structure (adenine), and three covalently linked phosphate groups. The covalent bonds linking the phosphate groups are relatively unstable because the phosphates carry net negative charges and are situated in close proximity, causing them to repel one another. The hydrolysis of ATP breaks these unstable bonds, releasing energy that cells use to fuel vital chemical reactions.",
        "questions": [
            {
                "q": "What are the three components that make up an ATP molecule?",
                "opts": [
                    "Glucose, adenine, and two phosphate groups",
                    "Ribose (5-carbon sugar), adenine (nitrogen double ring), and three phosphate groups",
                    "Deoxyribose, cytosine, and one phosphate group",
                    "Glycerol, fatty acids, and a carboxyl group"
                ],
                "a": 1,
                "exp": "ATP is composed of a 5-carbon sugar (ribose), a nitrogen-containing double ring (adenine), and three phosphate groups."
            },
            {
                "q": "Why are the covalent bonds between the phosphate groups in ATP relatively unstable?",
                "opts": [
                    "They are weak hydrogen bonds.",
                    "The phosphate groups have negative charges and are in close proximity, creating repulsive forces.",
                    "They are double covalent bonds that break easily in water.",
                    "They are ionic bonds between a metal and a non-metal."
                ],
                "a": 1,
                "exp": "The negative charges on the closely positioned phosphate groups repel each other, making the covalent bonds between them unstable and high in potential energy."
            }
        ]
    },
    46: {
        "unit": 2,
        "page": 46,
        "filename": "Unit_2_2.txt",
        "section_title": "Chemistry of Organic Molecules",
        "page_num_in_file": 10,
        "slide_title": "ATP",
        "original_text": "ATP",
        "explanation": "This slide serves as a placeholder for a diagram showing the chemical structure of ATP.",
        "questions": [
            {
                "q": "What molecule is featured on this placeholder slide?",
                "opts": ["Glucose", "DNA", "ATP", "Water"],
                "a": 2,
                "exp": "The slide title is 'ATP', representing the chemical structure of adenosine triphosphate."
            }
        ]
    },
    47: {
        "unit": 2,
        "page": 47,
        "filename": "Unit_2_2.txt",
        "section_title": "Chemistry of Organic Molecules",
        "page_num_in_file": 11,
        "slide_title": "Practice Exercise",
        "original_text": "Practice Exercise\u00a8On a sheet of paper using C and H atoms only, draw the following:\u00a4A 5 carbon structure\u00a4A 3 carbon structure\u00a4A 4 carbon structure with a single bonded –OH group",
        "explanation": "This is a student practice exercise. It asks students to draw three carbon-based structures using carbon (C) and hydrogen (H) atoms only: a 5-carbon structure, a 3-carbon structure, and a 4-carbon structure that includes a single-bonded hydroxyl (-OH) group.",
        "questions": [
            {
                "q": "Which functional group is requested to be drawn on the 4-carbon structure in this practice exercise?",
                "opts": ["Carboxyl group", "Amino group", "Hydroxyl group (-OH)", "Phosphate group"],
                "a": 2,
                "exp": "The prompt asks to draw 'a 4 carbon structure with a single bonded –OH group', which is a hydroxyl group."
            }
        ]
    },
    48: {
        "unit": 2,
        "page": 48,
        "filename": "Unit_2_2.txt",
        "section_title": "Chemistry of Organic Molecules",
        "page_num_in_file": 12,
        "slide_title": "Molecules of Life",
        "original_text": "Molecules of Life",
        "explanation": "This slide introduces the major 'Molecules of Life', which are the organic macromolecules found in all living systems.",
        "questions": [
            {
                "q": "What is the general title of the section introduced on this slide?",
                "opts": ["Inorganic Chemistry", "Molecules of Life", "Cell Biology", "Ecology"],
                "a": 1,
                "exp": "The slide is titled 'Molecules of Life'."
            }
        ]
    },
    49: {
        "unit": 2,
        "page": 49,
        "filename": "Unit_2_2.txt",
        "section_title": "Chemistry of Organic Molecules",
        "page_num_in_file": 13,
        "slide_title": "1: Carbohydrates",
        "original_text": "1: Carbohydrates\u00a8Carbohydrates: Carbon/ Water\u00a4Organic compounds composed of carbon, hydrogen and oxygen in a ratio of about 1C : 2H : 1O\u00a4Number of atoms can vary; ratio remains the same\u00a8Serve as energy source and structural material\u00a8Exist as monosaccharides, disaccharidesand polysaccharides",
        "explanation": "Carbohydrates are organic compounds consisting of carbon, hydrogen, and oxygen, with a characteristic atomic ratio of approximately 1 Carbon to 2 Hydrogen to 1 Oxygen (1C:2H:1O). Although the total number of atoms in different carbohydrates can vary, this ratio remains constant. Carbohydrates function as primary energy sources and structural materials in living things. They exist in three main forms: monosaccharides (single sugars), disaccharides (double sugars), and polysaccharides (complex chains).",
        "questions": [
            {
                "q": "What is the characteristic atomic ratio of elements in a carbohydrate?",
                "opts": ["1C : 1H : 1O", "2C : 1H : 2O", "1C : 2H : 1O", "1C : 2H : 2O"],
                "a": 2,
                "exp": "Carbohydrates are composed of carbon, hydrogen, and oxygen in a ratio of approximately 1C : 2H : 1O."
            },
            {
                "q": "What are the three structural forms in which carbohydrates exist?",
                "opts": [
                    "Amino acids, peptides, and proteins",
                    "Monosaccharides, disaccharides, and polysaccharides",
                    "Glycerol, fatty acids, and triglycerides",
                    "Nucleotides, DNA, and RNA"
                ],
                "a": 1,
                "exp": "Carbohydrates exist as monosaccharides, disaccharides, and polysaccharides."
            }
        ]
    },
    50: {
        "unit": 2,
        "page": 50,
        "filename": "Unit_2_2.txt",
        "section_title": "Chemistry of Organic Molecules",
        "page_num_in_file": 14,
        "slide_title": "1: Monosaccharides",
        "original_text": "1: Monosaccharides\u00a8Monosaccharide: monomer unit of carbohydrate\u00a4Also known as simple sugar\u00a4General formula: (CH2O)n where nis any whole number from 3-8nEx: (CH2O)6 \u00e0C6H12O6 \u00a8Most common monosaccharides:\u00a4Glucose–energy for cells (what most sugars are broken down into \u00a4Fructose–found in fruit; sweetest simple sugar  \u00a4Galactose–found in milk",
        "explanation": "A monosaccharide is the monomer building block of a carbohydrate, also commonly referred to as a simple sugar. The general chemical formula for a monosaccharide is (CH2O)n, where 'n' represents any whole number ranging from 3 to 8 (for example, when n is 6, the resulting formula is C6H12O6). The three most common monosaccharides are glucose, which is the primary energy source for cells and the molecule that most dietary sugars are ultimately broken down into; fructose, which is found in fruits and is the sweetest of the simple sugars; and galactose, which is a sugar found in milk.",
        "questions": [
            {
                "q": "What is the general formula for a monosaccharide?",
                "opts": [
                    "(CHO)n",
                    "(CH2O)n, where n is a whole number from 3-8",
                    "(C2H2O)n",
                    "(CH3O)n"
                ],
                "a": 1,
                "exp": "The general chemical formula for monosaccharides is (CH2O)n, where n ranges from 3 to 8."
            },
            {
                "q": "Which of the following matches the monosaccharide to its correct description?",
                "opts": [
                    "Glucose - milk sugar; Fructose - cellular energy; Galactose - fruit sugar",
                    "Glucose - sweetest sugar; Fructose - milk sugar; Galactose - cellular energy",
                    "Glucose - cellular energy; Fructose - fruit sugar (sweetest); Galactose - milk sugar",
                    "Glucose - fruit sugar; Fructose - milk sugar; Galactose - sweetest sugar"
                ],
                "a": 2,
                "exp": "Glucose provides energy for cells; Fructose is found in fruit and is the sweetest simple sugar; Galactose is found in milk."
            }
        ]
    },
    51: {
        "unit": 2,
        "page": 51,
        "filename": "Unit_2_2.txt",
        "section_title": "Chemistry of Organic Molecules",
        "page_num_in_file": 15,
        "slide_title": "1: Isomers",
        "original_text": "1: Isomers\u00a8All have same chemical formula (C6H12O6) but different structures\u00a4Isomer: compounds that have the same chemical formula, but different structures\u00a8Differences in structure determine the differences in properties of the compounds\nGlucoseFructoseGalactose",
        "explanation": "Although glucose, fructose, and galactose share the exact same chemical formula (C6H12O6), they possess different arrangements of their atoms. Compounds that share the same chemical formula but have different chemical structures are known as isomers. These structural differences are significant because they determine the distinct physical and chemical properties of each compound.",
        "questions": [
            {
                "q": "What is an isomer?",
                "opts": [
                    "Molecules with the same structure but different chemical formulas.",
                    "Compounds that have the same chemical formula but different structural arrangements.",
                    "Atoms of the same element with different numbers of neutrons.",
                    "Molecules that only dissolve in non-polar solvents."
                ],
                "a": 1,
                "exp": "An isomer is defined as a compound with the same chemical formula but a different structural arrangement."
            },
            {
                "q": "Which of the following sets of sugars are isomers of each other?",
                "opts": [
                    "Glucose, sucrose, starch",
                    "Glucose, fructose, galactose",
                    "Ribose, deoxyribose, glucose",
                    "Glycogen, cellulose, chitin"
                ],
                "a": 1,
                "exp": "Glucose, fructose, and galactose all have the chemical formula C6H12O6 but different structures, making them isomers."
            }
        ]
    },
    52: {
        "unit": 2,
        "page": 52,
        "filename": "Unit_2_2.txt",
        "section_title": "Chemistry of Organic Molecules",
        "page_num_in_file": 16,
        "slide_title": "1: Complex Sugars",
        "original_text": "1: Complex Sugars\u00a8Monosaccharidescombine via condensation reaction to form disaccharides& polysaccharides\u00a4Bond between carbohydrate monomers known as glycosidicbond \u00a8Disaccharide–double sugar\u00a4Ex: Glucose + fructose \u00e0sucrose (table sugar)\u00a8Polysaccharide–complex molecule composed of 3 or more monosaccharides\u00a4Ex: glycogen–animal storage of glucose\nnHundreds of glucose molecules bonded together in a highly branched chain\nnStored in liver & muscle; can quickly be broken down into glucose monomers for energy\u00a4Ex: starch–plant storage of glucose \nnCan be branched similar to glycogen or coiled & unbranched\u00a4Ex: cellulose–plant structural molecule; gives strength & rigidity to plant cells; 50% of the composition of wood\nnThousands of glucose molecules linked in long, straight chains that hydrogen bond to each other resulting in strong structure",
        "explanation": "Monosaccharides undergo condensation reactions to link together and form more complex carbohydrates, namely disaccharides (double sugars) and polysaccharides (complex molecules composed of three or more monosaccharides). The covalent bond that links carbohydrate monomers together is called a glycosidic bond. An example of a disaccharide is sucrose (common table sugar), which is formed by joining glucose and fructose. Important polysaccharides include glycogen, which is used by animals to store glucose, consisting of hundreds of glucose molecules linked in a highly branched chain stored in the liver and muscles for quick breakdown into energy; starch, which is the glucose storage molecule for plants, existing in either branched or coiled, unbranched forms; and cellulose, a structural polysaccharide in plants that provides strength and rigidity to plant cells (constituting about 50% of wood) and consists of thousands of glucose molecules linked in long, straight chains that hydrogen-bond to each other to form a highly durable structure.",
        "questions": [
            {
                "q": "What is the name of the chemical bond that links carbohydrate monomers together?",
                "opts": ["Peptide bond", "Glycosidic bond", "Phosphodiester bond", "Ester bond"],
                "a": 1,
                "exp": "The bond formed between monosaccharides in complex sugars is called a glycosidic bond."
            },
            {
                "q": "Which polysaccharide is used by animals for glucose storage and is stored in the liver and muscles?",
                "opts": ["Starch", "Cellulose", "Glycogen", "Chitin"],
                "a": 2,
                "exp": "Glycogen is a highly branched polysaccharide used by animals to store glucose in liver and muscle tissue."
            },
            {
                "q": "How does cellulose differ structurally from glycogen and starch, allowing it to provide rigidity to plant cells?",
                "opts": [
                    "It is highly branched and stored in animal muscles.",
                    "It is composed of fructose monomers instead of glucose.",
                    "It consists of thousands of glucose molecules in long, straight chains that hydrogen-bond to each other.",
                    "It is soluble in non-polar solvents."
                ],
                "a": 2,
                "exp": "Cellulose consists of thousands of glucose monomers in long, straight chains. These chains hydrogen-bond to one another, forming a strong, rigid structure that gives plant cell walls strength."
            }
        ]
    },
    53: {
        "unit": 2,
        "page": 53,
        "filename": "Unit_2_2.txt",
        "section_title": "Chemistry of Organic Molecules",
        "page_num_in_file": 17,
        "slide_title": "1: Di-and Polysaccharide Structures",
        "original_text": "1: Di-and Polysaccharide Structures\nSucrose\nCellulose",
        "explanation": "This slide displays diagrams showing the chemical structures of the disaccharide sucrose and the structural polysaccharide cellulose.",
        "questions": [
            {
                "q": "Which two carbohydrate structures are displayed as diagrams on this slide?",
                "opts": [
                    "Glucose and Galactose",
                    "Sucrose and Cellulose",
                    "Glycogen and Starch",
                    "Fructose and Lactose"
                ],
                "a": 1,
                "exp": "The slide title and text mention 'Sucrose' (a disaccharide) and 'Cellulose' (a polysaccharide)."
            }
        ]
    },
    54: {
        "unit": 2,
        "page": 54,
        "filename": "Unit_2_2.txt",
        "section_title": "Chemistry of Organic Molecules",
        "page_num_in_file": 18,
        "slide_title": "2: Proteins",
        "original_text": "2: Proteins\u00a8Proteins: organic compounds composed mainly of carbon, hydrogen, oxygen& nitrogen\u00a4Formed by the linkage of monomers: amino acids\u00a8Most common molecule in the body (after water)\u00a4Hair, nails, horns, skin, muscles, enzymes, etc. all composed of proteins\u00a4100,000’s of protein structures have been identified",
        "explanation": "Proteins are organic compounds composed primarily of carbon, hydrogen, oxygen, and nitrogen. They are formed by linking together monomer units known as amino acids. Next to water, proteins are the most abundant molecules in the human body, forming structures such as hair, nails, horns, skin, muscles, and enzymes. To date, hundreds of thousands of unique protein structures have been identified.",
        "questions": [
            {
                "q": "What are the monomer building blocks of proteins?",
                "opts": ["Monosaccharides", "Fatty acids", "Amino acids", "Nucleotides"],
                "a": 2,
                "exp": "Proteins are polymers formed by linking together amino acid monomers."
            },
            {
                "q": "Which element is found in proteins that is typically absent in simple carbohydrates?",
                "opts": ["Carbon", "Hydrogen", "Oxygen", "Nitrogen"],
                "a": 3,
                "exp": "Proteins are composed mainly of carbon, hydrogen, oxygen, and nitrogen. Nitrogen is a key element in proteins, whereas simple carbohydrates (C, H, O) do not contain nitrogen."
            }
        ]
    },
    55: {
        "unit": 2,
        "page": 55,
        "filename": "Unit_2_2.txt",
        "section_title": "Chemistry of Organic Molecules",
        "page_num_in_file": 19,
        "slide_title": "2: Amino Acids",
        "original_text": "2: Amino Acids\u00a820 amino acids; share the same basic structure:\u00a4Central C atom covalently bonded to 4 other atoms/functional groups\nnHydrogen atom\nnCarboxyl group\nnAmino group\nnVariable side chain, known as R group",
        "explanation": "There are 20 different amino acids that make up proteins, and they all share a common basic chemical structure. Each amino acid contains a central carbon (C) atom that is covalently bonded to four distinct atoms or functional groups: a hydrogen (H) atom, a carboxyl group (-COOH), an amino group (-NH2), and a variable side chain referred to as the R group, which is what distinguishes one amino acid from another.",
        "questions": [
            {
                "q": "Which of the following is NOT one of the groups bonded to the central carbon of an amino acid?",
                "opts": ["Carboxyl group", "Amino group", "Phosphate group", "Variable R group"],
                "a": 2,
                "exp": "An amino acid central carbon is bonded to a hydrogen atom, a carboxyl group, an amino group, and a variable R group. It does not contain a phosphate group as part of its basic monomer structure."
            },
            {
                "q": "What component of an amino acid's structure varies between the 20 different amino acids?",
                "opts": ["The carboxyl group", "The amino group", "The central carbon atom", "The variable side chain (R group)"],
                "a": 3,
                "exp": "The 20 amino acids share the same basic backbone but differ in their variable side chain, known as the R group."
            }
        ]
    }
}

for page, data in pages_data.items():
    file_path = os.path.join(dest_dir, f"page_{page}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

print("Saved pages 41 to 55 successfully.")
