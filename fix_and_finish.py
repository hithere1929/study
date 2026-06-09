"""
fix_and_finish.py
1) Adds 'section' fields to part1/2/3/4 exam JSONs based on question content analysis
2) Fixes double-escaped unicode in assemble_quiz.py
3) Adds [Unit X.Y] tags to exam question rendering
4) Regenerates index.html
"""
import json, os, re

base = r"c:\Users\elieu\OneDrive\Desktop\biofinaltest"

# ===== STEP 1: Add section fields to exam JSON files =====
print("=" * 60)
print("STEP 1: Adding section tags to exam JSON files...")
print("=" * 60)

# Topic -> section mapping based on the review outline
# Part 1 = General Knowledge Units 1-8 (20 MC questions)
# Part 2 = Units 3-6 (26 MC questions)  
# Part 3 = Units 7-8 (25 MC questions)
# Part 4 = Open-ended (12 prompts)

KEYWORD_MAP = {
    # Unit 1
    "lab safety": "1.1", "safety": "1.1", "fume hood": "1.1", "goggles": "1.1", "chemical spill": "1.1",
    "microscop": "1.2", "magnification": "1.2", "field of view": "1.2", "objective lens": "1.2", "compound light": "1.2",
    "scientific method": "1.3", "hypothesis": "1.3", "independent variable": "1.3", "dependent variable": "1.3",
    "control group": "1.3", "control experiment": "1.3", "controlled experiment": "1.3", "experimental design": "1.3",
    "peer review": "1.4", "scientific theory": "1.4", "scientific law": "1.4",
    "metric": "1.5", "measurement": "1.5", "significant figures": "1.5", "si unit": "1.5",
    
    # Unit 2
    "organic molecule": "2.1", "macromolecule": "2.1", "monomer": "2.1", "polymer": "2.1",
    "carbohydrate": "2.2", "monosaccharide": "2.2", "polysaccharide": "2.2", "glucose": "2.2", "starch": "2.2", "cellulose": "2.2", "glycogen": "2.2",
    "lipid": "2.2", "fatty acid": "2.2", "phospholipid": "2.2", "triglyceride": "2.2", "saturated": "2.2", "unsaturated fat": "2.2",
    "protein": "2.3", "amino acid": "2.3", "polypeptide": "2.3", "enzyme": "2.3", "denaturation": "2.3", "denature": "2.3",
    "tertiary structure": "2.3", "active site": "2.3", "substrate": "2.3", "catalys": "2.3",
    "competitive inhibit": "2.3", "noncompetitive": "2.3", "allosteric": "2.3",
    "nucleic acid": "2.4", "nucleotide": "2.4", "dna": "2.4", "rna": "2.4",
    "osmosis": "2.5", "diffusion": "2.5", "active transport": "2.5", "hypertonic": "2.5", "hypotonic": "2.5",
    "isotonic": "2.5", "facilitated diffusion": "2.5", "aquaporin": "2.5", "concentration gradient": "2.5",
    "endocytosis": "2.5", "exocytosis": "2.5", "cell membrane": "2.5", "phospholipid bilayer": "2.5",
    
    # Unit 3
    "cell theory": "3.1",
    "surface area": "3.2", "volume ratio": "3.2", "sa:v": "3.2", "cell size": "3.2",
    "prokaryot": "3.3", "eukaryot": "3.3", "organelle": "3.3", "mitochondri": "3.3", "chloroplast": "3.3",
    "ribosom": "3.3", "endoplasmic reticulum": "3.3", "golgi": "3.3", "lysosom": "3.3", "vacu": "3.3",
    "nucleus": "3.3", "cell wall": "3.3", "cytoplasm": "3.3", "cytoskeleton": "3.3",
    "cell cycle": "3.4", "mitosis": "3.4", "meiosis": "3.4", "interphase": "3.4", "prophase": "3.4",
    "metaphase": "3.4", "anaphase": "3.4", "telophase": "3.4", "cytokinesis": "3.4",
    "chromosome": "3.4", "chromatid": "3.4", "centromere": "3.4", "spindle": "3.4",
    "cancer": "3.5", "tumor": "3.5", "oncogene": "3.5", "tumor suppressor": "3.5", "metastas": "3.5",
    "benign": "3.5", "malignant": "3.5", "mutagen": "3.5", "carcinogen": "3.5", "apoptosis": "3.5",
    
    # Unit 4
    "dna replication": "4.1", "helicase": "4.1", "dna polymerase": "4.1", "leading strand": "4.1",
    "lagging strand": "4.1", "okazaki": "4.1", "semiconservative": "4.1", "replication fork": "4.1",
    "transcription": "4.2", "mrna": "4.2", "rna polymerase": "4.2", "promoter": "4.2",
    "translation": "4.3", "codon": "4.3", "anticodon": "4.3", "trna": "4.3", "ribosome": "4.3",
    "start codon": "4.3", "stop codon": "4.3", "aug": "4.3",
    "mutation": "4.4", "point mutation": "4.4", "frameshift": "4.4", "insertion": "4.4", "deletion": "4.4",
    "substitution": "4.4", "missense": "4.4", "nonsense": "4.4", "silent mutation": "4.4",
    "gene regulation": "4.5", "operon": "4.5", "lac operon": "4.5",
    "mendel": "4.6", "punnett": "4.6", "dominant": "4.6", "recessive": "4.6", "genotype": "4.6",
    "phenotype": "4.6", "heterozygous": "4.6", "homozygous": "4.6", "allele": "4.6",
    "incomplete dominance": "4.7", "codominance": "4.7", "multiple allele": "4.7", "blood type": "4.7",
    "polygenic": "4.7", "epistasis": "4.7", "pleiotropy": "4.7",
    "sex-linked": "4.8", "x-linked": "4.8", "autosomal": "4.8", "pedigree": "4.8",
    "karyotype": "4.8", "nondisjunction": "4.8", "trisomy": "4.8", "monosomy": "4.8",
    "biotechnology": "4.9", "gel electrophoresis": "4.9", "pcr": "4.9", "restriction enzyme": "4.9",
    "crispr": "4.9", "genetic engineering": "4.9", "transgenic": "4.9", "cloning": "4.9",
    "gmo": "4.9", "recombinant": "4.9",
    
    # Unit 5
    "darwin": "5.1", "natural selection": "5.1", "evolution": "5.1", "fitness": "5.1",
    "adaptation": "5.1", "artificial selection": "5.1", "descent with modification": "5.1",
    "evidence of evolution": "5.2", "fossil record": "5.2", "homologous structure": "5.2",
    "analogous structure": "5.2", "vestigial": "5.2", "embryology": "5.2", "comparative anatomy": "5.2",
    "biogeography": "5.2",
    "speciation": "5.3", "reproductive isolation": "5.3", "geographic isolation": "5.3",
    "allopatric": "5.3", "sympatric": "5.3",
    "hardy-weinberg": "5.3", "gene pool": "5.3", "genetic drift": "5.3", "bottleneck": "5.3",
    "founder effect": "5.3", "gene flow": "5.3", "allele frequency": "5.3",
    "taxonomy": "5.4", "phylogenet": "5.4", "cladogram": "5.4", "binomial nomenclature": "5.4",
    "classification": "5.4", "domain": "5.4", "kingdom": "5.4", "linnaeus": "5.4",
    
    # Unit 6
    "virus": "6.1", "lytic": "6.1", "lysogenic": "6.1", "bacteriophage": "6.1", "capsid": "6.1",
    "retrovirus": "6.1", "hiv": "6.1", "vaccine": "6.1",
    "bacteri": "6.2", "archaea": "6.2", "prokaryote": "6.2", "binary fission": "6.2",
    "conjugation": "6.2", "antibiotic": "6.2", "gram stain": "6.2", "peptidoglycan": "6.2",
    "protist": "6.3", "protozoa": "6.3", "algae": "6.3", "amoeba": "6.3", "paramecium": "6.3",
    "fung": "6.4", "mycelium": "6.4", "hypha": "6.4", "spore": "6.4", "decomposer": "6.4",
    "lichen": "6.4", "yeast": "6.4", "mushroom": "6.4",
    "plant": "6.5", "bryophyte": "6.5", "gymnosperm": "6.5", "angiosperm": "6.5", "fern": "6.5",
    "seed": "6.5", "pollen": "6.5", "flower": "6.5", "vascular": "6.5", "nonvascular": "6.5",
    "animal": "6.6", "invertebrate": "6.6", "vertebrate": "6.6", "arthropod": "6.6",
    "cnidarian": "6.6", "mollusk": "6.6", "echinoderm": "6.6", "chordate": "6.6",
    "endotherm": "6.7", "ectotherm": "6.7", "homeostas": "6.7",
    
    # Unit 7
    "photosynthesis": "7.1", "light reaction": "7.1", "calvin cycle": "7.1", "thylakoid": "7.1",
    "stroma": "7.1", "chlorophyll": "7.1", "nadph": "7.1", "photosystem": "7.1",
    "carbon fixation": "7.1",
    "cellular respiration": "7.2", "glycolysis": "7.2", "krebs cycle": "7.2", "citric acid cycle": "7.2",
    "electron transport chain": "7.2", "oxidative phosphorylation": "7.2", "atp": "7.2",
    "fermentation": "7.2", "anaerobic": "7.2", "aerobic": "7.2", "nad+": "7.2", "nadh": "7.2",
    "digestive": "7.3", "digestion": "7.3", "stomach": "7.3", "intestin": "7.3", "esophag": "7.3",
    "peristalsis": "7.3", "villi": "7.3", "pancrea": "7.3", "liver": "7.3", "bile": "7.3",
    "circulatory": "7.4", "heart": "7.4", "blood": "7.4", "artery": "7.4", "vein": "7.4",
    "capillary": "7.4", "atrium": "7.4", "ventricle": "7.4", "cardiac": "7.4",
    "respiratory": "7.5", "lung": "7.5", "alveol": "7.5", "bronch": "7.5", "trachea": "7.5",
    "diaphragm": "7.5", "gas exchange": "7.5", "inhal": "7.5", "exhal": "7.5",
    "nervous": "7.6", "neuron": "7.6", "synapse": "7.6", "axon": "7.6", "dendrite": "7.6",
    "neurotransmitter": "7.6", "brain": "7.6", "reflex": "7.6", "action potential": "7.6",
    "central nervous": "7.6", "peripheral nervous": "7.6",
    "immune": "7.7", "antibod": "7.7", "antigen": "7.7", "white blood cell": "7.7",
    "lymphocyte": "7.7", "t cell": "7.7", "b cell": "7.7", "pathogen": "7.7",
    "innate immun": "7.7", "adaptive immun": "7.7", "phagocyt": "7.7",
    "excretory": "7.8", "kidney": "7.8", "nephron": "7.8", "urinary": "7.8", "filtration": "7.8",
    "urine": "7.8", "reabsorption": "7.8",
    "endocrine": "7.9", "hormone": "7.9", "pituitary": "7.9", "thyroid": "7.9",
    "insulin": "7.9", "glucagon": "7.9", "adrenal": "7.9", "feedback loop": "7.9",
    "negative feedback": "7.9", "positive feedback": "7.9",
    
    # Unit 8
    "ecology": "8.1", "ecosystem": "8.1", "abiotic": "8.1", "biotic": "8.1",
    "biosphere": "8.1", "community": "8.1", "population": "8.1",
    "food chain": "8.2", "food web": "8.2", "trophic": "8.2", "producer": "8.2",
    "consumer": "8.2", "primary consumer": "8.2", "secondary consumer": "8.2",
    "decompos": "8.2", "autotroph": "8.2", "heterotroph": "8.2", "energy pyramid": "8.2",
    "carbon cycle": "8.3", "nitrogen cycle": "8.3", "water cycle": "8.3", "phosphorus cycle": "8.3",
    "biogeochemical": "8.3", "nitrogen fixation": "8.3",
    "symbiosis": "8.4", "mutualism": "8.4", "commensalism": "8.4", "parasitism": "8.4",
    "predator": "8.4", "prey": "8.4", "competition": "8.4", "niche": "8.4", "habitat": "8.4",
    "carrying capacity": "8.4", "limiting factor": "8.4",
    "succession": "8.5", "primary succession": "8.5", "secondary succession": "8.5",
    "pioneer species": "8.5", "climax community": "8.5",
    "biome": "8.6", "tundra": "8.6", "taiga": "8.6", "temperate": "8.6", "tropical": "8.6",
    "desert": "8.6", "grassland": "8.6", "rainforest": "8.6", "savanna": "8.6",
    "aquatic": "8.6", "freshwater": "8.6", "marine": "8.6", "estuary": "8.6", "coral reef": "8.6",
    "human impact": "8.7", "biodiversity": "8.7", "deforestation": "8.7", "pollution": "8.7",
    "global warming": "8.7", "climate change": "8.7", "greenhouse": "8.7", "ozone": "8.7",
    "endangered": "8.7", "invasive species": "8.7", "conservation": "8.7", "sustainability": "8.7",
}

def classify_question(q_text, explanations_text=""):
    """Classify a question into a unit.section based on keyword matching."""
    combined = (q_text + " " + explanations_text).lower()
    
    scores = {}
    for keyword, section in KEYWORD_MAP.items():
        if keyword in combined:
            weight = len(keyword)  # Longer keywords get higher weight
            scores[section] = scores.get(section, 0) + weight
    
    if scores:
        best = max(scores, key=scores.get)
        return best
    return None

# Process Part 1 (General Knowledge Units 1-8, 20 MC)
for part_name in ["part1", "part2", "part3", "part4"]:
    filepath = os.path.join(base, f"{part_name}_exam.json")
    if not os.path.exists(filepath):
        print(f"  Skipping {part_name}_exam.json (not found)")
        continue
    
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    changed = 0
    for item in data:
        if "section" in item and item["section"]:
            continue  # Already has a section
        
        q_text = item.get("q", "") or item.get("scenario", "") or item.get("prompt", "") or ""
        exp_text = ""
        if "explanations" in item and isinstance(item["explanations"], list):
            exp_text = " ".join(item["explanations"])
        elif "explanation" in item:
            exp_text = item.get("explanation", "")
        
        # For part4 (written prompts), also check the unit field
        if "unit" in item:
            unit_str = item["unit"].lower()
            # Parse "Unit 3" -> "3", "Unit 4 Part 1" -> "4"
            m = re.search(r'unit\s*(\d+)', unit_str)
            if m:
                unit_num = m.group(1)
                # Try to classify more specifically
                sec = classify_question(q_text, exp_text)
                if sec and sec.startswith(unit_num + "."):
                    item["section"] = sec
                else:
                    item["section"] = f"{unit_num}.1"
                changed += 1
                continue
        
        sec = classify_question(q_text, exp_text)
        if sec:
            item["section"] = sec
        else:
            # Fallback: try to guess from part number
            if part_name == "part1":
                item["section"] = "1.1"  # General
            elif part_name == "part2":
                item["section"] = "3.1"  # Units 3-6
            elif part_name == "part3":
                item["section"] = "7.1"  # Units 7-8
            elif part_name == "part4":
                item["section"] = "3.1"
        changed += 1
    
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"  {part_name}_exam.json: Added sections to {changed} questions")
    # Show a sample
    for i, item in enumerate(data[:3]):
        print(f"    Q{i+1}: [{item.get('section', '?')}] {(item.get('q', '') or item.get('scenario', ''))[:80]}...")

# ===== STEP 2: Fix assemble_quiz.py =====
print("\n" + "=" * 60)
print("STEP 2: Fixing assemble_quiz.py...")
print("=" * 60)

asm_path = os.path.join(base, "assemble_quiz.py")
with open(asm_path, "r", encoding="utf-8") as f:
    content = f.read()

# Fix 1: Double-escaped unicode (\\\\u2713 -> \\u2713)
# In Python source, \\u2713 becomes \u2713 in JS output which renders as ✓
old_count = content.count("\\\\u2713")
content = content.replace("\\\\u2713", "\\u2713")
content = content.replace("\\\\u2717", "\\u2717")
print(f"  Fixed {old_count} double-escaped unicode sequences")

# Fix 2: Add section tag display to exam MC rendering (renderExamMCList)
# Find the line: text.textContent = `${idx + 1}. ${q.q}`;
# In the renderExamMCList function
old_exam_mc_text = """text.textContent = `${idx + 1}. ${q.q}`;
    qBlock.appendChild(text);
    
    const optsDiv = document.createElement('div');
    optsDiv.className = 'opts-container';
    
    q.opts.forEach((optText, optIdx) => {
      const label = document.createElement('label');
      label.className = 'opt-label';
      if (answerArray[idx] === optIdx) label.classList.add('selected');
      
      const input = document.createElement('input');
      input.type = 'radio';
      input.name = `${namePrefix}_radio_${idx}`;"""

new_exam_mc_text = """text.textContent = `${idx + 1}. ${q.q}`;
    if (q.section) {
      const secTag = document.createElement('span');
      secTag.style.cssText = 'display:inline-block;background:var(--accent-soft);color:var(--accent);font-size:11px;font-weight:600;padding:2px 7px;border-radius:4px;margin-right:6px;font-family:DM Mono,monospace;vertical-align:middle;';
      secTag.textContent = '[Unit ' + q.section + ']';
      text.insertBefore(secTag, text.firstChild);
    }
    qBlock.appendChild(text);
    
    const optsDiv = document.createElement('div');
    optsDiv.className = 'opts-container';
    
    q.opts.forEach((optText, optIdx) => {
      const label = document.createElement('label');
      label.className = 'opt-label';
      if (answerArray[idx] === optIdx) label.classList.add('selected');
      
      const input = document.createElement('input');
      input.type = 'radio';
      input.name = `${namePrefix}_radio_${idx}`;"""

if old_exam_mc_text in content:
    content = content.replace(old_exam_mc_text, new_exam_mc_text, 1)
    print("  Added section tags to renderExamMCList")
else:
    print("  WARNING: Could not find renderExamMCList text to patch")

# Fix 3: Add section tag display to graded exam MC (renderExamGradedMC)
old_graded_mc_text = """text.textContent = `${idx + 1}. ${q.q}`;
    qBlock.appendChild(text);
    
    const optsDiv = document.createElement('div');
    optsDiv.className = 'opts-container';
    
    q.opts.forEach((optText, optIdx) => {
      const label = document.createElement('label');
      label.className = 'opt-label locked';"""

new_graded_mc_text = """text.textContent = `${idx + 1}. ${q.q}`;
    if (q.section) {
      const secTag = document.createElement('span');
      secTag.style.cssText = 'display:inline-block;background:var(--accent-soft);color:var(--accent);font-size:11px;font-weight:600;padding:2px 7px;border-radius:4px;margin-right:6px;font-family:DM Mono,monospace;vertical-align:middle;';
      secTag.textContent = '[Unit ' + q.section + ']';
      text.insertBefore(secTag, text.firstChild);
    }
    qBlock.appendChild(text);
    
    const optsDiv = document.createElement('div');
    optsDiv.className = 'opts-container';
    
    q.opts.forEach((optText, optIdx) => {
      const label = document.createElement('label');
      label.className = 'opt-label locked';"""

if old_graded_mc_text in content:
    content = content.replace(old_graded_mc_text, new_graded_mc_text, 1)
    print("  Added section tags to renderExamGradedMC")
else:
    print("  WARNING: Could not find renderExamGradedMC text to patch")

with open(asm_path, "w", encoding="utf-8") as f:
    f.write(content)

print("  assemble_quiz.py saved!")

# ===== STEP 3: Regenerate index.html =====
print("\n" + "=" * 60)
print("STEP 3: Regenerating index.html...")
print("=" * 60)

# Execute assemble_quiz.py
import subprocess
result = subprocess.run(
    ["python", os.path.join(base, "assemble_quiz.py")],
    cwd=base,
    capture_output=True,
    text=True
)
print(result.stdout)
if result.stderr:
    print("STDERR:", result.stderr)
if result.returncode == 0:
    html_size = os.path.getsize(os.path.join(base, "index.html"))
    print(f"\n  SUCCESS! index.html regenerated ({html_size:,} bytes)")
else:
    print(f"\n  ERROR: assemble_quiz.py returned code {result.returncode}")

print("\n" + "=" * 60)
print("ALL DONE!")
print("=" * 60)
