import json
import os

dest_dir = r"C:\Users\elieu\OneDrive\Desktop\biofinaltest\active_recall_temp\unit_2"
os.makedirs(dest_dir, exist_ok=True)

pages_data = {
    11: {
        "unit": 2,
        "page": 11,
        "filename": "Unit_2_1.txt",
        "section_title": "Chemistry of Living Things",
        "page_num_in_file": 11,
        "slide_title": "1: Compounds",
        "original_text": "1: Compounds\u00a8How elements combine to form compounds depends on number and arrangement of their electrons\u00a8Atoms are most stable when highest energy orbital is full with electrons\u00a4Known as valence orbital\u00a8Elements, such as He & Ne, that already have the maximum number of electrons in their valence orbitals are known as noble/inert; don’t react with other elements\u00a4Most elements not in stable form; react to add stability",
        "explanation": "The manner in which elements combine to form compounds is determined by the number and arrangement of their electrons. Atoms reach their most stable state when their highest energy orbital, known as the valence orbital, is completely filled with electrons. Elements that naturally possess a maximum number of electrons in their valence orbitals, such as helium (He) and neon (Ne), are referred to as noble or inert gases, and they do not react with other elements. However, most elements do not exist in this stable configuration and will chemically react with other atoms to achieve stability by filling their valence orbitals.",
        "questions": [
            {
                "q": "What is the outermost, highest-energy electron orbital called, which determines an atom's stability?",
                "opts": ["Core orbital", "Valence orbital", "Nuclear orbital", "Ground orbital"],
                "a": 1,
                "exp": "The highest energy orbital, which must be full for an atom to be stable, is known as the valence orbital."
            },
            {
                "q": "Why are elements like helium (He) and neon (Ne) considered chemically noble or inert?",
                "opts": [
                    "They have too many protons to react.",
                    "They already have the maximum number of electrons in their valence orbitals, making them stable.",
                    "They are unable to form solid states of matter.",
                    "They do not have any orbitals."
                ],
                "a": 1,
                "exp": "Helium and neon are noble/inert because they already contain the maximum number of electrons in their valence orbitals, meaning they are stable and do not need to react to achieve stability."
            }
        ]
    },
    12: {
        "unit": 2,
        "page": 12,
        "filename": "Unit_2_1.txt",
        "section_title": "Chemistry of Living Things",
        "page_num_in_file": 12,
        "slide_title": "1: Compounds",
        "original_text": "1: Compounds",
        "explanation": "This slide serves as an intermediate heading page for compounds.",
        "questions": [
            {
                "q": "What topic is continued on this slide?",
                "opts": ["Energy", "Compounds", "Solutions", "Water"],
                "a": 1,
                "exp": "The slide lists '1: Compounds', continuing the discussion on compounds."
            }
        ]
    },
    13: {
        "unit": 2,
        "page": 13,
        "filename": "Unit_2_1.txt",
        "section_title": "Chemistry of Living Things",
        "page_num_in_file": 13,
        "slide_title": "1: Chemical Bonds -Covalent",
        "original_text": "1: Chemical Bonds -Covalent\u00a8When elements react/interact, they form a chemical bond\u00a4Attractive force that hold atoms together\u00a8Major forms of chemical bonds: covalent& ionic\u00a8Covalent bond: when two atoms shareone or more pairs of electrons \u00a4Ex: H20 –each H needs 1 electron to become stable; O needs 2 electrons to become stable; all become stable by sharing electrons\u00a8Most covalent bonds between 2 non-metals\u00a8Lead to formation of molecules: smallest amount of a substance that retains its properties and can exist in a free state",
        "explanation": "When elements interact, they form a chemical bond, which is the attractive force holding the atoms together. The primary forms of chemical bonds are covalent and ionic bonds. A covalent bond is established when two atoms share one or more pairs of electrons. For example, in a water molecule (H2O), each hydrogen atom requires one electron to achieve stability, and the oxygen atom requires two; they achieve this stability by sharing electrons. Most covalent bonds form between non-metal elements, and they result in molecules, which represent the smallest amount of a substance that retains its chemical properties and can exist independently in a free state.",
        "questions": [
            {
                "q": "What type of chemical bond is formed when two atoms share one or more pairs of electrons?",
                "opts": ["Ionic bond", "Covalent bond", "Hydrogen bond", "Metallic bond"],
                "a": 1,
                "exp": "A covalent bond is defined as the sharing of one or more pairs of electrons between atoms."
            },
            {
                "q": "Which of the following describes a molecule?",
                "opts": [
                    "A positively charged atom.",
                    "An atom that has lost an electron.",
                    "The smallest amount of a substance that retains its properties and can exist in a free state.",
                    "A combination of a metal and a non-metal resulting in a salt."
                ],
                "a": 2,
                "exp": "A molecule is the smallest unit of a substance that retains the properties of that substance and can exist in a free state, typically formed via covalent bonding."
            }
        ]
    },
    14: {
        "unit": 2,
        "page": 14,
        "filename": "Unit_2_1.txt",
        "section_title": "Chemistry of Living Things",
        "page_num_in_file": 14,
        "slide_title": "1: Chemical Bonds -Ionic",
        "original_text": "1: Chemical Bonds -Ionic\u00a8Ionic bond: one atom transfersan outer electron to another atom, resulting in 2 ions\u00a4Ion: an atom or molecule with an electrical charge       (+ or –)\u00a8Positive and negative charges attract –this attractive force known as ionic bond\u00a8Most ionic bonds are between metals and non-metalsand result in “salts”",
        "explanation": "An ionic bond forms when one atom completely transfers one or more outer electrons to another atom. This electron transfer results in the formation of two ions, which are atoms or molecules carrying a net electrical charge (either positive or negative). The electrostatic attraction between these opposing positive and negative charges is what constitutes the ionic bond. Most ionic bonds occur between metal and non-metal elements, typically resulting in the formation of compounds known as salts.",
        "questions": [
            {
                "q": "How does an ionic bond form?",
                "opts": [
                    "Through the sharing of electrons between two non-metals.",
                    "Through the attraction of a hydrogen atom to an oxygen atom.",
                    "Through the transfer of an outer electron from one atom to another, followed by the attraction of the resulting oppositely charged ions.",
                    "By the fusion of two nuclei."
                ],
                "a": 2,
                "exp": "An ionic bond involves the transfer of an outer electron from one atom to another, producing positive and negative ions that attract one another."
            },
            {
                "q": "What is an ion?",
                "opts": [
                    "A neutral particle with no charge.",
                    "An atom or molecule with an electrical charge (positive or negative).",
                    "A sub-atomic particle in the nucleus.",
                    "A covalent compound."
                ],
                "a": 1,
                "exp": "An ion is defined as an atom or molecule that has gained or lost electrons, resulting in an electrical charge."
            }
        ]
    },
    15: {
        "unit": 2,
        "page": 15,
        "filename": "Unit_2_1.txt",
        "section_title": "Chemistry of Living Things",
        "page_num_in_file": 15,
        "slide_title": "2-1: Chemical Bonds -Ionic",
        "original_text": "2-1: Chemical Bonds -Ionic",
        "explanation": "This slide serves as a visual placeholder or separator illustrating ionic bonding.",
        "questions": [
            {
                "q": "What topic does this placeholder slide represent?",
                "opts": ["Covalent Bonds", "Ionic Bonds", "Atomic Structure", "Water Chemistry"],
                "a": 1,
                "exp": "The slide title is '2-1: Chemical Bonds -Ionic'."
            }
        ]
    },
    16: {
        "unit": 2,
        "page": 16,
        "filename": "Unit_2_1.txt",
        "section_title": "Chemistry of Living Things",
        "page_num_in_file": 16,
        "slide_title": "1: Chemical Bonds",
        "original_text": "1: Chemical Bonds\u00a8Although these are the two most common, they are not the only types of bonds. \u00a8We will discuss additional chemical bonds when we discuss water and all of it’s properties",
        "explanation": "While covalent and ionic bonds are the two most common forms of chemical bonds, they are not the only types. Other chemical bonds (such as hydrogen bonds) are introduced and discussed in detail when studying the unique properties of water.",
        "questions": [
            {
                "q": "Are covalent and ionic bonds the only types of chemical bonds?",
                "opts": [
                    "Yes, they are the only biological bonds.",
                    "No, other bonds exist and will be discussed in relation to water.",
                    "Yes, all other interactions are physical rather than chemical.",
                    "No, but they are the only bonds that involve electrons."
                ],
                "a": 1,
                "exp": "The slide states that covalent and ionic bonds are not the only types, and others will be discussed when covering water."
            }
        ]
    },
    17: {
        "unit": 2,
        "page": 17,
        "filename": "Unit_2_1.txt",
        "section_title": "Chemistry of Living Things",
        "page_num_in_file": 17,
        "slide_title": "Section 2: Energy",
        "original_text": "Section 2: Energy",
        "explanation": "This slide marks the beginning of Section 2, which focuses on Energy.",
        "questions": [
            {
                "q": "What is the focus of Section 2?",
                "opts": ["Composition of Matter", "Energy", "Water & Solutions", "Macromolecules"],
                "a": 1,
                "exp": "The section title slide is explicitly named 'Section 2: Energy'."
            }
        ]
    },
    18: {
        "unit": 2,
        "page": 18,
        "filename": "Unit_2_1.txt",
        "section_title": "Chemistry of Living Things",
        "page_num_in_file": 18,
        "slide_title": "2: Energy & States of Matter",
        "original_text": "2: Energy & States of Matter\u00a8Energy: ability to do work\u00a4Cannot be created or destroyed, only converted between different forms\nEx: Electrical, radiant, thermal, kinetic, potential, chemical, mechanical\u00a8States of matter: all matter is in constant motion that cannot be observed\u00a4Amount of motion and spacing between atoms determine its state:\nSolid–closest in space, least amount of movement, fixed volume & shape\nLiquid–medium amount of space, medium amount of movement, fixed volume, variable shape\nGas–most amount of space, most movement, variable shape & volume\u00a8Thermal energy must be added to a substance to change its state",
        "explanation": "Energy is defined as the ability to do work. According to physical laws, energy cannot be created or destroyed; it can only be converted from one form to another, such as electrical, radiant, thermal, kinetic, potential, chemical, or mechanical energy. Matter exists in different states, and all matter is in constant motion, even if it cannot be directly observed. The state of matter is determined by the spacing between atoms and the amount of their molecular motion. In a solid, atoms are closest together, show the least movement, and maintain a fixed volume and shape. In a liquid, there is a medium amount of space and movement, keeping a fixed volume but taking a variable shape. In a gas, atoms have the most spacing and movement, resulting in both variable shape and variable volume. The addition of thermal energy is required to change the state of a substance.",
        "questions": [
            {
                "q": "Which state of matter is characterized by having a fixed volume but a variable shape?",
                "opts": ["Solid", "Liquid", "Gas", "Plasma"],
                "a": 1,
                "exp": "A liquid has a fixed volume but a variable shape. A solid has fixed shape and volume, while a gas has variable shape and volume."
            },
            {
                "q": "What is required to change the state of matter of a substance?",
                "opts": [
                    "Destruction of its mass.",
                    "Adding thermal energy.",
                    "Creating new energy forms.",
                    "Reducing the speed of the electrons to zero."
                ],
                "a": 1,
                "exp": "According to the slide, thermal energy must be added to a substance in order to change its state."
            }
        ]
    },
    19: {
        "unit": 2,
        "page": 19,
        "filename": "Unit_2_1.txt",
        "section_title": "Chemistry of Living Things",
        "page_num_in_file": 19,
        "slide_title": "2: Chemical Reactions",
        "original_text": "2: Chemical Reactions\u00a8Chemical reaction: one or more substances change to produce one or more different substances\u00a4Energy is absorbed or released when chemical bonds are broken and new ones are formed\u00a4Generally written with starting material (reactants) on the left and the new material (products) on the right\nWhen the arrow is uni-directional (\u00e0) reaction only occurs in one direction (irreversible)\nWhen arrow is bi-directional (\u21c4) reaction can occur in either direction (reversible)\u00a8Occur constantly in the body: energy supplying substances are broken down to CO2, H2O, other products; releasing energy for cells to do work\u00a4Sum = metabolism",
        "explanation": "A chemical reaction occurs when one or more substances change to produce one or more different substances. During a chemical reaction, energy is either absorbed or released as chemical bonds are broken and new bonds are formed. In chemical equations, the starting materials, called reactants, are written on the left, while the resulting substances, called products, are on the right. A uni-directional arrow (-->) denotes an irreversible reaction that only occurs in one direction, whereas a bi-directional arrow indicates a reversible reaction that can proceed in either direction. Chemical reactions occur continuously in living bodies, such as when energy-supplying molecules are broken down into CO2, H2O, and other products to release energy for cellular work. The sum of all these chemical reactions in an organism is known as metabolism.",
        "questions": [
            {
                "q": "What term refers to the sum of all chemical reactions that occur within a living organism?",
                "opts": ["Catabolism", "Metabolism", "Anabolism", "Respiration"],
                "a": 1,
                "exp": "The sum of all chemical reactions occurring in the body (such as breaking down energy-supplying substances) is defined as metabolism."
            },
            {
                "q": "What does a bi-directional arrow in a chemical equation represent?",
                "opts": [
                    "The reaction is irreversible.",
                    "The reaction can occur in either direction (reversible).",
                    "The reaction is endothermic only.",
                    "The reaction requires a metal catalyst."
                ],
                "a": 1,
                "exp": "A bi-directional arrow indicates that the reaction is reversible, meaning it can proceed in both the forward and reverse directions."
            }
        ]
    },
    20: {
        "unit": 2,
        "page": 20,
        "filename": "Unit_2_1.txt",
        "section_title": "Chemistry of Living Things",
        "page_num_in_file": 20,
        "slide_title": "2: Change",
        "original_text": "2: Change\u00a8There are two main types of change that matter can undergo:\u00a4Physical Change –Matter changes form but not chemical identity\nWater Boiling, freezing, ice being chopped, metal being bent\u00a4Chemical Change –Matter undergoes a chemical reaction\nWood burning, food being cooked, iron rusting",
        "explanation": "Matter can undergo two primary types of change: physical changes and chemical changes. A physical change occurs when matter changes its physical form or state but retains its original chemical identity; examples include water boiling or freezing, ice being chopped, or metal being bent. In contrast, a chemical change involves a chemical reaction where matter is transformed into new substances with different chemical properties; examples include wood burning, food being cooked, or iron rusting.",
        "questions": [
            {
                "q": "Which of the following is an example of a chemical change?",
                "opts": ["Ice being chopped", "Water boiling", "Wood burning", "Metal being bent"],
                "a": 2,
                "exp": "Wood burning is a chemical change because a chemical reaction occurs, transforming wood into new substances (ash, gases). Boiling, chopping ice, and bending metal are physical changes."
            },
            {
                "q": "What is the defining feature of a physical change?",
                "opts": [
                    "A new substance is created.",
                    "Chemical bonds are permanently altered.",
                    "Matter changes its form but not its chemical identity.",
                    "The change is always irreversible."
                ],
                "a": 2,
                "exp": "During a physical change, the form or state of the matter changes, but its chemical identity remains unchanged."
            }
        ]
    },
    21: {
        "unit": 2,
        "page": 21,
        "filename": "Unit_2_1.txt",
        "section_title": "Chemistry of Living Things",
        "page_num_in_file": 21,
        "slide_title": "Section 3: Water & Solutions",
        "original_text": "Section 3: Water & Solutions",
        "explanation": "This slide serves as the transition slide to Section 3: Water & Solutions.",
        "questions": [
            {
                "q": "What is the topic of Section 3?",
                "opts": ["Macromolecules", "Energy", "Water & Solutions", "Basic Atoms"],
                "a": 2,
                "exp": "The section title page designates 'Section 3: Water & Solutions'."
            }
        ]
    },
    22: {
        "unit": 2,
        "page": 22,
        "filename": "Unit_2_1.txt",
        "section_title": "Chemistry of Living Things",
        "page_num_in_file": 22,
        "slide_title": "3: Polarity of Water",
        "original_text": "3: Polarity of Water\u00a8Biological function of water comes from its chemical structure\u00a4H’s and O share electrons in covalent bonds –unequally\u00a4O attracts more electrons than H, pulling them toward its own nucleus\u00a8Although molecule has net 0 charge, each atom has partial charge\u00a4O is partially –(σ-)and Hs are partially + (σ+). When charge is not equally distributed among atoms of a molecule, known as polar",
        "explanation": "The biological functions of water stem directly from its chemical structure. The hydrogen (H) and oxygen (O) atoms share electrons unequally via covalent bonds. Oxygen possesses a higher electronegativity, attracting the shared electrons more strongly and pulling them closer to its own nucleus. Although the overall water molecule has a net charge of zero, this unequal sharing gives rise to partial electrical charges on the individual atoms: the oxygen atom becomes partially negative (σ-), while the hydrogen atoms become partially positive (σ+). When electric charge is distributed unequally among the atoms of a molecule in this manner, the molecule is classified as polar.",
        "questions": [
            {
                "q": "Why is a water molecule considered polar?",
                "opts": [
                    "It has a net negative charge.",
                    "It has a net positive charge.",
                    "Electrons are shared unequally between oxygen and hydrogen, resulting in partial charges on the atoms.",
                    "The hydrogen atoms completely transfer their electrons to the oxygen atom."
                ],
                "a": 2,
                "exp": "Water is polar because hydrogen and oxygen share electrons unequally (with oxygen attracting them more), leading to partial positive charges on hydrogens and a partial negative charge on oxygen, despite an overall net charge of zero."
            },
            {
                "q": "What partial charge does the oxygen atom carry in a water molecule?",
                "opts": ["Partial positive (σ+)", "Partial negative (σ-)", "Net neutral (0)", "Double positive (2+)"],
                "a": 1,
                "exp": "Because oxygen attracts the shared electrons more strongly, it acquires a partial negative charge (σ-)."
            }
        ]
    },
    23: {
        "unit": 2,
        "page": 23,
        "filename": "Unit_2_1.txt",
        "section_title": "Chemistry of Living Things",
        "page_num_in_file": 23,
        "slide_title": "3: Solutions & Solubility",
        "original_text": "3: Solutions & Solubility\u00a8Solubility: ability of a substance to dissolve another substance\u00a4“Like dissolves like”: polar substances dissolve other polar substances (sugars, ionic compounds, some proteins); does not dissolve non-polar substances (oil, other substances with high CH content)\u00a4Ex: NaCl(ionic compound) can dissolve in water\nNa+attracted to σ-O; Cl-attracted to σ+H\u00a8Importance?\u00a4Ions (esp. Na+, Cl-, K+, Ca2+) necessary for essential body functions: muscle contraction, transmission of impulses throughout nervous system",
        "explanation": "Solubility is the ability of a substance to dissolve another substance. This process follows the principle of 'like dissolves like': polar substances can dissolve other polar substances (such as sugars, ionic compounds, and certain proteins), but they cannot dissolve non-polar substances (such as oil or molecules with high carbon-hydrogen content). For example, sodium chloride (NaCl), an ionic compound, dissolves in water because the positive sodium ions (Na+) are attracted to the partially negative oxygen atoms (σ- O) of water, while the negative chloride ions (Cl-) are attracted to the partially positive hydrogen atoms (σ+ H). The solubility of these ionic substances in water is biologically crucial because ions (especially Na+, Cl-, K+, and Ca2+) are essential for vital body functions, including muscle contraction and the transmission of nerve impulses.",
        "questions": [
            {
                "q": "Which principle explains why water (a polar solvent) can dissolve salt and sugar, but not oil?",
                "opts": ["Opposites attract", "Like dissolves like", "Conservation of mass", "Second law of thermodynamics"],
                "a": 1,
                "exp": "The rule 'like dissolves like' states that polar solvents dissolve polar and ionic solutes, whereas non-polar substances do not dissolve in polar solvents."
            },
            {
                "q": "How does sodium chloride (NaCl) dissolve in water at the molecular level?",
                "opts": [
                    "Na+ is attracted to the partial positive hydrogen, and Cl- is attracted to the partial negative oxygen.",
                    "Na+ is attracted to the partial negative oxygen, and Cl- is attracted to the partial positive hydrogen.",
                    "Water molecules form covalent bonds with sodium and chloride.",
                    "Sodium and chloride atoms share electrons equally with water."
                ],
                "a": 1,
                "exp": "Because water is polar, the positive Na+ ions are attracted to the partially negative oxygen atoms (σ- O), and the negative Cl- ions are attracted to the partially positive hydrogen atoms (σ+ H)."
            }
        ]
    },
    24: {
        "unit": 2,
        "page": 24,
        "filename": "Unit_2_1.txt",
        "section_title": "Chemistry of Living Things",
        "page_num_in_file": 24,
        "slide_title": "3: Hydrogen Bonding",
        "original_text": "3: Hydrogen Bonding\u00a8Polarity of water causes its molecules to be attracted to one another\u00a4σ-O attracted to σ+H of another molecule\u00a4This attractive force known a hydrogen bond\u00a8H bonding causes water to “cling” to itself and some other substances\u00a4These bonds constantly form, break, re-form\u00a4H2O (s) –all molecules are H bonded and do not break\u00a4H2O (l) –addition of energy breaks some H bonds until number of bonded and unbondedmolecules are equal\u00a4H2O (g) –addition of energy breaks remainder of H bonds until few to none remain\u00a8H bonding responsible for special properties of water:\u00a4Cohesion, adhesion, heat capacity, evaporative cooling, density of ice, solubility",
        "explanation": "The polarity of water causes individual water molecules to be attracted to one another. Specifically, the partially negative oxygen atom (σ- O) of one water molecule is attracted to the partially positive hydrogen atom (σ+ H) of a neighboring water molecule. This intermolecular attractive force is known as a hydrogen bond. Hydrogen bonding causes water molecules to 'cling' to each other and to other substances. These bonds are dynamic, constantly forming, breaking, and re-forming. In solid water (ice, H2O (s)), all molecules are held together by stable hydrogen bonds that do not break. In liquid water (H2O (l)), the addition of energy breaks some of these bonds, maintaining a dynamic equilibrium where the number of bonded and unbonded molecules is roughly equal. In gaseous water (steam/vapor, H2O (g)), additional energy breaks the remaining hydrogen bonds until very few or none remain. Hydrogen bonding is directly responsible for water's unique physical properties, including cohesion, adhesion, high heat capacity, evaporative cooling, the low density of ice, and high solubility.",
        "questions": [
            {
                "q": "What is a hydrogen bond in water?",
                "opts": [
                    "A covalent bond between hydrogen and oxygen in a single water molecule.",
                    "An attractive force between the partially negative oxygen of one water molecule and the partially positive hydrogen of another water molecule.",
                    "An ionic bond formed when hydrogen transfers an electron to oxygen.",
                    "A bond that only exists when water is in its gaseous state."
                ],
                "a": 1,
                "exp": "A hydrogen bond is an intermolecular attractive force between the partially negative oxygen (σ-) of one water molecule and the partially positive hydrogen (σ+) of another water molecule."
            },
            {
                "q": "In which state of water are all molecules hydrogen-bonded to one another without the bonds breaking?",
                "opts": ["Liquid water", "Gaseous water (steam)", "Solid water (ice)", "Supercritical fluid"],
                "a": 2,
                "exp": "In solid water (ice), all molecules are locked in place by hydrogen bonds that do not break. In liquid, they break and reform; in gas, few to none remain."
            }
        ]
    },
    25: {
        "unit": 2,
        "page": 25,
        "filename": "Unit_2_1.txt",
        "section_title": "Chemistry of Living Things",
        "page_num_in_file": 25,
        "slide_title": "3: Cohesion",
        "original_text": "3: Cohesion\u00a8Cohesion: attractive force that holds molecules of a single substance together\u00a4Ability of substance to stick to itself\u00a4Due to H bonding –allows upward movement of water from plant roots to leave\u00a8Related to cohesion –surface tension\u00a4Cohesive forces resulting from H bonds cause molecules at the surface of water to be pulled downward into the liquid\u00a4Result –water acts as if it has thin “skin” over the surface\nEx: in an over-filled glass, water appears to bulge over the rim\nEx: small creatures are able to run on water’s surface without sinking",
        "explanation": "Cohesion is the attractive force that holds molecules of a single substance together, representing the ability of a substance to stick to itself. In water, cohesion is caused by hydrogen bonding, which is biologically important as it enables the upward movement of water from plant roots to leaves. A closely related concept is surface tension, where cohesive forces draw water molecules at the surface downward into the liquid. This causes the surface of the water to behave as though it is covered by a thin, elastic 'skin'. This phenomenon is visible when water bulges over the rim of an over-filled glass, or when small creatures walk across the water's surface without sinking.",
        "questions": [
            {
                "q": "What is cohesion?",
                "opts": [
                    "The attraction between molecules of different substances.",
                    "The force that holds molecules of a single substance together.",
                    "The process of water turning into gas.",
                    "The chemical reaction between oxygen and hydrogen."
                ],
                "a": 1,
                "exp": "Cohesion is defined as the attractive force that holds molecules of a single substance together (sticking to itself)."
            },
            {
                "q": "What causes the phenomenon of surface tension in water?",
                "opts": [
                    "Repulsive forces between oxygen atoms.",
                    "Cohesive forces from hydrogen bonds that pull surface molecules downward into the liquid.",
                    "The high density of dissolved salts.",
                    "The covalent bonding between water and air molecules."
                ],
                "a": 1,
                "exp": "Surface tension is caused by cohesive forces (due to hydrogen bonds) that pull surface water molecules downward, making the surface act like a thin skin."
            }
        ]
    }
}

for page, data in pages_data.items():
    file_path = os.path.join(dest_dir, f"page_{page}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

print("Saved pages 11 to 25 successfully.")
