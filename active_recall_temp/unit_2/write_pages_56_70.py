import json
import os

dest_dir = r"C:\Users\elieu\OneDrive\Desktop\biofinaltest\active_recall_temp\unit_2"
os.makedirs(dest_dir, exist_ok=True)

pages_data = {
    56: {
        "unit": 2,
        "page": 56,
        "filename": "Unit_2_2.txt",
        "section_title": "Chemistry of Organic Molecules",
        "page_num_in_file": 20,
        "slide_title": "2: Amino Acids",
        "original_text": "2: Amino Acids\u00a8Amino acids differ in the composition of their R group\u00a4Can be simple or complex\nnEx: H (glycine), CH3(alanine)\nnEx: C rings (tryptophan, phenylalanine)",
        "explanation": "Amino acids differ from one another based on the specific composition of their variable side chains, known as R groups. The R group can be structurally simple or highly complex. For example, glycine has the simplest R group, consisting of a single hydrogen (H) atom, while alanine has a methyl group (-CH3). In contrast, more complex amino acids like tryptophan and phenylalanine feature R groups containing carbon rings.",
        "questions": [
            {
                "q": "Which amino acid has the simplest R group consisting of only a single hydrogen atom?",
                "opts": ["Alanine", "Glycine", "Tryptophan", "Phenylalanine"],
                "a": 1,
                "exp": "Glycine has the simplest R group, which is a single hydrogen atom (H)."
            },
            {
                "q": "Which of the following amino acids feature carbon rings in their R groups?",
                "opts": [
                    "Glycine and Alanine",
                    "Alanine and Valine",
                    "Tryptophan and Phenylalanine",
                    "Lysine and Arginine"
                ],
                "a": 2,
                "exp": "As listed on the slide, tryptophan and phenylalanine have complex R groups that contain carbon rings."
            }
        ]
    },
    57: {
        "unit": 2,
        "page": 57,
        "filename": "Unit_2_2.txt",
        "section_title": "Chemistry of Organic Molecules",
        "page_num_in_file": 21,
        "slide_title": "2: Importance of R-Groups",
        "original_text": "2: Importance of R-Groups\u00a8Differences in R groups gives proteins different shapes/structures\u00a8Different shapes/structures allow proteins to carry out variety of activities in living things\u00a4Enzymes\u00a4Bind to and activate/deactivate DNA\u00a4Inter-and intracellular signaling\u00a4Cell structures",
        "explanation": "The differences in the chemical composition of R groups are crucial because they dictate the unique three-dimensional shapes and structures of proteins. This structural diversity, in turn, allows proteins to perform a wide variety of functions in living systems, including acting as enzymes to catalyze reactions, binding to DNA to activate or deactivate genes, mediating inter- and intracellular signaling, and serving as building blocks for cellular structures.",
        "questions": [
            {
                "q": "Why are the differences in amino acid R groups biologically important?",
                "opts": [
                    "They allow proteins to convert into carbohydrates.",
                    "They give proteins different shapes/structures, which allows them to carry out diverse cellular activities.",
                    "They determine the number of peptide bonds formed.",
                    "They make all proteins completely hydrophobic."
                ],
                "a": 1,
                "exp": "The specific chemical nature of R groups determines protein folding and structure, which enables proteins to perform specialized functions like enzymatic activity, structural support, and signaling."
            },
            {
                "q": "Which of the following is a key function of proteins mentioned on this slide?",
                "opts": [
                    "Primary storage of genetic information",
                    "Binding to and activating/deactivating DNA",
                    "Serving as the cell's main solvent",
                    "Storing energy in plant seeds"
                ],
                "a": 1,
                "exp": "One of the major protein functions listed is binding to DNA to activate or deactivate it."
            }
        ]
    },
    58: {
        "unit": 2,
        "page": 58,
        "filename": "Unit_2_2.txt",
        "section_title": "Chemistry of Organic Molecules",
        "page_num_in_file": 22,
        "slide_title": "2: Di-& Polypeptides",
        "original_text": "2: Di-& Polypeptides\u00a8Two amino acids covalently bond to form a dipeptide\u00a4Condensationreaction\u00a4Bond between amino acids known as peptide bond\u00a8Polypeptide: long chain of amino acids\u00a8Proteins often composed of one or more polypeptides\u00a4Can be very large, containing hundreds of amino acids\u00a4Often bend and foldon themselves based on interactions between R groups of amino acids\nnHydrogen bonding\nnHydrophilic/hydrophobic interactions\u00a8Protein shape also influenced by temperature, pH, solvent, salt content",
        "explanation": "Two amino acids covalently bond to form a dipeptide through a condensation reaction, with the resulting link between them called a peptide bond. A polypeptide is a long chain of amino acids, and functional proteins are composed of one or more of these chains, which can contain hundreds of amino acids. Polypeptide chains bend and fold into specific shapes based on intermolecular interactions between their R groups, such as hydrogen bonding and hydrophilic or hydrophobic interactions. Additionally, a protein's final three-dimensional shape is highly sensitive to environmental factors, including temperature, pH, the type of solvent, and salt concentration.",
        "questions": [
            {
                "q": "What is the name of the covalent bond that links amino acids together in a polypeptide?",
                "opts": ["Glycosidic bond", "Ester bond", "Peptide bond", "Phosphodiester bond"],
                "a": 2,
                "exp": "The covalent bond formed between the amino group of one amino acid and the carboxyl group of another is a peptide bond."
            },
            {
                "q": "Which environmental factors can influence the final shape of a protein?",
                "opts": [
                    "Gravity and altitude only",
                    "Temperature, pH, solvent, and salt content",
                    "Carbon dioxide concentration only",
                    "Light intensity and water pressure"
                ],
                "a": 1,
                "exp": "Protein folding and shape are influenced by environmental factors such as temperature, pH, solvent, and salt content."
            }
        ]
    },
    59: {
        "unit": 2,
        "page": 59,
        "filename": "Unit_2_2.txt",
        "section_title": "Chemistry of Organic Molecules",
        "page_num_in_file": 23,
        "slide_title": "2: Protein Structure",
        "original_text": "2: Protein Structure",
        "explanation": "This slide acts as a placeholder for a diagram detailing the hierarchical structure of proteins.",
        "questions": [
            {
                "q": "What is the subject of this slide?",
                "opts": ["Carbohydrate synthesis", "Lipid bilayer structure", "Protein structure", "DNA replication"],
                "a": 2,
                "exp": "The slide is titled '2: Protein Structure'."
            }
        ]
    },
    60: {
        "unit": 2,
        "page": 60,
        "filename": "Unit_2_2.txt",
        "section_title": "Chemistry of Organic Molecules",
        "page_num_in_file": 24,
        "slide_title": "2: Enzymes",
        "original_text": "2: Enzymes\u00a8Enzymes are a special type of protein\u00a4Biologic Catalyst\nnWork to accelerate chemical reactions\nnIn biology, many enzymes act on other proteins known as substrates. \nnCan convert these substrates into other substances, or work to signal chemical pathways within the body to turn on or off.",
        "explanation": "Enzymes are a specialized class of proteins that function as biological catalysts, acting to accelerate chemical reactions within cells. In biological systems, enzymes often bind to specific target molecules called substrates (which are frequently other proteins). The enzyme can convert these substrates into different products or act as signals that turn metabolic pathways on or off.",
        "questions": [
            {
                "q": "What is the primary function of an enzyme?",
                "opts": [
                    "To act as a structural component of cell walls.",
                    "To store genetic information.",
                    "To function as a biological catalyst that accelerates chemical reactions.",
                    "To serve as a major energy storage lipid."
                ],
                "a": 2,
                "exp": "Enzymes are specialized proteins that act as biological catalysts to speed up chemical reactions."
            },
            {
                "q": "What is the term for the molecules upon which enzymes act?",
                "opts": ["Products", "Substrates", "Catalysts", "Polypeptides"],
                "a": 1,
                "exp": "The molecules that bind to enzymes and undergo chemical transformation are known as substrates."
            }
        ]
    },
    61: {
        "unit": 2,
        "page": 61,
        "filename": "Unit_2_2.txt",
        "section_title": "Chemistry of Organic Molecules",
        "page_num_in_file": 25,
        "slide_title": "3: Lipids",
        "original_text": "3: Lipids\u00a8Lipids: large, nonpolarorganic molecules\u00a4Do not dissolve in water\u00a8Includes:\u00a4Triglycerides\u00a4Phospholipids\u00a4Steroids\u00a4Waxes\u00a4Pigments\u00a8Have higher ratio of carbon & hydrogen to oxygen atoms than carbohydrates\u00a4Higher number of C-H bonds per gram than other organic compounds ; store more energy",
        "explanation": "Lipids are large, nonpolar organic molecules that are hydrophobic and do not dissolve in water. This class of macromolecules includes triglycerides, phospholipids, steroids, waxes, and pigments. Structurally, lipids possess a higher ratio of carbon and hydrogen atoms to oxygen atoms compared to carbohydrates. Because they have a higher number of energy-rich C-H bonds per gram than other organic compounds, lipids are highly efficient at storing energy.",
        "questions": [
            {
                "q": "Why are lipids insoluble in water?",
                "opts": [
                    "They are polar molecules.",
                    "They are large and nonpolar.",
                    "They contain too many oxygen atoms.",
                    "They are composed entirely of simple sugars."
                ],
                "a": 1,
                "exp": "Water is a polar solvent, and because lipids are large, nonpolar organic molecules, they do not dissolve in water ('like dissolves like')."
            },
            {
                "q": "Why do lipids store more energy per gram than carbohydrates?",
                "opts": [
                    "They have more double covalent bonds between oxygens.",
                    "They contain a higher number of energy-rich C-H bonds per gram.",
                    "They dissolve easily in water.",
                    "They are composed of amino acid monomers."
                ],
                "a": 1,
                "exp": "Lipids have a higher ratio of carbon and hydrogen to oxygen, giving them more C-H bonds per gram than other compounds, allowing them to store more energy."
            }
        ]
    },
    62: {
        "unit": 2,
        "page": 62,
        "filename": "Unit_2_2.txt",
        "section_title": "Chemistry of Organic Molecules",
        "page_num_in_file": 26,
        "slide_title": "3: Fatty Acids",
        "original_text": "3: Fatty Acids\u00a8Fatty acids: unbranched carbon chains with a carboxyl group that make up most lipids\u00a4Carboxyl end of molecule is polar(hydrophilic) and attracted to water molecules\u00a4Hydrocarbon end of molecule is nonpolar(hydrophobic) and repels water molecules\u00a8When carbon is bonded to 4atoms, it is “saturated”\u00a8When carbon forms double bonds within the chain, it is bonded to less than 4 atoms, and is “unsaturated”",
        "explanation": "Fatty acids are long, unbranched carbon chains terminated by a carboxyl group, and they serve as the building blocks for most lipids. Fatty acids are amphipathic: the carboxyl end is polar and hydrophilic (attracted to water), while the long hydrocarbon chain end is nonpolar and hydrophobic (repelling water). A fatty acid is classified as saturated when every carbon atom in the chain is bonded to four other atoms (containing only single bonds). It is classified as unsaturated when double bonds form between carbon atoms in the chain, meaning those carbons are bonded to fewer than four atoms.",
        "questions": [
            {
                "q": "Which part of a fatty acid molecule is polar and hydrophilic?",
                "opts": [
                    "The hydrocarbon chain end",
                    "The carboxyl group end",
                    "The glycerol backbone",
                    "The nitrogenous base"
                ],
                "a": 1,
                "exp": "The carboxyl group end of a fatty acid is polar and attracted to water (hydrophilic), whereas the hydrocarbon chain is nonpolar and hydrophobic."
            },
            {
                "q": "What is the difference between a saturated and an unsaturated fatty acid?",
                "opts": [
                    "Saturated fatty acids contain double bonds, while unsaturated fatty acids contain only single bonds.",
                    "Saturated fatty acids have carbons bonded to the maximum of 4 atoms, while unsaturated fatty acids contain carbon-carbon double bonds.",
                    "Saturated fatty acids dissolve in water, while unsaturated fatty acids do not.",
                    "Unsaturated fatty acids have a carboxyl group, while saturated fatty acids do not."
                ],
                "a": 1,
                "exp": "Saturated fatty acids have no double bonds, so each carbon is bonded to 4 atoms (saturated with hydrogen). Unsaturated fatty acids contain one or more carbon-carbon double bonds, meaning some carbons bond to fewer than 4 atoms."
            }
        ]
    },
    63: {
        "unit": 2,
        "page": 63,
        "filename": "Unit_2_2.txt",
        "section_title": "Chemistry of Organic Molecules",
        "page_num_in_file": 27,
        "slide_title": "3: Fatty Acids",
        "original_text": "3: Fatty AcidsCarboxyl group is the hydrophilic end of the molecule\nLook at the chemical formula for each of the molecules to the left. What do you notice about the formulas compared to carbohydrates?",
        "explanation": "This slide notes that the carboxyl group is the hydrophilic end of a fatty acid molecule and prompts students to compare their chemical formulas to carbohydrates. Visually, fatty acid formulas show a much higher proportion of carbon and hydrogen relative to oxygen, unlike carbohydrates which follow a strict 1C:2H:1O ratio.",
        "questions": [
            {
                "q": "How does the chemical formula of a fatty acid compare to that of a carbohydrate?",
                "opts": [
                    "Fatty acids have a 1:2:1 ratio of C:H:O.",
                    "Fatty acids contain a much higher proportion of carbon and hydrogen relative to oxygen than carbohydrates.",
                    "Fatty acids do not contain carbon.",
                    "Fatty acids have more oxygen atoms than carbon atoms."
                ],
                "a": 1,
                "exp": "Lipids/fatty acids contain mostly carbon and hydrogen with very few oxygen atoms, whereas carbohydrates have a strict 1C:2H:1O ratio."
            }
        ]
    },
    64: {
        "unit": 2,
        "page": 64,
        "filename": "Unit_2_2.txt",
        "section_title": "Chemistry of Organic Molecules",
        "page_num_in_file": 28,
        "slide_title": "3: Triglycerides",
        "original_text": "3: Triglycerides\u00a8Triglyceride: composed of 3 molecules of fatty acid joined to 1 molecule of the alcohol, glycerol\u00a4Saturated triglycerides contain saturated fatty acids \nnHave high melting points; tend to be solidat room temperature\nnEx: butter, fat found in meat\u00a4Unsaturated triglycerides contain unsaturated fatty acids \nnUsually soft or liquid at room temperature\nnFound primarily in plant seeds where they serve as energy/C source for germinating plant\nnEx: olive, corn oil",
        "explanation": "A triglyceride is a lipid molecule composed of three fatty acids chemically joined to a single molecule of the alcohol glycerol. Saturated triglycerides are made of saturated fatty acids, which pack tightly together, giving them high melting points and making them solid at room temperature (examples include butter and animal fats). Unsaturated triglycerides are made of unsaturated fatty acids, whose double bonds create kinks that prevent tight packing, keeping them liquid or soft at room temperature. These are found primarily in plant seeds where they serve as an energy and carbon source for germinating plants (examples include olive oil and corn oil).",
        "questions": [
            {
                "q": "What are the components of a triglyceride molecule?",
                "opts": [
                    "3 glycerols and 1 fatty acid",
                    "1 glycerol and 3 fatty acids",
                    "3 simple sugars and 1 phosphate group",
                    "1 amino acid and 2 fatty acids"
                ],
                "a": 1,
                "exp": "A triglyceride is composed of 3 fatty acid molecules bound to 1 glycerol molecule."
            },
            {
                "q": "Why are saturated triglycerides, like butter and animal fat, solid at room temperature while unsaturated triglycerides are liquid?",
                "opts": [
                    "Saturated triglycerides have lower melting points.",
                    "Saturated triglycerides have only single bonds in their fatty acid chains, allowing them to pack closely together and remain solid at higher temperatures.",
                    "Unsaturated triglycerides contain heavy metal ions.",
                    "Unsaturated triglycerides lack a glycerol backbone."
                ],
                "a": 1,
                "exp": "Saturated fatty acids are straight chains that pack together tightly, resulting in higher melting points and solid states at room temperature. Unsaturated chains have kinks from double bonds that prevent tight packing, keeping them liquid."
            }
        ]
    },
    65: {
        "unit": 2,
        "page": 65,
        "filename": "Unit_2_2.txt",
        "section_title": "Chemistry of Organic Molecules",
        "page_num_in_file": 29,
        "slide_title": "3: Saturated vs. Unsaturated Triglycerides",
        "original_text": "3: Saturated vs. Unsaturated Triglycerides",
        "explanation": "This slide serves as a visual layout showing the structural differences between saturated and unsaturated triglycerides.",
        "questions": [
            {
                "q": "What comparison is displayed on this slide?",
                "opts": [
                    "Hydrolysis vs Condensation",
                    "Saturated vs Unsaturated Triglycerides",
                    "DNA vs RNA structures",
                    "Acids vs Bases"
                ],
                "a": 1,
                "exp": "The slide title is '3: Saturated vs. Unsaturated Triglycerides'."
            }
        ]
    },
    66: {
        "unit": 2,
        "page": 66,
        "filename": "Unit_2_2.txt",
        "section_title": "Chemistry of Organic Molecules",
        "page_num_in_file": 30,
        "slide_title": "3: Phospholipids",
        "original_text": "3: Phospholipids\u00a8Phospholipids: 1 molecule of glycerolattached to 2 fatty acids and one phosphategroup\u00a4Hydrophilic “head”: glycerol/phosphateendof molecule\u00a4Hydrophobic “tail”: carbonchain\u00a8Cell membranes composed of 2 layers of phospholipids\u00a4Known as lipid bilayer\u00a4Hydrophobic nature of lipids allow them to serve as barrier between inside & outside of cell\nnBoth of which aqueous solutions",
        "explanation": "Phospholipids are structural lipids composed of a single glycerol molecule attached to two fatty acid chains and one phosphate group. This structure results in an amphipathic molecule: a hydrophilic head made of the polar glycerol and phosphate group, and two hydrophobic tails made of nonpolar fatty acid carbon chains. Cell membranes are constructed from two layers of these molecules, forming a phospholipid bilayer. The hydrophobic tails point inward, away from water, allowing the bilayer to act as an effective barrier separating the aqueous intracellular fluid from the aqueous extracellular fluid.",
        "questions": [
            {
                "q": "Describe the structure of a phospholipid.",
                "opts": [
                    "1 glycerol, 3 fatty acids, and 1 amino acid",
                    "1 glycerol, 2 fatty acids, and 1 phosphate group",
                    "1 glucose, 2 phosphates, and 1 nitrogenous base",
                    "2 glycerols and 2 fatty acids"
                ],
                "a": 1,
                "exp": "A phospholipid is composed of 1 glycerol molecule, 2 fatty acid chains, and 1 phosphate group."
            },
            {
                "q": "How does the structure of a phospholipid bilayer allow it to function as a cell membrane barrier?",
                "opts": [
                    "The hydrophilic tails face inward to block all water.",
                    "The hydrophobic tails point inward, creating a nonpolar barrier that separates the aqueous environments inside and outside the cell.",
                    "It dissolves completely in the surrounding aqueous solutions.",
                    "It forms covalent bonds with external proteins to seal the cell."
                ],
                "a": 1,
                "exp": "The hydrophobic tails pack together on the interior of the membrane, creating a barrier that is impermeable to most polar/aqueous substances, separating the cell's interior from the outside environment."
            }
        ]
    },
    67: {
        "unit": 2,
        "page": 67,
        "filename": "Unit_2_2.txt",
        "section_title": "Chemistry of Organic Molecules",
        "page_num_in_file": 31,
        "slide_title": "3: Phospholipids",
        "original_text": "3: Phospholipids",
        "explanation": "This slide serves as a visual placeholder for the diagram showing the structure of a phospholipid and the cell membrane bilayer.",
        "questions": [
            {
                "q": "What structural component is illustrated on this page?",
                "opts": ["A triglyceride", "A phospholipid bilayer", "A polysaccharide", "A polypeptide chain"],
                "a": 1,
                "exp": "The slide is titled '3: Phospholipids', which illustrates phospholipid and cell membrane structure."
            }
        ]
    },
    68: {
        "unit": 2,
        "page": 68,
        "filename": "Unit_2_2.txt",
        "section_title": "Chemistry of Organic Molecules",
        "page_num_in_file": 32,
        "slide_title": "3: Waxes",
        "original_text": "3: Waxes\u00a8Wax: type of structural lipid with a long fatty acid chainjoined to long alcohol chain\u00a4Waterproof\u00a8Plants use waxes as an outer coating for protection of leaves\u00a8Earwax prevents microorganisms from entering the ear canal",
        "explanation": "Waxes are a type of structural lipid composed of a long fatty acid chain joined to a long alcohol chain. Waxes are highly waterproof, which makes them useful for protective barriers in organisms. For example, plants secrete a waxy cuticle as an outer coating on their leaves to prevent water loss and offer protection, while animals produce earwax to trap and prevent microorganisms from entering the ear canal.",
        "questions": [
            {
                "q": "What are the chemical components that make up a wax molecule?",
                "opts": [
                    "A glycerol molecule and three fatty acids",
                    "A long fatty acid chain joined to a long alcohol chain",
                    "Four fused carbon rings",
                    "A phosphate group, ribose, and nitrogenous base"
                ],
                "a": 1,
                "exp": "Waxes are structurally defined by having a long fatty acid chain linked to a long alcohol chain."
            },
            {
                "q": "What is the primary physical property of waxes that makes them useful for leaves and ear canals?",
                "opts": ["They are highly soluble in water.", "They are waterproof (hydrophobic).", "They are gaseous at room temperature.", "They act as chemical catalysts."],
                "a": 1,
                "exp": "Waxes are waterproof, allowing them to prevent water loss in plants and block microorganisms in animal ear canals."
            }
        ]
    },
    69: {
        "unit": 2,
        "page": 69,
        "filename": "Unit_2_2.txt",
        "section_title": "Chemistry of Organic Molecules",
        "page_num_in_file": 33,
        "slide_title": "3: Steroids",
        "original_text": "3: Steroids\u00a8Steroid: molecules composed of 4 fused carbon rings with various functional groupsattached\u00a8Many animal hormonesare steroids\u00a4Testosterone, growth hormones\u00a8Cholesterolis a steroid\u00a4Necessary for nerve and other cells to function properly\u00a4Component of the cell                                       membrane\nnMaintains fluidity of the                                          membrane",
        "explanation": "Steroids are lipid molecules composed of four fused carbon rings with various functional groups attached. Unlike other lipids, they do not contain fatty acid chains. Many animal hormones are steroids, including testosterone and growth hormones. Cholesterol is also a steroid and is essential for the proper functioning of nerve and other cells. It is also an important component of animal cell membranes, where it helps maintain membrane fluidity.",
        "questions": [
            {
                "q": "What is the unique structural characteristic of a steroid?",
                "opts": [
                    "A glycerol backbone with three fatty acid tails.",
                    "A long fatty acid chain linked to a long alcohol chain.",
                    "Four fused carbon rings with attached functional groups.",
                    "A double helix of nucleotides."
                ],
                "a": 2,
                "exp": "Steroids are defined structurally by having four fused carbon rings rather than fatty acid chains."
            },
            {
                "q": "What is the function of cholesterol in the cell membrane?",
                "opts": [
                    "It acts as an enzyme to speed up reactions.",
                    "It forms a channel to transport water.",
                    "It helps maintain membrane fluidity.",
                    "It binds to DNA to turn off genes."
                ],
                "a": 2,
                "exp": "Cholesterol resides within the cell membrane and functions to maintain membrane fluidity."
            }
        ]
    },
    70: {
        "unit": 2,
        "page": 70,
        "filename": "Unit_2_2.txt",
        "section_title": "Chemistry of Organic Molecules",
        "page_num_in_file": 34,
        "slide_title": "4: Nucleic Acids",
        "original_text": "4: Nucleic Acids\u00a8Nucleic acid: very large, complex organic molecules that store and transfer important information in the cell\u00a4Deoxyribonucleic acid (DNA)\u00a4Ribonucleic acid (RNA)\u00a8DNA contains information that determines characteristics of an organism and directs cellular activities\u00a8RNA stores and transfers information from DNA that is essential for manufacturing proteins\u00a4Can also act as enzymes (ribozymes)\u00a8Polymers composed of thousands of linked monomers known as nucleotides\u00a4Linked by phosphodiesterbond\u00a43 main components of nucleotide: phosphate group, 5-carbon sugar, ring-shaped nitrogenous base",
        "explanation": "Nucleic acids are large, complex organic macromolecules that store and transfer essential information within cells. The two primary types are deoxyribonucleic acid (DNA) and ribonucleic acid (RNA). DNA holds the genetic instructions that determine an organism's traits and direct cellular processes. RNA's primary role is to store and transfer instructions from DNA to guide the synthesis of proteins, and some RNA molecules can also act as catalysts (known as ribozymes). Nucleic acids are polymers composed of thousands of linked nucleotide monomers connected by phosphodiester bonds. Each nucleotide consists of three components: a phosphate group, a 5-carbon sugar, and a ring-shaped nitrogenous base.",
        "questions": [
            {
                "q": "What are the three components of a nucleotide monomer?",
                "opts": [
                    "Glycerol, fatty acid, and phosphate group",
                    "Amino group, carboxyl group, and R group",
                    "Phosphate group, 5-carbon sugar, and nitrogenous base",
                    "Ribose sugar, adenine, and three phosphates"
                ],
                "a": 2,
                "exp": "A nucleotide consists of a phosphate group, a 5-carbon sugar (ribose or deoxyribose), and a nitrogenous base."
            },
            {
                "q": "What is the function of RNA in the cell?",
                "opts": [
                    "It forms a waterproof barrier on the cell membrane.",
                    "It stores and transfers genetic information from DNA to direct protein synthesis, and can act as an enzyme.",
                    "It serves as a high-energy storage molecule like glycogen.",
                    "It is the main structural component of hair and nails."
                ],
                "a": 1,
                "exp": "RNA is responsible for storing and transferring information from DNA that is essential for making proteins, and it can also exhibit catalytic activity as a ribozyme."
            }
        ]
    }
}

for page, data in pages_data.items():
    file_path = os.path.join(dest_dir, f"page_{page}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

print("Saved pages 56 to 70 successfully.")
