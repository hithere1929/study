$ErrorActionPreference = 'Stop'

$html = [IO.File]::ReadAllText((Join-Path $PSScriptRoot '..\index.html'))

$required = @(
  'id="subject-bio-btn"',
  'id="subject-history-btn"',
  'const HISTORY_QUIZ_DATA =',
  'function switchSubject(',
  'function renderHistoryFinalExam(',
  'history-final-exam',
  'const HISTORY_EXAM_DATA =',
  'Industrial Revolution',
  'Nationalism & Revolution',
  'Imperialism',
  'World War I'
)

foreach ($needle in $required) {
  if (-not $html.Contains($needle)) {
    throw "Missing required history integration marker: $needle"
  }
}

if (-not $html.Contains('Section 1 - 90 Objective Questions') -or
    -not $html.Contains('Section 2 - 30 Document-based Objective Questions') -or
    -not $html.Contains('Section 3 - 2 Open-ended Responses')) {
  throw 'History final exam structure is missing or incorrect.'
}

$suspiciousCodePoints = @(0x00C2, 0x00C3, 0x00E2, 0x00F0, 0x0178)
foreach ($codePoint in $suspiciousCodePoints) {
  $character = [char]$codePoint
  if ($html.Contains([string]$character)) {
    throw "Mojibake-like code point remains in index.html: U+$('{0:X4}' -f $codePoint)"
  }
}

foreach ($unit in 5..8) {
  $jsonPath = Join-Path $PSScriptRoot "..\history_unit${unit}_questions.json"
  $questions = [IO.File]::ReadAllText($jsonPath) | ConvertFrom-Json
  if ($questions.Count -lt 60) {
    throw "History Unit $unit should contain at least 60 questions; found $($questions.Count)."
  }

  $duplicatePrompts = $questions | Group-Object q | Where-Object Count -gt 1
  if ($duplicatePrompts) {
    throw "History Unit $unit contains duplicate question prompts."
  }

  foreach ($question in $questions) {
    if (-not $question.section -or -not $question.title -or -not $question.q -or -not $question.opts) {
      throw "History Unit $unit contains a question missing required fields."
    }
    if ($question.opts.Count -lt 4) {
      throw "History Unit $unit contains a question with fewer than four options."
    }
    if (-not $question.explanation -or $question.explanation.Length -lt 100) {
      throw "History Unit $unit contains an explanation shorter than 100 characters."
    }
    if ($question.t -eq 'mc' -and ($null -eq $question.a -or $question.a -lt 0 -or $question.a -ge $question.opts.Count)) {
      throw "History Unit $unit contains an invalid multiple-choice answer index."
    }
    if ($question.t -eq 'sa' -and (-not $question.correct -or $question.correct.Count -lt 2)) {
      throw "History Unit $unit contains an invalid select-all answer set."
    }
  }
}

Write-Host 'History integration checks passed.'
