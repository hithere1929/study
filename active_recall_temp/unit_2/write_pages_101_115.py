import json
import os

dest_dir = r"C:\Users\elieu\OneDrive\Desktop\biofinaltest\active_recall_temp\unit_2"
os.makedirs(dest_dir, exist_ok=True)

pages_data = {
    101: {
        "unit": 2,
        "page": 101,
        "filename": "Unit_2_4.txt",
        "section_title": "Metabolism",
        "page_num_in_file": 4,
        "slide_title": "Energy",
        "original_text": "Energy\u00a8What is energy?\u00a4Energyis the capacity to cause change or to perform work.\nnAllow living things to carry on processes of life, such as growth, development, metabolism, and reproduction\u00a4There are two basic forms of energy.1.Kinetic energyis the energy of motion.2.Potential energyis energy that matter possesses as a result of its location or structure.",
        "explanation": "Energy is defined as the capacity to cause change or to perform work. It is essential for living organisms as it allows them to carry out vital life processes such as growth, development, metabolism, and reproduction. Energy exists in two fundamental forms: kinetic energy, which is the energy associated with motion, and potential energy, which is stored energy that matter possesses as a result of its structural configuration or physical location.",
        "questions": [
            {
                "q": "What is the scientific definition of energy?",
                "opts": [
                    "The mass of an object in motion.",
                    "The capacity to cause change or perform work.",
                    "The force produced by gravity on an object.",
                    "The speed at which chemical bonds are broken."
                ],
                "a": 1,
                "exp": "Energy is defined as the capacity to cause change or to perform work, allowing organisms to carry out life processes."
            },
            {
                "q": "What are the two basic forms of energy?",
                "opts": [
                    "Thermal and Chemical energy",
                    "Kinetic and Potential energy",
                    "Electrical and Radiant energy",
                    "Metabolic and Structural energy"
                ],
                "a": 1,
                "exp": "The two basic forms of energy are kinetic energy (energy of motion) and potential energy (stored energy based on location or structure)."
            }
        ]
    },
    102: {
        "unit": 2,
        "page": 102,
        "filename": "Unit_2_4.txt",
        "section_title": "Metabolism",
        "page_num_in_file": 5,
        "slide_title": "Energy",
        "original_text": "Energy\u00a8Thermal energyis a type of kinetic energy associated with the random movement of atoms or molecules.\u00a8Thermal energy in transfer from one object to another is called heat.\u00a8Light is also a type of kinetic energy; it can be harnessed to power photosynthesis.",
        "explanation": "Thermal energy is a specific type of kinetic energy that arises from the random, constant movement of atoms or molecules within matter. When thermal energy is transferred from one object to another, it is referred to as heat. Light is another form of kinetic energy consisting of electromagnetic radiation, which can be harnessed by photosynthetic organisms to power the synthesis of organic molecules.",
        "questions": [
            {
                "q": "What is thermal energy in transfer from one object to another called?",
                "opts": ["Temperature", "Heat", "Entropy", "Potential energy"],
                "a": 1,
                "exp": "Thermal energy in transit between objects is scientifically referred to as heat."
            },
            {
                "q": "Which type of kinetic energy is harnessed by plants to power photosynthesis?",
                "opts": ["Heat", "Chemical energy", "Light", "Gravitational energy"],
                "a": 2,
                "exp": "Light is a type of kinetic energy that photosynthetic organisms capture to drive the synthesis of sugar."
            }
        ]
    },
    103: {
        "unit": 2,
        "page": 103,
        "filename": "Unit_2_4.txt",
        "section_title": "Metabolism",
        "page_num_in_file": 6,
        "slide_title": "Energy",
        "original_text": "Energy\u00a8Chemical energyis the\u00a4potential energy available for release in a chemical reaction and \u00a4the most important type of energy for living organisms to power the work of the cell.",
        "explanation": "Chemical energy is a form of potential energy that is stored within the chemical bonds of molecules and is available for release during a chemical reaction. It represents the most critical form of energy for living organisms, as cells harvest and utilize chemical energy to power metabolic, mechanical, and transport work.",
        "questions": [
            {
                "q": "What type of energy is chemical energy?",
                "opts": ["Kinetic energy", "Thermal energy", "Potential energy", "Heat energy"],
                "a": 2,
                "exp": "Chemical energy is potential energy stored in chemical bonds, waiting to be released during chemical reactions."
            },
            {
                "q": "Why is chemical energy the most important type of energy for living organisms?",
                "opts": [
                    "It is the only type of energy that cannot be converted.",
                    "It is used by cells to power cellular work.",
                    "It is released instantly as heat to warm the body.",
                    "It flows directly from the sun into cells."
                ],
                "a": 1,
                "exp": "Chemical energy is crucial because cells break chemical bonds in molecules (like glucose and ATP) to release energy that drives cellular work."
            }
        ]
    },
    104: {
        "unit": 2,
        "page": 104,
        "filename": "Unit_2_4.txt",
        "section_title": "Metabolism",
        "page_num_in_file": 7,
        "slide_title": "Energy",
        "original_text": "Energy",
        "explanation": "This slide serves as a transition or title page for the energy subsection.",
        "questions": [
            {
                "q": "What is the topic of this slide?",
                "opts": ["Entropy", "Metabolism", "Energy", "Thermodynamics"],
                "a": 2,
                "exp": "The slide is titled 'Energy'."
            }
        ]
    },
    105: {
        "unit": 2,
        "page": 105,
        "filename": "Unit_2_4.txt",
        "section_title": "Metabolism",
        "page_num_in_file": 8,
        "slide_title": "Thermodynamics",
        "original_text": "Thermodynamics\u00a8Thermodynamicsis the study of energy transformations that occur in a collection of matter.\u00a5The word systemis used for the matter under study.\u00a5The word surroundingsis used for everything outside the system; the rest of the universe.",
        "explanation": "Thermodynamics is the scientific study of energy transformations that occur within a designated collection of matter. In thermodynamic terminology, the term 'system' refers to the specific matter that is being studied or observed, while the term 'surroundings' refers to everything outside of that system, representing the remainder of the universe.",
        "questions": [
            {
                "q": "What is thermodynamics?",
                "opts": [
                    "The study of chemical bonds in organic molecules.",
                    "The study of energy transformations that occur in a collection of matter.",
                    "The study of heat tolerance in animals.",
                    "The study of water movement across membranes."
                ],
                "a": 1,
                "exp": "Thermodynamics is defined as the study of energy transformations within a collection of matter."
            },
            {
                "q": "In thermodynamics, what is the term for the matter under study?",
                "opts": ["Surroundings", "System", "Universe", "Entropy"],
                "a": 1,
                "exp": "The 'system' is the specific matter under study, and the 'surroundings' is everything else."
            }
        ]
    },
    106: {
        "unit": 2,
        "page": 106,
        "filename": "Unit_2_4.txt",
        "section_title": "Metabolism",
        "page_num_in_file": 9,
        "slide_title": "Thermodynamics",
        "original_text": "Thermodynamics\u00a8Two laws govern energy transformations in organisms. \u00a5Per the first law of thermodynamics(also known as the law of energy conservation), energy in the universe is constant.\nnEnergy cannot be created or destroyed, only change form\u00a5Per the second law of thermodynamics, energy conversions increase the disorder of the universe.\u00a8Entropyis the measure of disorder or randomness.",
        "explanation": "Two fundamental laws of thermodynamics govern all energy transformations in living organisms. The first law of thermodynamics, or the law of energy conservation, states that the total energy in the universe is constant: energy can neither be created nor destroyed, but can only be transformed from one form to another. The second law of thermodynamics states that every energy conversion increases the overall disorder of the universe. This disorder or randomness is measured quantitatively as entropy.",
        "questions": [
            {
                "q": "What does the first law of thermodynamics state?",
                "opts": [
                    "Energy conversions always decrease entropy.",
                    "Energy cannot be created or destroyed, only transformed from one form to another.",
                    "The universe is constantly losing energy.",
                    "All chemical reactions must release energy."
                ],
                "a": 1,
                "exp": "The first law (law of energy conservation) states that energy is constant; it cannot be created or destroyed, only converted between forms."
            },
            {
                "q": "What is entropy?",
                "opts": [
                    "A measure of the total potential energy in a cell.",
                    "A measure of disorder or randomness.",
                    "The speed of an enzyme-catalyzed reaction.",
                    "The pressure of water inside a plant cell wall."
                ],
                "a": 1,
                "exp": "Entropy is defined as the measure of disorder or randomness, which increases during energy conversions according to the second law of thermodynamics."
            }
        ]
    },
    107: {
        "unit": 2,
        "page": 107,
        "filename": "Unit_2_4.txt",
        "section_title": "Metabolism",
        "page_num_in_file": 10,
        "slide_title": "Thermodynamics",
        "original_text": "Thermodynamics\u00a8Chemical reactions either\u00a5release energy(exergonic reactions) or\u00a5require an input of energy and store energy (endergonic reactions).",
        "explanation": "From an energetic perspective, chemical reactions are divided into two main categories: exergonic reactions, which release energy, and endergonic reactions, which require an input of energy and store that energy within the chemical bonds of the products.",
        "questions": [
            {
                "q": "How are endergonic and exergonic reactions distinguished?",
                "opts": [
                    "Endergonic reactions release energy, whereas exergonic reactions require energy input.",
                    "Endergonic reactions require energy input and store energy, whereas exergonic reactions release energy.",
                    "Endergonic reactions occur in animal cells, whereas exergonic reactions occur only in plant cells.",
                    "Endergonic reactions are physical changes, whereas exergonic reactions are chemical changes."
                ],
                "a": 1,
                "exp": "Endergonic reactions consume energy to store it in products, while exergonic reactions release energy from reactants."
            }
        ]
    },
    108: {
        "unit": 2,
        "page": 108,
        "filename": "Unit_2_4.txt",
        "section_title": "Metabolism",
        "page_num_in_file": 11,
        "slide_title": "Exergonic Reactions",
        "original_text": "Exergonic Reactions\u00a8Exergonic reactionsrelease energy.\u00a5These reactions release the energy in covalent bonds of the reactants.\u00a5Examples?\u00a5Burning wood releases the energy in glucose as heat and light.\u00a5Cellular respiration\nninvolves many steps,\nnreleases energy slowly, and\nnuses some of the released energy to produce ATP.",
        "explanation": "Exergonic reactions are chemical reactions that release energy by breaking down reactant molecules and releasing the chemical energy stored in their covalent bonds. An everyday example of an exergonic reaction is burning wood, which releases the chemical energy stored in glucose covalent bonds as thermal energy (heat) and light. A biological example is cellular respiration, a multi-step pathway that breaks down glucose slowly, harvesting the released energy to synthesize ATP.",
        "questions": [
            {
                "q": "What is the source of the energy released during an exergonic reaction?",
                "opts": [
                    "The destruction of the atoms' nuclei.",
                    "The covalent bonds of the reactant molecules.",
                    "Thermal energy absorbed from the surroundings.",
                    "The kinetic movement of the water solvent."
                ],
                "a": 1,
                "exp": "Exergonic reactions release the potential chemical energy stored within the covalent bonds of the reactants."
            },
            {
                "q": "How does cellular respiration function as an exergonic process?",
                "opts": [
                    "It absorbs light to build glucose molecules.",
                    "It breaks down glucose in a single, explosive step to warm the cell.",
                    "It involves many steps, releasing energy slowly to produce ATP.",
                    "It requires a constant input of ATP energy to break down water."
                ],
                "a": 2,
                "exp": "Cellular respiration is a slow, multi-step exergonic process that captures released chemical energy to generate ATP."
            }
        ]
    },
    109: {
        "unit": 2,
        "page": 109,
        "filename": "Unit_2_4.txt",
        "section_title": "Metabolism",
        "page_num_in_file": 12,
        "slide_title": "Exergonic Reactions",
        "original_text": "Exergonic Reactions\nReactants\nEnergy\nProducts\nAmount of energy released\nPotential energy",
        "explanation": "This slide provides a graphical energy profile of an exergonic reaction. It shows that reactants start with a high level of potential energy, and as the reaction proceeds, energy is released. The resulting products have lower potential energy than the reactants, and the difference in energy levels is the net amount of energy released.",
        "questions": [
            {
                "q": "In an exergonic reaction graph, how do the energy levels of the reactants and products compare?",
                "opts": [
                    "Reactants have lower potential energy than products.",
                    "Reactants and products have equal potential energy.",
                    "Reactants have higher potential energy than products.",
                    "Products have infinite potential energy."
                ],
                "a": 2,
                "exp": "Because exergonic reactions release energy, the reactants start with higher potential energy and the products end up with lower potential energy."
            }
        ]
    },
    110: {
        "unit": 2,
        "page": 110,
        "filename": "Unit_2_4.txt",
        "section_title": "Metabolism",
        "page_num_in_file": 13,
        "slide_title": "Endergonic Reactions",
        "original_text": "Endergonic Reactions\u00a8An endergonic reaction\u00a5requires an input of energy and\u00a5yields products rich in potential energy.\u00a8Endergonic reactions\u00a5start with reactant molecules that contain relatively little potential energy but\u00a5end with products that contain more chemical energy.\u00a5Examples include building proteins, DNA, etc. Large molecules with stored energy",
        "explanation": "An endergonic reaction requires a net input of energy to proceed, resulting in products that are rich in potential chemical energy. These reactions start with simple reactant molecules containing relatively little potential energy and, by absorbing energy, assemble them into complex products that store higher amounts of chemical energy. Biological examples include anabolic processes such as synthesis of large molecules like proteins and DNA.",
        "questions": [
            {
                "q": "Which of the following is an example of an endergonic process?",
                "opts": [
                    "Burning wood",
                    "Cellular respiration",
                    "Synthesizing proteins or DNA from simpler building blocks",
                    "Boiling water"
                ],
                "a": 2,
                "exp": "Building complex macromolecules (like proteins or DNA) from simpler monomers requires energy input, making it an endergonic process."
            },
            {
                "q": "How do the reactant and product energy states compare in endergonic reactions?",
                "opts": [
                    "Reactants have high potential energy, and products have low chemical energy.",
                    "Reactants start with little potential energy, and products end with higher chemical energy.",
                    "Reactants and products have the same chemical energy.",
                    "Reactants have no potential energy whatsoever."
                ],
                "a": 1,
                "exp": "Endergonic reactions consume energy, so the simple reactants have low potential energy, and the complex products contain more stored chemical energy."
            }
        ]
    },
    111: {
        "unit": 2,
        "page": 111,
        "filename": "Unit_2_4.txt",
        "section_title": "Metabolism",
        "page_num_in_file": 14,
        "slide_title": "Endergonic Reactions",
        "original_text": "Endergonic Reactions\nReactants\nEnergy\nProducts\nAmount of energy required\nPotential energy",
        "explanation": "This slide displays the graphical energy profile of an endergonic reaction. It shows that reactants start with low potential energy. With the input of a specific amount of required energy, the reaction yields products that possess a much higher level of potential energy.",
        "questions": [
            {
                "q": "On an endergonic reaction energy profile, what does the difference between the reactant energy level and product energy level represent?",
                "opts": [
                    "The amount of energy released as heat.",
                    "The speed of the chemical reaction.",
                    "The amount of energy required for the reaction to proceed.",
                    "The quantity of catalyst consumed."
                ],
                "a": 2,
                "exp": "The difference in energy levels shows the net input of energy required to drive the endergonic reaction forward."
            }
        ]
    },
    112: {
        "unit": 2,
        "page": 112,
        "filename": "Unit_2_4.txt",
        "section_title": "Metabolism",
        "page_num_in_file": 15,
        "slide_title": "Exergonic v Endergonic",
        "original_text": "Exergonic v Endergonic",
        "explanation": "This slide acts as a visual summary comparing the energy profiles of exergonic (energy-releasing) and endergonic (energy-requiring) reactions.",
        "questions": [
            {
                "q": "What comparison is featured on this placeholder slide?",
                "opts": [
                    "Photosynthesis vs Cellular Respiration",
                    "Exergonic vs Endergonic reactions",
                    "Hydrolysis vs Condensation",
                    "Diffusion vs Osmosis"
                ],
                "a": 1,
                "exp": "The slide title is 'Exergonic v Endergonic'."
            }
        ]
    },
    113: {
        "unit": 2,
        "page": 113,
        "filename": "Unit_2_4.txt",
        "section_title": "Metabolism",
        "page_num_in_file": 16,
        "slide_title": "Metabolism",
        "original_text": "Metabolism\u00a8A living organism carries out thousands of endergonic and exergonic chemical reactions.\u00a8The total of an organism’s chemical reactions is called metabolism.\u00a8A metabolic pathwayis a series of chemical reactions that either\u00a5builds a complex molecule or \u00a5breaks down a complex molecule into simpler compounds.",
        "explanation": "Living organisms perform thousands of endergonic and exergonic chemical reactions simultaneously. The sum total of all these chemical reactions occurring within an organism is defined as metabolism. These reactions are organized into metabolic pathways, which are ordered series of chemical reactions that either build up a complex molecule (anabolism) or break down a complex molecule into simpler compounds (catabolism).",
        "questions": [
            {
                "q": "What is a metabolic pathway?",
                "opts": [
                    "A pathway that allows water to enter plant roots.",
                    "A series of chemical reactions that either builds a complex molecule or breaks one down into simpler compounds.",
                    "The movement of electrons in a valence orbital.",
                    "The flow of blood through capillaries."
                ],
                "a": 1,
                "exp": "A metabolic pathway is a linked chain of chemical reactions in a cell that either builds up or breaks down complex molecules."
            }
        ]
    },
    114: {
        "unit": 2,
        "page": 114,
        "filename": "Unit_2_4.txt",
        "section_title": "Metabolism",
        "page_num_in_file": 17,
        "slide_title": "ATP",
        "original_text": "ATP\u00a8Energy couplinguses the energy released from exergonic reactions to drive endergonic reactions, typically using the energy stored in ATP molecules.",
        "explanation": "Energy coupling is a vital cellular strategy where the energy released from exergonic (energy-generating) reactions is directly used to power endergonic (energy-consuming) reactions. This process is typically mediated by utilizing the chemical energy stored within ATP molecules.",
        "questions": [
            {
                "q": "What is energy coupling?",
                "opts": [
                    "The combining of two elements to form a salt.",
                    "Using energy released from exergonic reactions to drive endergonic reactions.",
                    "The pairing of adenine with thymine in DNA.",
                    "The transfer of thermal energy from one body to another."
                ],
                "a": 1,
                "exp": "Energy coupling is the pairing of an energy-releasing (exergonic) reaction with an energy-consuming (endergonic) reaction, often utilizing ATP as the transfer vehicle."
            }
        ]
    },
    115: {
        "unit": 2,
        "page": 115,
        "filename": "Unit_2_4.txt",
        "section_title": "Metabolism",
        "page_num_in_file": 18,
        "slide_title": "ATP",
        "original_text": "ATP\u00a8ATP, adenosine triphosphate, powers nearly all forms of life and consists of\u00a5adenosine and\u00a5a triphosphate tail of three phosphate groups.",
        "explanation": "Adenosine triphosphate (ATP) is the molecular currency of energy that powers nearly all biological work in living organisms. Structurally, ATP consists of an adenosine molecule attached to a triphosphate tail composed of three covalently linked phosphate groups.",
        "questions": [
            {
                "q": "What does ATP consist of structurally?",
                "opts": [
                    "Adenosine and a single phosphate group",
                    "Adenosine and a tail of three phosphate groups",
                    "Ribose sugar and a double rings of phosphates",
                    "Amino acids linked in a peptide chain"
                ],
                "a": 1,
                "exp": "As stated on the slide, ATP consists of adenosine and a triphosphate tail composed of three phosphate groups."
            }
        ]
    }
}

for page, data in pages_data.items():
    file_path = os.path.join(dest_dir, f"page_{page}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

print("Saved pages 101 to 115 successfully.")
