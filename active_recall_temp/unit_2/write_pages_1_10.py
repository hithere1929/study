import json
import os

dest_dir = r"C:\Users\elieu\OneDrive\Desktop\biofinaltest\active_recall_temp\unit_2"
os.makedirs(dest_dir, exist_ok=True)

pages_data = {
    1: {
        "unit": 2,
        "page": 1,
        "filename": "Unit_2_1.txt",
        "section_title": "Chemistry of Living Things",
        "page_num_in_file": 1,
        "slide_title": "BASIC CHEMISTRY OF LIVINGTHINGSBiology 9                   Mr. QueenanText -Ch 2.1-2.2 (p 42-51)",
        "original_text": "BASIC CHEMISTRY OF LIVINGTHINGSBiology 9                   Mr. QueenanText -Ch 2.1-2.2 (p 42-51)",
        "explanation": "This is the introductory title page for Unit 2, Section 1: Chemistry of Living Things. The slides cover the basic chemistry of living things, corresponding to Biology 9 with Mr. Queenan, referencing Textbook Chapters 2.1-2.2 on pages 42-51.",
        "questions": [
            {
                "q": "Which chapters of the textbook correspond to the basic chemistry section introduced on this page?",
                "opts": ["Chapters 1.1-1.2", "Chapters 2.1-2.2", "Chapters 3.1-3.2", "Chapters 4.1-4.2"],
                "a": 1,
                "exp": "The slide title explicitly mentions 'Text -Ch 2.1-2.2 (p 42-51)', indicating chapters 2.1 and 2.2."
            }
        ]
    },
    2: {
        "unit": 2,
        "page": 2,
        "filename": "Unit_2_1.txt",
        "section_title": "Chemistry of Living Things",
        "page_num_in_file": 2,
        "slide_title": "Section 1: Composition of Matter",
        "original_text": "Section 1: Composition of Matter",
        "explanation": "This slide serves as the transition page introducing Section 1, which focuses on the Composition of Matter.",
        "questions": [
            {
                "q": "What is the primary topic of Section 1 as introduced on this page?",
                "opts": ["Cell Structure", "Composition of Matter", "Energy and Metabolism", "Genetics"],
                "a": 1,
                "exp": "The title of the slide is 'Section 1: Composition of Matter', which specifies the topic of this section."
            }
        ]
    },
    3: {
        "unit": 2,
        "page": 3,
        "filename": "Unit_2_1.txt",
        "section_title": "Chemistry of Living Things",
        "page_num_in_file": 3,
        "slide_title": "1: Matter",
        "original_text": "1: Matter\u00a8Understanding chemistry is important to biologists:\u00a4Living things composed of the same kinds of matter as non-living things\u00a4Knowing how matter changes leads to understanding of life processes of organisms\u00a8Matter: anything that occupies space & has mass\u00a8Mass: quantity of matter in an object\u00a8Weight: force produced by gravity acting on mass\u00a4Mass \u2260 weight",
        "explanation": "Understanding chemistry is critical for biologists because living things are composed of the same types of matter as non-living things, and knowing how matter changes is essential for understanding the life processes of organisms. Matter is defined as anything that occupies space and has mass. Mass is the actual quantity of matter contained within an object, which remains constant regardless of location. In contrast, weight is the force produced by gravity acting upon that mass, meaning that mass and weight are not equal.",
        "questions": [
            {
                "q": "What is the key difference between mass and weight?",
                "opts": [
                    "Mass changes based on gravity, while weight remains constant.",
                    "Weight is the amount of space occupied, while mass is the quantity of matter.",
                    "Mass is the quantity of matter in an object, while weight is the gravitational force acting on that mass.",
                    "There is no difference; they are scientifically identical."
                ],
                "a": 2,
                "exp": "Mass is defined as the quantity of matter in an object, whereas weight represents the force produced by gravity acting on that mass. Because gravity varies depending on location, mass and weight are not the same."
            },
            {
                "q": "Why is understanding chemistry important to biologists?",
                "opts": [
                    "Because living things are made of different matter than non-living things.",
                    "Because chemical changes help explain the life processes of organisms.",
                    "Because it explains how gravity acts on mass.",
                    "Because living things do not consist of matter."
                ],
                "a": 1,
                "exp": "Biologists study chemistry because living things are composed of the same kinds of matter as non-living things, and knowing how matter changes leads to an understanding of the life processes of organisms."
            }
        ]
    },
    4: {
        "unit": 2,
        "page": 4,
        "filename": "Unit_2_1.txt",
        "section_title": "Chemistry of Living Things",
        "page_num_in_file": 4,
        "slide_title": "1: Elements",
        "original_text": "1: Elements\u00a8Substance that can not be converted into a simpler substance with different properties (density, solubility\u2026)\u00a8More than 100 elements identified (& continue to be identified)\u00a4\u2248 30 are involved in living processes\nPrimarily O, C, H, N\u00a8Elements organized on the periodic table\u00a8Each has own chemical symbol:\u00a41-3 letters; some are Latin abbr.\u00a4Atomic number\u00a4Atomic mass",
        "explanation": "An element is a substance that cannot be converted into a simpler substance with different properties (such as density, solubility, etc.). More than 100 elements have been identified, and discovery continues. Approximately 30 elements are involved in living processes, with Oxygen (O), Carbon (C), Hydrogen (H), and Nitrogen (N) being the primary elements involved in life. Elements are organized on the periodic table, and each has its own chemical symbol consisting of 1 to 3 letters (some of which are abbreviations of Latin names), along with an atomic number and atomic mass.",
        "questions": [
            {
                "q": "Which four elements are primarily involved in living processes?",
                "opts": [
                    "Carbon, Hydrogen, Iron, Oxygen",
                    "Oxygen, Carbon, Hydrogen, Nitrogen",
                    "Nitrogen, Sulfur, Phosphorus, Carbon",
                    "Sodium, Chlorine, Potassium, Hydrogen"
                ],
                "a": 1,
                "exp": "The elements primarily involved in living processes are Oxygen (O), Carbon (C), Hydrogen (H), and Nitrogen (N)."
            },
            {
                "q": "Which of the following describes an element?",
                "opts": [
                    "A substance that can be easily converted into a simpler substance with different properties.",
                    "A substance that cannot be converted into a simpler substance with different properties.",
                    "A mixture of different compounds that perform metabolic functions.",
                    "A particle composed of neutrons and protons only."
                ],
                "a": 1,
                "exp": "An element is defined as a substance that cannot be converted into a simpler substance with different properties (density, solubility, etc.)."
            }
        ]
    },
    5: {
        "unit": 2,
        "page": 5,
        "filename": "Unit_2_1.txt",
        "section_title": "Chemistry of Living Things",
        "page_num_in_file": 5,
        "slide_title": "1: Atoms",
        "original_text": "1: Atoms\u00a8Atom: smallest component of an element that retains its properties\u00a4Atomic properties determine structure and properties of matter they compose\u00a4Cannot be directly observed; understood through models\u00a8Atomic nucleus contains most of the mass of the atom; 2 types of sub-atomic particles: proton(+ charge) and neutron(0 charge)",
        "explanation": "An atom is the smallest component of an element that retains the properties of that element. The structure and properties of the matter that atoms compose are determined by these atomic properties. Atoms cannot be directly observed and are instead understood through scientific models. The atomic nucleus, which contains most of the mass of the atom, is composed of two types of sub-atomic particles: protons, which carry a positive (+) charge, and neutrons, which carry no charge (0 charge).",
        "questions": [
            {
                "q": "Which two sub-atomic particles are located in the atomic nucleus and make up most of the atom's mass?",
                "opts": [
                    "Protons and electrons",
                    "Neutrons and electrons",
                    "Protons and neutrons",
                    "Electrons and orbitals"
                ],
                "a": 2,
                "exp": "The atomic nucleus contains protons (positive charge) and neutrons (neutral/no charge), which together account for most of the mass of the atom."
            },
            {
                "q": "How do scientists primarily study and understand atoms since they cannot be directly observed?",
                "opts": [
                    "Through direct visual observation with optical microscopes",
                    "Through scientific models",
                    "By measuring their weight in water",
                    "By converting them into simpler substances"
                ],
                "a": 1,
                "exp": "Because atoms cannot be directly observed, they are understood through scientific models."
            }
        ]
    },
    6: {
        "unit": 2,
        "page": 6,
        "filename": "Unit_2_1.txt",
        "section_title": "Chemistry of Living Things",
        "page_num_in_file": 6,
        "slide_title": "1: Atoms",
        "original_text": "1: Atoms\u00a8Atomic number: number of protons in the atom\u00a8Atomic mass (Mass Number): number of protons + number of neutrons in the atom\u00a4Together, these can be used to determine the number of neutrons in the nucleus\u00a8Amount of charge in the atom is balanced\u00a4Number of protons (+) = number of electrons (-)\u00a4Atoms are neutral: 0 net charge",
        "explanation": "The atomic number represents the number of protons in an atom, whereas the atomic mass (or Mass Number) is the sum of the protons and neutrons. By subtracting the atomic number (protons) from the atomic mass (protons + neutrons), the number of neutrons in the nucleus can be determined. In a neutral atom, the electrical charge is balanced: the number of positively charged protons is equal to the number of negatively charged electrons, resulting in a net charge of zero.",
        "questions": [
            {
                "q": "How can the number of neutrons in an atom's nucleus be calculated?",
                "opts": [
                    "By adding the atomic number to the atomic mass.",
                    "By subtracting the number of electrons from the number of protons.",
                    "By subtracting the atomic number (number of protons) from the atomic mass (Mass Number).",
                    "By dividing the atomic mass by the atomic number."
                ],
                "a": 2,
                "exp": "Subtracting the atomic number (number of protons) from the atomic mass (protons + neutrons) yields the number of neutrons."
            },
            {
                "q": "Why do neutral atoms have a net charge of zero?",
                "opts": [
                    "They contain only neutrons, which have no charge.",
                    "The number of positively charged protons equals the number of negatively charged electrons.",
                    "The electrons reside in the nucleus, cancelling the protons' charge.",
                    "They have no electrons."
                ],
                "a": 1,
                "exp": "Atoms are neutral because the amount of charge is balanced: the number of positive protons equals the number of negative electrons, giving a net charge of zero."
            }
        ]
    },
    7: {
        "unit": 2,
        "page": 7,
        "filename": "Unit_2_1.txt",
        "section_title": "Chemistry of Living Things",
        "page_num_in_file": 7,
        "slide_title": "1: Atoms",
        "original_text": "1: Atoms\u00a8Electrons: high energy, negatively charged particles with negligible mass\u00a4Revolve around the nucleus in defined paths known as orbitals\n3D region around the nucleus indicating the probable location of an electron\u00a4Move so quickly \u2013if possible to observe, would not look like objects, but an electron cloud (blur)\u00a4Electrons further from the nucleus have more energy than those close to the nucleus",
        "explanation": "Electrons are high-energy, negatively charged particles with negligible mass. They revolve around the nucleus in defined paths known as orbitals, which are three-dimensional regions around the nucleus indicating the probable location of an electron. Because electrons move extremely quickly, if it were possible to observe them, they would appear not as distinct objects, but as a blurry electron cloud. Electrons that are located further from the nucleus possess more energy than those located closer to the nucleus.",
        "questions": [
            {
                "q": "What is an orbital?",
                "opts": [
                    "The path along which protons revolve around the nucleus.",
                    "A 3D region around the nucleus indicating the probable location of an electron.",
                    "The core of the atom containing protons and neutrons.",
                    "A chemical bond between two elements."
                ],
                "a": 1,
                "exp": "An orbital is a 3D region around the nucleus indicating the probable location of an electron."
            },
            {
                "q": "How does the energy level of an electron change in relation to its distance from the nucleus?",
                "opts": [
                    "Electrons closer to the nucleus have more energy.",
                    "Distance from the nucleus does not affect the energy of an electron.",
                    "Electrons further from the nucleus have more energy.",
                    "Electrons lose all energy when they move away from the nucleus."
                ],
                "a": 2,
                "exp": "Electrons that are further from the nucleus have more energy than those close to the nucleus."
            }
        ]
    },
    8: {
        "unit": 2,
        "page": 8,
        "filename": "Unit_2_1.txt",
        "section_title": "Chemistry of Living Things",
        "page_num_in_file": 8,
        "slide_title": "1: Atoms",
        "original_text": "1: Atoms\nA Boy and His Atom",
        "explanation": "This slide contains a reference or title to a short film or demonstration titled 'A Boy and His Atom' to illustrate atomic concepts.",
        "questions": [
            {
                "q": "What is the title of the atomic illustration or movie mentioned on this slide?",
                "opts": [
                    "A Boy and His Atom",
                    "An Atom's Journey",
                    "The Structure of Matter",
                    "The Quantum World"
                ],
                "a": 0,
                "exp": "The slide explicitly lists the text 'A Boy and His Atom'."
            }
        ]
    },
    9: {
        "unit": 2,
        "page": 9,
        "filename": "Unit_2_1.txt",
        "section_title": "Chemistry of Living Things",
        "page_num_in_file": 9,
        "slide_title": "1: Atoms & Isotopes",
        "original_text": "1: Atoms & Isotopes\u00a8All atoms of the same element have the same number of protons (constant)\u00a4Number of neutrons can vary\u00a8Isotope: variants of element with differing number of neutrons\u00a4Change the mass of the element\u00a4Most elements composed of a mixture of isotopes\nAtomic mass found in periodic table is actually average atomic mass which accounts for relative amounts of each isotope",
        "explanation": "All atoms of the same element must contain the exact same number of protons, which is constant. However, the number of neutrons can vary among these atoms. An isotope is a variant of an element that has a differing number of neutrons, which changes the total mass of the element. Most elements in nature exist as a mixture of different isotopes. The atomic mass listed on the periodic table is actually the average atomic mass, representing the weighted average that accounts for the relative abundances of each isotope.",
        "questions": [
            {
                "q": "What is an isotope?",
                "opts": [
                    "An atom with a different number of protons.",
                    "An atom with a different number of electrons, giving it a charge.",
                    "A variant of an element with a differing number of neutrons.",
                    "A compound made of two different elements."
                ],
                "a": 2,
                "exp": "An isotope is a variant of an element that has a differing number of neutrons, which alters the mass of the element."
            },
            {
                "q": "Why is the atomic mass on the periodic table often not a whole number?",
                "opts": [
                    "It represents the mass of protons and electrons only.",
                    "It is the average atomic mass, taking into account the relative abundance of different isotopes of that element.",
                    "It changes depending on the gravitational force acting on the element.",
                    "It is measured in different units than the mass number."
                ],
                "a": 1,
                "exp": "The atomic mass on the periodic table is the average atomic mass, which accounts for the relative amounts of each isotope found in nature."
            }
        ]
    },
    10: {
        "unit": 2,
        "page": 10,
        "filename": "Unit_2_1.txt",
        "section_title": "Chemistry of Living Things",
        "page_num_in_file": 10,
        "slide_title": "1: Compounds",
        "original_text": "1: Compounds\u00a8Elements not usually found alone\u00a8Atoms readily combine with other atoms of the same or different elements to form compounds\u00a4Made of atoms of 2 or more elements in fixed proportions\u00a8Chemical formula shows type and proportion of atoms in a compound\u00a4H2O, CO2, H2, CH4, CH3OH\u00a8Physical and chemical properties of compounds and their component elements are different\u00a4O2(g) + 2H2(g) \u00e02H2O (l)",
        "explanation": "Elements are not usually found alone in nature. Instead, atoms readily combine with other atoms of the same or different elements to form compounds. A compound is composed of atoms of two or more elements chemically combined in fixed proportions. A chemical formula, such as H2O, CO2, H2, CH4, or CH3OH, indicates the specific types and proportions of atoms within a compound. The physical and chemical properties of a compound are distinct and different from those of its component elements, as illustrated by the reaction where gaseous oxygen and hydrogen combine to form liquid water.",
        "questions": [
            {
                "q": "Which of the following is true regarding the properties of a compound compared to the properties of its component elements?",
                "opts": [
                    "The properties of the compound are identical to those of its component elements.",
                    "The properties of the compound are always gaseous.",
                    "The physical and chemical properties of a compound are different from those of the component elements.",
                    "Compounds have no physical properties, only chemical properties."
                ],
                "a": 2,
                "exp": "The physical and chemical properties of a compound are different from those of its component elements (e.g., gaseous oxygen and hydrogen combine to form liquid water)."
            },
            {
                "q": "What does a chemical formula represent?",
                "opts": [
                    "The number of protons and neutrons in an atom.",
                    "The types and proportions of atoms in a compound.",
                    "The state of matter of a substance.",
                    "The rate of a chemical reaction."
                ],
                "a": 1,
                "exp": "A chemical formula shows the type and proportion of atoms in a compound (e.g., H2O has two hydrogen atoms and one oxygen atom)."
            }
        ]
    }
}

for page, data in pages_data.items():
    file_path = os.path.join(dest_dir, f"page_{page}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

print("Saved pages 1 to 10 successfully.")
