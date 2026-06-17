import json
import os

dest_dir = r"C:\Users\elieu\OneDrive\Desktop\biofinaltest\active_recall_temp\unit_2"
os.makedirs(dest_dir, exist_ok=True)

pages_data = {
    131: {
        "unit": 2,
        "page": 131,
        "filename": "Unit_2_5.txt",
        "section_title": "Enzymes",
        "page_num_in_file": 9,
        "slide_title": "Enzymes",
        "original_text": "Enzymes\u00a8An enzyme\u00a5is very selective in the reaction it catalyzes and\u00a5has a shape that determines the enzyme’s specificity.\u00a8The specific reactant that an enzyme acts on is called the enzyme’s substrate.\u00a8A substrate fits into a region of the enzyme called the active site.\u00a8Enzymes are specific because only specific substrate molecules fit into their active site.",
        "explanation": "Enzymes are highly selective catalysts, meaning each enzyme typically catalyzes only one specific chemical reaction. An enzyme's unique three-dimensional shape determines its specificity. The specific reactant molecule that an enzyme binds to and acts upon is called the substrate. The substrate binds to a pocket or groove on the enzyme known as the active site. Because the structural shape of the active site is complementary only to specific substrate molecules, enzymes exhibit high specificity.",
        "questions": [
            {
                "q": "What is the term for the specific reactant molecule that an enzyme acts upon?",
                "opts": ["Product", "Substrate", "Inhibitor", "Cofactor"],
                "a": 1,
                "exp": "The substrate is the specific reactant molecule that binds to the enzyme and undergoes a chemical reaction."
            },
            {
                "q": "What region of an enzyme does the substrate bind to?",
                "opts": ["The allosteric site", "The phosphate group", "The active site", "The R group"],
                "a": 2,
                "exp": "The substrate fits into a specialized pocket or groove on the enzyme called the active site."
            }
        ]
    },
    132: {
        "unit": 2,
        "page": 132,
        "filename": "Unit_2_5.txt",
        "section_title": "Enzymes",
        "page_num_in_file": 10,
        "slide_title": "Glucose",
        "original_text": "Glucose\nFructose\nThe productsare releasedThe substrateis convertedto products\nH2O\nEnzyme(sucrase)\nSubstratebinds toenzyme withinduced fit.\nSubstrate(sucrose)Active siteThe enzyme availablewith an empty active site\n1. Active site is empty.\n2. Sucrose binds with induced fit.\n3. Water is added, converting substrate to glucose and fructose products.\n4. Products are released.",
        "explanation": "This slide details the catalytic cycle of the enzyme sucrase. In step 1, the sucrase enzyme is available with an empty active site. In step 2, the substrate sucrose binds to the active site with an induced fit, where the enzyme hugs the substrate slightly to bind it tightly. In step 3, a water molecule is added (hydrolysis), converting the substrate into the products glucose and fructose. In step 4, these products are released, leaving the enzyme unchanged and free to receive another substrate molecule.",
        "questions": [
            {
                "q": "In the catalytic cycle of sucrase, what are the products released after sucrose is hydrolyzed?",
                "opts": [
                    "Starch and Glycogen",
                    "Glucose and Fructose",
                    "Lactose and Galactose",
                    "Carbon dioxide and Water"
                ],
                "a": 1,
                "exp": "Sucrase catalyzes the hydrolysis of sucrose into its component monosaccharides, glucose and fructose."
            },
            {
                "q": "What is 'induced fit' in enzyme-substrate binding?",
                "opts": [
                    "The permanent denaturation of the enzyme.",
                    "The slight change in shape of the enzyme's active site so that it binds the substrate more snugly.",
                    "The chemical breakdown of the enzyme's peptide bonds.",
                    "The binding of a competitive inhibitor to the active site."
                ],
                "a": 1,
                "exp": "Induced fit is the dynamic interaction where the enzyme's active site changes shape slightly upon substrate binding to establish a snugger fit."
            }
        ]
    },
    133: {
        "unit": 2,
        "page": 133,
        "filename": "Unit_2_5.txt",
        "section_title": "Enzymes",
        "page_num_in_file": 11,
        "slide_title": "Enzymes",
        "original_text": "Enzymes\u00a8For every enzyme, there are optimal conditions under which it is most effective.\u00a8Temperature affects molecular motion.\u00a5An enzyme’s optimal temperature produces the highest rate of contact between the reactants and the enzyme’s active site.\u00a5Most human enzymes work best at 35–40°C.\u00a8The optimal pH for most enzymes is near neutrality.",
        "explanation": "Each enzyme has evolved to function best under specific optimal environmental conditions. Temperature influences molecular motion; as temperature increases, molecules move faster, increasing collisions. An enzyme's optimal temperature is the point at which the rate of contact between substrate molecules and the active site is maximized without causing the enzyme protein to denature. For most human enzymes, this optimal temperature ranges between 35°C and 40°C (close to normal body temperature). Additionally, the optimal pH for most biological enzymes is near neutrality (pH 7).",
        "questions": [
            {
                "q": "What is the optimal temperature range for most human enzymes?",
                "opts": ["0–10°C", "20–25°C", "35–40°C", "70–80°C"],
                "a": 2,
                "exp": "Most human enzymes function optimally between 35°C and 40°C, close to human body temperature (37°C)."
            },
            {
                "q": "What is the optimal pH environment for the majority of cellular enzymes?",
                "opts": ["Highly acidic (pH 1–2)", "Near neutrality (pH 7)", "Highly alkaline (pH 12–14)", "Fluctuating between pH 2 and 12"],
                "a": 1,
                "exp": "Most enzymes function best in a neutral pH environment near neutrality, though there are specific exceptions like digestive stomach enzymes."
            }
        ]
    },
    134: {
        "unit": 2,
        "page": 134,
        "filename": "Unit_2_5.txt",
        "section_title": "Enzymes",
        "page_num_in_file": 12,
        "slide_title": "Enzymes",
        "original_text": "Enzymes\u00a8Many enzymes require nonprotein helpers called cofactors, which\u00a5bind to the active site and\u00a5function in catalysis.\u00a8Some cofactors are inorganic, such as the ions of zinc, iron, or copper.\u00a8If a cofactor is an organic molecule, such as most vitamins, it is called a coenzyme.\u00a5Acetyl CoA, CoQ10\u00a5Enzymes and coenzymes/cofactors work together to signal processes to start, run, and end throughout biological systems",
        "explanation": "To perform catalysis, many enzymes require nonprotein helpers known as cofactors. Cofactors bind to the enzyme's active site and participate directly in the catalytic process. Inorganic cofactors include metallic ions such as zinc, iron, or copper. If the cofactor is an organic molecule, it is specifically termed a coenzyme; examples include most vitamins, Acetyl CoA, and CoQ10. Enzymes, cofactors, and coenzymes work in concert to coordinate and signal metabolic pathways to start, run, and terminate throughout biological systems.",
        "questions": [
            {
                "q": "What is a coenzyme?",
                "opts": [
                    "An inorganic helper ion like zinc or copper.",
                    "An organic cofactor, such as a vitamin, that helps enzymes function.",
                    "A protein that binds to DNA to block transcription.",
                    "A specialized carbohydrate chain on the cell membrane."
                ],
                "a": 1,
                "exp": "An organic cofactor is called a coenzyme. Many vitamins, Acetyl CoA, and CoQ10 function as coenzymes."
            },
            {
                "q": "Which of the following are examples of inorganic cofactors?",
                "opts": [
                    "Vitamins and Acetyl CoA",
                    "Ions of zinc, iron, or copper",
                    "Glucose and Galactose",
                    "Amino acids and Lipids"
                ],
                "a": 1,
                "exp": "Inorganic cofactors are typically metal ions, such as those of zinc, iron, or copper."
            }
        ]
    },
    135: {
        "unit": 2,
        "page": 135,
        "filename": "Unit_2_5.txt",
        "section_title": "Enzymes",
        "page_num_in_file": 13,
        "slide_title": "Enzymes",
        "original_text": "Enzymes\u00a8A chemical that interferes with an enzyme’s activity is called an inhibitor.\u00a8Competitive inhibitors\u00a5block substrates from entering the active site and\u00a5reduce an enzyme’s productivity.\u00a8Noncompetitive inhibitors\u00a5bind to the enzyme somewhere other than the active site, \u00a5change the shape of the active site, and\u00a5prevent the substrate from binding.",
        "explanation": "An inhibitor is any chemical compound that interferes with an enzyme's catalytic activity. Inhibitors are classified based on their mechanism of action. Competitive inhibitors mimic the substrate and bind directly to the active site, physically blocking the substrate from entering and thereby reducing the rate of reaction. Noncompetitive inhibitors bind to the enzyme at an allosteric site (a location other than the active site). This binding induces a conformational change in the enzyme's structure, which alters the shape of the active site so that the substrate can no longer bind.",
        "questions": [
            {
                "q": "How does a competitive inhibitor reduce an enzyme's productivity?",
                "opts": [
                    "By binding to an allosteric site and changing the enzyme's shape.",
                    "By physically blocking the substrate from entering the active site.",
                    "By destroying the substrate molecules.",
                    "By hydrolyzing the enzyme's peptide bonds."
                ],
                "a": 1,
                "exp": "Competitive inhibitors compete with the substrate for binding to the active site, blocking substrate entry."
            },
            {
                "q": "What is the mechanism of a noncompetitive inhibitor?",
                "opts": [
                    "It binds to the active site and covalently locks it.",
                    "It binds to a site other than the active site, changing the active site's shape so the substrate cannot bind.",
                    "It converts the substrate into a toxic product.",
                    "It increases the rate of reaction by lowering activation energy."
                ],
                "a": 1,
                "exp": "Noncompetitive inhibitors bind elsewhere on the enzyme, causing a conformational change that alters the active site, preventing substrate binding."
            }
        ]
    },
    136: {
        "unit": 2,
        "page": 136,
        "filename": "Unit_2_5.txt",
        "section_title": "Enzymes",
        "page_num_in_file": 14,
        "slide_title": "Substrate",
        "original_text": "Substrate\nEnzyme\nActive site\nNormal binding of substrate\nCompetitive inhibitor\nNoncompetitive inhibitor\nEnzyme inhibition",
        "explanation": "This slide displays a visual comparison between normal substrate binding, competitive inhibition (where the inhibitor blocks the active site), and noncompetitive inhibition (where the inhibitor binds to another site, causing a change in the active site's shape).",
        "questions": [
            {
                "q": "Which type of inhibition is shown when a molecule blocks the substrate from docking into the active site by fitting into it directly?",
                "opts": ["Allosteric inhibition", "Noncompetitive inhibition", "Competitive inhibition", "Feedback activation"],
                "a": 2,
                "exp": "Competitive inhibition occurs when the inhibitor directly occupies the active site, preventing substrate binding."
            }
        ]
    },
    137: {
        "unit": 2,
        "page": 137,
        "filename": "Unit_2_5.txt",
        "section_title": "Enzymes",
        "page_num_in_file": 15,
        "slide_title": "Enzymes",
        "original_text": "Enzymes\u00a8Enzyme inhibitors are important in regulating cell metabolism.\u00a8In some reactions, the product may act as an inhibitor of one of the enzymes in the pathway that produced it. This is called feedback inhibition.\nFeedback inhibition: Enzyme 1 -> Reaction 1 -> Product A -> Enzyme 2 -> Reaction 2 -> Product B -> Enzyme 3 -> Reaction 3 -> Product C -> Product D inhibits Enzyme 1",
        "explanation": "Enzyme inhibitors play a critical physiological role in regulating metabolic pathways within cells. In many metabolic pathways, the final end product of the pathway acts as an inhibitor of one of the early enzymes in the sequence that produced it. This self-regulating mechanism is known as feedback inhibition. When the concentration of the end product increases, it shuts down its own synthesis pathway, preventing the cell from wasting resources.",
        "questions": [
            {
                "q": "What is feedback inhibition?",
                "opts": [
                    "When an enzyme is activated by its substrate.",
                    "When the final product of a metabolic pathway acts as an inhibitor of an enzyme early in the pathway.",
                    "When cells use heat to denature enzymes.",
                    "When white blood cells engulf pathogens."
                ],
                "a": 1,
                "exp": "Feedback inhibition is a regulatory mechanism where the end product of a pathway inhibits an upstream enzyme to stop further production."
            }
        ]
    },
    138: {
        "unit": 2,
        "page": 138,
        "filename": "Unit_2_5.txt",
        "section_title": "Enzymes",
        "page_num_in_file": 16,
        "slide_title": "Enzymes",
        "original_text": "Enzymes\u00a8Many beneficial drugs act as enzyme inhibitors, including\u00a5ibuprofen, which inhibits an enzyme involved in the production of prostaglandins (messenger molecules that increase the sensation of pain and inflammation),\u00a5some blood pressure medicines,\u00a5some antidepressants,\u00a5many antibiotics, and \u00a5protease inhibitors used to fight HIV.\u00a8Enzyme inhibitors have also been developed as \u00a5pesticides and \u00a5deadly poisons for chemical warfare.",
        "explanation": "Many beneficial pharmaceutical drugs exploit enzyme inhibition to treat medical conditions. For example, ibuprofen acts by inhibiting an enzyme involved in synthesizing prostaglandins, which are messenger molecules that amplify pain and inflammation. Other examples of therapeutic inhibitors include blood pressure medications, antidepressants, antibiotics, and protease inhibitors used to combat HIV. However, enzyme inhibition can also have negative applications; inhibitors have been engineered as agricultural pesticides and as deadly chemical weapons.",
        "questions": [
            {
                "q": "How does ibuprofen function to reduce pain and inflammation?",
                "opts": [
                    "By destroying prostaglandins in the blood.",
                    "By inhibiting an enzyme involved in the production of prostaglandins.",
                    "By acting as a coenzyme for cellular respiration.",
                    "By binding to pain receptors in the brain."
                ],
                "a": 1,
                "exp": "Ibuprofen is an enzyme inhibitor that prevents the synthesis of prostaglandins, which are messenger molecules that signal pain and inflammation."
            },
            {
                "q": "Which of the following medical treatments does NOT rely on enzyme inhibition as described on this slide?",
                "opts": [
                    "HIV protease inhibitors",
                    "Many antibiotics",
                    "Ibuprofen",
                    "Hormone replacement therapy"
                ],
                "a": 3,
                "exp": "HIV protease inhibitors, antibiotics, and ibuprofen all act as enzyme inhibitors. Hormone replacement therapy is not mentioned as acting via enzyme inhibition."
            }
        ]
    }
}

for page, data in pages_data.items():
    file_path = os.path.join(dest_dir, f"page_{page}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

print("Saved pages 131 to 138 successfully.")
