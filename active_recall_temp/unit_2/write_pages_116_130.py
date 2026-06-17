import json
import os

dest_dir = r"C:\Users\elieu\OneDrive\Desktop\biofinaltest\active_recall_temp\unit_2"
os.makedirs(dest_dir, exist_ok=True)

pages_data = {
    116: {
        "unit": 2,
        "page": 116,
        "filename": "Unit_2_4.txt",
        "section_title": "Metabolism",
        "page_num_in_file": 19,
        "slide_title": "ATP",
        "original_text": "ATP\u00a8Hydrolysis of ATP releases energy by transferring its third phosphate from ATP to some other molecule in a process called phosphorylation.\u00a8Most cellular work depends on ATP energizing molecules by phosphorylating them.",
        "explanation": "The hydrolysis of ATP (adenosine triphosphate) releases chemical energy. This energy release is achieved by transferring the third phosphate group from the ATP molecule to another target molecule, a chemical process known as phosphorylation. Most cellular work—such as chemical synthesis, active transport, and mechanical movement—depends on ATP energizing molecules by phosphorylating them, which alters their energy state or shape.",
        "questions": [
            {
                "q": "What is the process of transferring a phosphate group from ATP to another molecule called?",
                "opts": ["Hydrolysis", "Condensation", "Phosphorylation", "Dehydration synthesis"],
                "a": 2,
                "exp": "Phosphorylation is the specific term for transferring a phosphate group (usually from ATP) to another molecule to energize it."
            },
            {
                "q": "How does ATP drive most cellular work?",
                "opts": [
                    "By absorbing heat from the cell's surroundings.",
                    "By transferring its third phosphate group to another molecule (phosphorylating it) to energize it.",
                    "By breaking down proteins into simple sugars.",
                    "By converting kinetic energy into potential energy."
                ],
                "a": 1,
                "exp": "Cells couple ATP hydrolysis to other reactions by transferring the released phosphate group to other molecules, which activates or energizes them to perform work."
            }
        ]
    },
    117: {
        "unit": 2,
        "page": 117,
        "filename": "Unit_2_4.txt",
        "section_title": "Metabolism",
        "page_num_in_file": 20,
        "slide_title": "ATP",
        "original_text": "ATP\u00a8A cell uses and regenerates ATP continuously.\u00a8In the ATP cycle, energy released in an exergonic reaction, such as the breakdown of glucose during cellular respiration, is used in an endergonic reaction to generate ATP from ADP.",
        "explanation": "A living cell continuously consumes and regenerates ATP in what is known as the ATP cycle. To regenerate ATP, energy released from exergonic (energy-yielding) pathways, such as the breakdown of glucose during cellular respiration, is harnessed to drive an endergonic (energy-requiring) reaction that attaches a free phosphate group back onto ADP (adenosine diphosphate).",
        "questions": [
            {
                "q": "What reactions provide the energy needed to regenerate ATP from ADP in the ATP cycle?",
                "opts": [
                    "Endergonic reactions, like building proteins",
                    "Exergonic reactions, like the breakdown of glucose in cellular respiration",
                    "Osmotic pressure changes across the membrane",
                    "Active transport of sodium ions"
                ],
                "a": 1,
                "exp": "The energy needed to regenerate ATP is supplied by exergonic reactions, primarily glucose catabolism during cellular respiration."
            }
        ]
    },
    118: {
        "unit": 2,
        "page": 118,
        "filename": "Unit_2_4.txt",
        "section_title": "Metabolism",
        "page_num_in_file": 21,
        "slide_title": "ATP",
        "original_text": "ATP\nATP synthesis is endergonic\nATP hydrolysis is exergonic\nEnergy from cellular respiration (exergonic) drives ATP synthesis\nATP hydrolysis releases energy for cellular work (endergonic)\nATP <-> ADP + P",
        "explanation": "This slide details the thermodynamics of the ATP cycle. ATP synthesis (joining ADP and a phosphate group) is endergonic, meaning it requires energy, which is provided by exergonic pathways like cellular respiration. Conversely, ATP hydrolysis (splitting ATP into ADP and a phosphate) is exergonic, meaning it releases energy, which is used to power endergonic cellular work.",
        "questions": [
            {
                "q": "Which of the following correctly pairs the ATP cycle process with its thermodynamic classification?",
                "opts": [
                    "ATP synthesis is exergonic; ATP hydrolysis is endergonic",
                    "ATP synthesis is endergonic; ATP hydrolysis is exergonic",
                    "Both ATP synthesis and hydrolysis are exergonic",
                    "Both ATP synthesis and hydrolysis are endergonic"
                ],
                "a": 1,
                "exp": "Synthesizing ATP from ADP and phosphate requires energy input (endergonic), while breaking ATP down to release energy is exergonic."
            }
        ]
    },
    119: {
        "unit": 2,
        "page": 119,
        "filename": "Unit_2_4.txt",
        "section_title": "Metabolism",
        "page_num_in_file": 22,
        "slide_title": "Metabolism",
        "original_text": "Metabolism\u00a8Catabolism\u00a5Relates to the degradative reactions that occur within cells\u00a5Energy released in the breaking of moleculesnProteins --> Amino Acids        \u00a8Anabolism\u00a5Relates to the constructive reactions that occur within a cell. \u00a5Energy must be input in the formation of moleculesnGlucose --> Complex Carbohydrates",
        "explanation": "Metabolism is composed of two opposing pathways: catabolism and anabolism. Catabolism refers to the degradative chemical reactions within cells that break down large, complex molecules into simpler units (such as breaking proteins down into amino acids), releasing stored chemical energy. Anabolism refers to the constructive, biosynthetic reactions within a cell that build complex molecules from simpler building blocks (such as building complex carbohydrates from glucose), which requires an input of energy.",
        "questions": [
            {
                "q": "What is the difference between catabolism and anabolism?",
                "opts": [
                    "Catabolism builds molecules and stores energy; anabolism breaks down molecules and releases energy.",
                    "Catabolism breaks down molecules and releases energy; anabolism builds complex molecules and requires energy input.",
                    "Catabolism occurs only in the nucleus; anabolism occurs only in the cytoplasm.",
                    "There is no difference; they are synonymous terms."
                ],
                "a": 1,
                "exp": "Catabolism refers to the degradative, energy-releasing reactions that break down molecules, while anabolism refers to constructive, energy-requiring reactions that build molecules."
            },
            {
                "q": "Which of the following is an example of an anabolic reaction?",
                "opts": [
                    "Breaking down a protein into amino acids.",
                    "Converting glucose into complex carbohydrates.",
                    "Hydrolyzing ATP into ADP and phosphate.",
                    "The breakdown of glucose during cellular respiration."
                ],
                "a": 1,
                "exp": "Building complex carbohydrates from glucose is a constructive (anabolic) process that requires energy, whereas breaking down proteins is catabolic."
            }
        ]
    },
    120: {
        "unit": 2,
        "page": 120,
        "filename": "Unit_2_4.txt",
        "section_title": "Metabolism",
        "page_num_in_file": 23,
        "slide_title": "Metabolism",
        "original_text": "Metabolism",
        "explanation": "This slide serves as a heading placeholder for concepts regarding cell metabolism.",
        "questions": [
            {
                "q": "What is the topic of this slide?",
                "opts": ["Respiration", "Photosynthesis", "Metabolism", "Enzymes"],
                "a": 2,
                "exp": "The slide is titled 'Metabolism'."
            }
        ]
    },
    121: {
        "unit": 2,
        "page": 121,
        "filename": "Unit_2_4.txt",
        "section_title": "Metabolism",
        "page_num_in_file": 24,
        "slide_title": "Metabolism",
        "original_text": "Metabolism\u00a8Glucose is considered to be the primary source of sugar used to generate ATP \u00a8Fats make excellent cellular fuel because they \u00a5contain many hydrogen atoms and thus many energy-rich electrons and\u00a5yield more than twice as much ATP per gram as a gram of carbohydrate. \u00a8Proteins can also be used for fuel, although your body preferentially burns sugars and fats first.",
        "explanation": "Glucose is the primary sugar utilized by cells to generate ATP. However, fats serve as highly efficient cellular fuel because they contain large numbers of hydrogen atoms, providing a dense source of energy-rich electrons. Consequently, fats yield more than twice as much ATP per gram compared to carbohydrates. While proteins can also be broken down and used for fuel, the body preferentially metabolizes sugars and fats first to spare proteins.",
        "questions": [
            {
                "q": "Why do fats yield more than twice as much ATP per gram as carbohydrates?",
                "opts": [
                    "They contain fewer C-H bonds.",
                    "They contain many hydrogen atoms and thus many energy-rich electrons.",
                    "They are soluble in water.",
                    "They contain high concentrations of nitrogen."
                ],
                "a": 1,
                "exp": "Fats contain many hydrogen atoms and energy-rich electrons, which allows them to yield more than double the energy (ATP) per gram compared to carbohydrates."
            },
            {
                "q": "Which fuel source does the human body preferentially burn first for energy?",
                "opts": ["Proteins and Nucleic acids", "Sugars (carbohydrates) and Fats", "Waxes and Steroids", "Amino acids only"],
                "a": 1,
                "exp": "The body preferentially burns sugars and fats for fuel before breaking down proteins."
            }
        ]
    },
    122: {
        "unit": 2,
        "page": 122,
        "filename": "Unit_2_4.txt",
        "section_title": "Metabolism",
        "page_num_in_file": 25,
        "slide_title": "Metabolism",
        "original_text": "Metabolism\u00a8Metabolism is:\u00a5the total anabolic and catabolic reactions\u00a5the total exergonic and endergonic reactions\u00a5the total energy being used and the total energy being stored",
        "explanation": "Metabolism is defined comprehensively as the sum total of all anabolic (building) and catabolic (breaking down) reactions, all exergonic (energy-releasing) and endergonic (energy-requiring) reactions, and the total energy being consumed and stored by an organism's cells.",
        "questions": [
            {
                "q": "Which of the following definitions describes metabolism?",
                "opts": [
                    "The process of water diffusing across a membrane.",
                    "The sum total of all anabolic, catabolic, exergonic, and endergonic reactions, representing the total energy used and stored in an organism.",
                    "The rate of DNA replication in a cell.",
                    "The physical changes that occur when matter changes state."
                ],
                "a": 1,
                "exp": "Metabolism is the sum of all chemical activities in the body, including anabolic/catabolic and endergonic/exergonic reactions, representing energy usage and storage."
            }
        ]
    },
    123: {
        "unit": 2,
        "page": 123,
        "filename": "Unit_2_5.txt",
        "section_title": "Enzymes",
        "page_num_in_file": 1,
        "slide_title": "UNIT 2: ENZYMESBiology 9              Mr. QueenanText -Ch 2.4 (p 58-63)",
        "explanation": "This is the title slide for Unit 2: Enzymes for Biology 9 with Mr. Queenan, which covers Textbook Chapter 2.4 on pages 58-63.",
        "questions": [
            {
                "q": "Which chapter and page range of the textbook correspond to the Enzymes section?",
                "opts": [
                    "Chapter 2.1 (p 42-45)",
                    "Chapter 2.4 (p 58-63)",
                    "Chapter 8.3 (p 260-273)",
                    "Chapter 2.3 (p 52-56)"
                ],
                "a": 1,
                "exp": "The slide title explicitly references 'Text -Ch 2.4 (p 58-63)'."
            }
        ]
    },
    124: {
        "unit": 2,
        "page": 124,
        "filename": "Unit_2_5.txt",
        "section_title": "Enzymes",
        "page_num_in_file": 2,
        "slide_title": "Questions",
        "original_text": "Questions\u00a8You are lost in the woods, and nightfall is approaching. You need to make a fire.\u00a5What materials do you need for the fire\u00a5If you had access, what could be used to create a larger fire, or help you make the fire faster?",
        "explanation": "This slide poses a warm-up scenario where students imagine making a fire in the woods. The exercise prompts students to think about materials needed and methods to accelerate fire production (such as using an accelerant or match), serving as an analogy for activation energy and catalysts.",
        "questions": [
            {
                "q": "What conceptual analogy is introduced by the fire-making questions on this slide?",
                "opts": [
                    "The difference between animal and plant cells.",
                    "Activation energy and the role of catalysts/enzymes in speeding up reactions.",
                    "The passive transport of water across membranes.",
                    "The structure of the DNA double helix."
                ],
                "a": 1,
                "exp": "Thinking about what is needed to start a fire (an initial spark/energy) and how to speed it up (catalyst) introduces the concepts of activation energy and enzymes."
            }
        ]
    },
    125: {
        "unit": 2,
        "page": 125,
        "filename": "Unit_2_5.txt",
        "section_title": "Enzymes",
        "page_num_in_file": 3,
        "slide_title": "Enzymes",
        "original_text": "Enzymes\u00a8Although biological molecules possess much potential energy, it is not released spontaneously.\u00a5An energy barrier must be overcome before a chemical reaction can begin.\u00a5This energy is called the activation energy(because it activates the reactants).",
        "explanation": "Even though biological molecules contain a significant amount of stored potential energy in their chemical bonds, this energy is not released spontaneously. An initial energy barrier must be overcome to initiate any chemical reaction. The energy input required to cross this barrier and start the reaction is called the activation energy, as it works to activate the reactant molecules.",
        "questions": [
            {
                "q": "What is activation energy?",
                "opts": [
                    "The energy released during ATP hydrolysis.",
                    "The energy barrier that must be overcome before a chemical reaction can begin.",
                    "The thermal energy of water at boiling point.",
                    "The energy stored inside a steroid ring."
                ],
                "a": 1,
                "exp": "Activation energy is the initial energy input required to overcome the energy barrier and start a chemical reaction."
            }
        ]
    },
    126: {
        "unit": 2,
        "page": 126,
        "filename": "Unit_2_5.txt",
        "section_title": "Enzymes",
        "page_num_in_file": 4,
        "slide_title": "Enzymes",
        "original_text": "Enzymes\u00a8We can think of activation energy as the amount of energy needed for a reactant molecule to move “uphill” to a higher-energy but an unstable state so that the “downhill” part of the reaction can begin.\u00a8One way to speed up a reaction is to add heat, which agitates atoms so that bonds break more easily and reactions can proceed, but too much heat will kill a cell.",
        "explanation": "Activation energy can be conceptualized as the 'uphill' energy needed to push reactant molecules into a highly unstable, high-energy transition state, allowing the 'downhill' portion of the reaction (forming products) to begin. While adding heat is a simple physical way to accelerate chemical reactions by agitating atoms and facilitating bond breakage, biological cells cannot use excessive heat because high temperatures would destroy cellular proteins and kill the cell.",
        "questions": [
            {
                "q": "Why is adding heat NOT a viable biological strategy for cells to speed up chemical reactions?",
                "opts": [
                    "Heat converts reactants into inorganic salts.",
                    "Heat slows down the movement of molecules.",
                    "Excessive heat destroys cellular structures and will kill the cell.",
                    "Heat prevents ATP from releasing phosphate."
                ],
                "a": 2,
                "exp": "Although heat speeds up reactions by agitating atoms, too much heat denatures proteins and destroys cells, making it unsafe for living organisms."
            }
        ]
    },
    127: {
        "unit": 2,
        "page": 127,
        "filename": "Unit_2_5.txt",
        "section_title": "Enzymes",
        "page_num_in_file": 5,
        "slide_title": "Enzymes",
        "original_text": "Enzymes\u00a8Enzymes\u00a5function as biological catalysts,\u00a5increase the rate of a reaction without being consumed by the reaction, and\u00a5are usually proteins (although some RNA molecules can function as enzymes (Ribozymes)).\u00a8Enzymes speed up a reaction by lowering the activation energy needed for a reaction to begin.",
        "explanation": "Enzymes are specialized biological catalysts that accelerate chemical reactions without being consumed or permanently altered in the process. Most enzymes are proteins, though some RNA molecules (known as ribozymes) can also act as catalysts. Enzymes speed up chemical reactions in cells by lowering the activation energy barrier required for the reaction to initiate, allowing reactions to occur rapidly at normal body temperatures.",
        "questions": [
            {
                "q": "How do enzymes speed up chemical reactions in cells?",
                "opts": [
                    "By increasing the temperature of the cell.",
                    "By increasing the amount of reactants.",
                    "By lowering the activation energy barrier needed for the reaction to begin.",
                    "By consuming the products of the reaction."
                ],
                "a": 2,
                "exp": "Enzymes accelerate chemical reactions by lowering the activation energy needed to start them, allowing reactions to proceed under physiological conditions."
            },
            {
                "q": "What are catalysts that consist of RNA molecules called?",
                "opts": ["Enzymatic proteins", "Ribozymes", "Polypeptides", "Coenzymes"],
                "a": 1,
                "exp": "While most enzymes are proteins, catalytic RNA molecules are known as ribozymes."
            }
        ]
    },
    128: {
        "unit": 2,
        "page": 128,
        "filename": "Unit_2_5.txt",
        "section_title": "Enzymes",
        "page_num_in_file": 6,
        "slide_title": "Enzymes",
        "original_text": "Enzymes",
        "explanation": "This slide serves as an intermediate title slide for the enzyme mechanism subsection.",
        "questions": [
            {
                "q": "What is the title of this section slide?",
                "opts": ["Metabolism", "Enzymes", "Activation Energy", "Ribozymes"],
                "a": 1,
                "exp": "The slide title is 'Enzymes'."
            }
        ]
    },
    129: {
        "unit": 2,
        "page": 129,
        "filename": "Unit_2_5.txt",
        "section_title": "Enzymes",
        "page_num_in_file": 7,
        "slide_title": "Enzymes",
        "original_text": "Enzymes\nWithout enzyme: high activation energy barrier\nWith enzyme: reduced activation energy barrier\nReactant -> Products",
        "explanation": "This slide presents a comparative diagram showing the energy changes in a reaction with and without an enzyme. Without an enzyme, the reaction must overcome a high activation energy barrier to convert reactants to products. When an enzyme is present, the activation energy barrier is significantly reduced, allowing the reaction to proceed much faster.",
        "questions": [
            {
                "q": "What change is seen in the activation energy barrier when an enzyme is added to a reaction?",
                "opts": [
                    "The barrier is completely eliminated.",
                    "The barrier is significantly reduced.",
                    "The barrier is raised to prevent reaction.",
                    "The energy of the products is increased."
                ],
                "a": 1,
                "exp": "The presence of an enzyme reduces the activation energy barrier, making it easier for reactants to transition into products."
            }
        ]
    },
    130: {
        "unit": 2,
        "page": 130,
        "filename": "Unit_2_5.txt",
        "section_title": "Enzymes",
        "page_num_in_file": 8,
        "slide_title": "Enzymes",
        "original_text": "Enzymes\nReactants\nProgress of the reaction\nProducts\na, b, c labels on energy curve",
        "explanation": "This slide displays a coordinate graph representing the progress of a chemical reaction. It plots energy on the vertical axis against the progress of the reaction on the horizontal axis, marking key energy states (reactants, transition state/activation energy, and products) with labels a, b, and c.",
        "questions": [
            {
                "q": "What parameters are typically plotted on the axes of an enzyme reaction coordinate graph?",
                "opts": [
                    "Time on the vertical axis, temperature on the horizontal axis.",
                    "Energy on the vertical axis, progress of the reaction on the horizontal axis.",
                    "Solute concentration on the vertical axis, solvent volume on the horizontal axis.",
                    "pH on the vertical axis, enzyme concentration on the horizontal axis."
                ],
                "a": 1,
                "exp": "Reaction coordinate graphs plot energy (potential energy) on the vertical axis versus the progress of the reaction on the horizontal axis."
            }
        ]
    }
}

for page, data in pages_data.items():
    file_path = os.path.join(dest_dir, f"page_{page}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

print("Saved pages 116 to 130 successfully.")
