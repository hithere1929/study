$ErrorActionPreference = 'Stop'

$root = Join-Path $PSScriptRoot '..'
$html = [IO.File]::ReadAllText((Join-Path $root 'index.html'))
$scriptPath = Join-Path $root 'final-blueprint.js'
$contentPath = Join-Path $root 'final-blueprint-content.js'
$stylePath = Join-Path $root 'final-blueprint.css'

foreach ($path in @($scriptPath, $contentPath, $stylePath)) {
  if (-not (Test-Path $path)) {
    throw "Missing Final Blueprint asset: $path"
  }
}

$script = [IO.File]::ReadAllText($scriptPath)
$content = [IO.File]::ReadAllText($contentPath)
$styles = [IO.File]::ReadAllText($stylePath)
$all = $html + "`n" + $script + "`n" + $content + "`n" + $styles

$required = @(
  'data-target="final-blueprint-2026"',
  'final-blueprint.css',
  'final-blueprint-content.js',
  'final-blueprint.js',
  'function renderFinalBlueprint(',
  'function renderBlueprintTrack(',
  'function renderBlueprintTopic(',
  'function startBlueprintRecall(',
  'function gradeBlueprintRecall(',
  'function startBlueprintDrill(',
  'function renderBlueprintOpenResponse(',
  'function saveBlueprintState(',
  'function calculateBlueprintReadiness(',
  'function openBlueprintActiveRecall(',
  'Part 1: General Knowledge',
  'Part 2: Units 3-6',
  'Part 3: Units 7-8',
  'Part 4: Open-Ended',
  '20 Multiple Choice',
  '26 Multiple Choice',
  '25 Multiple Choice',
  'Choose A or B',
  'bio_final_blueprint_2026_state_v1'
)

foreach ($marker in $required) {
  if (-not $all.Contains($marker)) {
    throw "Missing Final Blueprint marker: $marker"
  }
}

$outlineTopics = @(
  'Cell Theory',
  'Surface Area to Volume',
  'Prokaryotes and Eukaryotes',
  'Endosymbiotic Theory',
  'Animal Cell Structures',
  'Plant and Animal Cells',
  'Chromosome Structure',
  'Cell Cycle',
  'Cancer',
  'DNA Structure and Composition',
  'Euchromatin and Heterochromatin',
  'DNA Replication',
  'Transcription',
  'Translation',
  'The Operon',
  'Eukaryotic Gene Control and Mutations',
  'Biotechnology Techniques',
  'Meiosis',
  'Classical Genetics',
  'Punnett Squares',
  'Monohybrid and Dihybrid Crosses',
  'Autosomal Disorders',
  'Extensions of Mendelian Inheritance',
  'Evidence for Evolution',
  'Hardy-Weinberg Equation',
  'Hardy-Weinberg Meaning',
  'Forces of Evolution',
  'Speciation',
  'Kingdoms and Domains',
  'Viruses',
  'Prokaryote Characteristics',
  'Viruses and Bacteria',
  'Protists Plants and Fungi',
  'Vertebrates Mammals and Humans',
  'Monocots and Eudicots',
  'Plant Reproductive Structures',
  'Plant Tissues and Transport',
  'Plant Hormones',
  'Plant Tropisms',
  'Animal Tissue Types',
  'Circulatory System',
  'Respiratory System',
  'Nervous System Signaling',
  'Sensory Receptors',
  'Muscle Anatomy',
  'Nature and Nurture Behaviors',
  'Conditioning',
  'Population Reproductive Strategies',
  'Energy Flow',
  'Major Biomes',
  'Aquatic Ecosystem Zones',
  'Bioethics and Conservation',
  'Light-Dependent Reactions',
  'Light-Dependent and Light-Independent Reactions',
  'Photosynthesis Reactants and Products',
  'Plant Photosynthetic Strategies',
  'Cellular Respiration Stages',
  'Electron Transport Chains',
  'ATP Generation',
  'Energy Storage in Bonds'
)

foreach ($topic in $outlineTopics) {
  if (-not $content.Contains($topic)) {
    throw "Teacher-outline topic is missing from Final Blueprint content: $topic"
  }
}

if (([regex]::Matches($content, 'openResponseCategory')).Count -lt 6) {
  throw 'Final Blueprint must contain all six open-response categories.'
}

if (([regex]::Matches($content, '["'']?option["'']?\s*:\s*["'']A["'']')).Count -lt 6 -or
    ([regex]::Matches($content, '["'']?option["'']?\s*:\s*["'']B["'']')).Count -lt 6) {
  throw 'Each open-response category must provide A and B choices.'
}

$forbiddenWrites = @(
  "localStorage.setItem('bio_quiz_state_v3'",
  "localStorage.setItem('bio_final_exam_session'",
  "localStorage.setItem('bio_final_exam_result'",
  "localStorage.setItem('bio_memory_lab_v1'",
  "localStorage.setItem('quiz_recall_answers_v1'"
)

foreach ($write in $forbiddenWrites) {
  if ($script.Contains($write) -or $content.Contains($write)) {
    throw "Final Blueprint writes to existing saved progress: $write"
  }
}

Write-Host 'Final Blueprint structural and isolation checks passed.'
