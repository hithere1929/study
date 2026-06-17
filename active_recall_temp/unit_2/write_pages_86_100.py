import json
import os

dest_dir = r"C:\Users\elieu\OneDrive\Desktop\biofinaltest\active_recall_temp\unit_2"
os.makedirs(dest_dir, exist_ok=True)

pages_data = {
    86: {
        "unit": 2,
        "page": 86,
        "filename": "Unit_2_3.txt",
        "section_title": "Movement of Molecules",
        "page_num_in_file": 12,
        "slide_title": "Osmosis",
        "original_text": "Osmosis\u00a8If a membrane, permeable to water but not to a solute, separates two solutions with different concentrations of solute, water will cross the membrane, moving down its own concentration gradient, until the solute concentration on both sides is equal.",
        "explanation": "Osmosis occurs when a selectively permeable membrane (which allows water to pass through but blocks solute molecules) separates two solutions of unequal solute concentrations. In this scenario, water molecules will cross the membrane, moving down their own concentration gradient (from the side with a lower solute concentration, which has more free water molecules, to the side with a higher solute concentration) until the solute concentration becomes equal on both sides.",
        "questions": [
            {
                "q": "Under what condition will water move across a membrane during osmosis?",
                "opts": [
                    "When the membrane is permeable to the solute but not to water.",
                    "When the membrane is permeable to water but not to the solute, and there is a difference in solute concentration.",
                    "When both solute and water can cross the membrane with equal ease.",
                    "Only when ATP energy is applied to force water across."
                ],
                "a": 1,
                "exp": "Osmosis occurs specifically when a membrane is permeable to water but impermeable to the solute, allowing water to flow down its own concentration gradient to balance the solute concentrations."
            }
        ]
    },
    87: {
        "unit": 2,
        "page": 87,
        "filename": "Unit_2_3.txt",
        "section_title": "Movement of Molecules",
        "page_num_in_file": 13,
        "slide_title": "Tonicity",
        "original_text": "Tonicity\u00a8Tonicityis a term that describes the ability of a surrounding solution to cause a cell to gain or lose water.\u00a8The tonicity of a solution mainly depends on its concentration of solutes relative to the concentration of solutes inside the cell.\u00a4In anisotonicsolution, the concentration of solute is the same on both sides of a membrane, and the cell volume will not change.\u00a4In ahypotonicsolution, the solute concentration is lower outside the cell, water molecules move into the cell, and the cell will expand and may burst.\u00a4In ahypertonicsolution, the solute concentration is higher outside the cell, water molecules move out of the cell, and the cell will shrink.",
        "explanation": "Tonicity is a term describing the capacity of an extracellular solution to cause a cell to gain or lose water. A solution's tonicity depends primarily on its solute concentration relative to the solute concentration inside the cell. In an isotonic solution, solute concentrations are equal on both sides of the membrane, resulting in no net water movement and no change in cell volume. In a hypotonic solution, the solute concentration is lower outside the cell, causing water to flow into the cell, which expands and may burst. In a hypertonic solution, the solute concentration is higher outside the cell, driving water to flow out of the cell, which causes it to shrink.",
        "questions": [
            {
                "q": "What will happen to an animal cell placed in a hypotonic solution?",
                "opts": [
                    "It will shrivel due to water loss.",
                    "It will remain completely unchanged in volume.",
                    "Water will enter the cell, causing it to expand and potentially burst.",
                    "It will actively pump out all of its solutes."
                ],
                "a": 2,
                "exp": "A hypotonic solution has a lower solute concentration than the cell's interior, meaning water moves into the cell down its concentration gradient, causing the cell to expand and potentially lyse (burst)."
            },
            {
                "q": "Which type of solution has a solute concentration equal to that inside the cell, resulting in no net water movement?",
                "opts": ["Hypotonic solution", "Hypertonic solution", "Isotonic solution", "Hydrophobic solution"],
                "a": 2,
                "exp": "An isotonic solution has the same solute concentration on both sides of the membrane, so cell volume does not change."
            }
        ]
    },
    88: {
        "unit": 2,
        "page": 88,
        "filename": "Unit_2_3.txt",
        "section_title": "Movement of Molecules",
        "page_num_in_file": 14,
        "slide_title": "Tonicity",
        "original_text": "Tonicity\nAnimalcell\nPlantcell\nHypotonic solution(lower solute levels)Isotonic solution(equal solute levels)Hypertonic solution(higher solute levels)\nAnimal cell: Lysed, Normal, Shriveled\nPlant cell: Turgid (normal), Flaccid, Shriveled (plasmolyzed)",
        "explanation": "This slide illustrates the structural effects of different tonicities on animal and plant cells. In animal cells, which lack cell walls, a hypotonic solution causes them to become lysed (burst), an isotonic solution keeps them normal, and a hypertonic solution makes them shriveled. In plant cells, which possess rigid cell walls, a hypotonic solution is the normal state, keeping the cell turgid (firm) due to internal water pressure. An isotonic solution makes the plant cell flaccid (limp), and a hypertonic solution causes it to become shriveled or plasmolyzed (where the plasma membrane pulls away from the cell wall).",
        "questions": [
            {
                "q": "What is the normal, healthy state for a plant cell, and in which type of solution does it occur?",
                "opts": [
                    "Flaccid, occurring in an isotonic solution",
                    "Shriveled, occurring in a hypertonic solution",
                    "Turgid, occurring in a hypotonic solution",
                    "Lysed, occurring in a hypotonic solution"
                ],
                "a": 2,
                "exp": "A plant cell is normally turgid (firm) when placed in a hypotonic solution, because the rigid cell wall prevents the cell from bursting while internal turgor pressure supports the plant structure."
            },
            {
                "q": "What term describes a plant cell whose plasma membrane has shriveled and pulled away from its cell wall in a hypertonic environment?",
                "opts": ["Lysed", "Flaccid", "Turgid", "Plasmolyzed"],
                "a": 3,
                "exp": "When a plant cell is in a hypertonic solution, it loses water, shrivels, and undergoes plasmolysis (becomes plasmolyzed)."
            }
        ]
    },
    89: {
        "unit": 2,
        "page": 89,
        "filename": "Unit_2_3.txt",
        "section_title": "Movement of Molecules",
        "page_num_in_file": 15,
        "slide_title": "Facilitated Diffusion",
        "original_text": "Facilitated Diffusion\u00a8Hydrophobic substances easily diffuse across a cell membrane.\u00a8However, polar or charged substances do not easily cross cell membranes and, instead, move across membranes with the help of specific transport proteins in a process called facilitated diffusion, which\u00a4does not require energy and\u00a4relies on the concentration gradient.",
        "explanation": "Hydrophobic (nonpolar) substances can easily diffuse directly across the cell membrane's lipid bilayer. However, polar or charged substances cannot pass through the hydrophobic core easily. Instead, they cross membranes with the assistance of specific membrane-bound transport proteins. This process is called facilitated diffusion. Because it is a form of passive transport, it does not require energy expenditure by the cell and relies entirely on the existing concentration gradient, moving substances down their gradient.",
        "questions": [
            {
                "q": "How does facilitated diffusion differ from simple diffusion?",
                "opts": [
                    "It requires ATP energy to move molecules.",
                    "It moves molecules against their concentration gradient.",
                    "It requires the assistance of specific membrane transport proteins.",
                    "It only allows hydrophobic molecules to pass."
                ],
                "a": 2,
                "exp": "Facilitated diffusion is passive and moves solutes down their gradient like simple diffusion, but it requires specific transport proteins to help polar or charged molecules cross the membrane."
            },
            {
                "q": "Does facilitated diffusion require energy expenditure from the cell?",
                "opts": [
                    "Yes, it requires ATP to change the shape of transport proteins.",
                    "No, it is a passive process that relies on the concentration gradient.",
                    "Yes, but only for moving hydrophobic substances.",
                    "No, but it only occurs when the cell is dead."
                ],
                "a": 1,
                "exp": "Facilitated diffusion requires no energy input because it is a passive transport mechanism driving molecules down their concentration gradient."
            }
        ]
    },
    90: {
        "unit": 2,
        "page": 90,
        "filename": "Unit_2_3.txt",
        "section_title": "Movement of Molecules",
        "page_num_in_file": 16,
        "slide_title": "Facilitated Diffusion",
        "original_text": "Facilitated Diffusion\u00a8Some proteins function by becoming a hydrophilic tunnel for passage of ions or other molecules.\u00a8Other proteins bind their passenger, change shape, and release their passenger on the other side.\u00a8In both cases, the transport protein helps a specific substance diffuse across the membrane down its concentration gradient and thus requires no input of energy.\nAquaporin is specific type of protein identified in the rapid diffusion of water into or out of a cell",
        "explanation": "During facilitated diffusion, transport proteins assist solutes across the membrane using two main mechanisms: some proteins act as hydrophilic tunnels (channels) that allow ions or specific polar molecules to pass through, while other proteins (carriers) physically bind their target molecule, undergo a structural shape change, and release the molecule on the opposite side. In both instances, the protein simply helps the substance diffuse down its concentration gradient, requiring no cellular energy. A key example is aquaporin, a specialized channel protein that facilitates the rapid diffusion of water molecules into or out of cells.",
        "questions": [
            {
                "q": "What is the function of an aquaporin protein?",
                "opts": [
                    "To pump sodium ions out of the cell.",
                    "To act as a receptor for hormones.",
                    "To facilitate the rapid diffusion of water across the cell membrane.",
                    "To anchor adjacent cells in a tissue."
                ],
                "a": 2,
                "exp": "Aquaporins are specialized channel proteins that allow water molecules to cross the hydrophobic membrane rapidly by facilitated diffusion."
            },
            {
                "q": "What are the two ways transport proteins facilitate passive diffusion?",
                "opts": [
                    "By releasing water and using ATP",
                    "By forming a hydrophilic tunnel, or by binding the molecule and changing shape to release it on the other side",
                    "By dissolving the lipid bilayer and pumping ions",
                    "By binding to DNA and activating transcription"
                ],
                "a": 1,
                "exp": "Transport proteins can act as channel proteins (hydrophilic tunnels) or carrier proteins (which bind the solute, change shape, and release it)."
            }
        ]
    },
    91: {
        "unit": 2,
        "page": 91,
        "filename": "Unit_2_3.txt",
        "section_title": "Movement of Molecules",
        "page_num_in_file": 17,
        "slide_title": "Active Transport",
        "original_text": "Active Transport\u00a8In active transport, a cell must expend energy to move a solute againstits concentration gradient.\u00a8The energy molecule ATP supplies the energy for most active transport.\u00a4Proteins involved in active transport often called pumps\u00a4Sodium-Potassium Pumpmost famous in a cell",
        "explanation": "In active transport, a cell must expend energy to move a solute against (or up) its concentration gradient, moving it from an area of lower concentration to an area of higher concentration. The cell's primary energy carrier, ATP, provides the energy required for this process. Membrane proteins that perform active transport are commonly referred to as pumps, with the Sodium-Potassium Pump being the most famous active transport pump in animal cells.",
        "questions": [
            {
                "q": "What defines active transport?",
                "opts": [
                    "The movement of solutes down their concentration gradient using channel proteins.",
                    "The passive diffusion of water across a semipermeable membrane.",
                    "The movement of a solute against its concentration gradient, requiring the expenditure of cellular energy (ATP).",
                    "The random movement of small, nonpolar gas molecules."
                ],
                "a": 2,
                "exp": "Active transport is characterized by moving solutes against their concentration gradient, which requires the cell to expend energy, usually in the form of ATP."
            },
            {
                "q": "What is the most famous active transport pump found in cells?",
                "opts": [
                    "Aquaporin pump",
                    "Calcium pump",
                    "Sodium-Potassium pump",
                    "Proton/sucrose pump"
                ],
                "a": 2,
                "exp": "The Sodium-Potassium Pump is the most famous active transport pump in cells."
            }
        ]
    },
    92: {
        "unit": 2,
        "page": 92,
        "filename": "Unit_2_3.txt",
        "section_title": "Movement of Molecules",
        "page_num_in_file": 18,
        "slide_title": "Bulk Transport of Molecules",
        "original_text": "Bulk Transport of Molecules\u00a8A cell uses two mechanisms to move large molecules across membranes.1.Exocytosisis used to export bulky molecules, such as proteins or polysaccharides.2.Endocytosisis used to take in large molecules.\u00a8In both cases, material to be transported is packaged within a vesicle that fuses with the membrane.",
        "explanation": "Cells employ two primary bulk transport mechanisms to move large, bulky molecules across their membranes. Exocytosis is the process used to export large molecules, such as proteins or polysaccharides, out of the cell. Endocytosis is the process used to bring large molecules into the cell. In both bulk transport mechanisms, the substances are packaged inside a membrane-bound vesicle that fuses with the cell's plasma membrane to complete the transport.",
        "questions": [
            {
                "q": "Which bulk transport mechanism is used by a cell to export bulky molecules like proteins and polysaccharides?",
                "opts": ["Endocytosis", "Phagocytosis", "Exocytosis", "Facilitated diffusion"],
                "a": 2,
                "exp": "Exocytosis is the cellular process of exporting bulky materials by enclosing them in a vesicle that fuses with the plasma membrane to release the contents outside."
            },
            {
                "q": "What structure packages the materials during bulk transport?",
                "opts": ["An aquaporin tunnel", "A membrane-bound vesicle", "A carbohydrate chain", "A fused steroid ring"],
                "a": 1,
                "exp": "In both endocytosis and exocytosis, materials are packaged within a membrane-bound vesicle that fuses with the cell membrane."
            }
        ]
    },
    93: {
        "unit": 2,
        "page": 93,
        "filename": "Unit_2_3.txt",
        "section_title": "Movement of Molecules",
        "page_num_in_file": 19,
        "slide_title": "Exocytosis",
        "original_text": "Exocytosis\u00a8Intracellular vesicle fuses with plasma membrane and secretion of molecule occurs\u00a4Used for export of items such as:\nnHormones\nnNeurotransmitters\nnDigestive enzymes\u00a4Often produced by Golgi body in the cell\u00a4Vesicle becomes part of plasma membrane upon fusing",
        "explanation": "During exocytosis, an intracellular vesicle moves to and fuses with the plasma membrane, resulting in the secretion of its molecular contents into the extracellular space. This pathway is commonly used to export molecules like hormones, neurotransmitters, and digestive enzymes. These vesicles are often manufactured by the Golgi body within the cell. An important anatomical consequence of exocytosis is that the vesicle membrane becomes integrated into, and thus becomes part of, the cell's plasma membrane upon fusing.",
        "questions": [
            {
                "q": "Which cellular organelle is often responsible for producing the vesicles used in exocytosis?",
                "opts": ["The nucleus", "The Golgi body", "The mitochondrion", "The ribosome"],
                "a": 1,
                "exp": "Vesicles destined for exocytosis are commonly produced and packaged by the Golgi body."
            },
            {
                "q": "What happens to the membrane of a vesicle after it undergoes exocytosis?",
                "opts": [
                    "It is destroyed by digestive enzymes.",
                    "It is released into the extracellular fluid.",
                    "It becomes part of the plasma membrane.",
                    "It returns to the nucleus to be recycled."
                ],
                "a": 2,
                "exp": "When a vesicle fuses with the plasma membrane during exocytosis, its lipid bilayer is incorporated directly into the plasma membrane."
            }
        ]
    },
    94: {
        "unit": 2,
        "page": 94,
        "filename": "Unit_2_3.txt",
        "section_title": "Movement of Molecules",
        "page_num_in_file": 20,
        "slide_title": "Endocytosis",
        "original_text": "Endocytosis\u00a8There are two kinds of endocytosis.1.Phagocytosisis the engulfment of a particle by the cell wrapping cell membrane around it, forming a vacuole.1.Pinocytosiswhen engulfment of a liquid2.Receptor-mediated endocytosisuses membrane receptors for specific solutes. The region of the membrane with receptors pinches inward to form a vesicle.nReceptor-mediated endocytosis is used to take in cholesterol from the blood.",
        "explanation": "Endocytosis is the process of bringing materials into the cell and can be categorized into three forms. Phagocytosis ('cellular eating') involves the engulfment of solid particles by wrapping the cell membrane around the particle, pinching off to form an intracellular vacuole. Pinocytosis ('cellular drinking') is the engulfment of extracellular liquid. Receptor-mediated endocytosis is a highly selective process that utilizes specific membrane receptor proteins to bind target solutes; once bound, the receptor-containing region of the membrane pinches inward to form a vesicle. A key biological example of receptor-mediated endocytosis is the uptake of cholesterol from the bloodstream.",
        "questions": [
            {
                "q": "Which form of endocytosis involves the engulfment of liquid substances?",
                "opts": ["Phagocytosis", "Pinocytosis", "Receptor-mediated endocytosis", "Exocytosis"],
                "a": 1,
                "exp": "Pinocytosis is the cellular engulfment of extracellular fluid (liquid)."
            },
            {
                "q": "Which mechanism does the body use to selectively take in cholesterol from the blood?",
                "opts": ["Simple diffusion", "Phagocytosis", "Receptor-mediated endocytosis", "Osmosis"],
                "a": 2,
                "exp": "Receptor-mediated endocytosis uses specific cell surface receptors to bind cholesterol molecules and bring them into the cell selectively."
            }
        ]
    },
    95: {
        "unit": 2,
        "page": 95,
        "filename": "Unit_2_3.txt",
        "section_title": "Movement of Molecules",
        "page_num_in_file": 21,
        "slide_title": "Endocytosis",
        "original_text": "Endocytosis\nPinocytosis\nPhagocytosis",
        "explanation": "This slide serves as a visual layout showing diagrams of the processes of pinocytosis (liquid engulfment) and phagocytosis (solid particle engulfment).",
        "questions": [
            {
                "q": "Which two processes are visually compared on this slide?",
                "opts": [
                    "Exocytosis and Endocytosis",
                    "Pinocytosis and Phagocytosis",
                    "Active Transport and Osmosis",
                    "Hydrolysis and Condensation"
                ],
                "a": 1,
                "exp": "The slide illustrates Pinocytosis and Phagocytosis."
            }
        ]
    },
    96: {
        "unit": 2,
        "page": 96,
        "filename": "Unit_2_3.txt",
        "section_title": "Movement of Molecules",
        "page_num_in_file": 22,
        "slide_title": "Endocytosis",
        "original_text": "Endocytosis\nReceptor-mediated Endocytosis",
        "explanation": "This slide displays a diagram illustrating receptor-mediated endocytosis, demonstrating how extracellular solutes bind to specific receptors on the cell membrane before the membrane invaginates to form a vesicle.",
        "questions": [
            {
                "q": "What specific form of bulk transport is illustrated on this page?",
                "opts": ["Phagocytosis", "Pinocytosis", "Receptor-mediated Endocytosis", "Exocytosis"],
                "a": 2,
                "exp": "The slide is titled 'Receptor-mediated Endocytosis'."
            }
        ]
    },
    97: {
        "unit": 2,
        "page": 97,
        "filename": "Unit_2_3.txt",
        "section_title": "Movement of Molecules",
        "page_num_in_file": 23,
        "slide_title": "To Review",
        "original_text": "To Review\nPassive transport(requires no energy) vs Active transport(requires energy)\nPassive: Diffusion, Facilitated diffusion (moves solute from high to low), Osmosis (moves water from high to low free water concentration)\nActive: Moves solute from low to high solute concentration using ATP",
        "explanation": "This review slide summarizes membrane transport: passive transport requires no energy and includes simple diffusion, facilitated diffusion (both moving solutes down their concentration gradients), and osmosis (moving water down its concentration gradient, from high to low free water concentration). In contrast, active transport requires energy in the form of ATP to pump solutes against their concentration gradient, from an area of lower concentration to an area of higher concentration.",
        "questions": [
            {
                "q": "Which of the following statements correctly summarizes active transport?",
                "opts": [
                    "It moves water from low to high concentration without energy.",
                    "It moves solutes from high to low concentration using ATP.",
                    "It moves solutes from lower to higher concentration (against their gradient) and requires energy (ATP).",
                    "It is a random process that only occurs in dead cells."
                ],
                "a": 2,
                "exp": "Active transport is characterized by using ATP energy to move solutes from a lower concentration to a higher concentration."
            }
        ]
    },
    98: {
        "unit": 2,
        "page": 98,
        "filename": "Unit_2_4.txt",
        "section_title": "Metabolism",
        "page_num_in_file": 1,
        "slide_title": "UNIT 2: METABOLISM & ENERGYBiology 9              Mr. Queenan",
        "explanation": "This is the title slide introducing the section on Metabolism & Energy for Biology 9 with Mr. Queenan.",
        "questions": [
            {
                "q": "What is the topic of the new section introduced on this slide?",
                "opts": ["Genetics", "Metabolism & Energy", "Cell Division", "Ecology"],
                "a": 1,
                "exp": "The slide title explicitly states 'UNIT 2: METABOLISM & ENERGY'."
            }
        ]
    },
    99: {
        "unit": 2,
        "page": 99,
        "filename": "Unit_2_4.txt",
        "section_title": "Metabolism",
        "page_num_in_file": 2,
        "slide_title": "Question",
        "original_text": "Question\u00a8Why do we produce heat when it is hot (85°F) outside, even though our body temperature is 98.6°F?\u00a8Our bodies are always producing heat. \u00a8At these higher temperatures, we are producing more heat than we need to maintain a core body temperature 98.6°F. \u00a8Thus, we sweat and behave in ways that help release our extra heat generated in cellular respiration.",
        "explanation": "Our bodies generate heat continuously as a byproduct of metabolic processes like cellular respiration. Because of this constant production, when the environmental temperature is high (such as 85°F), our bodies generate more heat than is necessary to maintain our internal core body temperature of 98.6°F. To prevent overheating, we engage in physiological and behavioral mechanisms, such as sweating, to release this excess metabolic heat.",
        "questions": [
            {
                "q": "Why do our bodies produce heat even when the external temperature is hot?",
                "opts": [
                    "Our bodies absorb heat directly from the air to speed up reactions.",
                    "Heat is a constant byproduct of cellular respiration and other metabolic activities.",
                    "We stop sweating when it is hot outside.",
                    "To match our temperature with the environment."
                ],
                "a": 1,
                "exp": "Our bodies are always producing heat because cellular respiration and other metabolic processes constantly generate heat as a byproduct."
            }
        ]
    },
    100: {
        "unit": 2,
        "page": 100,
        "filename": "Unit_2_4.txt",
        "section_title": "Metabolism",
        "page_num_in_file": 3,
        "slide_title": "Energy",
        "original_text": "Energy\u00a8Cells transform energy as they perform work\u00a4Cells are miniature chemical factories, housing thousands of chemical reactions.\u00a4Some of these chemical reactions release energy, and others require energy.",
        "explanation": "Cells act as miniature chemical factories, carrying out thousands of chemical reactions to perform cellular work. In doing so, cells continuously transform energy from one form to another. Depending on the reaction, some of these chemical pathways release energy, while others require an input of energy to proceed.",
        "questions": [
            {
                "q": "How do cells perform work at the chemical level?",
                "opts": [
                    "By creating energy from nothing.",
                    "By transforming energy through thousands of chemical reactions, some of which release energy while others require it.",
                    "By remaining completely static and in equilibrium.",
                    "By converting all organic matter into inorganic salts."
                ],
                "a": 1,
                "exp": "Cells are like chemical factories that perform work by housing thousands of chemical reactions, transforming energy as some reactions release energy and others consume it."
            }
        ]
    }
}

for page, data in pages_data.items():
    file_path = os.path.join(dest_dir, f"page_{page}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

print("Saved pages 86 to 100 successfully.")
