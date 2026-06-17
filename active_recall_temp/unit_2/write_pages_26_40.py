import json
import os

dest_dir = r"C:\Users\elieu\OneDrive\Desktop\biofinaltest\active_recall_temp\unit_2"
os.makedirs(dest_dir, exist_ok=True)

pages_data = {
    26: {
        "unit": 2,
        "page": 26,
        "filename": "Unit_2_1.txt",
        "section_title": "Chemistry of Living Things",
        "page_num_in_file": 26,
        "slide_title": "3: Adhesion",
        "original_text": "3: Adhesion\u00a8Adhesion: attractive force between particles of different substances\u00a4Ex: water and glass\u00a8Related to adhesion –capillarity\u00a4Attraction between molecules resulting in rise of a surface of liquid when in contact with a solid\u00a8Cohesion, adhesion, capillarity work together to help water rise through narrow tubes against the force of gravity\u00a4Ex: plant vascular system",
        "explanation": "Adhesion is the attractive force that occurs between particles of different substances, such as the attraction between water and glass. A related phenomenon is capillarity, which is the attraction between molecules that results in the rise of a liquid's surface when it comes into contact with a solid. Together, cohesion (water sticking to itself), adhesion (water sticking to other surfaces), and capillarity work in unison to enable water to rise through narrow tubes against the downward force of gravity, which is essential for the vascular system of plants to transport water upward.",
        "questions": [
            {
                "q": "What is the term for the attractive force between particles of different substances?",
                "opts": ["Cohesion", "Adhesion", "Capillarity", "Solubility"],
                "a": 1,
                "exp": "Adhesion is the attractive force between different substances, whereas cohesion is between molecules of the same substance."
            },
            {
                "q": "How do cohesion, adhesion, and capillarity work together in plants?",
                "opts": [
                    "They allow water to evaporate rapidly from leaves.",
                    "They force plants to absorb nutrients without water.",
                    "They work together to help water rise through narrow tubes in the vascular system against gravity.",
                    "They turn water into a solid state to prevent freezing."
                ],
                "a": 2,
                "exp": "The combination of cohesion, adhesion, and capillarity allows water to climb upwards through narrow plant vascular tissues against gravity."
            }
        ]
    },
    27: {
        "unit": 2,
        "page": 27,
        "filename": "Unit_2_1.txt",
        "section_title": "Chemistry of Living Things",
        "page_num_in_file": 27,
        "slide_title": "3: Heat Capacity",
        "original_text": "3: Heat Capacity\u00a8Water has high heat capacity\u00a4Ability to absorb or release relatively large amounts of heat energy with only a slight change in temperature\u00a4Due to H bonding –energy is absorbed to break H bonds and is released when H bonds form\u00a8First, energy input breaks H bonds, then increases movement of moleculescausing increase in temperature\u00a8When temperature drops, H bonds re-form and release heat energy\nEx: Heat from sun absorbed by water which cools the air; at night, gradual cooling of water warms the air",
        "explanation": "Water possesses a high heat capacity, which is the ability to absorb or release relatively large quantities of heat energy while undergoing only a minimal change in temperature. This property is due to hydrogen bonding. When thermal energy is added to water, the energy input is first consumed to break hydrogen bonds before it can increase the movement of water molecules to raise the temperature. Conversely, when the temperature drops, hydrogen bonds re-form and release heat energy. For example, during the day, water absorbs heat from the sun and cools the surrounding air; at night, the gradual cooling of the water releases heat, warming the air.",
        "questions": [
            {
                "q": "Why is water able to absorb large amounts of heat with only a slight change in temperature?",
                "opts": [
                    "Because its molecules have high density.",
                    "Because added energy is first used to break hydrogen bonds before it can speed up molecular movement.",
                    "Because it is an inorganic salt.",
                    "Because covalent bonds between hydrogen and oxygen are constantly breaking."
                ],
                "a": 1,
                "exp": "Water's high heat capacity is due to hydrogen bonds: input energy is first absorbed to break these bonds, and only after that does it increase molecular motion to raise the temperature."
            },
            {
                "q": "What happens at the molecular level when the temperature of water drops?",
                "opts": [
                    "Hydrogen bonds are destroyed, absorbing heat.",
                    "Covalent bonds are formed, absorbing heat.",
                    "Hydrogen bonds re-form, releasing heat energy.",
                    "Water molecules speed up and release heat."
                ],
                "a": 2,
                "exp": "When water temperature drops, hydrogen bonds re-form, which releases heat energy into the surrounding environment."
            }
        ]
    },
    28: {
        "unit": 2,
        "page": 28,
        "filename": "Unit_2_1.txt",
        "section_title": "Chemistry of Living Things",
        "page_num_in_file": 28,
        "slide_title": "3: Evaporative Cooling",
        "original_text": "3: Evaporative Cooling\u00a8Heat capacity of water:\u00a4Allows oceans to stabilize temperature of Earth such that life can survive\u00a4Allows cells to maintain temperature despite changes in environmental temperature\u00a8Evaporative cooling: relatively large amount of energy absorbed by water during evaporation which significantly cools surface of remaining liquid\u00a4Prevents organisms from over-heating\nEx: sweating, panting",
        "explanation": "Water's high heat capacity plays a vital role in global and cellular homeostasis: it allows the Earth's oceans to stabilize global temperatures to sustain life, and it helps individual cells maintain a stable internal temperature despite fluctuations in the external environment. A related mechanism is evaporative cooling, where a relatively large amount of heat energy is absorbed by water as it evaporates, resulting in a significant cooling of the remaining liquid surface. This process prevents organisms from overheating, as exemplified by physiological responses like sweating in humans and panting in animals.",
        "questions": [
            {
                "q": "What is evaporative cooling?",
                "opts": [
                    "Water absorbing heat from the sun and warming the environment.",
                    "The process where water absorbs a large amount of energy during evaporation, cooling the surface of the remaining liquid.",
                    "The freezing of water from top to bottom.",
                    "The condensation of water vapor onto a cool surface."
                ],
                "a": 1,
                "exp": "Evaporative cooling is the process where liquid water absorbs a large amount of energy as it transitions to gas, thereby cooling the surface left behind (e.g., sweating)."
            },
            {
                "q": "Which of the following is a biological example of evaporative cooling to prevent overheating?",
                "opts": ["Shivering", "Sweating or panting", "Capillarity in roots", "Ice crystal formation"],
                "a": 1,
                "exp": "Sweating and panting are biological examples of evaporative cooling used by organisms to dump excess heat."
            }
        ]
    },
    29: {
        "unit": 2,
        "page": 29,
        "filename": "Unit_2_1.txt",
        "section_title": "Chemistry of Living Things",
        "page_num_in_file": 29,
        "slide_title": "3: Density of Ice",
        "original_text": "3: Density of Ice\u00a8Density: amount of matter per unit area\u00a8Solids: most dense of all forms of matter; except for solid water\u00a4Ice is LESS dense than liquid water due to the shape of water molecule and H bonding\nWide angle between H atoms allows formation of ice crystals with large amounts of open space (i.e. low density)\u00a8Allows ice to float in liquid water\u00a4Ponds and lakes freeze top \u00e0bottom; insulating water below and allowing aquatic organisms to survive",
        "explanation": "Density is defined on this slide as the amount of matter per unit area. While solids are generally the most dense state of matter for most substances, solid water (ice) is a notable exception because it is less dense than liquid water. This lower density is due to the shape of the water molecule and hydrogen bonding: the wide angle between the hydrogen atoms causes the molecules to form a crystalline lattice with large amounts of open space. This low density allows ice to float on liquid water. Consequently, ponds and lakes freeze from the top down, creating an insulating layer of ice at the surface that protects the liquid water below and allows aquatic organisms to survive the winter.",
        "questions": [
            {
                "q": "Why is ice less dense than liquid water?",
                "opts": [
                    "The hydrogen bonds break completely in ice, letting molecules escape.",
                    "The wide angle between H atoms and hydrogen bonding causes ice crystals to form with large amounts of open space.",
                    "Ice molecules contain fewer protons than liquid water.",
                    "Ice has a higher amount of dissolved gases."
                ],
                "a": 1,
                "exp": "Ice is less dense due to its molecular shape and hydrogen bonding: the wide angle between H atoms forces water molecules into a crystal lattice with lots of open space, reducing its density below that of liquid water."
            },
            {
                "q": "What is the biological importance of ice floating on top of ponds and lakes?",
                "opts": [
                    "It stops evaporation entirely.",
                    "It freezes the lakes solid from bottom to top.",
                    "It insulates the water below, allowing aquatic organisms to survive.",
                    "It increases the amount of dissolved oxygen in the water."
                ],
                "a": 2,
                "exp": "Floating ice creates an insulating layer at the top of lakes, preventing them from freezing solid and allowing life to survive underneath."
            }
        ]
    },
    30: {
        "unit": 2,
        "page": 30,
        "filename": "Unit_2_1.txt",
        "section_title": "Chemistry of Living Things",
        "page_num_in_file": 30,
        "slide_title": "3: Solutions",
        "original_text": "3: Solutions\u00a8Solution: mixture in which one or more substances are uniformly distributed in another substance\u00a4Can be a mixture of solid, liquid or gas\u00a8Parts of a solution:\u00a4Solute: a substance dissolved IN the solvent (the substance that is, itself, dissolved)\nCan be ions, atoms or molecules\u00a4Solvent: substance IN WHICH the solute is dissolved (the substance that does the dissolving)\nEx: sugar water –sugar = solute; water = solvent\u00a8Molecules can be hydrophobicor hydrophilic\u00a4Hydro –water; phobic –afraid of; philic-loves",
        "explanation": "A solution is a mixture in which one or more substances are uniformly distributed within another substance, and it can consist of mixtures of solids, liquids, or gases. A solution is composed of two parts: the solute, which is the substance being dissolved (such as ions, atoms, or molecules), and the solvent, which is the substance that does the dissolving. For example, in sugar water, sugar acts as the solute and water acts as the solvent. Furthermore, molecules can be categorized as hydrophobic ('water-fearing') or hydrophilic ('water-loving') based on their interaction with water.",
        "questions": [
            {
                "q": "In a solution of saltwater, what are the roles of salt and water?",
                "opts": [
                    "Salt is the solvent, water is the solute.",
                    "Salt is the solute, water is the solvent.",
                    "Both salt and water are solvents.",
                    "Both salt and water are solutes."
                ],
                "a": 1,
                "exp": "The solute is the substance that is dissolved (salt), and the solvent is the substance doing the dissolving (water)."
            },
            {
                "q": "What does the term 'hydrophobic' mean?",
                "opts": ["Water-loving", "Water-fearing", "Dissolved in water", "Uniformly mixed"],
                "a": 1,
                "exp": "Hydro means water and phobic means afraid of/fearing, so hydrophobic translates to 'water-fearing'."
            }
        ]
    },
    31: {
        "unit": 2,
        "page": 31,
        "filename": "Unit_2_1.txt",
        "section_title": "Chemistry of Living Things",
        "page_num_in_file": 31,
        "slide_title": "3: Aqueous Solutions",
        "original_text": "3: Aqueous Solutions\u00a8Aqueous solution: water is the solvent\u00a4Important to all living things\u00a4Ocean is a aqueous solution –marine life habitat\u00a4Nutrients for plants are in aqueous solution in soil\u00a4Cells exist in interstitial (intercellular) fluid, which is an aqueous solution\u00a4Cells filled with fluid that in an aqueous solution\u00a8Most chemical reaction in the body occur in aqueous solution",
        "explanation": "An aqueous solution is a solution in which water serves as the solvent. Aqueous solutions are critical to all living systems: the oceans are aqueous solutions providing habitats for marine life, plant nutrients in the soil are delivered via aqueous solutions, cells are bathed in intercellular (interstitial) fluid which is aqueous, and cells are filled with intracellular fluid which is also an aqueous solution. Consequently, the vast majority of chemical reactions in the body take place within an aqueous solution.",
        "questions": [
            {
                "q": "What defines an aqueous solution?",
                "opts": [
                    "A solution where alcohol is the solvent.",
                    "A solution where water is the solvent.",
                    "A solution where gas is dissolved in a solid.",
                    "A solution that contains no solute particles."
                ],
                "a": 1,
                "exp": "An aqueous solution is specifically defined as a solution where water is the solvent."
            },
            {
                "q": "Where do most chemical reactions in the human body occur?",
                "opts": ["In a vacuum", "In solid bone matrix", "In aqueous solution", "In lipid membranes only"],
                "a": 2,
                "exp": "Most chemical reactions in the body occur in aqueous solutions because cells and intercellular fluids are water-based."
            }
        ]
    },
    32: {
        "unit": 2,
        "page": 32,
        "filename": "Unit_2_1.txt",
        "section_title": "Chemistry of Living Things",
        "page_num_in_file": 32,
        "slide_title": "3: Acids & Bases",
        "original_text": "3: Acids & Bases\u00a8Acidity& alkalinityneed to be balanced in living systems\u00a8Acids & bases start with the ionization of water\u00a4Water molecules can collide with one another; sometimes the interaction is strong enough to cause a chemical changenWater molecule dissociates: H2O \u21c4 H+ + OH-\nH+ = proton; OH-= hydroxide ion\u00a8Acidity: measure of relative amount of protons\u00a8Alkalinity: measure of relative amount of hydroxide ion",
        "explanation": "Acidity and alkalinity must be carefully balanced in living systems. The chemistry of acids and bases begins with the ionization of water, which occurs when colliding water molecules interact strongly enough to cause a chemical dissociation. In this process, water dissociates into a proton (H+) and a hydroxide ion (OH-) according to the reversible reaction: H2O <-> H+ + OH-. Acidity is a measure of the relative concentration of protons (H+) in the solution, whereas alkalinity is a measure of the relative concentration of hydroxide ions (OH-).",
        "questions": [
            {
                "q": "What chemical reaction represents the ionization (dissociation) of water?",
                "opts": [
                    "2H2 + O2 -> 2H2O",
                    "H2O <-> H+ + OH-",
                    "HCl + NaOH -> NaCl + H2O",
                    "CO2 + H2O <-> H2CO3"
                ],
                "a": 1,
                "exp": "The ionization of water is represented by H2O dissociating into H+ (proton) and OH- (hydroxide ion)."
            },
            {
                "q": "What does alkalinity measure in a solution?",
                "opts": [
                    "The relative amount of protons (H+).",
                    "The total concentration of dissolved salts.",
                    "The relative amount of hydroxide ions (OH-).",
                    "The volume of the solvent."
                ],
                "a": 2,
                "exp": "Alkalinity measures the relative concentration of hydroxide ions (OH-), while acidity measures protons (H+)."
            }
        ]
    },
    33: {
        "unit": 2,
        "page": 33,
        "filename": "Unit_2_1.txt",
        "section_title": "Chemistry of Living Things",
        "page_num_in_file": 33,
        "slide_title": "3: Acids & Bases",
        "original_text": "3: Acids & Bases\u00a8When the amount of H+ = amount of OH--solution is neutral; pure water\u00a8When the amount of H+ > amount of OH--solution is an acid\u00a4Ex: HCl(aq) \u21c2 H+ + Cl-\nLeads to higher hydronium than hydroxide in solution \u00a4Acids tend to taste sour: vinegar (acetic acid); citrus fruit (citric acid)\u00a8When the amount of OH-> amount of H+ -solution is a base\u00a4Ex: NaOH(aq) \u21c2 Na+ + OH-\nLeads to higher hydroxide than hydronium in solution\u00a4Bases described as “alkaline”; tend to be bitter\u00a4Feel slippery because OH-reacts with oil in skin",
        "explanation": "A solution is neutral (like pure water) when the concentration of hydrogen ions (H+) is equal to the concentration of hydroxide ions (OH-). An acid is formed when the concentration of H+ is greater than OH-, such as when hydrochloric acid (HCl) dissociates into H+ and Cl-, leading to a higher concentration of hydronium/protons in the solution. Acids typically taste sour, like vinegar (acetic acid) or citrus fruits (citric acid). A base (also described as alkaline) is formed when the concentration of OH- is greater than H+, such as when sodium hydroxide (NaOH) dissociates into Na+ and OH-, resulting in a higher hydroxide concentration. Bases tend to taste bitter and feel slippery to the touch because hydroxide ions react with the natural oils on human skin.",
        "questions": [
            {
                "q": "What condition defines an acidic solution?",
                "opts": [
                    "The concentration of OH- is greater than H+.",
                    "The concentration of H+ is greater than OH-.",
                    "The concentration of H+ is equal to OH-.",
                    "The solution contains only water molecules."
                ],
                "a": 1,
                "exp": "An acidic solution is defined by having a higher concentration of H+ than OH-."
            },
            {
                "q": "Why do bases feel slippery on human skin?",
                "opts": [
                    "They evaporate extremely quickly.",
                    "The hydroxide ions (OH-) react with the oils present on the skin.",
                    "They contain lubricating oils.",
                    "They coat the skin in a protective layer of salt."
                ],
                "a": 1,
                "exp": "Bases feel slippery because the hydroxide ions (OH-) chemically react with the natural oils on the skin."
            }
        ]
    },
    34: {
        "unit": 2,
        "page": 34,
        "filename": "Unit_2_1.txt",
        "section_title": "Chemistry of Living Things",
        "page_num_in_file": 34,
        "slide_title": "3: pH",
        "original_text": "3: pH\u00a8pH scale used to compare relative concentrations of protons and hydroxide in solution \u00a8Ranges from 0 –14\u00a40 = very acidic; 7 = neutral; 14 = very alkaline\u00a8pH scale is logarithmic; each unit is equal to a 10-fold difference, not a 1-fold difference\u00a8Measured by:\u00a4Litmus paper –changes color based on pH\u00a4Chemical indicator –changes color based on pH\u00a4pH meter –directly measures pH and displays on screen",
        "explanation": "The pH scale is used to compare the relative concentrations of protons (H+) and hydroxide ions (OH-) in a solution. The scale ranges from 0 to 14, where 0 is highly acidic, 7 is neutral, and 14 is highly alkaline (basic). Importantly, the pH scale is logarithmic, meaning that each whole pH unit represents a 10-fold difference in proton concentration rather than a simple 1-fold difference. pH can be measured using litmus paper (which changes color based on acidity), chemical indicators (which also change color), or a digital pH meter that directly measures and displays the pH value.",
        "questions": [
            {
                "q": "Since the pH scale is logarithmic, how much more acidic is a solution with a pH of 5 compared to a solution with a pH of 6?",
                "opts": ["1 times more acidic", "2 times more acidic", "10 times more acidic", "100 times more acidic"],
                "a": 2,
                "exp": "Because the pH scale is logarithmic, each single unit decrease in pH represents a 10-fold increase in acidity (concentration of protons)."
            },
            {
                "q": "What pH value represents a neutral solution?",
                "opts": ["0", "7", "10", "14"],
                "a": 1,
                "exp": "A pH of 7 represents a neutral solution (such as pure water)."
            }
        ]
    },
    35: {
        "unit": 2,
        "page": 35,
        "filename": "Unit_2_1.txt",
        "section_title": "Chemistry of Living Things",
        "page_num_in_file": 35,
        "slide_title": "3: pH",
        "original_text": "3: pH",
        "explanation": "This slide is a title page placeholder for pH concepts.",
        "questions": [
            {
                "q": "What scale is introduced on this section slide?",
                "opts": ["Temperature scale", "pH scale", "Mass scale", "Density scale"],
                "a": 1,
                "exp": "The slide is titled '3: pH', referring to the pH scale."
            }
        ]
    },
    36: {
        "unit": 2,
        "page": 36,
        "filename": "Unit_2_1.txt",
        "section_title": "Chemistry of Living Things",
        "page_num_in_file": 36,
        "slide_title": "3: Control of pH",
        "original_text": "3: Control of pH\u00a8pH needs to be tightly controlled in living organisms\u00a4Enzymes & other proteins function only within narrow pH range\u00a8Control of pH in living system accomplished by buffers\u00a4Chemical substance that can neutralizesmall amounts of acid or base added to the solution\u00a8In blood, most important buffer system is bicarbonate/carbonic acidsystem\u00a4CO2+ H2O \u21c4 H2CO3 \u21c4 HCO3- + H+",
        "explanation": "The control of pH must be tightly regulated in living organisms because enzymes and other proteins can only function within a narrow, specific pH range. Organisms accomplish this pH regulation using buffers, which are chemical substances that neutralize small amounts of acid or base added to a solution. In human blood, the most critical buffer system is the bicarbonate/carbonic acid system, which maintains pH balance through the reversible chemical pathway: CO2 + H2O <-> H2CO3 <-> HCO3- + H+.",
        "questions": [
            {
                "q": "What is the function of a buffer in a biological system?",
                "opts": [
                    "To speed up chemical reactions.",
                    "To neutralize small amounts of acid or base to maintain pH stability.",
                    "To break down proteins into amino acids.",
                    "To generate thermal energy."
                ],
                "a": 1,
                "exp": "A buffer is a chemical substance that helps keep pH stable by neutralizing small amounts of acid or base added to a solution."
            },
            {
                "q": "Which buffer system is the most important for maintaining pH stability in human blood?",
                "opts": [
                    "Phosphate buffer system",
                    "Protein buffer system",
                    "Bicarbonate/carbonic acid buffer system",
                    "Ammonia buffer system"
                ],
                "a": 2,
                "exp": "As stated on the slide, the bicarbonate/carbonic acid buffer system is the most important system for regulating blood pH."
            }
        ]
    },
    37: {
        "unit": 2,
        "page": 37,
        "filename": "Unit_2_2.txt",
        "section_title": "Chemistry of Organic Molecules",
        "page_num_in_file": 1,
        "slide_title": "UNIT 2: CHEMISTRYOF ORGANICMOLECULESBiology 9              Mr. QueenanText -Ch 2.3 (p 52-56)",
        "explanation": "This is the title slide for Unit 2: Chemistry of Organic Molecules for Biology 9 with Mr. Queenan, which covers Textbook Chapter 2.3 on pages 52-56.",
        "questions": [
            {
                "q": "Which chapter and page range of the textbook correspond to the Chemistry of Organic Molecules section?",
                "opts": [
                    "Chapter 2.1 (p 42-45)",
                    "Chapter 2.2 (p 46-51)",
                    "Chapter 2.3 (p 52-56)",
                    "Chapter 2.4 (p 57-60)"
                ],
                "a": 2,
                "exp": "The slide title explicitly references 'Text -Ch 2.3 (p 52-56)'."
            }
        ]
    },
    38: {
        "unit": 2,
        "page": 38,
        "filename": "Unit_2_2.txt",
        "section_title": "Chemistry of Organic Molecules",
        "page_num_in_file": 2,
        "slide_title": "\u00a8What makes Carbon special?",
        "original_text": "\u00a8What makes Carbon special?",
        "explanation": "This slide serves as an introductory question prompt asking what makes carbon unique among elements.",
        "questions": [
            {
                "q": "Which element's unique properties are introduced on this page?",
                "opts": ["Oxygen", "Carbon", "Nitrogen", "Hydrogen"],
                "a": 1,
                "exp": "The slide asks the question: 'What makes Carbon special?'"
            }
        ]
    },
    39: {
        "unit": 2,
        "page": 39,
        "filename": "Unit_2_2.txt",
        "section_title": "Chemistry of Organic Molecules",
        "page_num_in_file": 3,
        "slide_title": "Organic vs. Inorganic Compounds",
        "original_text": "Organic vs. Inorganic Compounds\u00a8All compounds fall into 2 broad categories\u00a4Organic\u00a4Inorganic\u00a8Organic compounds: made primarily of carbon atoms\u00a4Most matter in living organisms consists of organic compounds\u00a8Inorganic compounds: generally do not contain carbon",
        "explanation": "All chemical compounds can be classified into two broad categories: organic compounds and inorganic compounds. Organic compounds are characterized by being made primarily of carbon atoms, and they constitute most of the matter found in living organisms. In contrast, inorganic compounds generally do not contain carbon atoms.",
        "questions": [
            {
                "q": "What is the primary defining characteristic of an organic compound?",
                "opts": [
                    "It is always a liquid.",
                    "It is made primarily of carbon atoms.",
                    "It cannot contain hydrogen atoms.",
                    "It is only found in non-living matter."
                ],
                "a": 1,
                "exp": "Organic compounds are defined as compounds that are made primarily of carbon atoms."
            },
            {
                "q": "How do inorganic compounds differ from organic compounds?",
                "opts": [
                    "They are larger and more complex.",
                    "They generally do not contain carbon atoms.",
                    "They are only formed via covalent bonds.",
                    "They can only exist in gaseous form."
                ],
                "a": 1,
                "exp": "Inorganic compounds generally do not contain carbon, whereas organic compounds are built around carbon."
            }
        ]
    },
    40: {
        "unit": 2,
        "page": 40,
        "filename": "Unit_2_2.txt",
        "section_title": "Chemistry of Organic Molecules",
        "page_num_in_file": 4,
        "slide_title": "Properties of Carbon",
        "original_text": "Properties of Carbon\u00a8Carbon:\u00a44 electrons in valence orbital –needs 8to be stable\u00a4Can form up to 4 covalent bonds with other elements\u00a4Unlike other elements, can bond with other carbon atoms\nForms straight chains, branched chains or rings\nResults in wide variety of organic compounds",
        "explanation": "Carbon has unique chemical properties that allow for structural diversity. It has 4 electrons in its valence orbital, meaning it requires 4 more electrons to reach a stable octet of 8. As a result, carbon can form up to 4 covalent bonds with other elements. Unlike most other elements, carbon can bond readily with other carbon atoms, forming straight chains, branched chains, or closed ring structures. This versatile bonding capability results in a vast variety of organic compounds.",
        "questions": [
            {
                "q": "How many covalent bonds can a single carbon atom form with other atoms?",
                "opts": ["1", "2", "3", "4"],
                "a": 3,
                "exp": "Because carbon has 4 valence electrons and needs 8 for stability, it can form up to 4 covalent bonds."
            },
            {
                "q": "What structures can carbon atoms form by bonding to other carbon atoms?",
                "opts": [
                    "Only straight lines",
                    "Only rings",
                    "Straight chains, branched chains, or rings",
                    "Only crystal lattices like table salt"
                ],
                "a": 2,
                "exp": "Carbon's unique bonding allows it to link with other carbon atoms to form straight chains, branched chains, or rings."
            }
        ]
    }
}

for page, data in pages_data.items():
    file_path = os.path.join(dest_dir, f"page_{page}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

print("Saved pages 26 to 40 successfully.")
