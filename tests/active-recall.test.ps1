$ErrorActionPreference = 'Stop'
$html = [IO.File]::ReadAllText((Join-Path $PSScriptRoot '..\index - Copy.html'))

$required = @(
  'const ACTIVE_RECALL_DATA =',
  'data-target="active-recall"',
  'function renderActiveRecall(',
  'function renderRecallPage(options = {})',
  'function gradeRecallQuestion(',
  'renderRecallPage({ preserveScroll: true })',
  'const previousScrollY = options.preserveScroll ? window.scrollY : 0;',
  'requestAnimationFrame(() => requestAnimationFrame(() => window.scrollTo({ top: previousScrollY',
  'overflow-anchor:none',
  'function jumpToRecallPage(',
  'function openRecallNotesPage(',
  'function recallLessonInfo(',
  'function recallLessonProgress(',
  'Lesson ${lessonInfo.lesson}',
  'Lesson Page ${lessonProgress.current} of ${lessonProgress.total}',
  'Unit Page ${recallState.page + 1} of ${pages.length}',
  'function setRecallReadingWidth(',
  'function startRecallResize(',
  'quiz_recall_width_v1',
  'id="recall-width-slider"',
  'class="recall-resize-handle"',
  'body.recall-active .layout-container',
  'body.notes-open.recall-active',
  'Open Exact Notes Page',
  'id="recall-page-input"',
  'class="recall-page-status"',
  'class="recall-page-nav"',
  'position:sticky',
  'quiz_recall_answers_v1',
  'quiz_recall_unit_v1',
  'quiz_recall_page_v1',
  'Reading Active Recall'
)

foreach ($marker in $required) {
  if (-not $html.Contains($marker)) {
    throw "Missing active recall marker: $marker"
  }
}

Write-Host 'Active recall structural checks passed.'
