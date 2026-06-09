$ErrorActionPreference = 'Stop'

$indexPath = Join-Path $PSScriptRoot 'index.html'
$html = [IO.File]::ReadAllText($indexPath)
$unitEntries = foreach ($unit in 5..8) {
  $json = [IO.File]::ReadAllText((Join-Path $PSScriptRoot "history_unit${unit}_questions.json")).Trim()
  [void]($json | ConvertFrom-Json)
  '"' + $unit + '":' + $json
}
$historyJson = '{' + ($unitEntries -join ',') + '}'
$pattern = 'const HISTORY_QUIZ_DATA = .*?;\r?\nlet ACTIVE_QUIZ_DATA'
$replacement = "const HISTORY_QUIZ_DATA = $historyJson;`r`nlet ACTIVE_QUIZ_DATA"
$updated = [regex]::Replace(
  $html,
  $pattern,
  $replacement,
  [Text.RegularExpressions.RegexOptions]::Singleline
)

if ($updated -eq $html) {
  throw 'Could not locate HISTORY_QUIZ_DATA in index.html.'
}

[IO.File]::WriteAllText($indexPath, $updated, (New-Object Text.UTF8Encoding($false)))
Write-Host 'Embedded history question banks into index.html.'
