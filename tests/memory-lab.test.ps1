$ErrorActionPreference = 'Stop'
$html = [IO.File]::ReadAllText((Join-Path $PSScriptRoot '..\index.html'))

$required = @(
  'data-target="memory-lab"',
  'function renderMemoryLab(',
  'function startMemorySession(',
  'function rateMemoryCard(',
  'Again',
  'Hard',
  'Good',
  'Easy',
  'Most Forgotten Concepts',
  'Confidence',
  'bio_memory_lab_v1'
)

foreach ($marker in $required) {
  if (-not $html.Contains($marker)) {
    throw "Missing Memory Lab marker: $marker"
  }
}

if (([regex]::Matches($html, "localStorage\.setItem\('bio_memory_lab_v1'")).Count -lt 1) {
  throw 'Memory Lab does not save to its isolated storage key.'
}

Write-Host 'Memory Lab structural checks passed.'
