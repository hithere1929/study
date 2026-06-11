const FINAL_BLUEPRINT_CONTENT = (() => {
  const topic = (
    id,
    title,
    unit,
    lesson,
    pages,
    mustKnow,
    recall,
    commonTrap,
    examWeight,
    sectionMappings
  ) => ({
    id,
    title,
    unit,
    lessonRefs: [{ lesson, pages, source: `Notes/${lesson}.pdf` }],
    mustKnow,
    recall: recall.map(([prompt, answer]) => ({ prompt, answer })),
    commonTrap,
    examWeight,
    sectionMappings: [...new Set(sectionMappings.flatMap(mapping => {
      const exactSections = String(mapping).match(/\b[1-8]\.[1-9]\b/g) || [];
      return [mapping, ...exactSections];
    }))]
  });

  const choice = (option, title, prompt, requiredPoints, noteRefs) => ({
    option,
    title,
    prompt,
    requiredPoints,
    checklist: requiredPoints,
    noteRefs
  });

  const rubric = {
    4: "Complete, accurate, mechanism-based response addressing every required point with correct vocabulary and a justified prediction or application.",
    2: "Partly correct response that addresses some required points but omits an important mechanism, comparison, calculation, or justification.",
    0: "Missing, irrelevant, or biologically incorrect response that does not demonstrate the required understanding."
  };

  const part1 = {
    id: "part1",
    label: "Part 1: General Knowledge",
    title: "Part 1: General Knowledge",
    format: "20 Multiple Choice",
    questionCount: 20,
    units: [1, 2, 3, 4, 5, 6, 7, 8],
    purpose: "Broad cumulative sampling from Units 1-8 using the existing active recall banks as the learning source.",
    breadthGuidance: [
      "Expect broad recognition and application rather than deep coverage of every lesson.",
      "Cycle through every unit; do not spend all review time on the heavily weighted later parts.",
      "Use unit active recall explanations to correct errors, then answer the same idea without choices.",
      "Prioritize definitions, structure-function relationships, process order, variables, data interpretation, and common comparisons."
    ],
    unitMappings: [
      { unit: 1, title: "Foundations of Biology", lessons: ["1.1 Lab Safety", "1.2 Intro to Biology", "1.3 The Process of Science", "1.4 Microscopy", "1.5 Biotechnology and Bioethics"], activeRecall: "unit1_active_recall.json", pages: "1-76", focus: "Safety, characteristics of life, experimental design, microscopy, bioethics." },
      { unit: 2, title: "Chemistry and Cells", lessons: ["2.1 Chemistry of Living Things", "2.2 Chemistry of Organic Molecules", "2.3 Movement of Molecules", "2.4 Metabolism", "2.5 Enzymes"], activeRecall: "unit2_active_recall.json", pages: "1-138", focus: "Water and bonds, macromolecules, membranes and transport, energy, enzymes." },
      { unit: 3, title: "Cells", lessons: ["3.1 Cell Biology", "3.2 Organelles", "3.3 Chromosomes", "3.4 The Cell Cycle", "3.5 Stem Cells and Cancer"], activeRecall: "unit3_active_recall.json", pages: "1-113", focus: "Cell theory, cell types, organelles, chromosomes, mitosis, cancer." },
      { unit: 4, title: "Genetics and Heredity", lessons: ["4.1 DNA Advances", "4.2 DNA Structure", "4.3 DNA Replication Transcription Translation", "4.4 Gene Expression", "4.5 Biotech and Genomics", "4.6 Meiosis", "4.7 Chromosome Syndromes", "4.8 Mendelian Genetics", "4.9 Genetic Disorders"], activeRecall: "unit4_active_recall.json", pages: "1-217", focus: "Molecular genetics, regulation, biotechnology, meiosis, inheritance." },
      { unit: 5, title: "Evolution", lessons: ["5.1 Darwin and Evidence", "5.2 Population Evolution", "5.3 Speciation and Macroevolution", "5.4 Taxonomy and Systematics"], activeRecall: "unit5_active_recall.json", pages: "1-84", focus: "Evolution evidence, Hardy-Weinberg, evolutionary forces, speciation, classification." },
      { unit: 6, title: "Diversity of Life", lessons: ["6.1 Viruses", "6.2 Prokaryotes", "6.3 Protists", "6.4 Fungi", "6.5 Plant Diversity", "6.6 Invertebrates", "6.7 Vertebrates"], activeRecall: "unit6_active_recall.json", pages: "1-92", focus: "Domains, kingdoms, pathogens, diversity, diagnostic traits." },
      { unit: 7, title: "Organism Structure and Function", lessons: ["7.1 Plant Structure", "7.2 Plant Transport", "7.3 Plant Responses", "7.4 Plant Reproduction", "7.5 Animal Organization", "7.6 Circulation", "7.7 Respiration", "7.8 Nervous System", "7.9 Sense Organs"], activeRecall: "unit7_active_recall.json", pages: "1-175", focus: "Plant and animal structure-function, transport, control, and homeostasis." },
      { unit: 8, title: "Behavior, Ecology, and Energy", lessons: ["8.1 Behavioral Ecology", "8.2 Population Ecology", "8.3 Community and Ecosystem Ecology", "8.4 Photosynthesis", "8.5 Cellular Respiration", "8.6 Major Ecosystems", "8.7 Conservation"], activeRecall: "unit8_active_recall.json", pages: "1-130", focus: "Behavior, ecology, energy flow, metabolism, biomes, conservation." }
    ],
    sectionMappings: ["unit1_active_recall.json", "unit2_active_recall.json", "unit3_active_recall.json", "unit4_active_recall.json", "unit5_active_recall.json", "unit6_active_recall.json", "unit7_active_recall.json", "unit8_active_recall.json"]
  };

  const part2Topics = [
    topic("p2-cell-theory", "Cell Theory", 3, "Unit 3.1 - Cell Biology", "5-6", [
      "All organisms contain one or more cells; the cell is the basic unit of structure and function; cells arise from existing cells.",
      "Hooke named cork compartments; Leeuwenhoek first observed living cells; Schleiden, Schwann, and Virchow completed the theory."
    ], [["State the three tenets of cell theory.", "Organisms are made of cells, cells are the basic unit, and cells come from preexisting cells."]], "Cell theory does not say every cell has a nucleus; prokaryotes do not.", "medium", ["Unit 3.1", "Part 2 section 3.2"]),

    topic("p2-sa-volume", "Surface Area to Volume", 3, "Unit 3.1 - Cell Biology", "9-10", [
      "Surface area scales with length squared while volume scales with length cubed, so SA:V falls as size rises.",
      "Low SA:V limits exchange of nutrients, gases, heat, and wastes; folds, microvilli, small size, and internal membranes increase effective area."
    ], [["Why are small cells efficient exchangers?", "They have more membrane surface per unit of metabolically active volume."]], "A tenfold increase in diameter gives 100 times the surface area but 1000 times the volume.", "high", ["Unit 3.1", "Part 2 section 3.2"]),

    topic("p2-pro-euk", "Prokaryotes and Eukaryotes", 3, "Unit 3.1 - Cell Biology", "13-16", [
      "Both have DNA, ribosomes, cytoplasm, and a plasma membrane.",
      "Prokaryotes lack a membrane-bound nucleus and organelles; eukaryotes compartmentalize functions in membrane-bound organelles."
    ], [["Name the two prokaryotic domains.", "Bacteria and Archaea."]], "Prokaryotes are not organelle-free: they have ribosomes, membranes, and organized internal regions.", "high", ["Unit 3.1", "Unit 6.2", "Part 2 sections 3.3 and 6.2"]),

    topic("p2-endosymbiosis", "Endosymbiotic Theory", 3, "Unit 3.2 - Organelles", "57-60", [
      "Mitochondria and chloroplasts likely descended from engulfed bacteria in a mutually beneficial relationship.",
      "Evidence includes double membranes, circular DNA, bacterial-sized 70S ribosomes, binary fission, and gene transfer to the nucleus."
    ], [["Which organelles are explained by endosymbiosis?", "Mitochondria and chloroplasts."]], "The host did not create these organelles from its endomembrane system.", "high", ["Unit 3.2", "Part 2 section 3.3"]),

    topic("p2-animal-structures", "Animal Cell Structures", 3, "Unit 3.2 - Organelles", "17-56", [
      "Nucleus stores DNA; ribosomes translate; RER makes secreted/membrane proteins; SER makes lipids and detoxifies.",
      "Golgi modifies and sorts; lysosomes digest; peroxisomes oxidize; mitochondria make ATP; cytoskeleton organizes transport and movement."
    ], [["Trace a secreted protein.", "Nucleus to ribosome/RER to transport vesicle to Golgi to secretory vesicle to plasma membrane."]], "Free ribosomes mainly make cytosolic proteins; bound ribosomes make secreted, lysosomal, and membrane proteins.", "high", ["Unit 3.2", "Part 2 section 3.3"]),

    topic("p2-plant-animal", "Plant and Animal Cells", 3, "Unit 3.2 - Organelles", "17-60", [
      "Both are eukaryotic and share nucleus, mitochondria, ER, Golgi, ribosomes, cytoskeleton, and plasma membrane.",
      "Plant cells add cellulose walls, chloroplasts, a large central vacuole, and plasmodesmata; animal cells commonly emphasize lysosomes and centrioles."
    ], [["What prevents a plant cell from bursting in hypotonic solution?", "The rigid cell wall resists expansion while turgor pressure builds."]], "Plant cells also perform cellular respiration and contain mitochondria.", "medium", ["Unit 3.2", "Part 2 sections 2.5 and 3.3"]),

    topic("p2-chromosome", "Chromosome Structure", 3, "Unit 3.3 - Chromosomes", "61-74", [
      "DNA wraps around histones to form nucleosomes and chromatin; replicated chromosomes contain sister chromatids joined at a centromere.",
      "Kinetochores attach spindle fibers; telomeres protect chromosome ends; homologs carry the same genes but may carry different alleles."
    ], [["Differentiate homologs and sister chromatids.", "Homologs are maternal and paternal versions of a chromosome; sister chromatids are replicated copies of one chromosome."]], "Chromosome number is counted by centromeres, not chromatids.", "high", ["Unit 3.3", "Part 2 sections 3.4 and 3.5"]),

    topic("p2-cell-cycle", "Cell Cycle", 3, "Unit 3.4 - The Cell Cycle", "75-95", [
      "Interphase includes G1 growth, S DNA replication, and G2 preparation; M phase includes mitosis and cytokinesis.",
      "G1, G2, and spindle checkpoints use cyclins/CDKs and damage signals to stop unsafe division."
    ], [["What does the spindle checkpoint verify?", "Every chromosome is attached correctly to spindle microtubules before anaphase."]], "Interphase is active growth and replication, not cellular rest.", "high", ["Unit 3.4", "Part 2 section 3.4"]),

    topic("p2-cancer", "Cancer", 3, "Unit 3.5 - Stem Cells & Cancer", "102-112", [
      "Cancer is uncontrolled division caused by accumulated mutations affecting proto-oncogenes, tumor suppressors, checkpoints, DNA repair, and apoptosis.",
      "Cancer cells may lose differentiation and contact inhibition, evade apoptosis, induce angiogenesis, and metastasize."
    ], [["Compare an oncogene with a tumor suppressor.", "An oncogene acts like a stuck growth accelerator; a tumor suppressor normally applies the cell-cycle brake."]], "A tumor is not automatically malignant; malignancy includes invasion and metastatic potential.", "high", ["Unit 3.5", "Part 2 sections 3.4 and 3.5"]),

    topic("p2-dna-structure", "DNA Structure and Composition", 4, "Unit 4.2 - DNA Structure", "15-29", [
      "DNA is an antiparallel double helix of nucleotides with deoxyribose-phosphate backbones and internal nitrogenous bases.",
      "A pairs with T by two hydrogen bonds; G pairs with C by three; base sequence stores information and strand complementarity enables copying."
    ], [["Write the complement of 5'-ATGC-3'.", "3'-TACG-5'."]], "Hydrogen bonds join bases between strands; phosphodiester bonds join nucleotides within a strand.", "high", ["Unit 4.2", "Part 2 section 2.3"]),

    topic("p2-chromatin", "Euchromatin and Heterochromatin", 4, "Unit 4.4 - Gene Expression", "63-75", [
      "Euchromatin is open and generally transcriptionally active; heterochromatin is compact and generally silent.",
      "Histone acetylation loosens chromatin; DNA methylation and histone deacetylation commonly promote repression."
    ], [["Why can compact chromatin silence a gene?", "Transcription factors and RNA polymerase cannot efficiently access its promoter."]], "Chromatin state regulates access without changing the DNA base sequence.", "high", ["Unit 4.4", "Part 2 section 3.5"]),

    topic("p2-replication", "DNA Replication", 4, "Unit 4.3 - DNA Replication, Transcription, Translation", "30-42", [
      "Replication is semiconservative and proceeds 5' to 3' from origins using helicase, primase, DNA polymerase, and ligase.",
      "The leading strand is continuous; the lagging strand uses RNA primers and Okazaki fragments that are replaced and joined."
    ], [["Which enzyme seals Okazaki fragments?", "DNA ligase."]], "DNA polymerase adds to a free 3' end; it does not synthesize 3' to 5'.", "high", ["Unit 4.3", "Part 2 section 4.1"]),

    topic("p2-transcription", "Transcription", 4, "Unit 4.3 - DNA Replication, Transcription, Translation", "43-52", [
      "RNA polymerase binds a promoter, reads the DNA template strand, and builds complementary RNA 5' to 3'.",
      "Eukaryotic pre-mRNA receives a 5' cap, poly-A tail, and splicing before export from the nucleus."
    ], [["What is removed during RNA splicing?", "Introns are removed and exons are joined."]], "RNA uses uracil instead of thymine; the coding strand matches RNA except T becomes U.", "high", ["Unit 4.3", "Part 2 section 4.2"]),

    topic("p2-translation", "Translation", 4, "Unit 4.3 - DNA Replication, Transcription, Translation", "53-62", [
      "Ribosomes read mRNA codons 5' to 3'; tRNA anticodons deliver amino acids; peptide bonds build a polypeptide.",
      "Translation begins at AUG and ends when a stop codon recruits a release factor."
    ], [["What determines amino acid order?", "The sequence of mRNA codons copied from the gene."]], "Stop codons do not code for a tRNA-carried amino acid.", "high", ["Unit 4.3", "Part 2 section 4.2"]),

    topic("p2-operon", "The Operon", 4, "Unit 4.4 - Gene Expression", "76-84", [
      "An operon coordinates bacterial genes under one promoter and operator.",
      "In the lac operon, lactose removes repressor control; low glucose raises cAMP so CAP activates strong transcription."
    ], [["When is the lac operon maximally expressed?", "When lactose is present and glucose is absent."]], "Lactose removes repression, but high glucose still prevents strong CAP-dependent activation.", "high", ["Unit 4.4", "Part 2 section 4.2"]),

    topic("p2-euk-control", "Eukaryotic Gene Control and Mutations", 4, "Unit 4.4 - Gene Expression", "63-94", [
      "Eukaryotic regulation uses chromatin remodeling, promoters, enhancers, transcription factors, RNA processing, RNA stability, translation, and protein modification.",
      "Substitutions can be silent, missense, or nonsense; insertions/deletions can cause frameshifts; effects depend on location and reading frame."
    ], [["How can a distant enhancer activate a promoter?", "DNA looping brings enhancer-bound activators and mediator proteins near the transcription machinery."]], "Not every mutation changes phenotype; redundancy and noncoding location can make effects neutral.", "high", ["Unit 4.4", "Part 2 section 4.2"]),

    topic("p2-biotech", "Biotechnology Techniques", 4, "Unit 4.5 - Biotech & Genomics", "95-122", [
      "PCR amplifies selected DNA; gel electrophoresis separates fragments by size; restriction enzymes cut sequences; ligase joins DNA.",
      "Plasmids clone genes; sequencing reads bases; CRISPR-Cas targets edits; DNA profiling compares variable loci."
    ], [["Why do shorter DNA fragments move farther in a gel?", "They pass through the gel matrix more easily toward the positive electrode."]], "PCR copies DNA; it does not separate fragments or directly read their sequence.", "high", ["Unit 4.5", "Part 2 section 4.2"]),

    topic("p2-meiosis", "Meiosis", 4, "Unit 4.6 - Meiosis", "123-146", [
      "One DNA replication followed by two divisions produces four genetically varied haploid cells.",
      "Synapsis and crossing over occur in prophase I; homologs separate in meiosis I; sister chromatids separate in meiosis II; independent assortment adds variation."
    ], [["What separates in anaphase I?", "Homologous chromosomes; sister chromatids remain together."]], "Meiosis II resembles mitosis but begins with haploid cells whose chromosomes are still duplicated.", "high", ["Unit 4.6", "Part 2 sections 3.4 and 4.1"]),

    topic("p2-classical-genetics", "Classical Genetics", 4, "Unit 4.8 - Mendelian Inheritance P1 - Mendelian Genetics", "165-180", [
      "Alleles segregate into gametes, and genes on different chromosomes assort independently unless linkage applies.",
      "Genotype describes alleles; phenotype is the observed trait; homozygous and heterozygous states affect expression under dominance."
    ], [["State Mendel's law of segregation.", "The two alleles for a gene separate during gamete formation so each gamete receives one."]], "Dominant does not mean common, stronger, or better.", "high", ["Unit 4.8", "Part 2 section 4.6"]),

    topic("p2-punnett", "Punnett Squares", 4, "Unit 4.8 - Mendelian Inheritance P1 - Mendelian Genetics", "181-196", [
      "A Punnett square combines possible gametes to predict expected offspring genotype and phenotype probabilities.",
      "Probabilities describe many independent offspring, not a guaranteed sequence in one family."
    ], [["What cross reveals an unknown dominant phenotype genotype?", "A testcross with a homozygous recessive individual."]], "Each birth is an independent event; prior outcomes do not force the next result.", "high", ["Unit 4.8", "Part 2 section 4.6"]),

    topic("p2-crosses", "Monohybrid and Dihybrid Crosses", 4, "Unit 4.8 - Mendelian Inheritance P1 - Mendelian Genetics", "181-196", [
      "A monohybrid cross follows one gene; Aa x Aa gives 1:2:1 genotypes and 3:1 phenotypes under complete dominance.",
      "A dihybrid AaBb x AaBb gives 9:3:3:1 phenotypes only when genes assort independently and show complete dominance."
    ], [["List gametes from AaBb.", "AB, Ab, aB, and ab."]], "Do not use 9:3:3:1 for linked genes or non-Mendelian dominance patterns.", "high", ["Unit 4.8", "Part 2 section 4.6"]),

    topic("p2-autosomal", "Autosomal Disorders", 4, "Unit 4.9 - Mendelian Inheritance P2 - Genetic Disorders", "197-217", [
      "Autosomal recessive traits can skip generations and affect sexes equally; two unaffected carriers can have an affected child.",
      "Autosomal dominant traits usually appear each generation; an affected heterozygote can pass the allele to half of children."
    ], [["What genotype is an affected person with an autosomal recessive disorder?", "Homozygous recessive."]], "A carrier of a recessive allele is usually phenotypically unaffected but can transmit it.", "medium", ["Unit 4.9", "Part 2 sections 4.6 and 4.7"]),

    topic("p2-extensions", "Extensions of Mendelian Inheritance", 4, "Unit 4.8 - Mendelian Inheritance P1 - Mendelian Genetics", "185-196", [
      "Incomplete dominance gives an intermediate heterozygote; codominance expresses both alleles; multiple alleles exceed two population variants.",
      "Polygenic traits involve many genes; pleiotropy gives one gene many effects; epistasis changes another gene's expression; sex linkage follows sex chromosomes."
    ], [["Why is roan coat color codominant?", "The heterozygote displays distinct red and white hairs, so both alleles are fully expressed."]], "Incomplete dominance is not allele blending; alleles remain discrete and can reappear.", "high", ["Unit 4.8", "Unit 4.9", "Part 2 sections 4.6 and 4.7"]),

    topic("p2-evolution-evidence", "Evidence for Evolution", 5, "Unit 5.1 - Darwin & Evidence for Evolution", "1-21", [
      "Fossils, biogeography, homologous and vestigial structures, embryology, and molecular similarities support common ancestry.",
      "Natural selection acts on heritable variation when individuals differ in reproductive success."
    ], [["What do homologous structures indicate?", "Shared ancestry despite possible differences in present function."]], "Individuals do not evolve during life; population allele frequencies change across generations.", "high", ["Unit 5.1", "Part 2 section 5.2"]),

    topic("p2-hw-equation", "Hardy-Weinberg Equation", 5, "Unit 5.2 - How Populations Evolve", "22-37", [
      "For two alleles, p + q = 1 and p^2 + 2pq + q^2 = 1.",
      "p^2 and q^2 are homozygote frequencies; 2pq is heterozygote frequency; use the recessive phenotype to find q^2 when dominance is complete."
    ], [["If q^2 = 0.09, what are q, p, and 2pq?", "q = 0.3, p = 0.7, and 2pq = 0.42."]], "The recessive phenotype frequency is q^2, not q.", "high", ["Unit 5.2", "Part 2 section 4.6"]),

    topic("p2-hw-meaning", "Hardy-Weinberg Meaning", 5, "Unit 5.2 - How Populations Evolve", "22-37", [
      "Hardy-Weinberg equilibrium is a null model in which allele frequencies remain stable between generations.",
      "It assumes a very large population, random mating, no mutation, no migration, and no natural selection."
    ], [["What does deviation from Hardy-Weinberg suggest?", "At least one evolutionary assumption is violated and the population may be evolving."]], "Equilibrium does not mean all alleles or genotypes have equal frequencies.", "high", ["Unit 5.2", "Part 2 section 4.6"]),

    topic("p2-forces", "Forces of Evolution", 5, "Unit 5.2 - How Populations Evolve", "38-49", [
      "Mutation creates alleles; gene flow moves alleles; genetic drift changes frequencies by chance; selection changes them through differential fitness.",
      "Founder and bottleneck effects are drift in small populations; nonrandom mating mainly changes genotype frequencies and can expose recessive alleles."
    ], [["Why is drift strongest in small populations?", "Random sampling error represents a larger fraction of the gene pool."]], "Selection is nonrandom with respect to phenotype, but mutations arise without regard to need.", "high", ["Unit 5.2", "Part 2 section 5.3"]),

    topic("p2-speciation", "Speciation", 5, "Unit 5.3 - Speciation & Macroevolution", "50-69", [
      "Speciation requires reduced gene flow and reproductive isolation; allopatric speciation begins with geography, while sympatric speciation occurs in the same area.",
      "Prezygotic barriers prevent mating or fertilization; postzygotic barriers reduce hybrid survival or fertility."
    ], [["Classify sterile but healthy hybrids.", "Hybrid sterility, a postzygotic barrier."]], "Temporal, habitat, behavioral, mechanical, and gametic isolation are prezygotic.", "high", ["Unit 5.3", "Part 2 sections 3.4 and 5.3"]),

    topic("p2-domains", "Kingdoms and Domains", 5, "Unit 5.4 - Principles of Taxonomy & Systematics", "70-84", [
      "The three domains are Bacteria, Archaea, and Eukarya; evolutionary classification uses shared derived traits and molecular evidence.",
      "A clade contains an ancestor and all descendants; binomial names use genus and species."
    ], [["Which domains contain prokaryotes?", "Bacteria and Archaea."]], "Fungi is a kingdom within Eukarya, not a domain.", "high", ["Unit 5.4", "Unit 6.2", "Part 2 section 6.2"]),

    topic("p2-viruses", "Viruses", 6, "Unit 6.1 - Viruses", "1-11", [
      "Viruses are acellular particles with nucleic acid inside a protein capsid; some have lipid envelopes.",
      "They depend on host machinery; lytic infection rapidly produces virions and damages cells, while latent/lysogenic states retain viral genetic material."
    ], [["Why are antibiotics ineffective against viruses?", "Viruses lack bacterial targets such as peptidoglycan walls and independent ribosomes/metabolism."]], "Viruses do not divide by binary fission and are not cells.", "high", ["Unit 6.1", "Part 2 section 6.1"]),

    topic("p2-prok-characteristics", "Prokaryote Characteristics", 6, "Unit 6.2 - Prokaryotes", "12-24", [
      "Prokaryotes generally have circular DNA in a nucleoid, plasmids, 70S ribosomes, and reproduce by binary fission.",
      "Bacteria usually contain peptidoglycan; Archaea lack peptidoglycan and have distinctive ether-linked membrane lipids."
    ], [["What protects some bacteria during severe stress?", "A resistant dormant endospore."]], "An endospore is a survival structure, not a reproductive spore.", "high", ["Unit 6.2", "Part 2 section 6.2"]),

    topic("p2-virus-bacteria", "Viruses and Bacteria", 6, "Unit 6.1 - Viruses", "1-11", [
      "Bacteria are living prokaryotic cells with metabolism and ribosomes; viruses are acellular obligate intracellular parasites.",
      "Antibiotics target bacterial structures or processes; vaccines prime adaptive immunity and antivirals disrupt viral entry, replication, or release."
    ], [["Give one feature shared by bacteria and viruses.", "Both contain genetic material and can evolve, but only bacteria are cells."]], "Disease severity alone cannot distinguish a viral from a bacterial infection.", "medium", ["Unit 6.1", "Unit 6.2", "Part 2 sections 6.1 and 6.2"]),

    topic("p2-protists-plants-fungi", "Protists Plants and Fungi", 6, "Unit 6.3 - Protists", "25-50", [
      "Protists are diverse eukaryotes; plant-like forms photosynthesize, animal-like forms ingest, and fungus-like forms absorb nutrients.",
      "Plants are photosynthetic with cellulose walls; fungi are absorptive heterotrophs with chitin walls and hyphae forming a mycelium."
    ], [["How do fungi obtain food?", "They secrete digestive enzymes and absorb small molecules across hyphae."]], "Fungi are heterotrophs and are evolutionarily closer to animals than plants.", "high", ["Unit 6.3", "Unit 6.4", "Unit 6.5", "Part 2 section 3.3"]),

    topic("p2-vertebrates", "Vertebrates Mammals and Humans", 6, "Unit 6.7 - Vertebrates", "80-92", [
      "Vertebrates are chordates with a vertebral column and cranium; major groups show transitions in jaws, limbs, amniotic eggs, feathers, and mammalian traits.",
      "Mammals have hair and mammary glands and are endothermic; humans are primates with grasping hands, forward-facing eyes, large brains, and habitual bipedalism."
    ], [["Which vertebrates have fully separated four-chambered hearts?", "Birds and mammals."]], "Fish have single-loop circulation; amphibians and most reptiles permit some mixing or shunting.", "medium", ["Unit 6.7", "Part 2 section 7.4"])
  ];

  const part2 = {
    id: "part2",
    label: "Part 2: Units 3-6",
    title: "Part 2: Units 3-6",
    format: "26 Multiple Choice",
    questionCount: 26,
    units: [3, 4, 5, 6],
    topics: part2Topics,
    sectionMappings: ["part2_exam.json", "unit3_active_recall.json", "unit4_active_recall.json", "unit5_active_recall.json", "unit6_active_recall.json"]
  };

  const part3Topics = [
    topic("p3-monocots-eudicots", "Monocots and Eudicots", 7, "Unit 7.1 - Plant Structure & Organization", "1-21", [
      "Monocots have one cotyledon, parallel veins, scattered stem vascular bundles, fibrous roots, and flower parts often in threes.",
      "Eudicots have two cotyledons, netted veins, vascular bundles in a ring, taproots, and flower parts often in fours or fives."
    ], [["Which group usually has vascular cambium and secondary growth?", "Eudicots; most monocots lack vascular cambium."]], "Cotyledon count is the defining name, but exam questions often combine several diagnostic traits.", "high", ["Unit 7.1", "Part 3 section 6.5"]),

    topic("p3-plant-reproduction", "Plant Reproductive Structures", 7, "Unit 7.4 - Plant Reproduction", "55-73", [
      "Stamens contain anther and filament and produce pollen; carpels contain stigma, style, and ovary with ovules.",
      "Pollination moves pollen; fertilization forms a zygote; in angiosperms double fertilization also forms triploid endosperm; ovule becomes seed and ovary becomes fruit."
    ], [["What do petals, stamens, and carpels become without class B floral genes?", "Petals become sepals and stamens become carpels."]], "Pollination is pollen transfer and occurs before fertilization.", "high", ["Unit 7.4", "Part 3 section 6.5"]),

    topic("p3-plant-tissues", "Plant Tissues and Transport", 7, "Unit 7.1 - Plant Structure & Organization", "6-21", [
      "Dermal tissue protects; ground tissue performs photosynthesis, storage, and support; vascular tissue transports.",
      "Xylem moves water/minerals mainly upward by cohesion-tension; phloem pressure flow moves sugars from sources to sinks."
    ], [["Why does an air embolism stop flow in a xylem vessel?", "It breaks the cohesive water column that transmits transpiration tension."]], "Xylem vessel elements are dead at maturity; phloem sieve tubes are living and assisted by companion cells.", "high", ["Unit 7.1", "Unit 7.2", "Part 3 sections 3.3 and 6.5"]),

    topic("p3-plant-hormones", "Plant Hormones", 7, "Unit 7.3 - Plant Control of Growth Responses", "36-54", [
      "Auxin promotes elongation and tropisms; gibberellins promote stem growth and germination; cytokinins promote division and delay aging.",
      "Ethylene promotes fruit ripening and abscission; ABA promotes seed dormancy and drought-induced stomatal closure."
    ], [["Predict an ABA-insensitive seed phenotype.", "Premature germination or vivipary because dormancy is not maintained."]], "Ethylene is a gaseous hormone that promotes ripening; ABA generally restrains growth under stress.", "high", ["Unit 7.3", "Part 3 section 4.2"]),

    topic("p3-tropisms", "Plant Tropisms", 7, "Unit 7.3 - Plant Control of Growth Responses", "36-54", [
      "Phototropism is directional growth to light; gravitropism responds to gravity; thigmotropism responds to touch.",
      "In shoots, auxin accumulates on the shaded side, activates proton pumps and expansins, and increases elongation so the shoot bends toward light."
    ], [["Why does blocking H+-ATPases block phototropism?", "The wall does not acidify, expansins do not loosen it, and shaded-side cells cannot elongate."]], "Tropic bending is differential growth, not movement of the entire plant toward a stimulus.", "high", ["Unit 7.3", "Part 3 section 1.3"]),

    topic("p3-animal-tissues", "Animal Tissue Types", 7, "Unit 7.5 - Animal Organization", "74-94", [
      "Epithelial tissue covers and lines; connective tissue supports and binds; muscle contracts; nervous tissue communicates.",
      "Tissue healing depends strongly on blood supply: bone is vascular, dense connective tissue is poorly vascularized, and cartilage is avascular."
    ], [["Why does cartilage heal slowly?", "Nutrients and repair signals must diffuse through matrix because cartilage lacks blood vessels."]], "Connective tissue is defined by abundant extracellular matrix, not by tightly packed cells.", "high", ["Unit 7.5", "Part 3 section 6.5"]),

    topic("p3-circulation", "Circulatory System", 7, "Unit 7.6 - Circulation & Cardiovascular System", "95-117", [
      "The right heart sends deoxygenated blood to lungs; the left heart sends oxygenated blood to the body; valves enforce one-way flow.",
      "Arteries carry blood away, veins return it, and thin capillaries exchange materials; closed double circulation supports high pressure and separation."
    ], [["Trace blood from vena cava to aorta.", "Right atrium, tricuspid valve, right ventricle, pulmonary valve/artery, lungs, pulmonary veins, left atrium, mitral valve, left ventricle, aortic valve, aorta."]], "Artery and vein names describe direction relative to the heart, not oxygen content.", "high", ["Unit 7.6", "Part 3 section 7.4"]),

    topic("p3-respiration", "Respiratory System", 7, "Unit 7.7 - Respiratory System", "118-138", [
      "Ventilation moves air; external respiration exchanges gases between alveoli and blood; internal respiration exchanges between blood and tissues.",
      "Diaphragm contraction increases thoracic volume and lowers pressure; alveoli provide thin, moist, high-area surfaces matched to capillaries."
    ], [["How is most oxygen transported?", "Bound reversibly to hemoglobin in red blood cells."]], "Breathing is bulk flow caused by pressure differences; gas exchange is diffusion down partial-pressure gradients.", "high", ["Unit 7.7", "Part 3 sections 7.2 and 7.4"]),

    topic("p3-neural-signaling", "Nervous System Signaling", 7, "Unit 7.8 - Nervous System", "139-160", [
      "Na+/K+ pumps establish ion gradients and K+ leaks help set a negative resting potential.",
      "Threshold opens voltage-gated Na+ channels for depolarization, then K+ channels repolarize; synaptic Ca2+ entry triggers neurotransmitter exocytosis."
    ], [["What does tetrodotoxin or saxitoxin do?", "It blocks voltage-gated Na+ channels, preventing action-potential depolarization and propagation."]], "The Na+/K+ pump maintains gradients but does not directly create each rapid action-potential spike.", "high", ["Unit 7.8", "Part 3 section 7.6"]),

    topic("p3-sensory", "Sensory Receptors", 7, "Unit 7.9 - Sense Organs", "161-175", [
      "Mechanoreceptors detect touch, sound, stretch, and balance; chemoreceptors detect chemicals; photoreceptors detect light; thermoreceptors detect temperature; nociceptors detect damage.",
      "Rods support dim/peripheral vision; cones support detailed color vision; cochlear hair cells detect sound; semicircular canals and vestibule detect balance."
    ], [["Which structures detect rotation versus gravity?", "Semicircular canals detect rotation; utricle and saccule in the vestibule detect linear acceleration and gravity."]], "The cochlea is for hearing; vestibular structures are for equilibrium.", "high", ["Unit 7.9", "Part 3 section 7.6"]),

    topic("p3-muscle", "Muscle Anatomy", 7, "Unit 7.5 - Animal Organization", "85-94", [
      "Skeletal muscle fibers contain myofibrils built from sarcomeres with actin thin filaments and myosin thick filaments.",
      "Ca2+ binds troponin, shifting tropomyosin; ATP powers cross-bridge cycling and is required for myosin release."
    ], [["Why can ATP-rich muscle not contract without Ca2+?", "Tropomyosin remains over actin's myosin-binding sites."]], "ATP is required both to energize myosin and to detach it from actin; no ATP produces rigor.", "high", ["Unit 7.5", "Unit 7.8", "Part 3 sections 7.2 and 7.6"]),

    topic("p3-nature-nurture", "Nature and Nurture Behaviors", 8, "Unit 8.1 - Behavioral Ecology", "1-15", [
      "Behavior can include inherited components shaped by selection and learned components shaped by experience.",
      "Fixed action patterns are strongly innate; imprinting occurs in a sensitive period; many real behaviors reflect gene-environment interaction."
    ], [["What did hybrid lovebird nesting behavior show?", "An inherited tendency was modified by trial-and-error learning, demonstrating both nature and nurture."]], "Evidence of learning does not prove genetics has no influence.", "high", ["Unit 8.1", "Part 3 section 8.1"]),

    topic("p3-conditioning", "Conditioning", 8, "Unit 8.1 - Behavioral Ecology", "1-15", [
      "Classical conditioning associates two stimuli so a formerly neutral cue predicts a response.",
      "Operant conditioning changes behavior through consequences such as reinforcement or punishment; habituation reduces response to repeated harmless stimuli."
    ], [["Trial-and-error learning is which type?", "Operant conditioning."]], "Classical conditioning links stimuli; operant conditioning links behavior to consequences.", "high", ["Unit 8.1", "Part 3 section 8.1"]),

    topic("p3-reproductive-strategies", "Population Reproductive Strategies", 8, "Unit 8.2 - Population Ecology", "16-34", [
      "High-growth strategies produce many offspring with low investment and rapid maturation; competitive strategies produce fewer offspring with greater care and longer lives.",
      "Type I survivorship has late loss, Type II constant loss, and Type III high juvenile loss; life histories trade current reproduction against survival and future reproduction."
    ], [["Which curve fits many offspring with little care?", "Type III survivorship."]], "No species is purely one strategy in every trait; use the pattern described.", "medium", ["Unit 8.2", "Part 3 section 8.4"]),

    topic("p3-energy-flow", "Energy Flow", 8, "Unit 8.3 - Community & Ecosystem Ecology", "35-53", [
      "Producers capture energy; consumers and decomposers transfer it through food webs; matter cycles but energy flows one way and dissipates as heat.",
      "Only about 10 percent of production becomes biomass at the next trophic level, limiting food-chain length and top-predator abundance."
    ], [["Why are top predators rare?", "Repeated inefficient energy transfers leave little biomass and energy at high trophic levels."]], "Biomagnification makes persistent pollutants more concentrated upward even while available energy decreases.", "high", ["Unit 8.3", "Part 3 section 8.2"]),

    topic("p3-biomes", "Major Biomes", 8, "Unit 8.6 - Major Ecosystems of the Biosphere", "92-110", [
      "Temperature and precipitation shape terrestrial biomes and their adaptations.",
      "Know tundra, taiga, temperate forest, temperate grassland, chaparral, desert, savanna, and tropical rainforest by climate, vegetation, soils, fire, and seasonality."
    ], [["Which biome has permafrost and a short growing season?", "Tundra."]], "Latitude is a clue, but elevation, rain shadows, currents, and local climate can shift biome patterns.", "high", ["Unit 8.6", "Part 3 section 8.7"]),

    topic("p3-aquatic-zones", "Aquatic Ecosystem Zones", 8, "Unit 8.6 - Major Ecosystems of the Biosphere", "100-110", [
      "Freshwater systems include lakes/ponds, wetlands, rivers, and streams; marine systems include intertidal, neritic, oceanic, benthic, and estuarine regions.",
      "Photic zones receive enough light for photosynthesis; aphotic zones do not; depth, salinity, flow, nutrients, and substrate organize communities."
    ], [["Why are estuaries highly productive?", "They mix nutrient-rich freshwater and seawater and provide shallow, protected habitat."]], "The benthic zone is the bottom substrate at any depth, not only the deep ocean.", "medium", ["Unit 8.6", "Part 3 section 8.7"]),

    topic("p3-bioethics-conservation", "Bioethics and Conservation", 8, "Unit 8.7 - Conservation of Biodiversity", "111-130", [
      "Conservation addresses habitat loss and fragmentation, invasive species, pollution, overharvest, climate change, and small-population genetics.",
      "Ethical decisions weigh biodiversity, ecosystem services, animal and human welfare, equity, uncertainty, and long-term consequences."
    ], [["How do wildlife corridors help fragmented populations?", "They reconnect habitat, permit movement and gene flow, and reduce isolation."]], "Edge habitat may help some species but fragmentation usually harms interior specialists and total biodiversity.", "high", ["Unit 1.5", "Unit 8.7", "Part 3 section 8.7"]),

    topic("p3-light-dependent", "Light-Dependent Reactions", 8, "Unit 8.4 - Photosynthesis", "54-63", [
      "In thylakoids, PSII absorbs light and splits water, releasing O2; electrons move through an ETC that builds a proton gradient.",
      "ATP synthase makes ATP; PSI re-energizes electrons and NADP+ reductase forms NADPH."
    ], [["What are the direct products of the light reactions?", "ATP, NADPH, and O2."]], "The oxygen released by photosynthesis comes from water, not carbon dioxide.", "high", ["Unit 8.4", "Part 3 section 5.1"]),

    topic("p3-light-both", "Light-Dependent and Light-Independent Reactions", 8, "Unit 8.4 - Photosynthesis", "54-72", [
      "Light reactions make ATP and NADPH in thylakoids; the Calvin cycle uses them in the stroma to reduce CO2 into G3P.",
      "The Calvin cycle includes carbon fixation, reduction, and RuBP regeneration; it depends indirectly on light-made energy carriers."
    ], [["How are the two stages coupled?", "Light reactions supply ATP and NADPH; the Calvin cycle returns ADP, phosphate, and NADP+."]], "Light-independent does not mean the Calvin cycle normally runs well in darkness.", "high", ["Unit 8.4", "Part 3 sections 5.1 and 8.1"]),

    topic("p3-photo-reactants", "Photosynthesis Reactants and Products", 8, "Unit 8.4 - Photosynthesis", "54-72", [
      "Overall: 6 CO2 + 6 H2O + light energy -> C6H12O6 + 6 O2, with glucose representing stored chemical energy.",
      "CO2 supplies carbon, water supplies electrons and released oxygen, and light drives electron excitation."
    ], [["Which product stores most captured energy?", "Sugar chemical bonds, represented by glucose."]], "The balanced overall equation summarizes many steps; free glucose is not made directly by the Calvin cycle.", "high", ["Unit 8.4", "Part 3 section 5.1"]),

    topic("p3-photo-strategies", "Plant Photosynthetic Strategies", 8, "Unit 8.4 - Photosynthesis", "64-72", [
      "C3 plants fix CO2 directly with Rubisco; hot, dry, low-CO2 conditions increase photorespiration.",
      "C4 plants spatially concentrate CO2 using PEP carboxylase and bundle-sheath cells; CAM plants separate fixation at night from the Calvin cycle by day."
    ], [["Why does PEP carboxylase help C4 plants?", "It fixes CO2 efficiently without binding O2, concentrating CO2 near Rubisco."]], "C4 and CAM reduce water loss/photorespiration but require extra ATP and are not universally superior.", "high", ["Unit 8.4", "Part 3 section 5.1"]),

    topic("p3-resp-stages", "Cellular Respiration Stages", 8, "Unit 8.5 - Cellular Respiration", "73-91", [
      "Glycolysis in cytosol makes pyruvate, 2 net ATP, and NADH; pyruvate oxidation makes acetyl-CoA.",
      "The citric acid cycle releases CO2 and loads NADH/FADH2; oxidative phosphorylation uses their electrons to make most ATP."
    ], [["Where is most ATP made in aerobic respiration?", "By oxidative phosphorylation across the inner mitochondrial membrane."]], "Oxygen is used directly at the end of the ETC, not in glycolysis or as a citric-acid-cycle reactant.", "high", ["Unit 8.5", "Part 3 sections 7.2 and 8.1"]),

    topic("p3-etcs", "Electron Transport Chains", 8, "Unit 8.4 - Photosynthesis", "58-63", [
      "An ETC transfers electrons through carriers and uses released energy to pump protons across a membrane.",
      "Photosynthetic ETCs operate in thylakoids and ultimately reduce NADP+; respiratory ETCs operate in the inner mitochondrial membrane and reduce O2 to water."
    ], [["What common principle links both ETCs?", "Electron energy builds a proton-motive force that powers ATP synthase."]], "Electrons do not directly push ATP synthase; proton flow through ATP synthase drives phosphorylation.", "high", ["Unit 8.4", "Unit 8.5", "Part 3 sections 5.1 and 7.2"]),

    topic("p3-atp", "ATP Generation", 8, "Unit 8.5 - Cellular Respiration", "73-91", [
      "Substrate-level phosphorylation transfers phosphate directly to ADP; chemiosmosis uses a proton gradient and ATP synthase.",
      "Fermentation regenerates NAD+ so glycolysis can continue but yields only 2 net ATP per glucose; aerobic respiration yields far more."
    ], [["What does an uncoupler do?", "It dissipates the proton gradient, so electron transport can continue while ATP synthesis falls or stops."]], "Fermentation's main purpose is NAD+ regeneration, not production of extra ATP after glycolysis.", "high", ["Unit 8.5", "Part 3 sections 7.2 and 8.1"]),

    topic("p3-energy-bonds", "Energy Storage in Bonds", 8, "Unit 8.5 - Cellular Respiration", "73-91", [
      "Reduced molecules with many C-H bonds store usable chemical energy; oxidation transfers electrons to NAD+ and FAD and ultimately to oxygen.",
      "ATP couples energy-releasing reactions to cellular work; hydrolysis is favorable because products are more stable and can be coupled to targets."
    ], [["Why does fat store more energy per gram than carbohydrate?", "Fat has more highly reduced C-H bonds whose oxidation transfers more high-energy electrons."]], "Energy is not released by simply breaking a bond; net energy comes from forming more stable product bonds.", "medium", ["Unit 2.4", "Unit 8.5", "Part 3 sections 7.2 and 8.1"])
  ];

  const part3 = {
    id: "part3",
    label: "Part 3: Units 7-8",
    title: "Part 3: Units 7-8",
    format: "25 Multiple Choice",
    questionCount: 25,
    units: [7, 8],
    topics: part3Topics,
    sectionMappings: ["part3_exam.json", "unit7_active_recall.json", "unit8_active_recall.json"]
  };

  const part4Categories = [
    {
      id: "p4-cells",
      title: "Cells",
      units: [3],
      openResponseCategory: true,
      directions: "Choose A or B",
      availableOptions: [{ option: "A" }, { option: "B" }],
      prompts: [
        choice("A", "Cell Size Limits and Surface Area to Volume Ratio", "A SEC14 mutant yeast grows in volume without adding enough plasma membrane. Explain how surface area and volume scale, predict effects on nutrient uptake and waste removal, and explain one adaptation that increases SA:V without greatly increasing volume.", [
          "State that surface area scales with length squared and volume with length cubed, so SA:V decreases as size rises.",
          "Connect limited membrane area to slower nutrient uptake per unit volume and waste accumulation.",
          "Name and explain a valid adaptation such as microvilli, membrane folds, or root hairs."
        ], ["Unit 3.1 Cell Biology, active recall pages 9-10", "Unit 3.2 Organelles, active recall pages 17-60", "part4_exam.json Unit 3 option A, section 3.2"]),
        choice("B", "Organelle Interactions and Vesicular Transport", "Pancreatic cells are treated with a drug that blocks COPII vesicles from the RER to the Golgi. Trace normal secretion, predict where proteins accumulate and how RER/Golgi structure changes, and connect unresolved ER stress to checkpoint arrest and apoptosis.", [
          "Trace ribosome/RER -> COPII vesicle -> cis/trans Golgi -> secretory vesicle -> exocytosis.",
          "Predict RER protein accumulation and dilation plus reduced/disassembled Golgi traffic.",
          "Explain unfolded protein response, checkpoint arrest, and apoptosis if stress cannot be resolved."
        ], ["Unit 3.2 Organelles, active recall pages 17-60", "Unit 3.4 Cell Cycle, pages 75-95", "Unit 3.5 Cancer, pages 96-113", "part4_exam.json Unit 3 option B, section 3.3"])
      ],
      requiredPoints: ["Answer all three numbered tasks for the selected option.", "Use structure-function and cause-effect reasoning.", "Make each prediction explicit."],
      checklist: ["Selected only A or B", "Defined core mechanism", "Applied mechanism to scenario", "Used note vocabulary", "Answered every subpart"],
      rubric
    },
    {
      id: "p4-gene-regulation",
      title: "Gene Regulation",
      units: [4],
      openResponseCategory: true,
      directions: "Choose A or B",
      availableOptions: [{ option: "A" }, { option: "B" }],
      prompts: [
        choice("A", "Epigenetic Regulation and Eukaryotic Transcription Control", "Compare silenced methylated p16 chromatin with acetylated overexpressed MYC chromatin. Explain promoter methylation and access by transcription machinery, then explain how a mutated distant enhancer can increase MYC transcription through DNA looping and mediator proteins.", [
          "Identify p16 as compact heterochromatin and MYC as open euchromatin.",
          "Explain DNA methylation/histone deacetylation versus histone acetylation and promoter accessibility.",
          "Explain activator binding, DNA looping, mediator interaction, and increased RNA polymerase II recruitment."
        ], ["Unit 4.4 Gene Expression, active recall pages 63-94", "Unit 3.5 Cancer, pages 96-113", "part4_exam.json Unit 4 Genetics option A, section 4.1"]),
        choice("B", "The Lac Operon and Bacterial Gene Regulation", "Analyze wild-type lac regulation and three mutants affecting lacI, lacO, or the CAP-binding site under specified glucose/lactose conditions. Predict structural-gene expression and justify each prediction using repressor, allolactose, cAMP, CAP, operator, and RNA polymerase.", [
          "Explain wild type with high glucose/no lactose: active repressor, inactive CAP, transcription off.",
          "Predict constitutive but CAP-dependent expression for lacI-null and operator mutants under both conditions.",
          "Predict only basal expression for a CAP-site mutant even with no glucose and high lactose."
        ], ["Unit 4.4 Gene Expression, active recall pages 76-94", "part4_exam.json Unit 4 Genetics option B, section 4.5"])
      ],
      requiredPoints: ["Identify each regulatory component and its state.", "Link chromatin or DNA-binding state to transcription level.", "Justify every mutant or scenario prediction."],
      checklist: ["Selected only A or B", "Named regulatory molecules", "Explained access/binding", "Predicted expression level", "Answered every subpart"],
      rubric
    },
    {
      id: "p4-heredity",
      title: "Heredity",
      units: [4],
      openResponseCategory: true,
      directions: "Choose A or B",
      availableOptions: [{ option: "A" }, { option: "B" }],
      prompts: [
        choice("A", "Meiotic Cell Division and Genetic Variation", "For an organism with 2n = 12 exposed to a spindle-disrupting drug, describe prophase I crossing over, compare chromosome separation in anaphase I and II, and predict gametes and zygotes produced after meiosis-I nondisjunction.", [
          "Explain synapsis, tetrads, chiasmata, crossing over between nonsister chromatids, and recombinant chromosomes.",
          "Contrast homolog separation in anaphase I with sister-chromatid separation in anaphase II.",
          "Predict n+1/n-1 gametes for one nondisjoined homolog pair and trisomic/monosomic zygotes after normal fertilization."
        ], ["Unit 4.6 Meiosis, active recall pages 123-146", "Unit 4.7 Chromosome Syndromes, pages 147-164", "part4_exam.json Unit 4 Heredity option A, section 4.1"]),
        choice("B", "Non-Mendelian Inheritance Patterns and Pedigree Analysis", "Use a Fabry disease pedigree in which affected fathers transmit to daughters but not sons and affected mothers transmit to either sex. Identify inheritance, explain variable female symptoms using X inactivation, and calculate/justify offspring risks for the specified parental cross.", [
          "Identify an X-linked dominant pattern from father-to-all-daughters and no father-to-son transmission.",
          "Explain random X inactivation and mosaic expression as a cause of variable severity in heterozygous females.",
          "Set up parental genotypes and calculate sex-specific probabilities without treating linked events as independent."
        ], ["Unit 4.8 Mendelian Genetics, active recall pages 165-196", "Unit 4.9 Genetic Disorders, pages 197-217", "part4_exam.json Unit 4 Heredity option B, section 4.6"])
      ],
      requiredPoints: ["Show chromosome or allele logic, not only the final result.", "Use correct meiosis or pedigree vocabulary.", "State numerical probabilities or chromosome outcomes clearly."],
      checklist: ["Selected only A or B", "Represented chromosomes/alleles", "Explained mechanism", "Calculated outcome", "Answered every subpart"],
      rubric
    },
    {
      id: "p4-evolution",
      title: "Evolution",
      units: [5],
      openResponseCategory: true,
      directions: "Choose A or B",
      availableOptions: [{ option: "A" }, { option: "B" }],
      prompts: [
        choice("A", "Hardy-Weinberg Equilibrium and Selection Forces", "For 490 red R1R1, 420 pink R1R2, and 90 white R2R2 flowers in a population of 1000, calculate p and q, calculate expected genotype frequencies, assess equilibrium, and predict how preferential reproduction of red flowers changes allele frequencies.", [
          "Count alleles to obtain p(R1) = 0.7 and q(R2) = 0.3.",
          "Calculate p^2 = 0.49, 2pq = 0.42, and q^2 = 0.09 and compare with observed values.",
          "Conclude the starting population matches equilibrium, then explain that nonrandom reproductive success/selection raises R1 and violates equilibrium."
        ], ["Unit 5.2 How Populations Evolve, active recall pages 22-49", "part4_exam.json Unit 5 option A, section 5.1"]),
        choice("B", "Speciation Dynamics and Phylogenetic Reconstruction", "Use the Ensatina salamander ring-species scenario to classify speciation around a geographic barrier, identify the reproductive barrier where terminal forms meet, and explain how molecular and morphological evidence should be used to reconstruct their phylogeny.", [
          "Classify the divergence as allopatric/ring-species divergence caused by geographic isolation and different selection pressures.",
          "Identify reduced hybrid survival as a postzygotic barrier and explain its effect on gene flow.",
          "Build the phylogenetic claim from shared ancestry, branching order, derived traits, and DNA sequence similarity rather than superficial resemblance alone."
        ], ["Unit 5.3 Speciation and Macroevolution, active recall pages 50-69", "Unit 5.4 Taxonomy and Systematics, pages 70-84", "part4_exam.json Unit 5 option B, section 5.3"])
      ],
      requiredPoints: ["Use equations or an explicit isolation model.", "Distinguish observation from evolutionary inference.", "Explain how the force or barrier changes allele flow over generations."],
      checklist: ["Selected only A or B", "Showed calculation/classification", "Named evolutionary mechanism", "Justified conclusion", "Answered every subpart"],
      rubric
    },
    {
      id: "p4-organism-systems",
      title: "Organism Systems",
      units: [7],
      openResponseCategory: true,
      directions: "Choose A or B",
      availableOptions: [{ option: "A" }, { option: "B" }],
      prompts: [
        choice("A", "Plant Transport Systems and Transpirational Pull", "For drought-stressed soybean plants, explain guard-cell opening and ABA-driven closing using H+ pumps, K+, and water potential; explain cohesion-tension in xylem; and evaluate the photosynthesis and heat-control tradeoff of stomatal closure.", [
          "Explain H+ pumping, K+ influx, osmosis, guard-cell turgor, and ABA-driven ion/water loss during closure.",
          "Explain transpiration tension, cohesion between water molecules, adhesion to xylem walls, and continuous pull.",
          "Explain that closure saves water but limits CO2 uptake/Calvin cycle and reduces evaporative cooling."
        ], ["Unit 7.2 Plant Nutrition and Transport, active recall pages 22-35", "Unit 7.3 Plant Responses, pages 36-54", "part4_exam.json Unit 7 option A, section 7.1"]),
        choice("B", "Neurophysiology, Synaptic Transmission, and Muscle Contraction", "Saxitoxin blocks voltage-gated Na+ channels. Explain resting potential, action-potential phases and toxin effect, then trace the failure from motor-neuron signaling through ACh release, muscle excitation, sarcoplasmic-reticulum Ca2+ release, troponin/tropomyosin, and cross-bridge contraction.", [
          "Explain 3 Na+ out/2 K+ in by the Na+/K+ pump plus K+ leak and negative resting potential.",
          "Explain threshold, Na+ depolarization, K+ repolarization, and why blocking Na+ channels prevents propagation.",
          "Trace no presynaptic AP -> no Ca2+ entry/ACh release -> no muscle AP/SR Ca2+ -> tropomyosin remains blocking actin -> no contraction."
        ], ["Unit 7.8 Nervous System, active recall pages 139-160", "Unit 7.5 Animal Organization, pages 74-94", "part4_exam.json Unit 7 option B, section 7.6"])
      ],
      requiredPoints: ["Trace the process in causal order.", "Name the relevant ions, channels, tissues, and structures.", "Connect the disrupted step to the final physiological effect."],
      checklist: ["Selected only A or B", "Established normal mechanism", "Located disruption", "Traced downstream effect", "Answered every subpart"],
      rubric
    },
    {
      id: "p4-ecology-energy",
      title: "Ecology and Energy",
      units: [8],
      openResponseCategory: true,
      directions: "Choose A or B",
      availableOptions: [{ option: "A" }, { option: "B" }],
      prompts: [
        choice("A", "Population Growth Dynamics and Trophic Cascades", "For elk growing without predators and then exposed to reintroduced wolves, compare exponential and logistic growth with equations and carrying capacity, predict a wolf-elk-plant trophic cascade, and explain the 10 percent rule and why apex predators are rare.", [
          "Contrast dN/dt = rN with dN/dt = rN(1 - N/K), define K, and name three density-dependent limits.",
          "Predict fewer/behaviorally shifted elk and increased aspen/willow through a top-down trophic cascade.",
          "Connect inefficient transfer and heat loss to roughly 10 percent transfer and low top-predator biomass."
        ], ["Unit 8.2 Population Ecology, active recall pages 16-34", "Unit 8.3 Community and Ecosystem Ecology, pages 35-53", "part4_exam.json Unit 8 option A, section 8.4"]),
        choice("B", "Photosynthetic and Cellular Respiration Coupling", "For C4 corn in light without CO2 and yeast with glucose without O2, explain light reactions and why lack of CO2 eventually backs up them, explain C4 carbon concentration and reduced photorespiration, and compare anaerobic glycolysis/fermentation ATP yield with aerobic respiration.", [
          "Trace PSII, water splitting, ETC/proton gradient, ATP synthase, PSI, and NADPH; explain Calvin-cycle stoppage and loss of recycled NADP+/ADP.",
          "Explain PEP carboxylase in mesophyll, four-carbon transport, CO2 release in bundle-sheath cells, and reduced Rubisco oxygenation.",
          "Explain glycolysis net 2 ATP/2 NADH, alcoholic fermentation regenerating NAD+, and much greater aerobic ATP yield."
        ], ["Unit 8.4 Photosynthesis, active recall pages 54-72", "Unit 8.5 Cellular Respiration, pages 73-91", "part4_exam.json Unit 8 option B, section 8.1"])
      ],
      requiredPoints: ["Use the relevant equation or pathway order.", "Track energy, matter, or population change explicitly.", "Explain the scenario prediction from the mechanism."],
      checklist: ["Selected only A or B", "Used equation/pathway", "Tracked inputs and outputs", "Explained prediction", "Answered every subpart"],
      rubric
    }
  ];

  const part4 = {
    id: "part4",
    label: "Part 4: Open-Ended",
    title: "Part 4: Open-Ended",
    format: "Choose A or B",
    categoryCount: 6,
    categories: part4Categories,
    sectionMappings: ["part4_exam.json", "unit3_active_recall.json", "unit4_active_recall.json", "unit5_active_recall.json", "unit7_active_recall.json", "unit8_active_recall.json"]
  };

  return {
    id: "final-blueprint-2026",
    title: "Biology Final Blueprint 2026",
    examParts: {
      part1: "20 Multiple Choice",
      part2: "26 Multiple Choice",
      part3: "25 Multiple Choice",
      part4: "Choose A or B"
    },
    tracks: [part1, part2, part3, part4],
    part1,
    part2,
    part3,
    part4
  };
})();
