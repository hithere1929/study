import json
import os

dest_dir = r"C:\Users\elieu\OneDrive\Desktop\biofinaltest\active_recall_temp\unit_2"
os.makedirs(dest_dir, exist_ok=True)

pages_data = {
    71: {
        "unit": 2,
        "page": 71,
        "filename": "Unit_2_2.txt",
        "section_title": "Chemistry of Organic Molecules",
        "page_num_in_file": 35,
        "slide_title": "Nucleic Acids",
        "original_text": "Nucleic Acids\u00a8DNA nitrogenous bases are\u00a4adenine (A),\u00a4thymine (T),\u00a4cytosine (C), and\u00a4guanine (G).\u00a8RNA also has A, C, and G, but instead of T, it has uracil (U).\u00a8RNA is usually a single polynucleotide strand.\u00a8DNA is a doublehelix, in which two polynucleotide strands wrap around each other.\u00a4The two strands are associated because particular bases always hydrogen-bond to one another.\u00a4A pairs with T, and C pairs with G, producing base pairs.",
        "explanation": "Nucleic acids exhibit differences in their nitrogenous bases and strandedness. In DNA, the nitrogenous bases are adenine (A), thymine (T), cytosine (C), and guanine (G). RNA contains the same bases except that thymine is replaced by uracil (U). Structurally, RNA is typically a single polynucleotide strand, whereas DNA is a double helix consisting of two polynucleotide strands wrapped around each other. These two DNA strands associate because their nitrogenous bases hydrogen-bond specifically to each other: adenine (A) always pairs with thymine (T), and cytosine (C) always pairs with guanine (G), creating base pairs.",
        "questions": [
            {
                "q": "Which nitrogenous base is unique to RNA and replaces thymine (T) in DNA?",
                "opts": ["Adenine", "Cytosine", "Uracil", "Guanine"],
                "a": 2,
                "exp": "RNA contains uracil (U) instead of thymine (T), which is found in DNA."
            },
            {
                "q": "How do the two strands of DNA associate to form a double helix?",
                "opts": [
                    "They form ionic bonds between phosphate groups.",
                    "They form covalent glycosidic bonds.",
                    "Specific nitrogenous bases hydrogen-bond to one another (A with T, and C with G).",
                    "They are linked together by peptide bonds."
                ],
                "a": 2,
                "exp": "The double helix is held together by hydrogen bonds between complementary base pairs: adenine pairs with thymine, and cytosine pairs with guanine."
            }
        ]
    },
    72: {
        "unit": 2,
        "page": 72,
        "filename": "Unit_2_2.txt",
        "section_title": "Chemistry of Organic Molecules",
        "page_num_in_file": 36,
        "slide_title": "4: Nucleic Acids",
        "original_text": "4: Nucleic Acids",
        "explanation": "This slide serves as a header placeholder for nucleic acids.",
        "questions": [
            {
                "q": "What category of organic molecules is featured on this placeholder slide?",
                "opts": ["Proteins", "Carbohydrates", "Lipids", "Nucleic Acids"],
                "a": 3,
                "exp": "The slide is titled '4: Nucleic Acids'."
            }
        ]
    },
    73: {
        "unit": 2,
        "page": 73,
        "filename": "Unit_2_2.txt",
        "section_title": "Chemistry of Organic Molecules",
        "page_num_in_file": 37,
        "slide_title": "4: ATP",
        "original_text": "4: ATP\nAdenosine Triphosphate is a special type of nucleotide, and as discussed already, is a high energy molecule, that powers many cellular processes.",
        "explanation": "Adenosine Triphosphate (ATP) is a specialized type of nucleotide. It serves as a high-energy molecule that fuels many cellular processes in living organisms.",
        "questions": [
            {
                "q": "ATP is a specialized version of which monomer class?",
                "opts": ["Amino acid", "Monosaccharide", "Nucleotide", "Fatty acid"],
                "a": 2,
                "exp": "As stated on the slide, Adenosine Triphosphate (ATP) is a special type of nucleotide."
            }
        ]
    },
    74: {
        "unit": 2,
        "page": 74,
        "filename": "Unit_2_2.txt",
        "section_title": "Chemistry of Organic Molecules",
        "page_num_in_file": 38,
        "slide_title": "Exit Ticket",
        "original_text": "Exit Ticket\u00a8Please go on to Google Classroom and fill out the exit ticket posted for Unit 2. \u00a8For this exit ticket, consider both presentations for Unit 2 to date:\u00a5Name 3 interesting things you learned so far in Unit 2\u00a5Name 2 things you want to learn more about in class or on your own\u00a5Ask one question about a topic that you feel needs more explanation",
        "explanation": "This slide details a classroom exit ticket assignment on Google Classroom. Students are prompted to identify three interesting facts they learned in Unit 2, two topics they want to explore further, and one question about a concept requiring further explanation.",
        "questions": [
            {
                "q": "What is the purpose of the Exit Ticket described on this slide?",
                "opts": [
                    "To take a formal Unit 2 exam.",
                    "To submit a biology lab report.",
                    "To reflect on Unit 2 learning by naming 3 interesting things, 2 topics to explore, and 1 question.",
                    "To draw the chemical structures of ATP and DNA."
                ],
                "a": 2,
                "exp": "The Exit Ticket asks students to consider the Unit 2 presentations and identify 3 interesting things, 2 things to learn more about, and 1 question."
            }
        ]
    },
    75: {
        "unit": 2,
        "page": 75,
        "filename": "Unit_2_3.txt",
        "section_title": "Movement of Molecules",
        "page_num_in_file": 1,
        "slide_title": "UNIT 2: MOVEMENT OF MOLECULESBiology 9              Mr. QueenanText -Ch 8.3 (p 260-273)",
        "explanation": "This is the title slide for Unit 2: Movement of Molecules for Biology 9 with Mr. Queenan, which covers Textbook Chapter 8.3 on pages 260-273.",
        "questions": [
            {
                "q": "Which chapter and page range of the textbook correspond to the Movement of Molecules section?",
                "opts": [
                    "Chapter 2.3 (p 52-56)",
                    "Chapter 8.3 (p 260-273)",
                    "Chapter 9.1 (p 280-290)",
                    "Chapter 10.2 (p 300-315)"
                ],
                "a": 1,
                "exp": "The slide title explicitly references 'Text -Ch 8.3 (p 260-273)'."
            }
        ]
    },
    76: {
        "unit": 2,
        "page": 76,
        "filename": "Unit_2_3.txt",
        "section_title": "Movement of Molecules",
        "page_num_in_file": 2,
        "slide_title": "Membrane Structure & Function",
        "original_text": "Membrane Structure & Function\u00a8Phospholipids, the key ingredient of biological membranes, spontaneously self-assemble into simple membranes\u00a4The formation of membrane-enclosed collections of molecules was a critical step in the evolution of the first cells.",
        "explanation": "Phospholipids are the key component of biological membranes, and they spontaneously self-assemble into simple membrane structures in water. The evolutionary formation of membrane-enclosed collections of molecules was a critical, fundamental step in the development of the very first living cells.",
        "questions": [
            {
                "q": "What characteristic behavior of phospholipids was crucial for the evolution of the first cells?",
                "opts": [
                    "They dissolve in water to form acids.",
                    "They spontaneously self-assemble into simple membranes.",
                    "They act as enzymatic catalysts for protein synthesis.",
                    "They replicate themselves using genetic codes."
                ],
                "a": 1,
                "exp": "Phospholipids spontaneously self-assemble into simple membrane structures, which enclosed collections of molecules to form the first cell-like structures."
            }
        ]
    },
    77: {
        "unit": 2,
        "page": 77,
        "filename": "Unit_2_3.txt",
        "section_title": "Movement of Molecules",
        "page_num_in_file": 3,
        "slide_title": "Membrane Structure & Function",
        "original_text": "Membrane Structure & Function\u00a8There are other molecules that are embedded in the phospholipid bilayer, and are relatively uniform across most animal cell membranes\u00a4Cholesterol and other lipid molecules\u00a4Glycoproteins and glycolipids\u00a4Proteins\u00a8These play a part in the fluidity of the membrane, and both the passive and active permeability of the membrane. \u00a8Fluid MozaicModel",
        "explanation": "In addition to phospholipids, cell membranes contain other embedded molecules that are distributed relatively uniformly across most animal cell membranes. These molecules include cholesterol and other lipid molecules, glycoproteins, glycolipids, and proteins. These components regulate the fluidity of the membrane and control both passive and active permeability, allowing selective transport. This structural organization is described by the Fluid Mosaic Model.",
        "questions": [
            {
                "q": "Which model is used to describe the structure of the cell membrane containing embedded proteins, lipids, and carbohydrates?",
                "opts": ["Lock and Key Model", "Fluid Mosaic Model", "Crystalline Lattice Model", "Osmotic Permeability Model"],
                "a": 1,
                "exp": "The cell membrane structure and its embedded molecules are described by the Fluid Mosaic Model (spelled 'Fluid Mozaic Model' on the slide)."
            },
            {
                "q": "What are the roles of embedded molecules like cholesterol, proteins, and glycoproteins in the cell membrane?",
                "opts": [
                    "They serve as genetic code templates.",
                    "They regulate membrane fluidity and control passive and active permeability.",
                    "They break down glucose for immediate ATP release.",
                    "They synthesize new phospholipids from amino acids."
                ],
                "a": 1,
                "exp": "Embedded molecules are responsible for maintaining membrane fluidity and managing passive and active permeability."
            }
        ]
    },
    78: {
        "unit": 2,
        "page": 78,
        "filename": "Unit_2_3.txt",
        "section_title": "Movement of Molecules",
        "page_num_in_file": 4,
        "slide_title": "Membrane Bound Lipids",
        "original_text": "Membrane Bound Lipids\u00a8Cholesterol and phospholipids\u00a4Help create membrane fluidity\u00a4Stop membrane from becoming too fluid at high temps; too rigid at cold temps\u00a8Individual molecules can flip from extracellular monolayer to intracellular monolayer.",
        "explanation": "Membrane-bound lipids, specifically cholesterol and phospholipids, play a key role in maintaining membrane stability. They help create membrane fluidity and act as temperature buffers, preventing the membrane from becoming too fluid at high temperatures and preventing it from becoming too rigid at cold temperatures. Additionally, individual lipid molecules are capable of flipping from the extracellular monolayer to the intracellular monolayer of the bilayer.",
        "questions": [
            {
                "q": "How do cholesterol and phospholipids stabilize cell membranes at extreme temperatures?",
                "opts": [
                    "They cause the membrane to dissolve at high temperatures.",
                    "They prevent the membrane from becoming too fluid at high temperatures and too rigid at cold temperatures.",
                    "They form covalent bonds to lock the membrane in a solid state.",
                    "They pump heat out of the cell."
                ],
                "a": 1,
                "exp": "These lipids regulate fluidity, buffering against temperature changes so the membrane doesn't get too fluid when hot or too rigid when cold."
            }
        ]
    },
    79: {
        "unit": 2,
        "page": 79,
        "filename": "Unit_2_3.txt",
        "section_title": "Movement of Molecules",
        "page_num_in_file": 5,
        "slide_title": "Membrane Bound Carbohydrates",
        "original_text": "Membrane Bound Carbohydrates\u00a8Glycoproteins and glycolipids\u00a4Phospholipids or proteins that have a sugar chain attached\u00a4Carbohydrate chains only occur on the outside surface of cell, making cell membrane “asymmetrical”\u00a4Main purpose of these molecules:\nnCell-to-cell adhesion\nnReception off signaling molecules\nnCell-to-cell signaling\u00a4Diversity of carbohydrate chains leads to cellular “fingerprints\"",
        "explanation": "Membrane-bound carbohydrates exist as glycoproteins (proteins with an attached sugar chain) and glycolipids (phospholipids with an attached sugar chain). These carbohydrate chains are located exclusively on the outer surface of the cell, which makes the cell membrane structurally asymmetrical. The primary functions of glycolipids and glycoproteins are to mediate cell-to-cell adhesion, serve in the reception of signaling molecules, and facilitate cell-to-cell signaling. The high diversity of these carbohydrate chains creates unique cellular 'fingerprints' that help identify cell types.",
        "questions": [
            {
                "q": "Why is the cell membrane considered 'asymmetrical' regarding its carbohydrate chains?",
                "opts": [
                    "Carbohydrates are only found on the inside surface of the cell membrane.",
                    "Carbohydrates only occur on the outside surface of the cell membrane.",
                    "The chains are of different lengths on each side.",
                    "Carbohydrates are only attached to proteins, never lipids."
                ],
                "a": 1,
                "exp": "Carbohydrate chains only occur on the outside surface of the cell, resulting in an asymmetrical membrane structure."
            },
            {
                "q": "What are the primary functions of glycoproteins and glycolipids?",
                "opts": [
                    "To act as enzymes and synthesize ATP.",
                    "To serve as genetic templates and replication sites.",
                    "Cell-to-cell adhesion, cell-to-cell signaling, and reception of signaling molecules.",
                    "To store carbon and energy in the cell membrane."
                ],
                "a": 2,
                "exp": "The main functions of membrane carbohydrates are cell adhesion, signaling, and serving as receptors for signal molecules."
            }
        ]
    },
    80: {
        "unit": 2,
        "page": 80,
        "filename": "Unit_2_3.txt",
        "section_title": "Movement of Molecules",
        "page_num_in_file": 6,
        "slide_title": "Membrane Bound Proteins",
        "original_text": "Membrane Bound Proteins\u00a8The proteins found in a membrane can differ depending on type of cell, or tissue system. \u00a86 main types of proteins, each with its own function\u00a4Channel Protein –allows passage of molecules or ions\u00a4Carrier Protein –selectively interacts w/ specific molecule\u00a4Cell Recognition Protein (MHC) –immunity/organ transplant\u00a4Receptor Protein –shaped so a molecule can bind to it\u00a4Enzymatic Protein –catalyzes a specific reaction\u00a4Junction Protein –joins cells to allow a tissue to function",
        "explanation": "The specific proteins found within a cell membrane differ depending on the cell type or tissue system. There are six major types of membrane-bound proteins, each performing a distinct function: channel proteins, which allow molecules or ions to pass through; carrier proteins, which selectively interact with specific molecules to transport them; cell recognition proteins (such as MHC), which identify cells and are crucial for immunity and organ transplant compatibility; receptor proteins, which possess a specific shape that allows signaling molecules to bind to them; enzymatic proteins, which catalyze specific metabolic reactions; and junction proteins, which join adjacent cells together to allow tissues to function cooperatively.",
        "questions": [
            {
                "q": "Which type of membrane protein is shaped specifically to bind to a signaling molecule?",
                "opts": ["Channel Protein", "Carrier Protein", "Receptor Protein", "Junction Protein"],
                "a": 2,
                "exp": "Receptor proteins are structurally shaped so that a specific signaling molecule can bind to them."
            },
            {
                "q": "What is the primary function of a Junction Protein?",
                "opts": [
                    "To selectively transport large glucose molecules.",
                    "To catalyze chemical reactions on the membrane surface.",
                    "To join cells together, allowing a tissue to function.",
                    "To serve as a cellular recognition marker for immunity."
                ],
                "a": 2,
                "exp": "Junction proteins connect adjacent cells to coordinate tissue-level function."
            }
        ]
    },
    81: {
        "unit": 2,
        "page": 81,
        "filename": "Unit_2_3.txt",
        "section_title": "Movement of Molecules",
        "page_num_in_file": 7,
        "slide_title": "EnzymeEnzyme",
        "original_text": "EnzymeEnzyme\nO2 CO2Diffusion of smallnonpolar molecules\nAttachmentproteinReceptorproteinChannelprotein\nCarrier/ ActivetransportproteinATP\nJunctionprotein\nMHC Protein\nJunctionprotein",
        "explanation": "This slide provides a visual diagram mapping the locations and configurations of the various types of membrane proteins, including enzyme proteins, attachment proteins, receptor proteins, channel proteins, carrier/active transport proteins (which utilize ATP), junction proteins, and MHC (major histocompatibility complex) recognition proteins. It also shows the passive diffusion of small, nonpolar molecules like O2 and CO2 directly through the phospholipid bilayer.",
        "questions": [
            {
                "q": "Which small, nonpolar molecules are illustrated diffusing directly through the phospholipid bilayer on this slide?",
                "opts": ["Glucose and Amino acids", "O2 and CO2", "Na+ and Cl-", "ATP and Enzymes"],
                "a": 1,
                "exp": "Small, nonpolar molecules like oxygen (O2) and carbon dioxide (CO2) can diffuse directly through the lipid bilayer."
            }
        ]
    },
    82: {
        "unit": 2,
        "page": 82,
        "filename": "Unit_2_3.txt",
        "section_title": "Movement of Molecules",
        "page_num_in_file": 8,
        "slide_title": "Membrane Permeability",
        "original_text": "Membrane Permeability\u00a8Plasma membrane of cells is selectively permeable\u00a4Allows in some substances while keeping other out.nSome molecules can freely move across the membrane without needing to expend any energynHydrophobic molecules are similar to inside of the bilayer, and can move across at no energy costnPolar molecules require energy input to move acrossmembrane",
        "explanation": "The plasma membrane is selectively permeable, meaning it allows certain substances to cross while blocking others. Some molecules cross the membrane freely without requiring cellular energy. Hydrophobic (nonpolar) molecules, being chemically similar to the interior of the lipid bilayer, can dissolve in and cross the bilayer at no energy cost. Conversely, polar or charged molecules cannot cross the hydrophobic core easily and require energy input (or transport proteins) to cross the membrane.",
        "questions": [
            {
                "q": "What does 'selective permeability' mean?",
                "opts": [
                    "All molecules can cross the membrane freely.",
                    "No molecules are allowed to cross the membrane.",
                    "Only water is allowed to cross.",
                    "The membrane allows some substances to pass while keeping others out."
                ],
                "a": 3,
                "exp": "Selective permeability is the property of a membrane that allows some substances to pass through while preventing others from doing so."
            },
            {
                "q": "Why can hydrophobic molecules cross the cell membrane at no energy cost?",
                "opts": [
                    "They are actively pumped by channel proteins.",
                    "They are chemically similar to the hydrophobic interior of the phospholipid bilayer.",
                    "They are broken down into ATP during transport.",
                    "They bind to carbohydrates on the membrane surface."
                ],
                "a": 1,
                "exp": "Because hydrophobic molecules are nonpolar, they are compatible with the hydrophobic core of the bilayer, allowing them to diffuse across without energy expenditure."
            }
        ]
    },
    83: {
        "unit": 2,
        "page": 83,
        "filename": "Unit_2_3.txt",
        "section_title": "Movement of Molecules",
        "page_num_in_file": 9,
        "slide_title": "Concentration Gradient",
        "original_text": "Concentration Gradient\u00a8Most molecules follow a concentration gradient\u00a4Move from areas of higher concentration to lower until equilibrium is reached\u00a4Ex. Oxygen and Carbon Dioxide in the cell. \nnOxygen is always flowing:\nnInto the cell because oxygen is being used\nnCarbon dioxide is always flowing:\nnOut of the cell because it is building up as a waste product of reactions",
        "explanation": "Most molecules move down a concentration gradient, moving from an area of higher concentration to an area of lower concentration until an equilibrium is established. A key cellular example is the movement of gases: oxygen is constantly consumed by metabolic reactions inside the cell, creating a low internal concentration that drives oxygen to flow into the cell; conversely, carbon dioxide builds up inside the cell as a waste product of chemical reactions, creating a high internal concentration that drives carbon dioxide to flow out of the cell.",
        "questions": [
            {
                "q": "How does a concentration gradient determine the direction of molecular movement?",
                "opts": [
                    "Molecules move from lower to higher concentration.",
                    "Molecules move randomly without any direction.",
                    "Molecules move from areas of higher concentration to areas of lower concentration.",
                    "Molecules are forced to stay in equilibrium and cannot move."
                ],
                "a": 2,
                "exp": "A concentration gradient drives the passive net movement of molecules from areas of high concentration to areas of low concentration."
            },
            {
                "q": "Why does oxygen constantly flow into a cell down its concentration gradient?",
                "opts": [
                    "The cell actively pumps oxygen out.",
                    "Oxygen is constantly being used up inside the cell, keeping its internal concentration low.",
                    "Oxygen is chemically attracted to the polar heads of phospholipids.",
                    "The outside of the cell has no oxygen."
                ],
                "a": 1,
                "exp": "Oxygen flows into the cell because it is continuously consumed by cellular processes, keeping the concentration lower inside than outside."
            }
        ]
    },
    84: {
        "unit": 2,
        "page": 84,
        "filename": "Unit_2_3.txt",
        "section_title": "Movement of Molecules",
        "page_num_in_file": 10,
        "slide_title": "Passive Transport -Diffusion",
        "original_text": "Passive Transport -Diffusion\u00a8Diffusion–Movement of molecules from a higher to lower concentration until equilibrium is achieved and molecules are distributed equally.\n\u00a4Random process\u00a4In cells, only certain moleculescan enter and exit cells by diffusionnGases –small and nonpolar",
        "explanation": "Diffusion is a type of passive transport defined as the movement of molecules from a higher concentration to a lower concentration until equilibrium is achieved and molecules are distributed equally. Diffusion is a random molecular process. In cells, only specific types of molecules can cross the plasma membrane via simple diffusion, primarily small and nonpolar gases like oxygen and carbon dioxide.",
        "questions": [
            {
                "q": "What is diffusion?",
                "opts": [
                    "The movement of molecules from low to high concentration using ATP.",
                    "The movement of molecules from higher to lower concentration until equilibrium is achieved.",
                    "The active pumping of ions across a membrane.",
                    "The self-assembly of phospholipids in water."
                ],
                "a": 1,
                "exp": "Diffusion is the passive, random movement of molecules from high concentration to low concentration until they are equally distributed."
            },
            {
                "q": "Which types of molecules can cross cell membranes by simple diffusion?",
                "opts": [
                    "Large polar proteins",
                    "Charged ions like Na+ and Cl-",
                    "Small, nonpolar gases",
                    "Polysaccharides like starch"
                ],
                "a": 2,
                "exp": "Only small, nonpolar molecules (such as gases like O2 and CO2) can pass directly through the lipid bilayer via simple diffusion."
            }
        ]
    },
    85: {
        "unit": 2,
        "page": 85,
        "filename": "Unit_2_3.txt",
        "section_title": "Movement of Molecules",
        "page_num_in_file": 11,
        "slide_title": "Passive Transport -Osmosis",
        "original_text": "Passive Transport -Osmosis\u00a8Osmosis–The diffusion of water across a semipermeable membrane from high to low concentration\u00a4Water flows from areas of high osmotic pressure to low osmotic pressure\nnThis is the process by which wateris absorbed by the kidneys in the body &\nnTaken up by capillaries in tissues &\nnHow water crosses membranes",
        "explanation": "Osmosis is a specialized form of passive transport defined as the diffusion of water across a semipermeable membrane from an area of higher water concentration to an area of lower water concentration. Water flows from areas of high osmotic pressure to low osmotic pressure. Osmosis is the primary mechanism by which water crosses membranes, is absorbed by the kidneys, and is taken up by capillaries in tissues.",
        "questions": [
            {
                "q": "What is osmosis?",
                "opts": [
                    "The diffusion of solutes across a selectively permeable membrane.",
                    "The movement of water across a semipermeable membrane from high to low water concentration.",
                    "The active transport of water using ATP.",
                    "The movement of gases from high to low pressure."
                ],
                "a": 1,
                "exp": "Osmosis is specifically the passive diffusion of water molecules across a semipermeable membrane from an area of higher water concentration to lower water concentration."
            },
            {
                "q": "Which of the following processes in the human body relies on osmosis?",
                "opts": [
                    "The synthesis of proteins by ribosomes",
                    "The replication of DNA in the nucleus",
                    "The absorption of water by the kidneys and uptake by tissue capillaries",
                    "The electrical conduction of nerve impulses"
                ],
                "a": 2,
                "exp": "Water absorption by the kidneys and capillary uptake in tissues are major physiological processes driven by osmosis."
            }
        ]
    }
}

for page, data in pages_data.items():
    file_path = os.path.join(dest_dir, f"page_{page}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

print("Saved pages 71 to 85 successfully.")
