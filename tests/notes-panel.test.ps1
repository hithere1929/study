$ErrorActionPreference = 'Stop'
$html = [IO.File]::ReadAllText((Join-Path $PSScriptRoot '..\index.html'))

$required = @(
  'id="notes-panel"',
  'function openSectionNotes(',
  'function closeNotesPanel(',
  'function findQuestionInNotes(',
  'function searchNotes(',
  'function startNotesResize(',
  'function resetNotesWidth(',
  'class="notes-resize-handle"',
  'body.notes-open',
  'id="notes-pages"',
  'notes-highlight',
  'pdfjsLib.getDocument',
  "location.protocol === 'file:'",
  'Open Local PDF',
  'Open Notes',
  'Find This Question',
  'notes-search-input'
)

foreach ($marker in $required) {
  if (-not $html.Contains($marker)) {
    throw "Missing notes panel marker: $marker"
  }
}

Write-Host 'Notes panel structural checks passed.'
